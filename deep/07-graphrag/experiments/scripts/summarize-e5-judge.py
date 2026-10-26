# E5 판정 결과 세기 (층위 2)
#
# 하는 일:
#   (1) 답별 citation-judge 결과: e5-judge-units.json의 "나온 곳"으로 고유 단위의 판정을 원래 자리마다 펼쳐,
#       답 네 개(1번 검색만, 1번 그래프 경유, 2번 검색만, 2번 그래프 경유)마다 단위 수, 뒷받침됨 수,
#       뒷받침 안 됨 수, 형식 오류 수, 뒷받침됨 비율을 센다. 질문 종류별(A: Q1·Q2, B: Q3·Q4, C: Q5·Q6,
#       D: Q7·Q8, E: Q9·Q10, 통제: T1~T5)로도 같은 것을 센다.
#   (2) 두 판정기 비교: e5-codex-output.md 표에서 번호와 판정을 읽고 e5-codex-key.json으로 단위 번호에 잇는다.
#       Codex의 "정보 부족"은 "뒷받침 안 됨"으로 본다. 40개에서 일치 수, 일치율, 2×2 표
#       (Codex 판정 × citation-judge 판정), "정보 부족" 개수를 낸다. 표에서 40개를 모두 읽지 못하면 멈추고
#       읽은 개수만 낸다.
#   (3) 지어낸 답(방법 7절): 답마다 골든 룰 G8 위반 수(두 검사 스크립트를 다시 돌려 출력에서 G8 줄을 셈)와
#       (1)의 뒷받침 안 됨 수를 함께 적는다.
#   개수와 비율만 출력한다. 주장 값, 근거 문장, 요약은 출력하지 않는다. python 표준 라이브러리만 쓴다.
# 입력: deep/07-graphrag/experiments/e5-judge-units.json, e5-judge-claude.json, e5-codex-output.md, e5-codex-key.json,
#   deep/07-graphrag/ai-consulting/e5-answers-search.json, e5-answers-graph.json,
#   deep/07-graphrag/oil-trade/e5-answers-search.json, e5-answers-graph.json(골든 룰 검사 스크립트에 넘김),
#   deep/07-graphrag/experiments/scripts/check-golden-rules.py, check-golden-rules-oil-trade.py
# 출력: 표준 출력에 (1)~(3)의 표. 파일은 쓰지 않는다.
# 실행: python3 deep/07-graphrag/experiments/scripts/summarize-e5-judge.py

import json
import re
import subprocess
import sys
from pathlib import Path

G = Path(__file__).resolve().parent.parent.parent  # deep/07-graphrag
EXP = G / "experiments"
SCRIPTS = EXP / "scripts"
ANSWERS = [  # (이름, 도메인, 방식, 골든 룰 검사 스크립트)
    ("1번 검색만", "ai-consulting", "search", "check-golden-rules.py"),
    ("1번 그래프 경유", "ai-consulting", "graph", "check-golden-rules.py"),
    ("2번 검색만", "oil-trade", "search", "check-golden-rules-oil-trade.py"),
    ("2번 그래프 경유", "oil-trade", "graph", "check-golden-rules-oil-trade.py"),
]
KINDS = [("A", ["Q1", "Q2"]), ("B", ["Q3", "Q4"]), ("C", ["Q5", "Q6"]), ("D", ["Q7", "Q8"]),
         ("E", ["Q9", "Q10"]), ("통제", ["T1", "T2", "T3", "T4", "T5"])]
KIND_OF = {q: k for k, qs in KINDS for q in qs}
YES, NO, BAD, INFO = "뒷받침됨", "뒷받침 안 됨", "형식 오류", "정보 부족"


def pct(a, b):
    return f"{a / b * 100:.1f}%" if b else "-"


def count(verdicts):
    n = len(verdicts)
    y = sum(1 for v in verdicts if v == YES)
    no = sum(1 for v in verdicts if v == NO)
    bad = sum(1 for v in verdicts if v == BAD)
    return [str(n), str(y), str(no), str(bad), pct(y, n)]


def table(head, rows):
    print("\t".join(head))
    for r in rows:
        print("\t".join(r))


def main():
    units = json.loads((EXP / "e5-judge-units.json").read_text(encoding="utf-8"))
    judged = {x["단위 번호"]: x["판정"] for x in json.loads((EXP / "e5-judge-claude.json").read_text(encoding="utf-8"))}
    missing = [u["번호"] for u in units if u["번호"] not in judged]
    if missing:
        print(f"citation-judge 판정이 없는 단위 {len(missing)}개 — 멈춤")
        sys.exit(1)

    # (1) 고유 단위 판정을 원래 자리마다 펼친다
    spread = {name: [] for name, *_ in ANSWERS}  # 이름 -> [(질문, 판정)]
    key_of = {(dom, m): name for name, dom, m, _ in ANSWERS}
    for u in units:
        for place in u["나온 곳"]:
            spread[key_of[(u["도메인"], place["방식"])]].append((place["질문"], judged[u["번호"]]))

    head = ["답", "단위 수", "뒷받침됨", "뒷받침 안 됨", "형식 오류", "뒷받침됨 비율"]
    print("## (1) 답별 citation-judge 결과 (고유 단위 판정을 원래 자리마다 펼침)")
    print(f"고유 단위 {len(units)}개, 펼친 단위 {sum(len(v) for v in spread.values())}개")
    print()
    table(head, [[name] + count([v for _, v in spread[name]]) for name, *_ in ANSWERS])
    print()
    print("### 질문 종류별")
    for name, *_ in ANSWERS:
        print()
        print(f"[{name}]")
        table(["종류"] + head[1:],
              [[k] + count([v for q, v in spread[name] if KIND_OF.get(q) == k]) for k, _ in KINDS])
    print()

    # (2) 두 판정기 비교
    print("## (2) 두 판정기 비교 (Codex 표본 40개)")
    codex = {}
    for line in (EXP / "e5-codex-output.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            codex[int(m.group(1))] = m.group(2)
    keymap = {k["Codex 번호"]: k["단위 번호"] for k in json.loads((EXP / "e5-codex-key.json").read_text(encoding="utf-8"))}
    if len(codex) != 40 or set(codex) != set(range(1, 41)) or set(keymap) != set(codex):
        print(f"표에서 읽은 번호 {len(codex)}개 — 멈춤")
        sys.exit(1)
    unknown = [n for n, v in codex.items() if v not in (YES, NO, INFO)]
    if unknown:
        print(f"판정 값을 알 수 없는 번호 {len(unknown)}개 — 멈춤")
        sys.exit(1)

    pairs = []  # (Codex 원래 판정, Codex 판정(정보 부족→뒷받침 안 됨), citation-judge 판정)
    for n in range(1, 41):
        raw = codex[n]
        pairs.append((raw, NO if raw == INFO else raw, judged[keymap[n]]))
    agree = sum(1 for _, c, j in pairs if c == j)
    print(f"읽은 번호: {len(pairs)}개")
    print(f"일치: {agree}/{len(pairs)} ({pct(agree, len(pairs))})")
    print(f"Codex \"정보 부족\": {sum(1 for r, _, _ in pairs if r == INFO)}개 (\"뒷받침 안 됨\"으로 봄)")
    print(f"citation-judge \"형식 오류\": {sum(1 for _, _, j in pairs if j == BAD)}개")
    print()
    cj_vals = [YES, NO]
    print("Codex \\ citation-judge\t" + "\t".join(cj_vals) + "\t합계")
    for c in (YES, NO):
        row = [sum(1 for _, cc, j in pairs if cc == c and j == jv) for jv in cj_vals]
        print(f"{c}\t" + "\t".join(map(str, row)) + f"\t{sum(row)}")
    col = [sum(1 for _, _, j in pairs if j == jv) for jv in cj_vals]
    print("합계\t" + "\t".join(map(str, col)) + f"\t{sum(col)}")
    print()
    print("Codex 원래 판정별 citation-judge 판정")
    print("Codex 원래 판정\t" + "\t".join(cj_vals) + "\t합계")
    for r in (YES, NO, INFO):
        row = [sum(1 for rr, _, j in pairs if rr == r and j == jv) for jv in cj_vals]
        print(f"{r}\t" + "\t".join(map(str, row)) + f"\t{sum(row)}")
    print()

    # (3) 지어낸 답
    print("## (3) 지어낸 답 (방법 7절)")
    rows = []
    for name, dom, m, script in ANSWERS:
        ans = G / dom / f"e5-answers-{m}.json"
        out = subprocess.run([sys.executable, str(SCRIPTS / script), str(ans)],
                             capture_output=True, text=True, encoding="utf-8").stdout
        g8 = sum(1 for line in out.splitlines() if "G8" in line.split("\t"))
        no = sum(1 for _, v in spread[name] if v == NO)
        rows.append([name, str(g8), str(no)])
    table(["답", "골든 룰 G8 위반 수(통제 항목)", "citation-judge 뒷받침 안 됨 수"], rows)


if __name__ == "__main__":
    main()
