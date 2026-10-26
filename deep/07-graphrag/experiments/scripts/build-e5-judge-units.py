# E5 판정 단위와 Codex 표본 만들기 (판정 전)
#
# 하는 일: E5 답 네 개에서 판정 단위(상태가 "답함"인 답의 주장 하나와 그 근거 전부)를 뽑고,
#   같은 도메인 안에서 같은 주장·같은 근거인 단위를 하나로 합친다(열쇠를 만들 때만 공백을 모두 지움).
#   1번에서 관계가 "수행"이고 근거 문장이 "원장"인 주장은 뺀다(골든 룰 G7이 봄).
#   고유 단위에서 Codex 표본 40개를 random.Random(20261022).sample로 뽑는다. 판정은 하지 않는다.
#   python 표준 라이브러리만 쓴다.
# 입력: deep/07-graphrag/ai-consulting/e5-answers-search.json, e5-answers-graph.json,
#   deep/07-graphrag/oil-trade/e5-answers-search.json, e5-answers-graph.json,
#   deep/07-graphrag/shared/codex-judge-rules.md("1." 줄부터 "5." 줄까지)
# 출력: deep/07-graphrag/experiments/e5-judge-units.json(단위 목록),
#   e5-codex-input.md(Codex 판정 입력, 도메인·방식·질문·단위 번호 없음), e5-codex-key.json(Codex 번호와 단위 번호의 짝).
#   표준 출력에 답 파일별 단위 수, 도메인별 고유 단위 수, 전체 고유 단위 수, 표본 수.
# 실행: python3 deep/07-graphrag/experiments/scripts/build-e5-judge-units.py

import json
import random
import re
from pathlib import Path

G = Path(__file__).resolve().parent.parent.parent  # deep/07-graphrag
EXP = G / "experiments"
FILES = [("ai-consulting", "search"), ("ai-consulting", "graph"), ("oil-trade", "search"), ("oil-trade", "graph")]
GUIDE = ('아래 1~40번마다, 근거 문장이 주장을 뒷받침하는지 판정한다. 판정 값은 "뒷받침됨" 또는 "뒷받침 안 됨"이고, '
         '근거 문장만으로 판단할 수 없으면 "정보 부족"으로 쓴다. 근거 문장 칸에는 판단에 쓴 근거 문장의 표현을 짧게 쓴다.')
OT_FIELDS = ["주어", "관계", "값", "분류 체계", "업무 단계", "주체"]


def ns(v):
    return re.sub(r"\s+", "", "" if v is None else str(v))


def units_of(dom, items):
    out = []
    for item in items:
        if item.get("상태") != "답함":
            continue
        for ci, c in enumerate(item.get("주장") or [], 1):
            if dom == "ai-consulting":
                if c.get("관계") == "수행" and c.get("근거 문장") == "원장":
                    continue
                claim = {k: c.get(k) for k in ("원장 번호", "관계", "값")}
                ev = [{"원장 번호": c.get("원장 번호"), "위치": "", "근거 문장": c.get("근거 문장")}]
                key = (ns(c.get("원장 번호")), ns(c.get("관계")), ns(c.get("값")), ns(c.get("근거 문장")))
            else:
                claim = {k: c.get(k) for k in OT_FIELDS}
                ev = [{"원장 번호": e.get("원장 번호"), "위치": e.get("위치"), "근거 문장": e.get("근거 문장")}
                      for e in (c.get("근거") or [])]
                key = tuple(ns(c.get(k)) for k in OT_FIELDS) + (
                    tuple(sorted((ns(e["원장 번호"]), ns(e["근거 문장"])) for e in ev)),)
            out.append((key, claim, ev, item.get("질문"), ci))
    return out


def claim_text(dom, u):
    c = u["주장"]
    if dom == "ai-consulting":
        return f"원장 {c['원장 번호']}번 사례 — {c['관계']}: {c['값']}"
    s = f"{c['주어']} — {c['관계']}: {c['값']}"
    for k in ("분류 체계", "업무 단계", "주체"):
        if c.get(k):
            s += f" ({k}: {c[k]})"
    return s


def main():
    units, index, per_file, per_dom = [], {}, {}, {}
    for dom, m in FILES:
        items = json.loads((G / dom / f"e5-answers-{m}.json").read_text(encoding="utf-8"))
        found = units_of(dom, items)
        per_file[(dom, m)] = len(found)
        for key, claim, ev, q, ci in found:
            k = (dom, key)
            if k not in index:
                index[k] = len(units)
                units.append({"번호": f"U{len(units) + 1:03d}", "도메인": dom, "주장": claim, "근거": ev, "나온 곳": []})
                per_dom[dom] = per_dom.get(dom, 0) + 1
            units[index[k]]["나온 곳"].append({"방식": m, "질문": q, "주장 순번": ci})

    (EXP / "e5-judge-units.json").write_text(json.dumps(units, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    ids = sorted(u["번호"] for u in units)
    sample = random.Random(20261022).sample(ids, min(40, len(ids)))
    by_id = {u["번호"]: u for u in units}

    rules = (G / "shared" / "codex-judge-rules.md").read_text(encoding="utf-8").split("\n")
    s = next(i for i, l in enumerate(rules) if l.startswith("1. "))
    e = next(i for i, l in enumerate(rules) if l.startswith("5. "))
    lines = rules[s:e + 1] + ["", GUIDE, ""]
    for n, uid in enumerate(sample, 1):
        u = by_id[uid]
        lines += [f"### {n}", f"주장: {claim_text(u['도메인'], u)}", "근거 문장:"]
        for ev in u["근거"]:
            where = f"원장 {ev['원장 번호']}번, {ev['위치']}" if ev.get("위치") else f"원장 {ev['원장 번호']}번"
            lines.append(f"- {ev['근거 문장']} ({where})")
        lines.append("")
    (EXP / "e5-codex-input.md").write_text("\n".join(lines), encoding="utf-8")
    key = [{"Codex 번호": n, "단위 번호": uid} for n, uid in enumerate(sample, 1)]
    (EXP / "e5-codex-key.json").write_text(json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for (dom, m), n in per_file.items():
        print(f"{dom} {m}: 단위 {n}개")
    for dom in ("ai-consulting", "oil-trade"):
        print(f"{dom} 고유 단위: {per_dom.get(dom, 0)}개")
    print(f"전체 고유 단위: {len(units)}개")
    print(f"Codex 표본: {len(sample)}개")


if __name__ == "__main__":
    main()
