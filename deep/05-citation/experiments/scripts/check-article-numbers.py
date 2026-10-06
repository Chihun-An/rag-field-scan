# 층위 1 자동 판정: 답변이 인용한 조항 번호가 발췌본에 실재하는지 대조한다.
#
# 하는 일:
#   1. 법령 발췌본에서 조·항·호·목 목록을 만든다.
#      - 조: 줄 시작이 "제<숫자>조(" 또는 "제<숫자>조의<숫자>(" 인 곳. 다음 조 시작 전까지가 그 조의 범위.
#      - 항: 조 범위 안의 동그라미 숫자(① ~ ⑳).
#      - 호: 각 항 범위 안에서 줄 시작이 "<숫자>. " 또는 "<숫자>의<숫자>. " 인 것. 항이 없는 조는 조 직속 호로 본다.
#      - 목: 각 호 범위 안에서 줄 시작이 "가. " ~ "하. " 인 것.
#   2. 실험 결과 파일의 각 "## Q" 절에서 "실제 인용 조항:" 줄을 읽어
#      개별 (조, 항, 호, 목) 항목으로 펼친다.
#      - 코드 블록(``` 또는 ~~~) 안의 줄은 절 구분과 인용 줄 찾기에 쓰지 않는다.
#      - 줄 뒤 값이 비어 있으면 바로 아래 "- " 목록을 값으로 읽는다(항목을 쉼표로 잇는다).
#      - 앞 항목의 조(또는 조·항, 조·항·호)를 생략한 표기("제15조 제1항, 제3항"의 "제3항")는
#        바로 앞 항목에서 생략된 부분을 이어받는다.
#   3. 각 항목을 발췌본 목록과 대조해 "실재함 / 발췌 범위 밖 / 다른 법률 / 파싱 실패" 중 하나로 판정한다.
#   4. 인용 항목이 0건이거나 파싱 실패가 절반 이상이면 경고를 내고 종료 코드 2로 끝낸다.
#
# 이 스크립트가 보지 않는 것:
#   조항 번호가 실재하는지만 본다. 그 조항의 내용이 답변 문장을 뒷받침하는지는 보지 않는다.
#   "발췌 범위 밖"은 그 자체로 오류가 아니다. 오류 여부는 사람이 판정한다.
#
# 입력 1: 법령 발췌본       (--law,       기본 deep/05-citation/data/sanan-law.md)
# 입력 2: 실험 결과 파일    (--results,   기본 deep/05-citation/experiments/results-01.md)
# 출력  : 층위 1 결과 파일  (--out,       기본 deep/05-citation/experiments/results-01-layer1.md)
#         (터미널에도 같은 내용을 요약해 출력)
# 링크용: 질문 목록 파일    (--questions, 기본 deep/05-citation/questions.md, 출력 파일 맨 아래 링크에만 씀)
#
# 실행: 저장소 루트에서  python3 deep/05-citation/experiments/scripts/check-article-numbers.py
#       다른 입력:       python3 deep/05-citation/experiments/scripts/check-article-numbers.py \
#                          --law deep/05-citation/data/privacy-law.md \
#                          --results deep/05-citation/experiments/results-04.md \
#                          --out deep/05-citation/experiments/results-04-layer1.md \
#                          --questions deep/05-citation/experiments/questions-04.md
# 표준 라이브러리만 사용한다. 설치할 것이 없다.

import argparse
import os
import re
import sys
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

CIRCLED = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
MOK_LETTERS = "가나다라마바사아자차카타파하"

REAL = "실재함"
OUT_OF_RANGE = "발췌 범위 밖"
OTHER_LAW = "다른 법률"
PARSE_FAIL = "파싱 실패"
VERDICTS = [REAL, OUT_OF_RANGE, OTHER_LAW, PARSE_FAIL]

KIND_DIRECT = "직접 인용"
KIND_REF = "참조"
KIND_OTHER_LAW = "다른 법률"

EXIT_WARNING = 2

EXP_DIR = Path(__file__).resolve().parent.parent
LAW_PATH = EXP_DIR.parent / "data" / "sanan-law.md"
RESULTS_PATH = EXP_DIR / "results-01.md"
OUT_PATH = EXP_DIR / "results-01-layer1.md"
QUESTIONS_PATH = EXP_DIR.parent / "questions.md"


# ---------------------------------------------------------------- 번호 표기

def fmt_jo(jo):
    """jo = (조 번호, 가지번호 또는 None) -> "제28조의2" """
    n, sub = jo
    return "제%d조" % n + ("의%d" % sub if sub is not None else "")


def fmt_ho_num(ho):
    """ho = (호 번호, 가지번호 또는 None) -> "1의2" """
    n, sub = ho
    return "%d" % n + ("의%d" % sub if sub is not None else "")


def fmt(jo, hang, ho, mok, law=None):
    out = fmt_jo(jo)
    if hang is not None:
        out += " 제%d항" % hang
    if ho is not None:
        out += " 제%d호" % ho[0] + ("의%d" % ho[1] if ho[1] is not None else "")  # 법령 표기: 제1호의2
    if mok is not None:
        out += " %s목" % mok
    return ("「%s」 " % law + out) if law else out


def opt_int(s):
    return int(s) if s is not None else None


# ---------------------------------------------------------------- (a) 발췌본 파싱

def read_law_name(text):
    """발췌본 첫 제목 줄 "# 산업안전보건법 (발췌)" 에서 법률 이름을 읽는다. 없으면 None."""
    for line in text.split("\n"):
        m = re.match(r"^#\s+(.+?)\s*(?:\(발췌\))?\s*$", line)
        if m:
            return m.group(1)
        if line.strip():
            return None
    return None


def parse_law(text):
    """발췌본에서 {조 키: {"title", "hang", "ho", "mok"}} 를 만든다.

    조 키: (조 번호, 가지번호 또는 None). hang: 항 번호 목록(등장 순서).
    ho: {항 번호 또는 None(조 직속): [호 키]}. 호 키: (호 번호, 가지번호 또는 None).
    mok: {(항, 호 키): [목 글자]}.
    """
    jo_header = re.compile(r"^제(\d+)조(?:의(\d+))?\((.*?)\)")
    ho_line = re.compile(r"^(\d+)(?:의(\d+))?\.\s")
    mok_line = re.compile(r"^([%s])\.\s" % MOK_LETTERS)
    articles = OrderedDict()
    current = None
    current_hang = None
    current_ho = None
    started = False

    for line in text.split("\n"):
        m = jo_header.match(line)
        if m:
            started = True
            key = (int(m.group(1)), opt_int(m.group(2)))
            if key in articles:
                raise SystemExit("오류: %s 시작 줄이 두 번 나옵니다." % fmt_jo(key))
            current = {"title": m.group(3), "hang": [], "ho": OrderedDict(), "mok": OrderedDict()}
            articles[key] = current
            current_hang = None
            current_ho = None
        elif started and line.strip() == "---":
            break  # 본문 끝(맺음 구분선)
        if current is None:
            continue
        # 같은 줄(조 시작 줄 포함) 안의 동그라미 숫자는 모두 항 번호로 읽는다.
        for ch in line:
            if ch in CIRCLED:
                current_hang = CIRCLED.index(ch) + 1
                current["hang"].append(current_hang)
                current_ho = None
        h = ho_line.match(line)
        if h:
            current_ho = (int(h.group(1)), opt_int(h.group(2)))
            current["ho"].setdefault(current_hang, []).append(current_ho)
            continue
        k = mok_line.match(line)
        if k and current_ho is not None:
            current["mok"].setdefault((current_hang, current_ho), []).append(k.group(1))
    return articles


# ---------------------------------------------------------------- (b) 인용 줄 읽기

CITE_MISSING = "missing"   # Q 절 안에 "실제 인용 조항:" 줄이 없음
CITE_EMPTY = "empty"       # 줄은 있으나 같은 줄에도, 바로 아래 목록에도 값이 없음
CITE_OK = "ok"


def read_citation_lines(text):
    """각 "## Q" 절의 "실제 인용 조항:" 값을 읽는다.

    반환: (cites, warnings). cites = {Q: (상태, 값)}. warnings = 사람이 봐야 할 이상 목록.
    """
    cites = OrderedDict()
    warnings = []
    section = None
    in_fence = False
    fence_mark = None
    fence_start = None
    collecting = None      # 목록을 모으는 중인 Q
    collected = []
    cite_line = re.compile(r"^실제 인용 조항\s*[:：]\s*(.*)$")

    def finish_collect():
        nonlocal collecting, collected
        if collecting is not None:
            if collected:
                cites[collecting] = (CITE_OK, ", ".join(collected))
            else:
                cites[collecting] = (CITE_EMPTY, "")
        collecting = None
        collected = []

    for lineno, line in enumerate(text.split("\n"), 1):
        f = re.match(r"^\s*(```|~~~)", line)
        if f:
            if not in_fence:
                finish_collect()
                in_fence, fence_mark, fence_start = True, f.group(1), lineno
                continue
            if f.group(1) == fence_mark:
                in_fence = False
                continue
        if in_fence:
            continue

        if collecting is not None:
            item = re.match(r"^\s*[-*]\s+(.*\S)\s*$", line)
            if item:
                collected.append(item.group(1))
                continue
            if not line.strip() and not collected:
                continue  # 줄과 목록 사이의 빈 줄
            finish_collect()

        m = re.match(r"^## (Q\d+)\s*$", line)
        if m:
            section = m.group(1)
            cites[section] = (CITE_MISSING, "")
            continue
        if line.startswith("## "):
            section = None
            continue
        c = cite_line.match(line)
        if c:
            if section is None:
                warnings.append("%d행: \"실제 인용 조항:\" 줄이 어느 \"## Q\" 절에도 속하지 않아 읽지 않았습니다." % lineno)
            elif c.group(1).strip():
                cites[section] = (CITE_OK, c.group(1).strip())
            else:
                collecting = section
    finish_collect()
    if in_fence:
        warnings.append("%d행에서 연 코드 블록이 닫히지 않았습니다. 그 뒤의 줄은 읽지 않았습니다." % fence_start)
    return cites, warnings


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


def mok_span(a, b):
    i, j = MOK_LETTERS.index(a), MOK_LETTERS.index(b)
    if i > j:
        raise ValueError("목 범위의 시작이 끝보다 큽니다")
    return list(MOK_LETTERS[i:j + 1])


def parse_ref(token, prev=None):
    """"제42조 제1항~제6항" 같은 표기 하나를 [(조 키, 항, 호 키, 목), ...] 로 펼친다.

    prev 는 바로 앞 항목의 (조 키, 항, 호 키). 조를 생략하고 "제3항", "제2호", "나목"으로
    시작하면 생략된 윗단위를 prev 에서 이어받는다. 규칙에 맞지 않으면 ValueError.
    """
    s = token.strip()
    pos = 0
    m = re.match(r"제(\d+)조(?:의(\d+))?", s)
    if m:
        jo = (int(m.group(1)), opt_int(m.group(2)))
        pos = m.end()
        r = re.compile(r"\s*~\s*제(\d+)조").match(s, pos)
        if r:  # 조 범위: 뒤에 항·호가 오면 안 된다
            if jo[1] is not None:
                raise ValueError("가지번호가 있는 조의 범위는 해석하지 않습니다")
            pos = r.end()
            if s[pos:].strip():
                raise ValueError("조 범위 뒤에 다른 표기가 있습니다")
            return [((j, None), None, None, None) for j in span(jo[0], r.group(1), "조")]
        hangs, hos = [None], [None]
        level = "jo"
    else:
        if re.match(r"제\d+(?:~\d+)?항", s):
            level = "hang"
        elif re.match(r"제\d+(?:~\d+)?호", s):
            level = "ho"
        elif re.match(r"[%s](?:목|~)" % MOK_LETTERS, s):
            level = "mok"
        else:
            raise ValueError("'제○조'로 시작하지 않습니다")
        if prev is None:
            raise ValueError("'제○조'로 시작하지 않았고, 이어받을 앞 항목도 없습니다")
        jo = prev[0]
        hangs = [None] if level == "hang" else [prev[1]]
        hos = [prev[2]] if level == "mok" else [None]
        if level == "mok" and prev[2] is None:
            raise ValueError("목을 이어받을 앞 항목에 호가 없습니다")

    if level in ("jo", "hang"):
        m = re.compile(r"\s*제(\d+)항\s*~\s*제(\d+)항").match(s, pos)
        if not m:
            m = re.compile(r"\s*제(\d+)(?:~(\d+))?항").match(s, pos)
        if m:
            hangs = span(m.group(1), m.group(2) or m.group(1), "항")
            pos = m.end()

    if level in ("jo", "hang", "ho"):
        m = re.compile(r"\s*제(\d+)호\s*~\s*제(\d+)호(?!의)").match(s, pos)
        if m:
            hos = [(n, None) for n in span(m.group(1), m.group(2), "호")]
            pos = m.end()
        else:
            m = re.compile(r"\s*제(\d+)(?:~(\d+))?호(?:의(\d+))?").match(s, pos)
            if m:
                if m.group(2) and m.group(3):
                    raise ValueError("호 범위와 가지번호를 함께 해석하지 않습니다")
                if m.group(3):
                    hos = [(int(m.group(1)), int(m.group(3)))]
                else:
                    hos = [(n, None) for n in span(m.group(1), m.group(2) or m.group(1), "호")]
                pos = m.end()

    moks = [None]
    m = re.compile(r"\s*([{0}])목\s*~\s*([{0}])목".format(MOK_LETTERS)).match(s, pos)
    if not m:
        m = re.compile(r"\s*([{0}])(?:~([{0}]))?목".format(MOK_LETTERS)).match(s, pos)
    if m:
        if hos == [None]:
            raise ValueError("호 없이 목이 왔습니다")
        moks = mok_span(m.group(1), m.group(2) or m.group(1))
        pos = m.end()

    if s[pos:].strip():
        raise ValueError("해석하지 못한 남은 글자: '%s'" % s[pos:].strip())
    return [(jo, h, o, k) for h in hangs for o in hos for k in moks]


def expand_line(raw, own_law_names):
    """"실제 인용 조항:" 값 하나를 판정 대상 항목 목록으로 펼친다.

    항목: dict(text, kind, law, ref, fail). ref 는 (조 키, 항, 호 키, 목), fail 은 파싱 실패 사유.
    """
    items = []
    segments, failures = split_segments(raw)
    for why in failures:
        items.append({"text": why, "kind": "-", "law": None, "ref": None, "fail": "괄호 해석 실패"})

    for kind, body in segments:
        if not body.strip():
            continue
        prev = None
        prev_law = None
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
                if name not in own_law_names:
                    law = name
            elif not rest.startswith("제") or re.match(r"제\d+(?:~\d+)?[항호]", rest):
                law = prev_law  # 조를 생략한 표기는 앞 항목의 법률도 이어받는다
            kind_now = KIND_OTHER_LAW if law else kind
            try:
                refs = parse_ref(rest, prev)
                for ref in refs:
                    items.append({"text": fmt(*ref, law=law), "kind": kind_now, "law": law,
                                  "ref": ref, "fail": None})
                last = refs[-1]
                prev = (last[0], last[1], last[2])
                prev_law = law
            except ValueError as e:
                items.append({"text": token, "kind": kind_now, "law": law, "ref": None, "fail": str(e)})
                prev = None
                prev_law = None
    return items


# ---------------------------------------------------------------- (d) 대조

def judge(item, articles):
    if item["fail"]:
        return PARSE_FAIL
    if item["law"]:
        return OTHER_LAW
    jo, hang, ho, mok = item["ref"]
    art = articles.get(jo)
    if art is None:
        return OUT_OF_RANGE
    if hang is not None and hang not in art["hang"]:
        return OUT_OF_RANGE
    if ho is not None and ho not in art["ho"].get(hang, []):
        return OUT_OF_RANGE
    if mok is not None and mok not in art["mok"].get((hang, ho), []):
        return OUT_OF_RANGE
    return REAL


# ---------------------------------------------------------------- 출력

def compress(keys):
    """[(1,None),(1,2),(2,None),(3,None)] -> "1, 1의2, 2~3" """
    if not keys:
        return "-"
    nums = sorted(set(keys), key=lambda k: (k[0], -1 if k[1] is None else k[1]))
    parts = []
    run = [nums[0]]
    for k in nums[1:]:
        last = run[-1]
        if k[1] is None and last[1] is None and k[0] == last[0] + 1:
            run.append(k)
            continue
        parts.append(run)
        run = [k]
    parts.append(run)
    out = []
    for r in parts:
        if len(r) == 1:
            out.append(fmt_ho_num(r[0]))
        else:
            out.append("%d~%d" % (r[0][0], r[-1][0]))
    return ", ".join(out)


def hang_label(h):
    return "조 직속" if h is None else CIRCLED[h - 1]


def article_rows(articles):
    rows = []
    for jo, art in articles.items():
        hang = "".join(CIRCLED[h - 1] for h in art["hang"]) or "없음"
        ho_total = sum(len(v) for v in art["ho"].values())
        detail = " / ".join("%s: %s" % (hang_label(h), compress(v)) for h, v in art["ho"].items()) or "-"
        rows.append((fmt_jo(jo), art["title"], len(art["hang"]), hang, ho_total, detail))
    return rows


def mok_rows(articles):
    rows = []
    for jo, art in articles.items():
        for (h, ho), letters in art["mok"].items():
            rows.append((fmt_jo(jo), hang_label(h), fmt_ho_num(ho), "".join(letters)))
    return rows


def rel(path, base):
    return Path(os.path.relpath(Path(path).resolve(), Path(base).resolve())).as_posix()


def experiment_label(results_path):
    m = re.match(r"^results-(\d+)\.md$", Path(results_path).name)
    return m.group(1) if m else Path(results_path).name


def build_markdown(articles, results, now, command, py_version, paths, warnings, fatal):
    law_path, results_path, out_path, questions_path = paths
    out_dir = Path(out_path).parent
    law_shown = rel(law_path, EXP_DIR.parent)
    out = []
    out.append("# 실험 결과 %s — 층위 1 자동 판정 (조항 번호 실재 여부)" % experiment_label(results_path))
    out.append("")
    out.append("이 파일은 `check-article-numbers.py`가 만든 결과다. 직접 고치지 않는다.")
    out.append("")
    out.append("- 실행 명령: `%s`" % command)
    out.append("- 실행 시각: %s" % now.strftime("%Y-%m-%d %H:%M:%S %z"))
    out.append("- 파이썬 버전: %s" % py_version)
    out.append("- 입력 1: [%s](%s)" % (law_shown, rel(law_path, out_dir)))
    out.append("- 입력 2: [%s](%s) (각 질문의 \"실제 인용 조항\" 줄)" % (rel(results_path, out_dir), rel(results_path, out_dir)))
    out.append("")
    out.append("## 1. 발췌본에서 찾은 조")
    out.append("")
    out.append("파서가 발췌본을 제대로 읽었는지 사람이 확인하는 표다. 원문과 다르면 파서 오류다.")
    out.append("")
    out.append("| 조 | 제목 | 항 개수 | 항 번호 | 호 개수 | 항별 호 번호 |")
    out.append("|----|------|---------|---------|---------|--------------|")
    for jo, title, n_hang, hang, n_ho, detail in article_rows(articles):
        out.append("| %s | %s | %d | %s | %d | %s |" % (jo, title, n_hang, hang, n_ho, detail))
    out.append("")
    moks = mok_rows(articles)
    if moks:
        out.append("목(가·나·다…)이 있는 호:")
        out.append("")
        out.append("| 조 | 항 | 호 | 목 |")
        out.append("|----|----|----|----|")
        for jo, h, ho, letters in moks:
            out.append("| %s | %s | %s | %s |" % (jo, h, ho, letters))
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
    if warnings:
        out.append("## 경고")
        out.append("")
        if fatal:
            out.append("이 실행은 정상 결과로 보지 않는다(종료 코드 %d)." % EXIT_WARNING)
            out.append("")
        for w in warnings:
            out.append("- %s" % w)
        out.append("")
    out.append("## 4. 이 층위가 판정하지 않는 것")
    out.append("")
    out.append("이 스크립트는 조항 번호가 실재하는지만 본다. 그 조항의 내용이 답변 문장을 실제로 뒷받침하는지는 "
               "보지 않는다. 또 \"발췌 범위 밖\"은 그 자체로 오류가 아니다. 발췌본 안의 조문이 다른 조를 참조하고 "
               "있을 수 있고, 답변이 그 참조를 그대로 옮겼을 수 있기 때문이다. 오류인지 아닌지는 사람이 판정한다.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("[결과 기록](%s) · [실험 설계](%s) · [질문 목록](%s)"
               % (rel(results_path, out_dir), rel(EXP_DIR / "design-01.md", out_dir), rel(questions_path, out_dir)))
    out.append("")
    return "\n".join(out), counts


def main():
    ap = argparse.ArgumentParser(description="층위 1: 인용 조항 번호가 발췌본에 실재하는지 대조한다.")
    ap.add_argument("--law", default=str(LAW_PATH), help="법령 발췌본 (기본: data/sanan-law.md)")
    ap.add_argument("--results", default=str(RESULTS_PATH), help="실험 결과 파일 (기본: results-01.md)")
    ap.add_argument("--out", default=str(OUT_PATH), help="출력 파일 (기본: results-01-layer1.md)")
    ap.add_argument("--questions", default=str(QUESTIONS_PATH), help="출력 파일 맨 아래 링크에 쓸 질문 목록")
    args = ap.parse_args()
    law_path, results_path, out_path = Path(args.law), Path(args.results), Path(args.out)

    law_text = law_path.read_text(encoding="utf-8")
    results_text = results_path.read_text(encoding="utf-8")

    articles = parse_law(law_text)
    if not articles:
        raise SystemExit("오류: 발췌본에서 조를 하나도 찾지 못했습니다.")
    law_name = read_law_name(law_text)
    own_law_names = ("이 법",) + ((law_name,) if law_name else ())
    cites, warnings = read_citation_lines(results_text)
    if not cites:
        raise SystemExit("오류: 결과 파일에서 '## Q' 절을 하나도 찾지 못했습니다.")

    results = OrderedDict()
    for q, (status, raw) in cites.items():
        if status == CITE_MISSING:
            item = {"text": "('실제 인용 조항:' 줄 없음)", "kind": "-", "law": None, "ref": None,
                    "fail": "줄 없음"}
            results[q] = [(item, PARSE_FAIL)]
            continue
        if status == CITE_EMPTY:
            item = {"text": "('실제 인용 조항:' 줄은 있으나 값과 바로 아래 목록이 모두 비어 있음)", "kind": "-",
                    "law": None, "ref": None, "fail": "값 없음"}
            results[q] = [(item, PARSE_FAIL)]
            continue
        items = expand_line(raw, own_law_names)
        results[q] = [(it, judge(it, articles)) for it in items]

    total = sum(len(rows) for rows in results.values())
    n_fail = sum(1 for rows in results.values() for _, v in rows if v == PARSE_FAIL)
    fatal = False
    if total == 0:
        warnings.append("인용 항목이 0건입니다. 결과 파일의 \"실제 인용 조항\" 형식을 확인하세요.")
        fatal = True
    elif n_fail * 2 >= total:
        warnings.append("파싱 실패가 전체 %d건 중 %d건으로 절반 이상입니다." % (total, n_fail))
        fatal = True

    now = datetime.now().astimezone()
    command = "python3 " + " ".join(sys.argv)
    py_version = sys.version.split()[0]
    paths = (law_path, results_path, out_path, Path(args.questions))
    markdown, counts = build_markdown(articles, results, now, command, py_version, paths, warnings, fatal)
    out_path.write_text(markdown, encoding="utf-8")

    # 터미널 출력
    print("실행 명령: %s" % command)
    print("실행 시각: %s" % now.strftime("%Y-%m-%d %H:%M:%S %z"))
    print("파이썬 버전: %s" % py_version)
    print()
    print("[발췌본에서 찾은 조] %d개" % len(articles))
    for jo, title, n_hang, hang, n_ho, detail in article_rows(articles):
        print("  %s(%s): 항 %d개 %s / 호 %d개 %s" % (jo, title, n_hang, hang, n_ho, detail))
    moks = mok_rows(articles)
    if moks:
        print("  목: " + " / ".join("%s %s 제%s호 %s" % row for row in moks))
    print()
    print("[질문별 판정]")
    for q, rows in results.items():
        if not rows:
            print("  %s | (인용 항목 없음) | - | -" % q)
        for item, verdict in rows:
            print("  %s | %s | %s | %s" % (q, item["text"], item["kind"], verdict))
    print()
    print("[층위 1 요약]")
    for v in VERDICTS:
        print("  %s: %d" % (v, counts[v]))
    print("  전체 항목: %d" % sum(counts.values()))
    print()
    print("출력 파일: %s" % out_path.resolve())
    if warnings:
        for w in warnings:
            print("경고: %s" % w, file=sys.stderr)
    if fatal:
        print("경고: 정상 결과로 보지 않고 종료 코드 %d로 끝냅니다." % EXIT_WARNING, file=sys.stderr)
        sys.exit(EXIT_WARNING)


if __name__ == "__main__":
    main()
