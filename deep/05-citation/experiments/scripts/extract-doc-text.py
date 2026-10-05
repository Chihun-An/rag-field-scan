# 판정 쌍의 doc_ref에 해당하는 조문 원문을 법령 발췌본에서 뽑아 화면에 출력한다.
#
# 하는 일:
#   1. pairs-01-ko.md의 "## P<숫자>" 절마다 doc_ref, claim_id, claim_ko, human, hypothesis를 읽는다.
#   2. doc_ref("제42조 제2항", "제15조 제1항 제1호", "제42조 제1항+제2항" 등)를 해석해
#      sanan-law.md에서 해당 조·항·호의 원문을 그대로 뽑는다. 원문을 다시 타이핑하지 않는다.
#      - 조만 적힌 경우: 조 전체(조 제목 줄 포함)
#      - 항이 적힌 경우: 그 항 표시(①~⑳)부터 다음 항 표시 전까지(그 항의 호 줄 포함)
#      - 호가 적힌 경우: 그 호 줄 하나(목 줄은 포함하지 않는다)
#      - "본문"이 붙은 경우("제15조 제1항 본문"): 그 항 표시부터 첫 호 줄 전까지(조 제목 줄은 넣지 않는다)
#      - "제목"이 붙은 경우("제15조 제목"): 조 첫 줄의 "제○조(제목)" 부분만(첫 항 표시 앞까지)
#      - "+"로 묶인 경우: 앞에서부터 순서대로 빈 줄 하나를 두고 이어 붙인다
#        뒤쪽에 호만 적혀 있으면("+제1호") 앞쪽의 조·항을 이어받는다
#   3. 조·항·호 해석은 check-article-numbers.py의 로직(parse_law, parse_ref, judge)을 재사용한다.
#      이 스크립트의 조문 자르기 결과가 parse_law의 항·호 목록과 같은지 실행할 때마다 검사한다.
#
# 입력 1: deep/05-citation/data/sanan-law.md
# 입력 2: deep/05-citation/experiments/pairs-01-ko.md (기본값. 첫 인자로 다른 쌍 파일을 줄 수 있다)
# 출력  : 화면 (파일을 만들지 않는다)
#
# 실행: 저장소 루트에서  python3 deep/05-citation/experiments/scripts/extract-doc-text.py
#       실험 02:        python3 deep/05-citation/experiments/scripts/extract-doc-text.py deep/05-citation/experiments/pairs-02-ko.md
# 표준 라이브러리만 사용한다. 설치할 것이 없다.
#
# 다른 스크립트에서 쓰는 함수: load_checker, load_pairs, build_doc_texts

import importlib.util
import re
import sys
from collections import OrderedDict
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
EXP_DIR = SCRIPT_DIR.parent
LAW_PATH = EXP_DIR.parent / "data" / "sanan-law.md"
PAIRS_PATH = EXP_DIR / "pairs-01-ko.md"
CHECK_PATH = SCRIPT_DIR / "check-article-numbers.py"
KEYS = ("doc_ref", "claim_id", "claim_ko", "human", "hypothesis")
BODY = "본문"  # parse_doc_ref가 "제○항 본문"을 호 자리에 이 값으로 표시한다
TITLE = "제목"  # parse_doc_ref가 "제○조 제목"을 호 자리에 이 값으로 표시한다


def load_checker():
    """파일 이름에 하이픈이 있어 import로 못 불러오므로, 경로로 직접 불러와 재사용한다."""
    spec = importlib.util.spec_from_file_location("check_article_numbers", CHECK_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_pairs(path=PAIRS_PATH):
    """"## P<숫자>" 절마다 KEYS의 값을 읽어 {쌍 이름: {키: 값}}을 만든다."""
    pairs = OrderedDict()
    current = None
    for line in path.read_text(encoding="utf-8").split("\n"):
        m = re.match(r"^## (P\d+)\s*$", line)
        if m:
            current = m.group(1)
            pairs[current] = {}
            continue
        if line.startswith("## "):
            current = None
            continue
        if current:
            k = re.match(r"^(%s):\s*(.*)$" % "|".join(KEYS), line)
            if k:
                if k.group(1) in pairs[current]:
                    raise SystemExit("오류: %s 안에 %s가 두 번 나옵니다." % (current, k.group(1)))
                pairs[current][k.group(1)] = k.group(2).strip()
    for name, fields in pairs.items():
        for key in KEYS:
            if key not in fields:
                raise SystemExit("오류: %s에 %s 값이 없습니다." % (name, key))
    return pairs


def split_articles(law_text):
    """조마다 줄 목록을 만든다: {조 번호: [줄, ...]} (본문 끝 구분선 전까지)."""
    header = re.compile(r"^제(\d+)조\(")
    articles = OrderedDict()
    current = None
    for line in law_text.split("\n"):
        m = header.match(line)
        if m:
            current = int(m.group(1))
            articles[current] = [line]
            continue
        if current is not None and line.strip() == "---":
            break
        if current is not None:
            articles[current].append(line)
    return articles


def hang_marks(body, circled):
    """조 본문에서 항 표시(동그라미 숫자)의 (위치, 항 번호) 목록."""
    return [(m.start(), circled.index(m.group()) + 1) for m in re.finditer("[" + circled + "]", body)]


def ho_numbers(region):
    """구간 안에서 줄 시작이 "<숫자>. " 인 호 번호 목록."""
    out = []
    for line in region.split("\n"):
        m = re.match(r"^(\d+)\.\s", line)
        if m:
            out.append(int(m.group(1)))
    return out


def verify_consistency(articles, parsed, circled):
    """이 스크립트의 항·호 자르기가 check-article-numbers.py의 parse_law 결과와 같은지 검사한다."""
    if list(articles.keys()) != list(parsed.keys()):
        raise SystemExit("오류: 조 목록이 parse_law 결과와 다릅니다.")
    for jo, lines in articles.items():
        body = "\n".join(lines)
        marks = hang_marks(body, circled)
        if [n for _, n in marks] != parsed[jo]["hang"]:
            raise SystemExit("오류: 제%d조의 항 목록이 parse_law 결과와 다릅니다." % jo)
        regions = OrderedDict()
        regions[None] = body[:marks[0][0]] if marks else body
        for i, (pos, num) in enumerate(marks):
            end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
            regions[num] = body[pos:end]
        mine = OrderedDict((k, ho_numbers(v)) for k, v in regions.items() if ho_numbers(v))
        theirs = OrderedDict((k, v) for k, v in parsed[jo]["ho"].items() if v)
        if dict(mine) != dict(theirs):
            raise SystemExit("오류: 제%d조의 호 목록이 parse_law 결과와 다릅니다." % jo)


def extract_one(articles, circled, jo, hang, ho):
    """(조, 항 또는 None, 호 또는 None) 하나에 해당하는 원문을 뽑는다."""
    body = "\n".join(articles[jo])
    if hang is None and ho is None:
        return body.strip()
    marks = hang_marks(body, circled)
    if hang is None:
        region = body[:marks[0][0]] if marks else body
    else:
        region = None
        for i, (pos, num) in enumerate(marks):
            if num == hang:
                end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
                region = body[pos:end]
                break
        if region is None:
            raise SystemExit("오류: 제%d조에 제%d항이 없습니다." % (jo, hang))
    if ho is None:
        return region.strip()
    for line in region.split("\n"):
        if re.match(r"^%d\.\s" % ho, line):
            return line.strip()
    raise SystemExit("오류: 제%d조 제%s항 안에 제%d호가 없습니다." % (jo, hang, ho))


def extract_hang_body(articles, circled, jo, hang):
    """제○항의 각 호 앞 본문(항 표시부터 첫 호 줄 전까지)을 뽑는다. 조 제목 줄은 넣지 않는다."""
    region = extract_one(articles, circled, jo, hang, None)
    out = []
    for line in region.split("\n"):
        if re.match(r"^\d+\.\s", line):
            break
        out.append(line)
    if len(out) == len(region.split("\n")):
        raise SystemExit("오류: 제%d조 제%d항에 호가 없어 '본문'을 따로 뽑을 수 없습니다." % (jo, hang))
    return "\n".join(out).strip()


def extract_title(articles, circled, jo):
    """조 제목 줄의 "제○조(제목)" 부분만 뽑는다. 첫 항 표시가 있으면 그 앞까지다."""
    header = articles[jo][0]
    mark = re.search("[" + circled + "]", header)
    if mark:
        return header[:mark.start()].strip()
    m = re.match(r"^제\d+조\([^)]*\)", header)
    if not m:
        raise SystemExit("오류: 제%d조의 제목을 찾지 못했습니다." % jo)
    return m.group(0)


def parse_doc_ref(doc_ref, checker):
    """"제42조 제1항+제2항", "제15조 제1항 본문+제1호" 같은 doc_ref를 (조, 항, 호) 목록으로 푼다.

    "+"로 묶인 뒤쪽 표기에 조가 없으면 앞쪽의 조를 이어받고, 호만 적혀 있으면 앞쪽의 조·항을
    이어받는다. 항 뒤에 "본문"이 붙으면 호 자리에 BODY를, 조 뒤에 "제목"이 붙으면 호 자리에
    TITLE을 넣는다. 해석은 parse_ref를 재사용한다.
    """
    parts = [p.strip() for p in doc_ref.split("+")]
    first_jo = re.match(r"^제\d+조", parts[0])
    if not first_jo:
        raise SystemExit("오류: doc_ref가 '제○조'로 시작하지 않습니다: %s" % doc_ref)
    refs = []
    prev_jo_hang = first_jo.group(0)
    for part in parts:
        if re.match(r"^제\d+호", part):
            part = prev_jo_hang + " " + part
        elif not re.match(r"^제\d+조", part):
            part = first_jo.group(0) + " " + part
        body = re.search(r"\s*본문$", part)
        if body:
            part = part[:body.start()]
        title = re.search(r"\s*제목$", part)
        if title:
            part = part[:title.start()]
        try:
            parsed = checker.parse_ref(part)
        except ValueError as e:
            raise SystemExit("오류: doc_ref를 해석하지 못했습니다 (%s): %s" % (doc_ref, e))
        if title:
            if len(parsed) != 1 or parsed[0][1] is not None or parsed[0][2] is not None:
                raise SystemExit("오류: '제목'은 조 하나 뒤에만 쓸 수 있습니다: %s" % doc_ref)
            parsed = [(parsed[0][0], None, TITLE)]
        if body:
            if len(parsed) != 1 or parsed[0][1] is None or parsed[0][2] is not None:
                raise SystemExit("오류: '본문'은 항 하나 뒤에만 쓸 수 있습니다: %s" % doc_ref)
            parsed = [(parsed[0][0], parsed[0][1], BODY)]
        hang_m = re.match(r"^(제\d+조\s*제\d+항)", part)
        prev_jo_hang = hang_m.group(1) if hang_m else re.match(r"^제\d+조", part).group(0)
        refs.extend(parsed)
    return refs


def build_doc_texts(pairs=None):
    """{쌍 이름: 조문 원문} 을 만든다. 실재하지 않는 조항이면 오류로 멈춘다."""
    checker = load_checker()
    law_text = LAW_PATH.read_text(encoding="utf-8")
    parsed = checker.parse_law(law_text)
    articles = split_articles(law_text)
    verify_consistency(articles, parsed, checker.CIRCLED)
    pairs = pairs or load_pairs()
    texts = OrderedDict()
    for name, fields in pairs.items():
        chunks = []
        for jo, hang, ho in parse_doc_ref(fields["doc_ref"], checker):
            ref = (jo, hang, None if ho in (BODY, TITLE) else ho)
            item = {"fail": None, "law": None, "ref": ref}
            if checker.judge(item, parsed) != checker.REAL:
                raise SystemExit("오류: %s의 doc_ref '%s'가 발췌본에 없습니다." % (name, fields["doc_ref"]))
            if ho is TITLE:
                chunks.append(extract_title(articles, checker.CIRCLED, jo))
            elif ho is BODY:
                chunks.append(extract_hang_body(articles, checker.CIRCLED, jo, hang))
            else:
                chunks.append(extract_one(articles, checker.CIRCLED, jo, hang, ho))
        texts[name] = "\n\n".join(chunks)
    return texts


def main():
    pairs_path = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else PAIRS_PATH
    print("입력 쌍 파일: %s" % pairs_path.name)
    pairs = load_pairs(pairs_path)
    texts = build_doc_texts(pairs)
    print("조문 자르기 검사: parse_law 결과와 일치 (조 %d개)" % len(load_checker().parse_law(
        LAW_PATH.read_text(encoding="utf-8"))))
    print("쌍 %d개" % len(pairs))
    for name, fields in pairs.items():
        print()
        print("=" * 70)
        print("[%s] doc_ref: %s  (claim_id: %s)" % (name, fields["doc_ref"], fields["claim_id"]))
        print("=" * 70)
        print(texts[name])


if __name__ == "__main__":
    main()
