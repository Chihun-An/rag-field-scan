# 1번 AI 컨설팅 그래프 CSV 형식 검사 스크립트 (E4)
#
# 하는 일: 사람 그래프·에이전트 그래프 CSV(ai-consulting/schema.md 7절 기록 형식)가 형식 규칙을 지키는지 검사한다.
#   값이 맞는지(사람 대 에이전트 비교)는 보지 않는다. python 표준 라이브러리만 쓴다.
# 입력: 명령줄 인자 1개 — 검사할 CSV 파일(utf-8-sig, 머리줄 "사례 번호,관계,값,근거 문장")
# 출력: 표준 출력에 위반마다 "줄 N: 규칙 이름"(count는 "사례 N: count: 관계 이름") 한 줄,
#   끝에 "사례 X건, 줄 Y개, 위반 Z건". 값과 근거 문장 내용은 출력하지 않는다.
# 종료 코드: 0 위반 없음, 1 위반 있음, 2 파일이 없거나 머리줄이 틀림.
#
# 검사 규칙: header, columns, case-id, relation, empty, closed-list, source-ledger, count, duplicate
# 실행: python3 deep/07-graphrag/experiments/scripts/check-graph-csv.py <csv 경로>

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

HEADER = ["사례 번호", "관계", "값", "근거 문장"]
RELATIONS = ["수행", "고객", "고객 산업", "적용 업무", "해결하려던 병목", "사용 기술", "낸 성과"]
CLOSED = {
    "수행": ["McKinsey", "BCG", "Bain", "Deloitte", "PwC", "EY", "KPMG"],
    "고객 산업": ["에너지", "소재", "산업재", "경기소비재", "필수소비재", "헬스케어", "금융",
              "정보기술", "커뮤니케이션 서비스", "유틸리티", "부동산"],
    "적용 업무": ["AI 전략·로드맵 수립", "AI 활용 과제 발굴·우선순위 선정", "사업성·투자 타당성 분석",
              "데이터·기술 기반 구축", "AI 신상품·신사업 기획 및 사업화", "업무 프로세스 재설계",
              "AI 솔루션 개발·실증", "전사 확산·성과 관리", "AI 거버넌스·리스크 관리", "조직·인력·변화 관리"],
    "사용 기술": ["생성형 AI(LLM 포함)", "예측·분류 머신러닝", "추천·개인화", "컴퓨터 비전",
              "음성 인식·합성", "최적화·시뮬레이션"],
}
# 사례마다 관계별 줄 수(최소, 최대)
COUNT = {"수행": (1, 1), "고객": (1, 1), "고객 산업": (0, 1), "적용 업무": (1, 3),
         "해결하려던 병목": (1, 3), "사용 기술": (0, 3), "낸 성과": (0, 3)}


def main():
    if len(sys.argv) != 2:
        print("사용: python3 check-graph-csv.py <csv 경로>")
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"파일이 없음: {path}")
        return 2
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] != HEADER:
        print("줄 1: header")
        return 2

    out = []
    cases = set()
    counts = defaultdict(Counter)  # 사례 번호 -> 관계별 줄 수
    seen = defaultdict(list)       # (사례 번호, 관계, 값) -> 줄 번호들
    n_lines = 0

    # 줄 번호는 CSV 레코드 순번(머리줄이 1). 값 안에 줄바꿈이 없으면 파일 줄 번호와 같다
    for ln, r in enumerate(rows[1:], 2):
        n_lines += 1
        if len(r) != 4:
            out.append(f"줄 {ln}: columns")
            continue
        cid_s, rel, val, ev = (x.strip() for x in r)

        cid = None
        if cid_s.isdigit() and 1 <= int(cid_s) <= 17:
            cid = int(cid_s)
            cases.add(cid)
        else:
            out.append(f"줄 {ln}: case-id")

        rel_ok = rel in RELATIONS
        if not rel_ok:
            out.append(f"줄 {ln}: relation")

        if not val or not ev:
            out.append(f"줄 {ln}: empty")

        if rel in CLOSED and val:
            allowed = val in CLOSED[rel] or (rel != "수행" and val.startswith("기타: "))
            if not allowed:
                out.append(f"줄 {ln}: closed-list")

        if rel == "수행" and ev != "원장":
            out.append(f"줄 {ln}: source-ledger")

        if cid is not None and rel_ok:
            counts[cid][rel] += 1
            seen[(cid, rel, val)].append(ln)

    for (cid, rel, val), lns in seen.items():
        if len(lns) > 1:
            for ln in lns:
                out.append(f"줄 {ln}: duplicate")

    count_out = []
    for cid in sorted(cases):
        for rel in RELATIONS:
            lo, hi = COUNT[rel]
            if not lo <= counts[cid][rel] <= hi:
                count_out.append(f"사례 {cid}: count: {rel}")

    out.sort(key=lambda s: int(s.split()[1].rstrip(":")))
    for line in out + count_out:
        print(line)
    n_viol = len(out) + len(count_out)
    print(f"사례 {len(cases)}건, 줄 {n_lines}개, 위반 {n_viol}건")
    return 0 if n_viol == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
