# 2번 무역 & 기름 골든 룰 검사 스크립트 (E3)
#
# 하는 일: E5 답 JSON 파일이 oil-trade/golden-rules.md 3절의 골든 룰 G1~G9를 지키는지 검사한다.
#   정답(기대 답)과는 비교하지 않는다. python 표준 라이브러리만 쓴다.
#   정규화와 하이픈 처리는 1번 스크립트(check-golden-rules.py)와 같은 방식이다.
# 입력:
#   - 명령줄 인자 1개: 답 JSON 파일(질문별 답의 목록. 칸 이름은 질문·상태·주장·요약,
#     주장은 주어·관계·값·분류 체계·업무 단계·주체·근거, 근거는 원장 번호·위치·근거 문장)
#   - deep/07-graphrag/oil-trade/schema.md: 스크립트 안 목록 상수가 스키마 본문에 그대로 있는지 확인
#   - deep/07-graphrag/oil-trade/sources.csv: 원장 번호(G3)
#   - deep/07-graphrag/oil-trade/raw/ot-NN.txt: 원문(G4)
# 출력: 표준 출력에 검사한 질문 수, 주장 수, 근거 수와 위반 목록(질문, 주장 순번, 근거 순번, 규칙, 이유)을 한국어로 쓴다.
#   경고가 있으면 그 뒤에 "경고 N건"과 같은 칸의 경고 목록을 쓴다.
# 경고 규칙: G4 경고(space-only) — 공백을 모두 지워야만 원문에 있는 근거 문장은 G4 위반이 아니라 경고로 센다
#   (원문이 PDF에서 뽑은 글자라 낱말 중간에 공백이 있음, experiments/e5-method.md 4절). 경고는 종료 코드에 넣지 않는다.
# 종료 코드: 0 위반 없음, 1 위반 있음, 2 입력 오류(질문을 하나도 읽지 못한 경우 포함. 주장 0개만으로는 오류가 아님).
#
# 실행(저장소 맨 위에서): python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py <답 JSON 파일>

import csv
import json
import re
import sys
from pathlib import Path

OT = Path(__file__).resolve().parent.parent.parent / "oil-trade"
SCHEMA = OT / "schema.md"
SOURCES = OT / "sources.csv"
RAW = OT / "raw"

PRODUCTS = ["UMO", "ULO", "PPO"]
SYSTEMS = ["HS(관세율표·WCO)", "바젤 부속서", "국내 폐기물 분류", "수출입 폐기물 구분"]
ACTORS = ["수출자", "수입자", "운반자", "처리자", "국내 주무관청", "상대국·경유국 정부", "세관"]
STAGES = ["품목 확인·분류", "수출입자 자격·보증", "허가·신고", "상대국·경유국 동의",
          "이동서류·인계인수 기록", "포장·표지·운반", "처리·재활용", "결과 통보·보고·장부",
          "금지·사후 조치"]
RELATIONS = ["원문 용어", "품목 분류", "요건"]

# 채워져 있으면 목록 이름 그대로이거나 "기타: "로 시작해야 하는 칸
CLOSED_FIELDS = {"분류 체계": SYSTEMS, "업무 단계": STAGES, "주체": ACTORS}
# 관계별로 채워야 하는 칸(나머지는 비어 있어야 함)
PAIR = {"품목 분류": {"분류 체계"}, "요건": {"업무 단계", "주체"}, "원문 용어": set()}

QUESTIONS = [f"Q{i}" for i in range(1, 11)] + [f"T{i}" for i in range(1, 6)]
STATUSES = ["답함", "자료에 없음", "전제가 틀림"]
FIELDS = ["질문", "상태", "주장", "요약"]
CLAIM_FIELDS = ["주어", "관계", "값", "분류 체계", "업무 단계", "주체", "근거"]
EV_FIELDS = ["원장 번호", "위치", "근거 문장"]


def input_error(msg):
    print(f"입력 오류: {msg}")
    sys.exit(2)


def check_schema():
    if not SCHEMA.is_file():
        input_error(f"스키마 파일이 없음: {SCHEMA}")
    text = SCHEMA.read_text(encoding="utf-8")
    missing = [v for v in PRODUCTS + SYSTEMS + ACTORS + STAGES + RELATIONS if v not in text]
    if missing:
        input_error("스크립트의 목록 값이 schema.md 본문에 없음: " + ", ".join(missing))


def load_ledger():
    if not SOURCES.is_file():
        input_error(f"원장 파일이 없음: {SOURCES}")
    with SOURCES.open(encoding="utf-8", newline="") as f:
        nums = {int(r["번호"]) for r in csv.DictReader(f)}
    if not nums:
        input_error("원장에서 번호를 하나도 읽지 못함")
    return nums


def load_raw(nums):
    if not RAW.is_dir():
        input_error(f"원문 폴더가 없음: {RAW}")
    raw = {}
    for n in nums:
        p = RAW / f"ot-{n:02d}.txt"
        if not p.is_file():
            input_error(f"원문 파일이 없음: {p}")
        raw[n] = p.read_text(encoding="utf-8")
    return raw


QUOTES = str.maketrans({"‘": "'", "’": "'", "‚": "'", "‛": "'",
                        "“": '"', "”": '"', "„": '"', "‟": '"'})


def normalize(text, join_hyphen=True):
    text = text.translate(QUOTES)
    if join_hyphen:
        text = re.sub(r"-[ \t]*\r?\n\s*", "", text)  # 줄 끝 하이픈 줄바꿈을 붙임
    return re.sub(r"\s+", " ", text).strip()


def nospace(text):
    # 따옴표를 바꾼 뒤 공백을 모두 지운다(G4 경고 space-only용)
    return re.sub(r"\s+", "", text.translate(QUOTES))


def in_raw(sentence, raw_text):
    s = normalize(sentence)
    if s and s in normalize(raw_text):
        return True
    # 원문 줄 끝 하이픈이 낱말 안의 하이픈인 경우를 위해, 하이픈을 남긴 정규화로도 본다
    s2 = normalize(sentence, join_hyphen=False)
    return bool(s2) and s2 in normalize(raw_text, join_hyphen=False)


def empty(v):
    return v is None or (isinstance(v, str) and not v.strip())


def is_int(v):
    return isinstance(v, int) and not isinstance(v, bool)


def main():
    if len(sys.argv) != 2:
        input_error("답 JSON 파일 경로 하나를 인자로 주세요")
    path = Path(sys.argv[1])
    if not path.is_file():
        input_error(f"답 파일이 없음: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        input_error(f"JSON을 읽지 못함: {e}")
    if not isinstance(data, list):
        input_error("맨 위가 JSON 목록이 아님")

    check_schema()
    ledger = load_ledger()
    raw = load_raw(ledger)

    violations = []  # (질문, 주장 순번, 근거 순번, 규칙, 이유)
    warnings = []    # 같은 칸. G4 경고(space-only)
    n_items = n_claims = n_ev = 0

    for idx, item in enumerate(data, 1):
        n_items += 1
        if not isinstance(item, dict):
            violations.append((f"(항목 {idx})", "-", "-", "G1", "항목이 JSON 객체가 아님"))
            continue
        q = item.get("질문")
        ql = q if isinstance(q, str) and q else f"(항목 {idx})"
        status = item.get("상태")
        claims = item.get("주장")

        # G1 정해진 모양(항목)
        for fld in FIELDS:
            if fld not in item:
                violations.append((ql, "-", "-", "G1", f'"{fld}" 칸이 없음'))
        if "질문" in item and q not in QUESTIONS:
            violations.append((ql, "-", "-", "G1", f"질문 값이 Q1~Q10·T1~T5가 아님: {q!r}"))
        if "상태" in item and status not in STATUSES:
            violations.append((ql, "-", "-", "G1", f"상태 값이 세 값 중 하나가 아님: {status!r}"))
        if "주장" in item and not isinstance(claims, list):
            violations.append((ql, "-", "-", "G1", "주장이 목록이 아님"))
        if not isinstance(claims, list):
            claims = []
        n_claims += len(claims)

        # G2 답했으면 주장이 있다
        if status == "답함" and not claims:
            violations.append((ql, "-", "-", "G2", "상태가 답함인데 주장이 없음"))

        # G8 통제 항목
        if q in ("T1", "T3", "T4"):
            if status != "자료에 없음":
                violations.append((ql, "-", "-", "G8", f'상태가 "자료에 없음"이 아님: {status!r}'))
            if claims:
                violations.append((ql, "-", "-", "G8", f"주장이 0개가 아님: {len(claims)}개"))
        if q == "T2" and status != "전제가 틀림":
            violations.append((ql, "-", "-", "G8", f'상태가 "전제가 틀림"이 아님: {status!r}'))

        for ci, c in enumerate(claims, 1):
            if not isinstance(c, dict):
                violations.append((ql, ci, "-", "G1", "주장이 JSON 객체가 아님"))
                continue
            # G1 주장의 일곱 칸과 근거 목록
            for fld in CLAIM_FIELDS:
                if fld not in c:
                    violations.append((ql, ci, "-", "G1", f'주장의 "{fld}" 칸이 없음'))
            evs = c.get("근거")
            if "근거" in c and not isinstance(evs, list):
                violations.append((ql, ci, "-", "G1", "근거가 목록이 아님"))
            if not isinstance(evs, list):
                evs = []
            n_ev += len(evs)

            subj = c.get("주어")
            rel = c.get("관계")
            val = c.get("값")

            # G2 주어·관계·값과 근거 개수
            if status == "답함":
                for fld in ("주어", "관계", "값"):
                    if empty(c.get(fld)):
                        violations.append((ql, ci, "-", "G2", f'주장의 "{fld}" 칸이 비어 있음'))
                if not evs:
                    violations.append((ql, ci, "-", "G2", "근거가 없음"))

            # G5 관계 이름
            if not empty(rel) and rel not in RELATIONS:
                violations.append((ql, ci, "-", "G5", f"스키마 2절에 없는 관계: {rel!r}"))

            # G6 닫힌 목록 값
            if rel in ("원문 용어", "품목 분류") and not empty(subj) and subj not in PRODUCTS:
                violations.append((ql, ci, "-", "G6", f"주어가 UMO·ULO·PPO가 아님: {subj!r}"))
            for fld, allowed in CLOSED_FIELDS.items():
                v = c.get(fld)
                if not empty(v) and not (isinstance(v, str) and (v in allowed or v.startswith("기타: "))):
                    violations.append((ql, ci, "-", "G6", f'"{fld}"의 목록에 없는 값: {v!r}'))

            # G7 칸 짝
            if rel in PAIR:
                for fld in CLOSED_FIELDS:
                    need = fld in PAIR[rel]
                    if need and empty(c.get(fld)):
                        violations.append((ql, ci, "-", "G7", f'{rel}인데 "{fld}"가 비어 있음'))
                    if not need and not empty(c.get(fld)):
                        violations.append((ql, ci, "-", "G7", f'{rel}인데 "{fld}"가 채워져 있음: {c.get(fld)!r}'))

            # G9 질문이 정한 조건(주장 단위)
            if q == "Q1" and rel != "요건":
                violations.append((ql, ci, "-", "G9", f"Q1의 주장은 관계가 요건이어야 하는데 {rel!r}"))
            if q == "Q2":
                if subj != "ULO":
                    violations.append((ql, ci, "-", "G9", f"Q2의 주장은 주어가 ULO여야 하는데 {subj!r}"))
                if not any(isinstance(e, dict) and e.get("원장 번호") == 17 for e in evs):
                    violations.append((ql, ci, "-", "G9", "Q2의 주장 근거에 원장 17번이 없음"))
            if q == "Q3" and rel == "요건" and c.get("업무 단계") != "허가·신고":
                violations.append((ql, ci, "-", "G9", f'Q3에서 요건의 업무 단계는 "허가·신고"여야 하는데 {c.get("업무 단계")!r}'))
            if q == "Q4" and rel == "요건" and c.get("주체") != "처리자":
                violations.append((ql, ci, "-", "G9", f'Q4에서 요건의 주체는 "처리자"여야 하는데 {c.get("주체")!r}'))
            if q in ("Q7", "Q8") and rel in ("원문 용어", "품목 분류"):
                want = "ULO" if q == "Q7" else "UMO"
                if subj != want:
                    violations.append((ql, ci, "-", "G9", f"{q}에서 {rel}의 주어는 {want}여야 하는데 {subj!r}"))
            if q == "Q8" and rel == "요건" and c.get("주체") not in ("수출자", "상대국·경유국 정부"):
                violations.append((ql, ci, "-", "G9", f'Q8에서 요건의 주체는 "수출자" 또는 "상대국·경유국 정부"여야 하는데 {c.get("주체")!r}'))

            for ei, e in enumerate(evs, 1):
                if not isinstance(e, dict):
                    violations.append((ql, ci, ei, "G1", "근거가 JSON 객체가 아님"))
                    continue
                num = e.get("원장 번호")
                loc = e.get("위치")
                sent = e.get("근거 문장")

                # G2 근거의 세 칸
                if status == "답함":
                    for fld in EV_FIELDS:
                        if empty(e.get(fld)):
                            violations.append((ql, ci, ei, "G2", f'근거의 "{fld}" 칸이 비어 있음'))

                # G3 원장 번호
                num_ok = is_int(num) and num in ledger
                if not empty(num) and not num_ok:
                    violations.append((ql, ci, ei, "G3", f"원장에 없는 번호: {num!r}"))

                # G4 근거 문장이 원문에 있다
                if num_ok and not empty(sent):
                    if not isinstance(sent, str) or not in_raw(sent, raw[num]):
                        if isinstance(sent, str) and nospace(sent) and nospace(sent) in nospace(raw[num]):
                            warnings.append((ql, ci, ei, "G4 경고(space-only)", f"공백을 모두 지우면 원장 {num}번 원문에 있음"))
                        else:
                            violations.append((ql, ci, ei, "G4", f"근거 문장이 원장 {num}번 원문에 없음"))

                # G9 Q1의 근거는 원장 4번 제7조
                if q == "Q1":
                    if num != 4:
                        violations.append((ql, ci, ei, "G9", f"Q1의 근거는 원장 4번이어야 하는데 {num!r}"))
                    if not (isinstance(loc, str) and "제7조" in loc):
                        violations.append((ql, ci, ei, "G9", f'Q1의 근거 위치에 "제7조"가 없음: {loc!r}'))

    if n_items == 0:
        input_error("질문을 하나도 읽지 못함(질문 0개)")

    print(f"검사한 질문 {n_items}개, 주장 {n_claims}개, 근거 {n_ev}개")
    if not violations:
        print("위반 없음")
    else:
        order = {f"G{i}": i for i in range(1, 10)}
        violations.sort(key=lambda v: order[v[3]])
        print(f"위반 {len(violations)}건")
        print("질문\t주장\t근거\t규칙\t이유")
        for v in violations:
            print("\t".join(str(x) for x in v))
    if warnings:
        print(f"경고 {len(warnings)}건")
        print("질문\t주장\t근거\t규칙\t이유")
        for w in warnings:
            print("\t".join(str(x) for x in w))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
