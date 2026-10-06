# 실험 결과 파일의 답변 원문을 문장 단위로 기계적으로 나눠 층위 2 판정 쌍(P 절)을 만든다.
#
# 하는 일:
#   1. 결과 파일의 각 "## Q<숫자>" 절에서 "실제 답변:" 아래 첫 코드 블록(```)을 답변 원문으로 읽는다.
#   2. 답변 원문에서 다음 줄은 뺀다: "#"으로 시작하는 제목 줄, "---" 줄, 빈 줄,
#      "**사용한 조항"으로 시작하는 줄부터 블록 끝까지(답변 끝 조항 목록).
#   3. 남은 줄에서 앞의 "- "와 굵게 표시 "**"를 지우고, 마침표 뒤 공백(또는 줄 끝)에서 문장을 나눈다.
#      목록 한 줄에 마침표가 없으면 그 줄 전체가 한 문장이다.
#   4. 문장 안의 대괄호 [ ... ] 가운데 "제<숫자>조"로 시작하는 표기를 인용으로 본다.
#      대괄호 안을 쉼표로 나누고, 조를 생략한 표기("제3항")는 같은 대괄호 안 앞 표기의 조를 붙인다.
#      "[제○조 제○항]"처럼 숫자가 아닌 표기는 인용으로 보지 않는다.
#   5. 인용이 하나 이상 있는 문장 하나가 쌍 하나다. doc_ref는 그 문장의 인용을 나온 순서대로 "+"로 잇는다(중복 제거).
#      인용이 없는 문장은 쌍을 만들지 않고 "쌍으로 만들지 않은 문장"에 적는다.
#   6. claim_ko는 문장에서 인용 대괄호를 지운 것이다. 단 대괄호 바로 뒤에 마침표·쉼표가 오거나 문장이 끝날 때만 지운다.
#      대괄호 뒤에 다른 글자가 붙어 있으면("[제2조 제1호 다목]처럼") 문장의 일부로 보고 남긴다.
#   이 규칙 밖의 판단(어느 문장이 사실 주장인지 등)은 하지 않는다.
#
# 입력: deep/05-citation/experiments/results-04.md (첫 인자로 다른 결과 파일을 줄 수 있다)
# 출력: 화면 (pairs 파일에 붙여 넣을 Markdown). --start 로 첫 P 번호를 정한다(기본 13).
#
# 실행: 저장소 루트에서  python3 deep/05-citation/experiments/scripts/split-answer-sentences.py --start 13
# 표준 라이브러리만 사용한다. 설치할 것이 없다.

import argparse
import re
from collections import OrderedDict
from pathlib import Path

EXP_DIR = Path(__file__).resolve().parent.parent
RESULTS_PATH = EXP_DIR / "results-04.md"
CITE_TOKEN = re.compile(r"^제\d+조(?:의\d+)?(?=\s|$)")
ELIDED = re.compile(r"^제\d+(?:항|호)")


def read_answers(text):
    """{Q: 답변 원문 줄 목록} — "실제 답변:" 아래 첫 코드 블록."""
    answers = OrderedDict()
    section = None
    state = None  # None, "after_label", "in_block", "done"
    for line in text.split("\n"):
        m = re.match(r"^## (Q\d+)\s*$", line)
        if m:
            section, state = m.group(1), None
            continue
        if line.startswith("## ") and state != "in_block":
            section, state = None, None
            continue
        if section is None:
            continue
        if state is None and line.startswith("실제 답변:"):
            state = "after_label"
        elif state == "after_label" and line.startswith("```"):
            state = "in_block"
            answers[section] = []
        elif state == "in_block":
            if line.startswith("```"):
                state = "done"
            else:
                answers[section].append(line)
    return answers


def answer_lines(lines):
    out = []
    for line in lines:
        if line.startswith("**사용한 조항"):
            break
        s = line.strip()
        if not s or s.startswith("#") or s == "---":
            continue
        s = re.sub(r"^-\s+", "", s).replace("**", "")
        out.append(s)
    return out


def split_sentences(line):
    return [p for p in re.split(r"(?<=\.)\s+", line) if p]


def citations(sentence):
    refs = []
    for body in re.findall(r"\[([^\]]+)\]", sentence):
        prev_jo = None
        for token in [t.strip() for t in body.split(",")]:
            m = CITE_TOKEN.match(token)
            if m:
                prev_jo = m.group(0)
            elif prev_jo and ELIDED.match(token):
                token = prev_jo + " " + token
            else:
                continue
            if token not in refs:
                refs.append(token)
    return refs


def claim_text(sentence):
    return re.sub(r"\s*\[[^\]]+\](?=[.,]|$)", "", sentence).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("results", nargs="?", default=str(RESULTS_PATH))
    ap.add_argument("--start", type=int, default=13)
    args = ap.parse_args()
    answers = read_answers(Path(args.results).read_text(encoding="utf-8"))
    n = args.start
    skipped = []
    out = []
    for q, lines in answers.items():
        idx = 0
        for line in answer_lines(lines):
            for sentence in split_sentences(line):
                idx += 1
                sid = "%s-s%02d" % (q, idx)
                refs = citations(sentence)
                if not refs:
                    skipped.append((sid, sentence))
                    continue
                out.append("## P%d" % n)
                out.append("")
                out.append("doc_ref: %s" % "+".join(refs))
                out.append("claim_id: %s" % sid)
                out.append("claim_ko: %s" % claim_text(sentence))
                out.append("human: (answer-key-04-pairs.md에 둠)")
                out.append("hypothesis: - (기계적 분할 쌍, 사전 가설 없음)")
                out.append("")
                n += 1
    out.append("## 쌍으로 만들지 않은 문장 (인용 없음)")
    out.append("")
    for sid, sentence in skipped:
        out.append("- %s: %s" % (sid, sentence))
    out.append("")
    print("\n".join(out))


if __name__ == "__main__":
    main()
