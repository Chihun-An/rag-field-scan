# 층위 1 자동 판정: 답변이 인용한 조항 번호가 발췌본에 실재하는지 대조한다.
#
# 하는 일:
#   1. 법령 발췌본에서 조·항·호 목록을 만든다.
#      - 조: 줄 시작이 "제<숫자>조(" 인 곳. 다음 조 시작 전까지가 그 조의 범위.
#      - 항: 조 범위 안의 동그라미 숫자(① ~ ⑳).
#      - 호: 각 항 범위 안에서 줄 시작이 "<숫자>. " 인 것. 항이 없는 조는 조 직속 호로 본다.
#   2. 실험 결과 파일의 각 "## Q" 절에서 "실제 인용 조항:" 줄을 읽어
#      개별 (조, 항, 호) 항목으로 펼친다.
#   3. 각 항목을 발췌본 목록과 대조해 "실재함 / 발췌 범위 밖 / 다른 법률 / 파싱 실패" 중 하나로 판정한다.
#
# 이 스크립트가 보지 않는 것:
#   조항 번호가 실재하는지만 본다. 그 조항의 내용이 답변 문장을 뒷받침하는지는 보지 않는다.
#   "발췌 범위 밖"은 그 자체로 오류가 아니다. 오류 여부는 사람이 판정한다.
#
# 입력 1: deep/05-citation/data/sanan-law.md
# 입력 2: deep/05-citation/experiments/results-01.md
# 출력  : deep/05-citation/experiments/results-01-layer1.md  (터미널에도 같은 내용을 요약해 출력)
#
# 실행: 저장소 루트에서  python3 deep/05-citation/experiments/scripts/check-article-numbers.py
# 표준 라이브러리만 사용한다. 설치할 것이 없다.

import re
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
OWN_LAW_NAMES = ("산업안전보건법", "이 법")

REAL = "실재함"
OUT_OF_RANGE = "발췌 범위 밖"
OTHER_LAW = "다른 법률"
PARSE_FAIL = "파싱 실패"
VERDICTS = [REAL, OUT_OF_RANGE, OTHER_LAW, PARSE_FAIL]

KIND_DIRECT = "직접 인용"
KIND_REF = "참조"
KIND_OTHER_LAW = "다른 법률"

EXP_DIR = Path(__file__).resolve().parent.parent
LAW_PATH = EXP_DIR.parent / "data" / "sanan-law.md"
RESULTS_PATH = EXP_DIR / "results-01.md"
OUT_PATH = EXP_DIR / "results-01-layer1.md"


# ---------------------------------------------------------------- (a) 발췌본 파싱

def parse_law(text):
    """발췌본에서 {조 번호: {"title", "hang", "ho"}} 를 만든다.

    hang: 항 번호 목록(등장 순서). ho: {항 번호 또는 None(조 직속): 호 번호 목록}.
    """
    jo_header = re.compile(r"^제(\d+)조\((.*?)\)")
    ho_line = re.compile(r"^(\d+)\.\s")
    articles = OrderedDict()
    current = None
    current_hang = None
    started = False

    for line in text.split("\n"):
        m = jo_header.match(line)
        if m:
            started = True
            number = int(m.group(1))
            if number in articles:
                raise SystemExit("오류: 제%d조 시작 줄이 두 번 나옵니다." % number)
            current = {"title": m.group(2), "hang": [], "ho": OrderedDict()}
            articles[number] = current
            current_hang = None
        elif started and line.strip() == "---":
            break  # 본문 끝(맺음 구분선)
        if current is None:
            continue
        # 같은 줄(조 시작 줄 포함) 안의 동그라미 숫자는 모두 항 번호로 읽는다.
        for ch in line:
            if ch in CIRCLED:
                current_hang = CIRCLED.index(ch) + 1
                current["hang"].append(current_hang)
        h = ho_line.match(line)
        if h:
            current["ho"].setdefault(current_hang, []).append(int(h.group(1)))
    return articles


# ---------------------------------------------------------------- (b) 인용 줄 읽기

def read_citation_lines(text):
    """각 "## Q" 절의 "실제 인용 조항:" 줄 값을 읽는다. 줄이 없으면 None."""
    cites = OrderedDict()
    section = None
    for line in text.split("\n"):
        m = re.match(r"^## (Q\d+)\s*$", line)
        if m:
            section = m.group(1)
            cites[section] = None
        elif line.startswith("## "):
            section = None
        elif section:
            c = re.match(r"^실제 인용 조항\s*[:：]\s*(.*)$", line)
            if c:
                cites[section] = c.group(1).strip()
    return cites


# ---------------------------------------------------------------- (c) 표기 펼치기

def split_segments(raw):
    """괄호 밖(직접 인용)과 "(참조: ...)" 안(참조)으로 나눈다.

    반환: [(종류, 텍스트)] 와 파싱 실패 목록 [원문].
    """
    segments = []
    failures = []
    outside = []
    inside = []
    depth = 0
    for ch in raw:
        if ch == "(":
            depth += 1
            if depth > 1:
                inside.append(ch)
            continue
        if ch == ")":
            if depth == 0:
                failures.append("짝이 맞지 않는 닫는 괄호")
                continue
            depth -= 1
            if depth == 0:
                body = "".join(inside)
                inside = []
                m = re.match(r"^\s*참조\s*[:：]\s*(.*)$", body, re.S)
                if m:
                    segments.append((KIND_REF, m.group(1)))
                else:
                    failures.append("(" + body + ")")
            else:
                inside.append(ch)
            continue
        (inside if depth > 0 else outside).append(ch)
    if depth != 0:
        failures.append("닫히지 않은 여는 괄호")
    segments.insert(0, (KIND_DIRECT, "".join(outside)))
    return segments, failures


def span(a, b, label):
    a, b = int(a), int(b)
    if a > b:
        raise ValueError("%s 범위의 시작이 끝보다 큽니다" % label)
    return list(range(a, b + 1))


def parse_ref(token):
    """"제42조 제1항~제6항" 같은 표기 하나를 [(조, 항 또는 None, 호 또는 None), ...] 로 펼친다.

    규칙에 맞지 않으면 ValueError.
    """
    s = token.strip()
    m = re.match(r"제(\d+)조", s)
    if not m:
        raise ValueError("'제○조'로 시작하지 않습니다")
    jo_first = m.group(1)
    pos = m.end()

    m = re.compile(r"\s*~\s*제(\d+)조").match(s, pos)
    if m:  # 조 범위: 뒤에 항·호가 오면 안 된다
        pos = m.end()
        if s[pos:].strip():
            raise ValueError("조 범위 뒤에 다른 표기가 있습니다")
        return [(j, None, None) for j in span(jo_first, m.group(1), "조")]

    jo = int(jo_first)
    hangs = [None]
    m = re.compile(r"\s*제(\d+)항\s*~\s*제(\d+)항").match(s, pos)
    if not m:
        m = re.compile(r"\s*제(\d+)(?:~(\d+))?항").match(s, pos)
    if m:
        hangs = span(m.group(1), m.group(2) or m.group(1), "항")
        pos = m.end()

    hos = [None]
    m = re.compile(r"\s*제(\d+)호\s*~\s*제(\d+)호").match(s, pos)
    if not m:
        m = re.compile(r"\s*제(\d+)(?:~(\d+))?호").match(s, pos)
    if m:
        hos = span(m.group(1), m.group(2) or m.group(1), "호")
        pos = m.end()

    if s[pos:].strip():
        raise ValueError("해석하지 못한 남은 글자: '%s'" % s[pos:].strip())
    return [(jo, h, o) for h in hangs for o in hos]


def fmt(jo, hang, ho, law=None):
    out = "제%d조" % jo
    if hang is not None:
        out += " 제%d항" % hang
    if ho is not None:
        out += " 제%d호" % ho
    return ("「%s」 " % law + out) if law else out


def expand_line(raw):
    """"실제 인용 조항:" 줄 값 하나를 판정 대상 항목 목록으로 펼친다.

    항목: dict(text, kind, law, ref, fail). ref 는 (조, 항, 호), fail 은 파싱 실패 사유.
    """
    items = []
    segments, failures = split_segments(raw)
    for why in failures:
        items.append({"text": why, "kind": "-", "law": None, "ref": None, "fail": "괄호 해석 실패"})

    for kind, body in segments:
        if not body.strip():
            continue
        for token in body.split(","):
            token = token.strip()
            if not token:
                items.append({"text": "(빈 항목)", "kind": kind, "law": None, "ref": None,
                              "fail": "쉼표 사이가 비어 있음"})
                continue
            law = None
            m = re.match(r"^「([^」]+)」\s*(.*)$", token)
            rest = token
            if m:
                name, rest = m.group(1), m.group(2)
                if name not in OWN_LAW_NAMES:
                    law = name
                    kind_now = KIND_OTHER_LAW
                else:
                    kind_now = kind
            else:
                kind_now = kind
            try:
                for ref in parse_ref(rest):
                    items.append({"text": fmt(*ref, law=law), "kind": kind_now, "law": law,
                                  "ref": ref, "fail": None})
            except ValueError as e:
                items.append({"text": token, "kind": kind_now, "law": law, "ref": None, "fail": str(e)})
    return items


# ---------------------------------------------------------------- (d) 대조

def judge(item, articles):
    if item["fail"]:
        return PARSE_FAIL
    if item["law"]:
        return OTHER_LAW
    jo, hang, ho = item["ref"]
    art = articles.get(jo)
    if art is None:
        return OUT_OF_RANGE
    if hang is not None and hang not in art["hang"]:
        return OUT_OF_RANGE
    if ho is not None and ho not in art["ho"].get(hang, []):
        return OUT_OF_RANGE
    return REAL


# ---------------------------------------------------------------- 출력

def compress(numbers):
    """[1,2,3,5] -> "1~3, 5" """
    if not numbers:
        return "-"
    nums = sorted(set(numbers))
    parts = []
    start = prev = nums[0]
    for n in nums[1:]:
        if n == prev + 1:
            prev = n
            continue
        parts.append(str(start) if start == prev else "%d~%d" % (start, prev))
        start = prev = n
    parts.append(str(start) if start == prev else "%d~%d" % (start, prev))
    return ", ".join(parts)


def hang_label(h):
    return "조 직속" if h is None else CIRCLED[h - 1]


def article_rows(articles):
    rows = []
    for jo, art in articles.items():
        hang = "".join(CIRCLED[h - 1] for h in art["hang"]) or "없음"
        ho_total = sum(len(v) for v in art["ho"].values())
        detail = " / ".join("%s: %s" % (hang_label(h), compress(v)) for h, v in art["ho"].items()) or "-"
        rows.append((jo, art["title"], len(art["hang"]), hang, ho_total, detail))
    return rows


def build_markdown(articles, results, now, command, py_version):
    out = []
    out.append("# 실험 결과 01 — 층위 1 자동 판정 (조항 번호 실재 여부)")
    out.append("")
    out.append("이 파일은 `check-article-numbers.py`가 만든 결과다. 직접 고치지 않는다.")
    out.append("")
    out.append("- 실행 명령: `%s`" % command)
    out.append("- 실행 시각: %s" % now.strftime("%Y-%m-%d %H:%M:%S %z"))
    out.append("- 파이썬 버전: %s" % py_version)
    out.append("- 입력 1: [data/sanan-law.md](../data/sanan-law.md)")
    out.append("- 입력 2: [results-01.md](results-01.md) (각 질문의 \"실제 인용 조항\" 줄)")
    out.append("")
    out.append("## 1. 발췌본에서 찾은 조")
    out.append("")
    out.append("파서가 발췌본을 제대로 읽었는지 사람이 확인하는 표다. 원문과 다르면 파서 오류다.")
    out.append("")
    out.append("| 조 | 제목 | 항 개수 | 항 번호 | 호 개수 | 항별 호 번호 |")
    out.append("|----|------|---------|---------|---------|--------------|")
    for jo, title, n_hang, hang, n_ho, detail in article_rows(articles):
        out.append("| 제%d조 | %s | %d | %s | %d | %s |" % (jo, title, n_hang, hang, n_ho, detail))
    out.append("")
    out.append("## 2. 질문별 판정")
    out.append("")
    out.append("| 질문 | 인용 항목 | 종류 | 층위 1 판정 |")
    out.append("|------|-----------|------|-------------|")
    counts = OrderedDict((v, 0) for v in VERDICTS)
    for q, rows in results.items():
        if not rows:
            out.append("| %s | (인용 항목 없음) | - | - |" % q)
        for item, verdict in rows:
            out.append("| %s | %s | %s | %s |" % (q, item["text"], item["kind"], verdict))
            counts[verdict] += 1
    out.append("")
    out.append("## 3. 층위 1 요약")
    out.append("")
    total = sum(counts.values())
    for v in VERDICTS:
        out.append("- %s: %d" % (v, counts[v]))
    out.append("- 전체 항목: %d" % total)
    out.append("")
    out.append("## 4. 이 층위가 판정하지 않는 것")
    out.append("")
    out.append("이 스크립트는 조항 번호가 실재하는지만 본다. 그 조항의 내용이 답변 문장을 실제로 뒷받침하는지는 "
               "보지 않는다. 또 \"발췌 범위 밖\"은 그 자체로 오류가 아니다. 발췌본 안의 조문이 다른 조를 참조하고 "
               "있을 수 있고, 답변이 그 참조를 그대로 옮겼을 수 있기 때문이다. 오류인지 아닌지는 사람이 판정한다.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("[결과 기록](results-01.md) · [실험 설계](design-01.md) · [질문 목록](../questions.md)")
    out.append("")
    return "\n".join(out), counts


def main():
    law_text = LAW_PATH.read_text(encoding="utf-8")
    results_text = RESULTS_PATH.read_text(encoding="utf-8")

    articles = parse_law(law_text)
    if not articles:
        raise SystemExit("오류: 발췌본에서 조를 하나도 찾지 못했습니다.")
    cites = read_citation_lines(results_text)
    if not cites:
        raise SystemExit("오류: 결과 파일에서 '## Q' 절을 하나도 찾지 못했습니다.")

    results = OrderedDict()
    for q, raw in cites.items():
        if raw is None:
            item = {"text": "('실제 인용 조항:' 줄 없음)", "kind": "-", "law": None, "ref": None,
                    "fail": "줄 없음"}
            results[q] = [(item, PARSE_FAIL)]
            continue
        items = expand_line(raw)
        results[q] = [(it, judge(it, articles)) for it in items]

    now = datetime.now().astimezone()
    command = "python3 " + " ".join(sys.argv)
    py_version = sys.version.split()[0]
    markdown, counts = build_markdown(articles, results, now, command, py_version)
    OUT_PATH.write_text(markdown, encoding="utf-8")

    # 터미널 출력
    print("실행 명령: %s" % command)
    print("실행 시각: %s" % now.strftime("%Y-%m-%d %H:%M:%S %z"))
    print("파이썬 버전: %s" % py_version)
    print()
    print("[발췌본에서 찾은 조] %d개" % len(articles))
    for jo, title, n_hang, hang, n_ho, detail in article_rows(articles):
        print("  제%d조(%s): 항 %d개 %s / 호 %d개 %s" % (jo, title, n_hang, hang, n_ho, detail))
    print()
    print("[질문별 판정]")
    for q, rows in results.items():
        for item, verdict in rows:
            print("  %s | %s | %s | %s" % (q, item["text"], item["kind"], verdict))
    print()
    print("[층위 1 요약]")
    for v in VERDICTS:
        print("  %s: %d" % (v, counts[v]))
    print("  전체 항목: %d" % sum(counts.values()))
    print()
    print("출력 파일: %s" % OUT_PATH)


if __name__ == "__main__":
    main()
