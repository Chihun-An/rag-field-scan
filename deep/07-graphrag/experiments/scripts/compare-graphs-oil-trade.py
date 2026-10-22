# 2번 무역 & 기름 E4 비교 스크립트 (기준 대 에이전트, 1회차 대 2회차)
#
# 하는 일: experiments/e4-method-oil-trade.md의 정의대로 그래프 CSV 두 개를 짝짓고,
#   닫힌 목록 칸 일치율, 재현율·정밀도(참고값), 자카드 지수를 계산한다. python 표준 라이브러리만 쓴다.
#   값·근거 문장·주어 이름은 출력하지 않고 개수와 비율만 낸다. 짝 목록 같은 중간 파일은 만들지 않는다.
# 입력: 명령줄 인자 2개 — A CSV(기준 그래프 또는 1회차), B CSV(에이전트 그래프 또는 2회차).
#   utf-8-sig, 머리줄 "주어,관계,값,분류 체계,업무 단계,주체,원장 번호,위치,근거 문장"(check-graph-csv-oil-trade.py와 같음)
# 출력: 표준 출력에 줄 수, 짝 수, 닫힌 목록 일치율(전체·칸별), 뺀 칸 수, A 재현율, B 정밀도, 자카드 지수(비율은 소수점 한 자리 %)
# 종료 코드: 0 정상, 2 입력 오류(파일 없음, 머리줄 틀림)
#
# 정한 것(방법 파일에 없던 경우): 닫힌 목록 칸이 한쪽만 비면 불일치, 양쪽 모두 비면 비교에서 빼고 "양쪽 빈 칸"으로 센다.
#   빈 근거 문장(원문 용어·품목 분류는 빈 값도)인 줄은 후보가 되지 않는다(방법 파일 짝짓기 5번).
# 실행: python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py <A CSV> <B CSV>

import csv
import difflib
import re
import sys
from pathlib import Path

HEADER = ["주어", "관계", "값", "분류 체계", "업무 단계", "주체", "원장 번호", "위치", "근거 문장"]
STAGES = ["품목 확인·분류", "수출입자 자격·보증", "허가·신고", "상대국·경유국 동의",
          "이동서류·인계인수 기록", "포장·표지·운반", "처리·재활용", "결과 통보·보고·장부",
          "금지·사후 조치"]
RELATIONS = ["원문 용어", "품목 분류", "요건"]
# 관계별로 비교하는 닫힌 목록 칸
CLOSED_BY_REL = {"품목 분류": ["분류 체계"], "요건": ["업무 단계", "주체"], "원문 용어": []}
FIELD_ORDER = ["분류 체계", "업무 단계", "주체"]

# check-graph-csv-oil-trade.py와 같은 나누기·업무 단계 번호 모양
SPLIT_RE = re.compile(r"\s*(?:,|/|;| 및 )\s*")
STAGE_NUM_RE = re.compile(r"([1-9])(?:[.)]\s*|\s+)(.+)")

# check-golden-rules-oil-trade.py와 같은 정규화
QUOTES = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'",
                        "“": '"', "”": '"', "„": '"', "‟": '"'})


def normalize(text, join_hyphen=True):
    text = text.translate(QUOTES)
    if join_hyphen:
        text = re.sub(r"-[ \t]*\r?\n\s*", "", text)  # 줄 끝 하이픈 줄바꿈을 붙임
    return re.sub(r"\s+", " ", text).strip()


def input_error(msg):
    print(f"입력 오류: {msg}")
    sys.exit(2)


def load(path):
    p = Path(path)
    if not p.is_file():
        input_error(f"파일이 없음: {path}")
    with p.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows or [x.strip() for x in rows[0]] != HEADER:
        input_error(f"머리줄이 다름: {path}")
    good, bad = [], 0
    for r in rows[1:]:
        if len(r) != 9:
            bad += 1
            continue
        d = dict(zip(HEADER, (x.strip() for x in r)))
        d["_ev"] = normalize(d["근거 문장"])
        d["_val"] = normalize(d["값"])
        good.append(d)
    return good, bad


def contains_either(x, y):
    return x == y or x in y or y in x


def is_candidate(a, b):
    if (a["주어"], a["관계"], a["원장 번호"]) != (b["주어"], b["관계"], b["원장 번호"]):
        return False
    if not a["_ev"] or not b["_ev"]:
        return False
    if not contains_either(a["_ev"], b["_ev"]):
        return False
    if a["관계"] in ("원문 용어", "품목 분류"):
        if not a["_val"] or not b["_val"]:
            return False
        if not contains_either(a["_val"], b["_val"]):
            return False
    return True


def piece_set(v, field):
    out = set()
    for p in SPLIT_RE.split(v):
        if not p:
            continue
        if field == "업무 단계":
            if re.fullmatch(r"[1-9]", p):
                p = STAGES[int(p) - 1]
            else:
                m = STAGE_NUM_RE.fullmatch(p)
                if m and m.group(2).strip() == STAGES[int(m.group(1)) - 1]:
                    p = m.group(2).strip()
        out.add(p)
    return out


def compare_field(va, vb, field):
    """반환: 'same', 'diff', 'both-other', 'both-empty'"""
    if not va and not vb:
        return "both-empty"
    if not va or not vb:
        return "diff"
    oa, ob = va.startswith("기타: "), vb.startswith("기타: ")
    if oa and ob:
        return "both-other"
    if oa or ob:
        return "diff"
    return "same" if piece_set(va, field) == piece_set(vb, field) else "diff"


def frac(n, d):
    return f"{n} / {d} (해당 없음)" if d == 0 else f"{n} / {d} ({100 * n / d:.1f}%)"


def main():
    if len(sys.argv) != 3:
        print("사용: python3 compare-graphs-oil-trade.py <A CSV> <B CSV>")
        return 2
    A, bad_a = load(sys.argv[1])
    B, bad_b = load(sys.argv[2])

    cand = [(i, j) for i, a in enumerate(A) for j, b in enumerate(B) if is_candidate(a, b)]
    cand_a = {}
    cand_b = {}
    for i, j in cand:
        cand_a[i] = cand_a.get(i, 0) + 1
        cand_b[j] = cand_b.get(j, 0) + 1
    multi_a = sum(1 for n in cand_a.values() if n >= 2)
    multi_b = sum(1 for n in cand_b.values() if n >= 2)

    scored = sorted(cand, key=lambda ij: (-difflib.SequenceMatcher(None, A[ij[0]]["_val"], B[ij[1]]["_val"]).ratio(),
                                          ij[0], ij[1]))
    used_a, used_b, pairs = set(), set(), []
    for i, j in scored:
        if i not in used_a and j not in used_b:
            used_a.add(i)
            used_b.add(j)
            pairs.append((i, j))

    same = {f: 0 for f in FIELD_ORDER}
    compared = {f: 0 for f in FIELD_ORDER}
    both_other = both_empty = 0
    for i, j in pairs:
        for f in CLOSED_BY_REL.get(A[i]["관계"], []):
            res = compare_field(A[i][f], B[j][f], f)
            if res == "both-other":
                both_other += 1
            elif res == "both-empty":
                both_empty += 1
            else:
                compared[f] += 1
                same[f] += res == "same"

    def by_rel(rows, used):
        parts = []
        for rel in RELATIONS:
            idx = [k for k, r in enumerate(rows) if r["관계"] == rel]
            parts.append(f"{rel} {frac(sum(1 for k in idx if k in used), len(idx))}")
        return ", ".join(parts)

    n_pairs = len(pairs)
    print(f"A 줄 수: {len(A)}, B 줄 수: {len(B)} (칸 수가 틀려 뺀 줄: A {bad_a}, B {bad_b})")
    print(f"짝 수: {n_pairs}, 후보가 둘 이상이었던 줄 수: A {multi_a}, B {multi_b}")
    print(f"닫힌 목록 일치율: {frac(sum(same.values()), sum(compared.values()))}")
    print("칸별 일치율: " + ", ".join(f"{f} {frac(same[f], compared[f])}" for f in FIELD_ORDER))
    print(f"뺀 칸 수: 양쪽 모두 기타 {both_other}, 양쪽 빈 칸 {both_empty}")
    print(f"A 재현율: {frac(len(used_a), len(A))} / 관계별: {by_rel(A, used_a)}")
    print(f"B 정밀도: {frac(len(used_b), len(B))} / 관계별: {by_rel(B, used_b)}")
    print(f"자카드 지수: {frac(n_pairs, len(A) + len(B) - n_pairs)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
