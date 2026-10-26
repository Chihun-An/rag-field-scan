# E5 채점 점수 계산 (e5-method.md 6·7절)
#
# 하는 일: 채점 숫자 표(A/B)를 e5-blind-key.json으로 방식(검색만, 그래프 경유)에 잇고 점수를 낸다.
#   - 질문 점수 = 맞힘 / 기대 항목 수 (Q1~Q10, T5)
#   - 종류 점수 = 두 질문 점수의 평균(A: Q1·Q2, B: Q3·Q4, C: Q5·Q6, D: Q7·Q8, E: Q9·Q10).
#     도메인마다 두 방식의 종류 점수, 차이(그래프 경유 − 검색만, %p), 판정(+10%p 이상 "그래프 경유가 나음",
#     −10%p 이하 "그래프 경유가 못함", 그 사이 "비슷")
#   - 도메인마다 Q1~Q10 전체 점수(다섯 종류 점수의 평균)와 차이. 두 도메인의 차이끼리 비교
#     (2번 차이 − 1번 차이, %p)와 판정(10%p 이상 벌어지면 차이가 더 큰 도메인, 아니면 "비슷")
#   - 통제 항목: T1~T4는 골든 룰 G8을 통과하면 1, 아니면 0(두 골든 룰 검사 스크립트를 네 답에 다시 돌려
#     G8 줄을 질문별로 셈). T5는 질문 점수. 방식별 통제 점수 합계
#   - 방식별 틀린 항목 합계(Q1~Q10)
#   10%p 경계에서 소수 오차가 나지 않도록 분수(fractions)로 계산하고, 출력할 때만 소수로 바꾼다
#   (점수는 소수 첫째 자리 %, 차이는 반올림이 헷갈리지 않도록 소수 둘째 자리 %p).
#   숫자만 출력한다. python 표준 라이브러리만 쓴다.
# 입력: deep/07-graphrag/experiments/e5-scores-ai-consulting.md, e5-scores-oil-trade.md, e5-blind-key.json,
#   deep/07-graphrag/ai-consulting/e5-answers-search.json, e5-answers-graph.json,
#   deep/07-graphrag/oil-trade/e5-answers-search.json, e5-answers-graph.json(골든 룰 검사 스크립트에 넘김),
#   deep/07-graphrag/experiments/scripts/check-golden-rules.py, check-golden-rules-oil-trade.py
# 출력: 표준 출력에 표. 파일은 쓰지 않는다.
# 실행: python3 deep/07-graphrag/experiments/scripts/score-e5.py

import json
import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

G = Path(__file__).resolve().parent.parent.parent  # deep/07-graphrag
EXP = G / "experiments"
SCRIPTS = EXP / "scripts"
DOMAINS = [("1번", "ai-consulting", "check-golden-rules.py"), ("2번", "oil-trade", "check-golden-rules-oil-trade.py")]
METHODS = [("search", "검색만"), ("graph", "그래프 경유")]
KINDS = [("A", "Q1", "Q2"), ("B", "Q3", "Q4"), ("C", "Q5", "Q6"), ("D", "Q7", "Q8"), ("E", "Q9", "Q10")]
QS = [f"Q{i}" for i in range(1, 11)]
TEN = Fraction(10)


def pct(x):
    return f"{float(x * 100):.1f}%"


def pp(x):
    return f"{float(x):+.2f}%p"


def verdict(diff_pp):
    if diff_pp >= TEN:
        return "그래프 경유가 나음"
    if diff_pp <= -TEN:
        return "그래프 경유가 못함"
    return "비슷"


def read_scores(path):
    """질문 -> {"기대": n, "A": (맞힘, 틀린), "B": (맞힘, 틀린)}"""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*((?:Q|T)\d+)\s*\|" + r"\s*(\d+)\s*\|" * 5 + r"\s*$", line)
        if m:
            q, exp, ah, aw, bh, bw = m.group(1), *map(int, m.groups()[1:])
            out[q] = {"기대": exp, "A": (ah, aw), "B": (bh, bw)}
    return out


def g8_by_question(script, answers):
    out = subprocess.run([sys.executable, str(SCRIPTS / script), str(answers)],
                         capture_output=True, text=True, encoding="utf-8").stdout
    qs = []
    for line in out.splitlines():
        cols = line.split("\t")
        if "G8" in cols:
            qs.append(cols[0])
    return qs


def main():
    key = json.loads((EXP / "e5-blind-key.json").read_text(encoding="utf-8"))
    results = {}  # dom -> method -> dict
    for label, dom, script in DOMAINS:
        table = read_scores(EXP / f"e5-scores-{dom}.md")
        need = QS + ["T5"]
        if any(q not in table for q in need):
            print(f"{label}: 채점 표에서 읽지 못한 질문 {[q for q in need if q not in table]} — 멈춤")
            sys.exit(1)
        side_of = {key[dom]["A"]: "A", key[dom]["B"]: "B"}
        if set(side_of) != {"search", "graph"}:
            print(f"{label}: 열쇠에서 방식을 읽지 못함 — 멈춤")
            sys.exit(1)
        results[dom] = {}
        for method, _ in METHODS:
            side = side_of[method]
            qscore = {q: Fraction(table[q][side][0], table[q]["기대"]) for q in need}
            kinds = {k: (qscore[a] + qscore[b]) / 2 for k, a, b in KINDS}
            overall = sum(kinds.values()) / len(kinds)
            wrong = sum(table[q][side][1] for q in QS)
            g8 = g8_by_question(script, G / dom / f"e5-answers-{method}.json")
            ctrl = {t: (0 if t in g8 else 1) for t in ("T1", "T2", "T3", "T4")}
            results[dom][method] = {"side": side, "q": qscore, "kinds": kinds, "overall": overall,
                                    "wrong": wrong, "ctrl": ctrl, "t5": qscore["T5"],
                                    "ctrl_sum": sum(ctrl.values()) + qscore["T5"]}

    for label, dom, _ in DOMAINS:
        s, g = results[dom]["search"], results[dom]["graph"]
        print(f"## {label} ({dom})")
        print()
        print("### 질문 점수")
        print("질문\t검색만\t그래프 경유")
        for q in QS + ["T5"]:
            print(f"{q}\t{pct(s['q'][q])}\t{pct(g['q'][q])}")
        print()
        print("### 종류 점수")
        print("종류\t검색만\t그래프 경유\t차이(그래프 경유 − 검색만)\t판정")
        for k, _, _ in KINDS:
            d = (g["kinds"][k] - s["kinds"][k]) * 100
            print(f"{k}\t{pct(s['kinds'][k])}\t{pct(g['kinds'][k])}\t{pp(d)}\t{verdict(d)}")
        d = (g["overall"] - s["overall"]) * 100
        print(f"Q1~Q10 전체\t{pct(s['overall'])}\t{pct(g['overall'])}\t{pp(d)}\t{verdict(d)}")
        print()
        print("### 통제 항목 (T1~T4: G8 통과 1, 아니면 0 / T5: 질문 점수)")
        print("방식\tT1\tT2\tT3\tT4\tT5\t합계(5점 만점)")
        for method, name in METHODS:
            r = results[dom][method]
            c = r["ctrl"]
            print(f"{name}\t{c['T1']}\t{c['T2']}\t{c['T3']}\t{c['T4']}\t{float(r['t5']):.2f}\t{float(r['ctrl_sum']):.2f}")
        print()
        print("### 틀린 항목 합계 (Q1~Q10)")
        print("방식\t틀린 항목")
        for method, name in METHODS:
            print(f"{name}\t{results[dom][method]['wrong']}")
        print()

    print("## 두 도메인 비교 (Q1~Q10 전체 점수의 차이)")
    diffs = {dom: (results[dom]["graph"]["overall"] - results[dom]["search"]["overall"]) * 100 for _, dom, _ in DOMAINS}
    print("도메인\t검색만\t그래프 경유\t차이(그래프 경유 − 검색만)")
    for label, dom, _ in DOMAINS:
        print(f"{label}\t{pct(results[dom]['search']['overall'])}\t{pct(results[dom]['graph']['overall'])}\t{pp(diffs[dom])}")
    gap = diffs["oil-trade"] - diffs["ai-consulting"]
    if gap >= TEN:
        v = "2번이 효과가 더 큼"
    elif gap <= -TEN:
        v = "1번이 효과가 더 큼"
    else:
        v = "비슷"
    print(f"2번 차이 − 1번 차이\t{pp(gap)}\t판정\t{v}")


if __name__ == "__main__":
    main()
