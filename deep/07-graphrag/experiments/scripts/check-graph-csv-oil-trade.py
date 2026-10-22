# 2번 무역 & 기름 그래프 CSV 형식 검사 스크립트 (E4)
#
# 하는 일: 에이전트 그래프 CSV(oil-trade/schema.md 5절 기록 형식)가 형식 규칙을 지키는지 검사한다.
#   근거 문장이 그 원장의 원문에 있는지도 대조한다. 공백을 모두 지워야만 원문에 있는 근거 문장은
#   위반(not-in-raw)이 아니라 경고(space-only)로 센다(원문이 PDF 추출이라 낱말 중간에 공백이 있음).
#   값이 맞는지(기준 그래프와 비교)는 보지 않는다.
#   python 표준 라이브러리만 쓴다.
# 입력: 명령줄 인자 1개 — 검사할 CSV 파일(utf-8-sig, 머리줄 "주어,관계,값,분류 체계,업무 단계,주체,원장 번호,위치,근거 문장")
#   원장 번호 목록은 deep/07-graphrag/oil-trade/sources.csv, 원문은 deep/07-graphrag/oil-trade/raw/ot-NN.txt(스크립트 위치 기준)
# 출력: 표준 출력에 위반마다 "줄 N: 규칙 이름", 경고마다 "줄 N: 경고: 규칙 이름"을 줄 번호 순서로 쓰고,
#   "관계별 줄 수: …", "주어별 줄 수: …", 마지막 줄에 "줄 X개, 위반 Y건, 경고 Z건"을 쓴다.
#   값과 근거 문장, 그 밖의 주어 이름은 출력하지 않는다. 줄 번호는 CSV 레코드 순번(머리줄이 1).
# 종료 코드: 0 위반 없음(경고만 있어도 0), 1 위반 있음,
#   2 입력 오류(파일 없음, 머리줄 틀림, sources.csv나 raw/ 폴더가 없음, 근거로 든 원장의 원문 파일이 없음).
#
# 위반 규칙: columns, relation, subject, empty, extra-field, closed-list, ledger, not-in-raw, duplicate
# 경고 규칙(위반 수에 넣지 않음): multi-value, stage-number, space-only
# 목록 상수와 정규화(normalize·in_raw)는 check-golden-rules-oil-trade.py와 같다.
# 실행: python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py <csv 경로>

import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

OT = Path(__file__).resolve().parent.parent.parent / "oil-trade"
SOURCES = OT / "sources.csv"
RAW = OT / "raw"

HEADER = ["주어", "관계", "값", "분류 체계", "업무 단계", "주체", "원장 번호", "위치", "근거 문장"]
PRODUCTS = ["UMO", "ULO", "PPO"]
SYSTEMS = ["HS(관세율표·WCO)", "바젤 부속서", "국내 폐기물 분류", "수출입 폐기물 구분"]
ACTORS = ["수출자", "수입자", "운반자", "처리자", "국내 주무관청", "상대국·경유국 정부", "세관"]
STAGES = ["품목 확인·분류", "수출입자 자격·보증", "허가·신고", "상대국·경유국 동의",
          "이동서류·인계인수 기록", "포장·표지·운반", "처리·재활용", "결과 통보·보고·장부",
          "금지·사후 조치"]
RELATIONS = ["원문 용어", "품목 분류", "요건"]
CLOSED_FIELDS = {"분류 체계": SYSTEMS, "업무 단계": STAGES, "주체": ACTORS}

SPLIT_RE = re.compile(r"\s*(?:,|/|;| 및 )\s*")
STAGE_NUM_RE = re.compile(r"([1-9])(?:[.)]\s*|\s+)(.+)")

QUOTES = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'",
                        "“": '"', "”": '"', "„": '"', "‟": '"'})


def normalize(text, join_hyphen=True):
    text = text.translate(QUOTES)
    if join_hyphen:
        text = re.sub(r"-[ \t]*\r?\n\s*", "", text)  # 줄 끝 하이픈 줄바꿈을 붙임
    return re.sub(r"\s+", " ", text).strip()


def in_raw(sentence, raw_text):
    s = normalize(sentence)
    if s and s in normalize(raw_text):
        return True
    # 원문 줄 끝 하이픈이 낱말 안의 하이픈인 경우를 위해, 하이픈을 남긴 정규화로도 본다
    s2 = normalize(sentence, join_hyphen=False)
    return bool(s2) and s2 in normalize(raw_text, join_hyphen=False)


def nospace(text):
    # 따옴표를 바꾼 뒤 공백을 모두 지운다(space-only 경고용)
    return re.sub(r"\s+", "", text.translate(QUOTES))


def input_error(msg):
    print(f"입력 오류: {msg}")
    sys.exit(2)


def is_multi_value(v, allowed):
    parts = [p for p in SPLIT_RE.split(v) if p]
    return len(parts) >= 2 and all(p in allowed for p in parts)


def is_stage_number(v):
    if re.fullmatch(r"[1-9]", v):
        return True
    m = STAGE_NUM_RE.fullmatch(v)
    return bool(m) and m.group(2).strip() == STAGES[int(m.group(1)) - 1]


def main():
    if len(sys.argv) != 2:
        print("사용: python3 check-graph-csv-oil-trade.py <csv 경로>")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        input_error(f"파일이 없음: {path}")
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows or [x.strip() for x in rows[0]] != HEADER:
        print("줄 1: header")
        return 2
    if not SOURCES.is_file():
        input_error(f"원장 파일이 없음: {SOURCES}")
    if not RAW.is_dir():
        input_error(f"원문 폴더가 없음: {RAW}")
    with SOURCES.open(encoding="utf-8", newline="") as f:
        ledger = {int(r["번호"]) for r in csv.DictReader(f)}

    raw_cache = {}
    raw_nospace_cache = {}

    def raw_text(n):
        if n not in raw_cache:
            p = RAW / f"ot-{n:02d}.txt"
            if not p.is_file():
                input_error(f"원문 파일이 없음: {p}")
            raw_cache[n] = p.read_text(encoding="utf-8")
        return raw_cache[n]

    def raw_nospace(n):
        if n not in raw_nospace_cache:
            raw_nospace_cache[n] = nospace(raw_text(n))
        return raw_nospace_cache[n]

    found = []  # (줄 번호, 경고인지, 규칙)
    rel_count = Counter()
    subj_count = Counter()
    seen = defaultdict(list)
    n_lines = 0

    for ln, r in enumerate(rows[1:], 2):
        n_lines += 1
        if len(r) != 9:
            found.append((ln, False, "columns"))
            continue
        subj, rel, val, system, stage, actor, num_s, loc, ev = (x.strip() for x in r)
        fields = {"분류 체계": system, "업무 단계": stage, "주체": actor}
        hits = []

        if rel in RELATIONS:
            rel_count[rel] += 1
        else:
            hits.append("relation")
        subj_count[subj if subj in PRODUCTS else "그 밖"] += 1

        if rel in ("원문 용어", "품목 분류") and subj and subj not in PRODUCTS:
            hits.append("subject")

        if (not subj or not val or not num_s or not loc or not ev
                or (rel == "품목 분류" and not system)
                or (rel == "요건" and (not stage or not actor))):
            hits.append("empty")

        if (rel != "품목 분류" and system) or (rel != "요건" and (stage or actor)):
            hits.append("extra-field")

        warns = []
        bad_closed = False
        for fld, allowed in CLOSED_FIELDS.items():
            v = fields[fld]
            if not v or v in allowed or v.startswith("기타: "):
                continue
            if is_multi_value(v, allowed):
                warns.append("multi-value")
            elif fld == "업무 단계" and is_stage_number(v):
                warns.append("stage-number")
            else:
                bad_closed = True
        if bad_closed:
            hits.append("closed-list")

        num_ok = num_s.isdigit() and int(num_s) in ledger
        if num_s and not num_ok:
            hits.append("ledger")
        if num_ok and ev and not in_raw(ev, raw_text(int(num_s))):
            ns = nospace(ev)
            if ns and ns in raw_nospace(int(num_s)):
                warns.append("space-only")
            else:
                hits.append("not-in-raw")

        seen[(subj, rel, val, num_s, loc)].append(ln)
        found += [(ln, False, h) for h in hits]
        found += [(ln, True, w) for w in warns]

    for lns in seen.values():
        if len(lns) > 1:
            found += [(ln, False, "duplicate") for ln in lns]

    found.sort(key=lambda x: x[0])
    for ln, warn, rule in found:
        print(f"줄 {ln}: 경고: {rule}" if warn else f"줄 {ln}: {rule}")
    n_viol = sum(1 for x in found if not x[1])
    n_warn = sum(1 for x in found if x[1])
    print("관계별 줄 수: " + ", ".join(f"{r} {rel_count[r]}" for r in RELATIONS))
    print("주어별 줄 수: " + ", ".join(f"{s} {subj_count[s]}" for s in PRODUCTS) + f", 그 밖의 주어 {subj_count['그 밖']}")
    print(f"줄 {n_lines}개, 위반 {n_viol}건, 경고 {n_warn}건")
    return 0 if n_viol == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
