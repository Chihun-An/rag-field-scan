# 1번 AI 컨설팅 E4 비교 스크립트 (사람 그래프 대 에이전트 그래프)
#
# 하는 일: experiments/e4-method.md의 정의대로 사람 그래프와 에이전트 그래프 1·2회차를 비교한다.
#   python 표준 라이브러리만 쓴다.
#   - closed: 닫힌 목록 관계(고객 산업, 적용 업무, 사용 기술)의 일치율(재현율)·정밀도, 수행 포함 참고값,
#     기타 줄 수, 회차끼리 자카드 지수를 계산한다.
#   - make-codex: 열린 값 관계(고객, 해결하려던 병목, 낸 성과)를 A/B로 섞어 Codex 판정 입력 파일과 열쇠 파일을 만든다.
#   - open run1|run2: Codex 판정 결과를 열쇠로 되돌려 열린 값의 재현율·정밀도를 계산한다.
# 입력(--base 폴더, 기본값 deep/07-graphrag/ai-consulting):
#   human-graph.csv, agent-graph-1.csv, agent-graph-2.csv (utf-8-sig, 머리줄 "사례 번호,관계,값,근거 문장")
#   make-codex는 shared/codex-judge-rules.md도 읽는다.
#   open은 --out 폴더의 e4-codex-key.json과 e4-codex-output-run1.md(또는 run2)를 읽는다.
# 출력(--out 폴더, 기본값 deep/07-graphrag/experiments):
#   closed → e4-closed-results.md(화면에도 출력)
#   make-codex → e4-codex-input-run1.md, e4-codex-input-run2.md, e4-codex-key.json
#   open → e4-open-results-run1.md(또는 run2)
# 비교 대상 사례는 사람 그래프에 있는 사례 번호다.
#
# 실행(저장소 맨 위에서):
#   python3 deep/07-graphrag/experiments/scripts/compare-graphs.py closed
#   python3 deep/07-graphrag/experiments/scripts/compare-graphs.py make-codex
#   python3 deep/07-graphrag/experiments/scripts/compare-graphs.py open run1

import argparse
import csv
import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_BASE = HERE.parent.parent / "ai-consulting"
DEFAULT_OUT = HERE.parent
RULES = HERE.parent.parent / "shared" / "codex-judge-rules.md"

CLOSED_RELS = ["고객 산업", "적용 업무", "사용 기술"]
OPEN_RELS = ["고객", "해결하려던 병목", "낸 성과"]
ABBR = {"고객": "고객", "해결하려던 병목": "병목", "낸 성과": "성과"}
RUNS = ["run1", "run2"]
SEED = 20261022

TASK = """## 할 일

아래 사례마다 A 목록과 B 목록이 있다. 두 목록은 같은 글에서 따로 뽑은 값이다. A의 값마다 B에 같은 뜻의 값이 있는지, B의 값마다 A에 같은 뜻의 값이 있는지 판정한다.

- 같은 뜻이면 "같음: 상대 번호"로 쓴다. 짝이 여럿이면 쉼표로 잇는다.
- 같은 뜻의 값이 없으면 "없음", 판단할 수 없으면 "정보 부족"으로 쓴다.
- 표현이 달라도 가리키는 대상이나 사실이 같으면 같은 뜻이다. 한쪽 값이 다른 쪽 값을 포함하면 같은 뜻으로 본다. 수치가 들어 있으면 수치까지 같아야 같은 뜻이다.
- 답은 표 하나로 쓴다. 칸은 "| 번호 | 판정 | 근거 |"이고, 모든 번호를 한 줄씩 빠짐없이 적는다."""

ID_RE = re.compile(r"^(\d+)-(고객|병목|성과)-([AB])(\d+)$")


def fail(msg):
    print(f"입력 오류: {msg}")
    sys.exit(2)


def load(path):
    if not path.is_file():
        fail(f"파일이 없음: {path}")
    with path.open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows or rows[0] != ["사례 번호", "관계", "값", "근거 문장"]:
        fail(f"머리줄이 다름: {path}")
    out = []
    for r in rows[1:]:
        if len(r) != 4:
            fail(f"4칸이 아닌 줄이 있음: {path}")
        out.append((int(r[0].strip()), r[1].strip(), " ".join(r[2].split())))
    return out


def load_all(base):
    return {"human": load(base / "human-graph.csv"),
            "run1": load(base / "agent-graph-1.csv"),
            "run2": load(base / "agent-graph-2.csv")}


def frac(n, d):
    return f"{n}/{d} (해당 없음)" if d == 0 else f"{n}/{d} ({100 * n / d:.1f}%)"


def is_other(v):
    return v.startswith("기타: ")


def matched_sets(h, a):
    # 기타 값은 글자가 같아도 자동으로 일치로 세지 않는다(양쪽 모두 기타면 Codex 판정 대상)
    hm = {x for x in h if not is_other(x[2]) and x in a}
    am = {x for x in a if not is_other(x[2]) and x in h}
    return hm, am


# ---------------------------------------------------------------- closed

def cmd_closed(base, out):
    g = load_all(base)
    targets = sorted({c for c, _, _ in g["human"]})
    lines = ["# E4 닫힌 목록 결과 (1번 도메인)", "",
             f"compare-graphs.py closed로 만들었다. 비교 대상 사례(사람 그래프의 사례 번호): {', '.join(map(str, targets))}", "",
             "- 일치: 사례 번호·관계·값이 모두 같다. 기타 값은 글자가 같아도 여기서는 일치로 세지 않는다(양쪽 모두 기타면 Codex 판정 대상, schema.md 8절).", ""]

    def pick(rows, rels, cases=None):
        return {x for x in rows if x[1] in rels and (cases is None or x[0] in cases)}

    h_all = pick(g["human"], CLOSED_RELS + ["수행"], set(targets))
    for run in RUNS:
        a_all = pick(g[run], CLOSED_RELS + ["수행"], set(targets))
        lines += [f"## {run}", "", "| 관계 | 일치율(재현율) | 정밀도 |", "|------|----------------|--------|"]
        tot_h = tot_a = tot_hm = tot_am = 0
        for rel in CLOSED_RELS:
            h = {x for x in h_all if x[1] == rel}
            a = {x for x in a_all if x[1] == rel}
            hm, am = matched_sets(h, a)
            lines.append(f"| {rel} | {frac(len(hm), len(h))} | {frac(len(am), len(a))} |")
            tot_h += len(h); tot_a += len(a); tot_hm += len(hm); tot_am += len(am)
        lines.append(f"| 합계 | {frac(tot_hm, tot_h)} | {frac(tot_am, tot_a)} |")
        h = {x for x in h_all if x[1] == "수행"}
        a = {x for x in a_all if x[1] == "수행"}
        hm, am = matched_sets(h, a)
        lines.append(f"| 참고: 수행 포함 합계 | {frac(tot_hm + len(hm), tot_h + len(h))} | {frac(tot_am + len(am), tot_a + len(a))} |")
        h_other = [x for x in h_all if x[1] in CLOSED_RELS and is_other(x[2])]
        a_other_keys = {(x[0], x[1]) for x in a_all if x[1] in CLOSED_RELS and is_other(x[2])}
        need = [x for x in h_other if (x[0], x[1]) in a_other_keys]
        lines += ["", f"- 사람 쪽 기타 줄: {len(h_other)}줄",
                  f"- 양쪽 모두 기타라 Codex 판정이 필요한 사람 줄(같은 사례·관계에 에이전트 기타가 있음): {len(need)}줄. 위 표에서는 불일치로 셌다", ""]

    lines += ["## 회차끼리 일관성 (자카드 지수, 수행 제외)", "", "| 범위 | 자카드 지수 |", "|------|-------------|"]
    r1 = pick(g["run1"], CLOSED_RELS)
    r2 = pick(g["run2"], CLOSED_RELS)
    all_cases = sorted({x[0] for x in r1 | r2})
    lines.append(f"| 전체(두 회차의 모든 사례, {len(all_cases)}건) | {frac(len(r1 & r2), len(r1 | r2))} |")
    t1 = {x for x in r1 if x[0] in targets}
    t2 = {x for x in r2 if x[0] in targets}
    lines.append(f"| 비교 대상 사례({len(targets)}건) | {frac(len(t1 & t2), len(t1 | t2))} |")
    text = "\n".join(lines) + "\n"
    (out / "e4-closed-results.md").write_text(text, encoding="utf-8")
    print(text, end="")


# ---------------------------------------------------------------- make-codex

def cmd_make_codex(base, out):
    g = load_all(base)
    targets = sorted({c for c, _, _ in g["human"]})
    if not RULES.is_file():
        fail(f"판정 규칙 파일이 없음: {RULES}")
    rules = RULES.read_text(encoding="utf-8").rstrip("\n")
    for word in ("사람", "에이전트"):
        if word in rules or word in TASK:
            fail(f'입력 파일의 고정 문장에 "{word}"가 들어 있음')
    rng = random.Random(SEED)
    key = {"seed": SEED}
    for run in RUNS:
        parts = [rules, "", TASK, ""]
        key[run] = {}
        for c in targets:
            for rel in OPEN_RELS:
                hv = [v for cc, r, v in g["human"] if cc == c and r == rel]
                av = [v for cc, r, v in g[run] if cc == c and r == rel]
                human_is_a = rng.random() < 0.5
                A, B = (hv, av) if human_is_a else (av, hv)
                ab = ABBR[rel]
                parts += [f"### 사례 {c} · {rel}", "", "A"]
                parts += [f"- {c}-{ab}-A{i}: {v}" for i, v in enumerate(A, 1)] or ["- (값 없음)"]
                parts += ["", "B"]
                parts += [f"- {c}-{ab}-B{i}: {v}" for i, v in enumerate(B, 1)] or ["- (값 없음)"]
                parts.append("")
                key[run][f"{c}-{ab}"] = {"사례": c, "관계": rel, "사람": "A" if human_is_a else "B",
                                        "A 개수": len(A), "B 개수": len(B)}
        (out / f"e4-codex-input-{run}.md").write_text("\n".join(parts), encoding="utf-8")
    (out / "e4-codex-key.json").write_text(json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"만듦: {out / 'e4-codex-input-run1.md'}, {out / 'e4-codex-input-run2.md'}, {out / 'e4-codex-key.json'}")


# ---------------------------------------------------------------- open

def cmd_open(run, out):
    kp = out / "e4-codex-key.json"
    op = out / f"e4-codex-output-{run}.md"
    if not kp.is_file():
        fail(f"열쇠 파일이 없음: {kp}")
    if not op.is_file():
        fail(f"Codex 판정 파일이 없음: {op}")
    key = json.loads(kp.read_text(encoding="utf-8"))[run]

    expected = {}  # 번호 -> (관계, 사람인지)
    for sec, k in key.items():
        for side in "AB":
            for i in range(1, k[f"{side} 개수"] + 1):
                expected[f"{sec}-{side}{i}"] = (k["관계"], side == k["사람"])

    verdict = {}
    dup, unknown_ids, unread = [], [], []
    for line in op.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if not cells or not ID_RE.match(cells[0]):
            continue
        vid = cells[0]
        j = cells[1] if len(cells) > 1 else ""
        if vid not in expected:
            unknown_ids.append(vid)
            continue
        if vid in verdict:
            dup.append(vid)
            continue
        if j.startswith("같음"):
            verdict[vid] = "같음"
        elif j.startswith("없음"):
            verdict[vid] = "없음"
        elif j.startswith("정보 부족"):
            verdict[vid] = "정보 부족"
        else:
            verdict[vid] = "읽지 못함"
            unread.append(vid)

    missing = [v for v in expected if v not in verdict]
    lines = [f"# E4 열린 값 결과 {run} (1번 도메인)", "",
             f"compare-graphs.py open {run}으로 만들었다. 입력: e4-codex-output-{run}.md, 열쇠: e4-codex-key.json", "",
             "- \"정보 부족\", 판정이 빠진 번호, 읽지 못한 판정은 짝 없음으로 셌다.", "",
             "| 관계 | 재현율(사람 값) | 정밀도(에이전트 값) |", "|------|-----------------|---------------------|"]
    th = tm_h = ta = tm_a = 0
    for rel in OPEN_RELS:
        hs = [v for v, (r, h) in expected.items() if r == rel and h]
        as_ = [v for v, (r, h) in expected.items() if r == rel and not h]
        mh = sum(1 for v in hs if verdict.get(v) == "같음")
        ma = sum(1 for v in as_ if verdict.get(v) == "같음")
        lines.append(f"| {rel} | {frac(mh, len(hs))} | {frac(ma, len(as_))} |")
        th += len(hs); tm_h += mh; ta += len(as_); tm_a += ma
    lines.append(f"| 합계 | {frac(tm_h, th)} | {frac(tm_a, ta)} |")
    n_info = sum(1 for v in verdict.values() if v == "정보 부족")
    lines += ["", f"- \"정보 부족\": {n_info}개",
              f"- 판정이 빠진 번호: {', '.join(missing) if missing else '없음'}",
              f"- 판정을 읽지 못한 번호: {', '.join(unread) if unread else '없음'}",
              f"- 두 번 나온 번호(처음 것만 씀): {', '.join(dup) if dup else '없음'}",
              f"- 열쇠에 없는 번호: {', '.join(unknown_ids) if unknown_ids else '없음'}"]
    text = "\n".join(lines) + "\n"
    (out / f"e4-open-results-{run}.md").write_text(text, encoding="utf-8")
    print(text, end="")


def main():
    p = argparse.ArgumentParser(description="E4 비교 스크립트")
    p.add_argument("command", choices=["closed", "make-codex", "open"])
    p.add_argument("run", nargs="?", choices=RUNS)
    p.add_argument("--base", default=str(DEFAULT_BASE))
    p.add_argument("--out", default=str(DEFAULT_OUT))
    a = p.parse_args()
    base, out = Path(a.base), Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    if a.command == "closed":
        cmd_closed(base, out)
    elif a.command == "make-codex":
        cmd_make_codex(base, out)
    else:
        if not a.run:
            fail("open에는 run1 또는 run2를 주세요")
        cmd_open(a.run, out)


if __name__ == "__main__":
    main()
