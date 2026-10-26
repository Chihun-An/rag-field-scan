# E5 사람 판정과 자동 판정(citation-judge, Codex) 비교
#
# 하는 일: e5-human-judge.md 표(번호, 사람 판정)와 e5-codex-output.md 표(번호, 판정)를 읽고,
#   e5-codex-key.json으로 단위 번호에 이어 e5-judge-claude.json의 citation-judge 판정을 붙인다.
#   40개를 모두 읽지 못하면 멈추고 읽은 개수만 낸다. 사람·Codex의 "정보 부족"은 "뒷받침 안 됨"으로 본다.
#   낼 것: 사람 대 citation-judge 일치 수·일치율과 2×2 표, 사람 대 Codex 일치 수·일치율과 2×2 표,
#   세 판정이 모두 같은 수, 사람 "정보 부족" 개수, 사람 원래 판정(세 값)별 citation-judge 판정과
#   Codex 원래 판정(세 값)의 표, 도메인별(1번, 2번, e5-judge-units.json의 도메인 칸) 일치율.
#   개수와 비율만 출력한다. 주장 값과 근거 문장은 출력하지 않는다. python 표준 라이브러리만 쓴다.
# 입력: deep/07-graphrag/experiments/e5-human-judge.md, e5-codex-output.md, e5-codex-key.json,
#   e5-judge-claude.json, e5-judge-units.json
# 출력: 표준 출력에 위의 표. 파일은 쓰지 않는다.
# 실행: python3 deep/07-graphrag/experiments/scripts/compare-e5-human-judge.py

import json
import re
import sys
from pathlib import Path

EXP = Path(__file__).resolve().parent.parent  # deep/07-graphrag/experiments
YES, NO, INFO, BAD = "뒷받침됨", "뒷받침 안 됨", "정보 부족", "형식 오류"
DOMAINS = [("1번", "ai-consulting"), ("2번", "oil-trade")]


def read_table(path):
    """'| 번호 | 판정 | ...' 표에서 번호 -> 판정."""
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def pct(a, b):
    return f"{a / b * 100:.1f}%" if b else "-"


def two_by_two(title, rows_name, cols_name, pairs):
    """pairs: [(행 판정, 열 판정)], 값은 뒷받침됨/뒷받침 안 됨."""
    agree = sum(1 for r, c in pairs if r == c)
    print(f"### {title}")
    print(f"일치: {agree}/{len(pairs)} ({pct(agree, len(pairs))})")
    print()
    print(f"{rows_name} \\ {cols_name}\t{YES}\t{NO}\t합계")
    for r in (YES, NO):
        row = [sum(1 for a, b in pairs if a == r and b == c) for c in (YES, NO)]
        print(f"{r}\t{row[0]}\t{row[1]}\t{sum(row)}")
    col = [sum(1 for _, b in pairs if b == c) for c in (YES, NO)]
    print(f"합계\t{col[0]}\t{col[1]}\t{sum(col)}")
    print()


def main():
    human = read_table(EXP / "e5-human-judge.md")
    codex = read_table(EXP / "e5-codex-output.md")
    keymap = {k["Codex 번호"]: k["단위 번호"] for k in json.loads((EXP / "e5-codex-key.json").read_text(encoding="utf-8"))}
    want = set(range(1, 41))
    if set(human) != want or set(codex) != want or set(keymap) != want:
        print(f"읽은 번호: 사람 {len(human)}개, Codex {len(codex)}개, 열쇠 {len(keymap)}개 — 멈춤")
        sys.exit(1)
    bad_vals = [n for n in want if human[n] not in (YES, NO, INFO) or codex[n] not in (YES, NO, INFO)]
    if bad_vals:
        print(f"판정 값을 알 수 없는 번호 {len(bad_vals)}개 — 멈춤")
        sys.exit(1)
    cj_all = {x["단위 번호"]: x["판정"] for x in json.loads((EXP / "e5-judge-claude.json").read_text(encoding="utf-8"))}
    dom_of = {u["번호"]: u["도메인"] for u in json.loads((EXP / "e5-judge-units.json").read_text(encoding="utf-8"))}
    if any(keymap[n] not in cj_all or keymap[n] not in dom_of for n in want):
        print("열쇠의 단위 번호 중 citation-judge 판정이나 단위 목록에 없는 것이 있음 — 멈춤")
        sys.exit(1)

    rows = []  # (사람 원래, 사람, Codex 원래, Codex, citation-judge, 도메인)
    for n in sorted(want):
        uid = keymap[n]
        h, c = human[n], codex[n]
        rows.append((h, NO if h == INFO else h, c, NO if c == INFO else c, cj_all[uid], dom_of[uid]))

    cj_bad = sum(1 for r in rows if r[4] == BAD)
    print("## 사람 판정 40개와 자동 판정 비교")
    print(f"읽은 번호: {len(rows)}개")
    print(f"사람 \"정보 부족\": {sum(1 for r in rows if r[0] == INFO)}개 (\"뒷받침 안 됨\"으로 봄)")
    print(f"Codex \"정보 부족\": {sum(1 for r in rows if r[2] == INFO)}개 (\"뒷받침 안 됨\"으로 봄)")
    print(f"citation-judge \"형식 오류\": {cj_bad}개")
    print()
    two_by_two("사람 대 citation-judge", "사람", "citation-judge", [(r[1], r[4]) for r in rows])
    two_by_two("사람 대 Codex", "사람", "Codex", [(r[1], r[3]) for r in rows])
    three = sum(1 for r in rows if r[1] == r[3] == r[4])
    print(f"### 세 판정이 모두 같은 수: {three}/{len(rows)} ({pct(three, len(rows))})")
    print()

    print("### 사람 원래 판정별 citation-judge 판정과 Codex 원래 판정")
    print(f"사람 원래 판정\t개수\tcitation-judge {YES}\tcitation-judge {NO}\tCodex {YES}\tCodex {NO}\tCodex {INFO}")
    for h in (YES, NO, INFO):
        sub = [r for r in rows if r[0] == h]
        vals = [len(sub)] + [sum(1 for r in sub if r[4] == v) for v in (YES, NO)] + \
               [sum(1 for r in sub if r[2] == v) for v in (YES, NO, INFO)]
        print(f"{h}\t" + "\t".join(map(str, vals)))
    print()

    print("### 도메인별 일치율")
    print("도메인\t개수\t사람 대 citation-judge\t사람 대 Codex")
    for label, dom in DOMAINS:
        sub = [r for r in rows if r[5] == dom]
        a = sum(1 for r in sub if r[1] == r[4])
        b = sum(1 for r in sub if r[1] == r[3])
        print(f"{label}\t{len(sub)}\t{a}/{len(sub)} ({pct(a, len(sub))})\t{b}/{len(sub)} ({pct(b, len(sub))})")


if __name__ == "__main__":
    main()
