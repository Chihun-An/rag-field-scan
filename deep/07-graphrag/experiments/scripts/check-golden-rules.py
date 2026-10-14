# 1번 AI 컨설팅 골든 룰 검사 스크립트 (E3)
#
# 하는 일: E5 답 JSON 파일이 ai-consulting/golden-rules.md 3절의 골든 룰 G1~G9를 지키는지 검사한다.
#   정답(기대 답)과는 비교하지 않는다. python 표준 라이브러리만 쓴다.
# 입력:
#   - 명령줄 인자 1개: 답 JSON 파일(질문별 답의 목록. 칸 이름은 질문·상태·주장·요약)
#   - deep/07-graphrag/ai-consulting/schema.md: 스크립트 안 목록 상수가 스키마 본문에 그대로 있는지 확인
#   - deep/07-graphrag/ai-consulting/sources.csv: 원장 번호와 펌(G3, G7)
#   - deep/07-graphrag/ai-consulting/raw/ac-NN.txt: 원문(G4)
# 출력: 표준 출력에 검사한 질문 수와 주장 수, 위반 목록(질문, 주장 순번, 규칙, 이유)을 한국어로 쓴다.
# 종료 코드: 0 위반 없음, 1 위반 있음, 2 입력 오류(질문을 하나도 읽지 못한 경우 포함. 주장 0개만으로는 오류가 아님).
#
# 실행(저장소 맨 위에서): python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py <답 JSON 파일>

import csv
import json
import re
import sys
from pathlib import Path

AC = Path(__file__).resolve().parent.parent.parent / "ai-consulting"
SCHEMA = AC / "schema.md"
SOURCES = AC / "sources.csv"
RAW = AC / "raw"

FIRMS = ["McKinsey", "BCG", "Bain", "Deloitte", "PwC", "EY", "KPMG"]
INDUSTRIES = ["에너지", "소재", "산업재", "경기소비재", "필수소비재", "헬스케어", "금융",
              "정보기술", "커뮤니케이션 서비스", "유틸리티", "부동산"]
WORK_TYPES = ["AI 전략·로드맵 수립", "AI 활용 과제 발굴·우선순위 선정", "사업성·투자 타당성 분석",
              "데이터·기술 기반 구축", "AI 신상품·신사업 기획 및 사업화", "업무 프로세스 재설계",
              "AI 솔루션 개발·실증", "전사 확산·성과 관리", "AI 거버넌스·리스크 관리", "조직·인력·변화 관리"]
AI_TECH = ["생성형 AI(LLM 포함)", "예측·분류 머신러닝", "추천·개인화", "컴퓨터 비전",
           "음성 인식·합성", "최적화·시뮬레이션"]
RELATIONS = ["수행", "고객", "고객 산업", "적용 업무", "해결하려던 병목", "사용 기술", "낸 성과"]

CLOSED = {"수행": FIRMS, "고객 산업": INDUSTRIES, "적용 업무": WORK_TYPES, "사용 기술": AI_TECH}

QUESTIONS = [f"Q{i}" for i in range(1, 11)] + [f"T{i}" for i in range(1, 6)]
STATUSES = ["답함", "자료에 없음", "전제가 틀림"]
FIELDS = ["질문", "상태", "주장", "요약"]
CLAIM_FIELDS = ["원장 번호", "관계", "값", "근거 문장"]

# G9: 질문이 정한 조건
G9_LEDGER = {"Q1": 2, "Q2": 5}
G9_VALUE = {"Q3": ("사용 기술", "생성형 AI(LLM 포함)"), "Q4": ("적용 업무", "AI 솔루션 개발·실증"),
            "Q7": ("고객 산업", "금융")}


def input_error(msg):
    print(f"입력 오류: {msg}")
    sys.exit(2)


def check_schema():
    if not SCHEMA.is_file():
        input_error(f"스키마 파일이 없음: {SCHEMA}")
    text = SCHEMA.read_text(encoding="utf-8")
    missing = [v for v in FIRMS + INDUSTRIES + WORK_TYPES + AI_TECH + RELATIONS if v not in text]
    if missing:
        input_error("스크립트의 목록 값이 schema.md 본문에 없음: " + ", ".join(missing))


def load_ledger():
    if not SOURCES.is_file():
        input_error(f"원장 파일이 없음: {SOURCES}")
    with SOURCES.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    ledger = {}
    for r in rows:
        ledger[int(r["번호"])] = r["펌"]
    if not ledger:
        input_error("원장에서 번호를 하나도 읽지 못함")
    return ledger


def load_raw(ledger):
    if not RAW.is_dir():
        input_error(f"원문 폴더가 없음: {RAW}")
    raw = {}
    for n in ledger:
        p = RAW / f"ac-{n:02d}.txt"
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


def in_raw(sentence, raw_text):
    s = normalize(sentence)
    if s and s in normalize(raw_text):
        return True
    # 원문 줄 끝 하이픈이 낱말 안의 하이픈(예: AI-powered)인 경우를 위해, 하이픈을 남긴 정규화로도 본다
    s2 = normalize(sentence, join_hyphen=False)
    return bool(s2) and s2 in normalize(raw_text, join_hyphen=False)


def empty(v):
    return v is None or (isinstance(v, str) and not v.strip())


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

    violations = []  # (질문, 주장 순번, 규칙, 이유)
    n_items = 0
    n_claims = 0

    for idx, item in enumerate(data, 1):
        n_items += 1
        if not isinstance(item, dict):
            violations.append((f"(항목 {idx})", "-", "G1", "항목이 JSON 객체가 아님"))
            continue
        q = item.get("질문")
        qlabel = q if isinstance(q, str) and q else f"(항목 {idx})"
        status = item.get("상태")
        claims = item.get("주장")

        # G1 정해진 모양
        for fld in FIELDS:
            if fld not in item:
                violations.append((qlabel, "-", "G1", f'"{fld}" 칸이 없음'))
        if "질문" in item and q not in QUESTIONS:
            violations.append((qlabel, "-", "G1", f"질문 값이 Q1~Q10·T1~T5가 아님: {q!r}"))
        if "상태" in item and status not in STATUSES:
            violations.append((qlabel, "-", "G1", f"상태 값이 세 값 중 하나가 아님: {status!r}"))
        if "주장" in item and not isinstance(claims, list):
            violations.append((qlabel, "-", "G1", "주장이 목록이 아님"))
        if not isinstance(claims, list):
            claims = []
        n_claims += len(claims)

        # G2 답했으면 출처가 있다
        if status == "답함" and not claims:
            violations.append((qlabel, "-", "G2", "상태가 답함인데 주장이 없음"))

        # G8 통제 항목
        if q in ("T1", "T3", "T4"):
            if status != "자료에 없음":
                violations.append((qlabel, "-", "G8", f'상태가 "자료에 없음"이 아님: {status!r}'))
            if claims:
                violations.append((qlabel, "-", "G8", f"주장이 0개가 아님: {len(claims)}개"))
        if q == "T2" and status != "전제가 틀림":
            violations.append((qlabel, "-", "G8", f'상태가 "전제가 틀림"이 아님: {status!r}'))

        for ci, c in enumerate(claims, 1):
            if not isinstance(c, dict):
                violations.append((qlabel, ci, "G1", "주장이 JSON 객체가 아님"))
                continue
            num = c.get("원장 번호")
            rel = c.get("관계")
            val = c.get("값")
            ev = c.get("근거 문장")

            # G2 네 칸이 비어 있지 않다
            if status == "답함":
                for fld in CLAIM_FIELDS:
                    if empty(c.get(fld)):
                        violations.append((qlabel, ci, "G2", f'주장의 "{fld}" 칸이 비어 있음'))

            # G3 원장 번호가 실재한다
            num_ok = isinstance(num, int) and not isinstance(num, bool) and num in ledger
            if not empty(num) and not num_ok:
                violations.append((qlabel, ci, "G3", f"원장에 없는 번호: {num!r}"))

            # G5 관계 이름
            rel_ok = rel in RELATIONS
            if not empty(rel) and not rel_ok:
                violations.append((qlabel, ci, "G5", f"스키마 6절에 없는 관계: {rel!r}"))

            # G6 닫힌 목록 값
            if rel in CLOSED and not empty(val):
                if not (isinstance(val, str) and (val in CLOSED[rel] or val.startswith("기타: "))):
                    violations.append((qlabel, ci, "G6", f'"{rel}"의 목록에 없는 값: {val!r}'))

            # G7 펌이 원장과 맞는다
            if rel == "수행" and num_ok and not empty(val) and val != ledger[num]:
                violations.append((qlabel, ci, "G7",
                                   f"원장 {num}번의 펌은 {ledger[num]}인데 값은 {val!r}"))

            # G4 근거 문장이 원문에 있다(수행 + "원장"은 G7로 봄)
            if num_ok and not empty(ev) and not (rel == "수행" and ev == "원장"):
                if not isinstance(ev, str) or not in_raw(ev, raw[num]):
                    violations.append((qlabel, ci, "G4", f"근거 문장이 원장 {num}번 원문에 없음"))

            # G9 질문이 정한 조건
            if q in G9_LEDGER and num != G9_LEDGER[q]:
                violations.append((qlabel, ci, "G9",
                                   f"{q}의 주장은 원장 {G9_LEDGER[q]}번이어야 하는데 {num!r}"))
            if q in G9_VALUE and rel == G9_VALUE[q][0] and val != G9_VALUE[q][1]:
                violations.append((qlabel, ci, "G9",
                                   f'{q}에서 "{rel}" 값은 "{G9_VALUE[q][1]}"이어야 하는데 {val!r}'))

    if n_items == 0:
        input_error("질문을 하나도 읽지 못함(질문 0개)")

    print(f"검사한 질문 {n_items}개, 주장 {n_claims}개")
    if not violations:
        print("위반 없음")
        return 0
    order = {f"G{i}": i for i in range(1, 10)}
    violations.sort(key=lambda v: order[v[2]])
    print(f"위반 {len(violations)}건")
    print("질문\t주장\t규칙\t이유")
    for v in violations:
        print("\t".join(str(x) for x in v))
    return 1


if __name__ == "__main__":
    sys.exit(main())
