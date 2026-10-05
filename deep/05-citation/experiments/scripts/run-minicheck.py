# [미사용 기록] 이 스크립트는 끝까지 실행되지 않았다.
# MiniCheck로 층위 2를 돌리려 했으나 아래 이유로 경로를 바꿨다.
#  - 1차 실행이 accelerate 누락으로 실패:
#    ValueError: Using a `device_map` ... requires `accelerate`
#  - 가중치 용량 flan-t5-large 3.13GB / roberta-large 1.42GB,
#    실행 시점 디스크 여유 7.2GiB(사용률 97%)
#  - MiniCheck 체크포인트는 모두 구형 pytorch_model.bin 형식이고 설치된
#    transformers는 5.18.0이어서, 구형 체크포인트 로딩 가능 여부가 불확실했다.
#  - 대신 .claude/agents/citation-judge.md 서브에이전트로 한국어 원문을 그대로 판정했다.
# 가상환경(~/.venvs/minicheck)은 2026-10-05에 삭제했다. 이 파일은 시도한 경로의 기록으로 남긴다.
# 관련 기록: ../../../../worklog.md (2026-10-04, 2026-10-05)

# 층위 2 자동 판정: MiniCheck로 (문서, 주장) 쌍이 "뒷받침됨"인지 판정하고 사람 판정과 비교한다.
#
# 하는 일:
#   1. pairs-01.md의 "## P<숫자>" 절마다 doc_id, doc_en, claim_id, claim_en, human, hypothesis를 읽는다.
#      doc_en이 "(same as P2)" 형태이면 해당 쌍의 doc_en을 가져다 쓴다.
#   2. MiniCheck(flan-t5-large)로 전체 쌍을 한 번에 판정한다. (라벨 1 = 뒷받침됨, 0 = 뒷받침 안 됨)
#   3. 자동 판정과 사람 판정(pairs-01.md의 human 값)을 같은 표에서 열을 나눠 적고, 갈린 쌍을 따로 모은다.
#      사람 판정 값은 읽기만 한다. 자동 판정 결과로 덮어쓰지 않는다.
#
# 입력: deep/05-citation/experiments/pairs-01.md
# 출력: deep/05-citation/experiments/results-01-layer2.md  (터미널에도 같은 내용을 출력)
#
# 실행: 저장소 루트에서
#   ~/.venvs/minicheck/bin/python deep/05-citation/experiments/scripts/run-minicheck.py
# 필요한 것: ~/.venvs/minicheck 가상환경에 설치된 MiniCheck (저장소 밖). 모델 가중치(약 3GB)는
#   ~/.cache/minicheck-ckpts 에 내려받으며 저장소 안에 두지 않는다.

import importlib.metadata
import json
import os
import re
import sys
import time
from collections import OrderedDict
from datetime import datetime
from pathlib import Path

MODEL_NAME = "flan-t5-large"
CACHE_DIR = os.path.expanduser("~/.cache/minicheck-ckpts")
VENV_DISPLAY = "~/.venvs/minicheck"

# 설치 직후 로그에서 옮겨 적은 값 (설치는 이 스크립트가 하지 않는다)
INSTALL_COMMANDS = [
    "python3 -m venv ~/.venvs/minicheck",
    'pip install "minicheck @ git+https://github.com/Liyan06/MiniCheck.git@main"  (가상환경 안의 pip)',
]
INSTALL_RESULT = "성공 (종료 코드 0)"
INSTALL_DURATION = "약 88초 (pip install, 2026-10-04 21:02:51 ~ 21:04:19 +0900)"
INSTALL_NOTES = [
    "[llm] 추가 의존성은 리눅스 전용이라 설치하지 않았다.",
    "pip 자체 업데이트 안내(25.0.1 -> 26.2.1)가 출력됐으나 오류가 아니다.",
]

LABEL_TEXT = {1: "뒷받침됨", 0: "뒷받침 안 됨"}
# pairs-01.md의 human 값을 라벨로 바꾸는 대응. "맞음"은 답변이 맞다는 뜻이므로 뒷받침됨(1)으로 대응시켜 비교한다.
HUMAN_TO_LABEL = {"맞음": 1, "뒷받침됨": 1, "뒷받침 안 됨": 0}

EXP_DIR = Path(__file__).resolve().parent.parent
PAIRS_PATH = EXP_DIR / "pairs-01.md"
OUT_PATH = EXP_DIR / "results-01-layer2.md"
KEYS = ("doc_id", "doc_en", "claim_id", "claim_en", "human", "hypothesis")


# ---------------------------------------------------------------- 입력 읽기

def parse_pairs(text):
    """"## P<숫자>" 절마다 KEYS의 값을 읽어 {쌍 이름: {키: 값}}을 만든다."""
    pairs = OrderedDict()
    current = None
    for line in text.split("\n"):
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


def resolve_docs(pairs):
    """doc_en이 "(same as P2)"이면 그 쌍의 doc_en을 가져온다."""
    resolved = OrderedDict()
    for name, fields in pairs.items():
        value = fields["doc_en"]
        seen = [name]
        while True:
            m = re.fullmatch(r"\(same as (P\d+)\)", value)
            if not m:
                break
            ref = m.group(1)
            if ref not in pairs or ref in seen:
                raise SystemExit("오류: %s의 doc_en이 가리키는 %s를 찾을 수 없거나 순환합니다." % (name, ref))
            seen.append(ref)
            value = pairs[ref]["doc_en"]
        resolved[name] = value
    return resolved


# ---------------------------------------------------------------- 출력 만들기

def minicheck_version():
    try:
        version = importlib.metadata.version("minicheck")
    except importlib.metadata.PackageNotFoundError:
        return "확인 필요 (버전 정보를 찾지 못함)"
    try:
        raw = importlib.metadata.distribution("minicheck").read_text("direct_url.json")
        commit = json.loads(raw)["vcs_info"]["commit_id"] if raw else None
    except Exception:
        commit = None
    return "%s (git commit %s)" % (version, commit[:12]) if commit else version


def cell(text):
    return text.replace("|", "\\|")


def compare(label, human):
    expected = HUMAN_TO_LABEL.get(human)
    if expected is None:
        return None
    return label == expected


def label_cell(label):
    return "%d (%s)" % (label, LABEL_TEXT[label])


def build_markdown(pairs, docs, labels, probs, meta):
    out = []
    out.append("# 실험 결과 01 — 층위 2 자동 판정 (MiniCheck)")
    out.append("")
    out.append("이 파일은 `run-minicheck.py`가 만든 결과다. 직접 고치지 않는다. "
               "층위 2는 인용한 조항의 내용이 답변 문장을 실제로 뒷받침하는지를 본다.")
    out.append("")
    out.append("## 1. 설치 기록")
    out.append("")
    out.append("- 가상환경 경로: `%s` (저장소 밖)" % VENV_DISPLAY)
    for c in INSTALL_COMMANDS:
        out.append("- 설치 명령: `%s`" % c)
    out.append("- 성공 여부: %s" % INSTALL_RESULT)
    out.append("- 설치에 걸린 시간: %s" % INSTALL_DURATION)
    for n in INSTALL_NOTES:
        out.append("- 참고: %s" % n)
    out.append("- 모델 이름: `%s` (내려받는 체크포인트 `lytang/MiniCheck-Flan-T5-Large`)" % MODEL_NAME)
    out.append("- 모델 캐시 경로: `~/.cache/minicheck-ckpts` (저장소 밖, 약 3GB)")
    out.append("")
    out.append("## 2. 실행 기록")
    out.append("")
    out.append("- 실행 명령: `%s`" % meta["command"])
    out.append("- 실행 시각: %s" % meta["now"])
    out.append("- 파이썬 버전: %s" % meta["python"])
    out.append("- MiniCheck 버전: %s" % meta["minicheck"])
    out.append("- 입력: [pairs-01.md](pairs-01.md) (쌍 %d개)" % len(pairs))
    out.append("- 모델 불러오기: %.1f초, 판정(전체 쌍 한 번에): %.1f초" % (meta["load_sec"], meta["score_sec"]))
    out.append("")
    out.append("## 3. 쌍별 판정")
    out.append("")
    out.append("자동 판정은 MiniCheck가 낸 값이고, 사람 판정은 pairs-01.md의 human 값을 그대로 옮긴 것이다. "
               "비교할 때 사람 판정 \"맞음\"은 \"뒷받침됨\"(1)으로, \"뒷받침 안 됨\"은 0으로 대응시켰다.")
    out.append("")
    out.append("| 쌍 | 문서 | 주장 | 자동 판정(라벨) | 확률 | 사람 판정 | 일치 여부 |")
    out.append("|----|------|------|-----------------|------|-----------|-----------|")
    diverged = []
    for (name, fields), label, prob in zip(pairs.items(), labels, probs):
        same = compare(label, fields["human"])
        verdict = "비교 불가" if same is None else ("일치" if same else "불일치")
        if same is False:
            diverged.append((name, label, fields))
        out.append("| %s | %s | [%s] %s | %s | %.4f | %s | %s |" % (
            name, cell(fields["doc_id"]), cell(fields["claim_id"]), cell(fields["claim_en"]),
            label_cell(label), prob, cell(fields["human"]), verdict))
    out.append("")
    out.append("## 4. 자동 판정과 사람 판정이 갈린 쌍")
    out.append("")
    if not diverged:
        out.append("갈린 쌍이 없다.")
        out.append("")
    for name, label, fields in diverged:
        out.append("### %s" % name)
        out.append("")
        out.append("- 자동 판정: %s, 사람 판정: %s" % (label_cell(label), fields["human"]))
        out.append("- pairs-01.md의 hypothesis: \"%s\"" % fields["hypothesis"])
        out.append("")
    out.append("## 5. 한계")
    out.append("")
    out.append("- 영어 데이터로 학습된 모델에 사람이 번역한 한국어 법령(문서)과 답변(주장)을 넣었다. "
               "한국어 원문을 그대로 넣은 것이 아니므로, 이 결과는 \"번역문 위에서의 판정\"이다.")
    out.append("- 번역이 판정을 바꿀 수 있다. 같은 내용이라도 어떤 영어 표현으로 옮겼는지에 따라 "
               "자동 판정이 달라질 수 있고, 이번 실험은 번역을 바꿔 가며 확인하지 않았다.")
    p8 = [(n, l) for (n, f), l in zip(pairs.items(), labels) if f["claim_id"] == "통제군"]
    if p8:
        n8, l8 = p8[0]
        if l8 == 0:
            out.append("- 통제군(%s)은 사람이 만든 거짓 주장이다. 판정기는 이것을 \"뒷받침 안 됨\"으로 판정해 사람 판정과 "
                       "일치했다. 다만 통제군이 한 쌍뿐이라 이것만으로 판정값 전체의 신뢰도를 보증하지는 못한다." % n8)
        else:
            out.append("- 통제군(%s)은 사람이 만든 거짓 주장인데 판정기가 \"뒷받침됨\"으로 판정했다. pairs-01.md의 %s "
                       "hypothesis는 \"%s\"라고 적고 있다. 따라서 이번 판정값 전체를 신뢰할 수 없다." % (
                           n8, n8, pairs[n8]["hypothesis"]))
    out.append("- 쌍이 %d개뿐이라 통계적인 결론은 낼 수 없다. 갈림과 일치는 개별 사례로만 읽는다." % len(pairs))
    out.append("")
    out.append("---")
    out.append("")
    out.append("[판정 쌍](pairs-01.md) · [층위 1 결과](results-01-layer1.md) · [결과 기록](results-01.md) · "
               "[실험 설계](design-01.md)")
    out.append("")
    return "\n".join(out), diverged


def main():
    pairs = parse_pairs(PAIRS_PATH.read_text(encoding="utf-8"))
    if not pairs:
        raise SystemExit("오류: pairs-01.md에서 '## P<숫자>' 절을 하나도 찾지 못했습니다.")
    docs = resolve_docs(pairs)
    doc_list = [docs[n] for n in pairs]
    claim_list = [f["claim_en"] for f in pairs.values()]

    # 모델은 실제 판정이 필요할 때만 불러온다 (무거운 import)
    from minicheck.minicheck import MiniCheck

    t0 = time.time()
    scorer = MiniCheck(model_name=MODEL_NAME, cache_dir=CACHE_DIR)
    load_sec = time.time() - t0

    t1 = time.time()
    pred_label, raw_prob, _, _ = scorer.score(docs=doc_list, claims=claim_list)
    score_sec = time.time() - t1

    labels = [int(x) for x in pred_label]
    probs = [float(x) for x in raw_prob]

    meta = {
        "command": "%s %s" % (VENV_DISPLAY + "/bin/python", " ".join(sys.argv)),
        "now": datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z"),
        "python": sys.version.split()[0],
        "minicheck": minicheck_version(),
        "load_sec": load_sec,
        "score_sec": score_sec,
    }
    markdown, diverged = build_markdown(pairs, docs, labels, probs, meta)
    OUT_PATH.write_text(markdown, encoding="utf-8")

    # 터미널 출력
    print("실행 명령: %s" % meta["command"])
    print("실행 시각: %s" % meta["now"])
    print("파이썬 버전: %s / MiniCheck 버전: %s" % (meta["python"], meta["minicheck"]))
    print("모델: %s (캐시 %s)" % (MODEL_NAME, CACHE_DIR))
    print("모델 불러오기 %.1f초, 판정 %.1f초" % (load_sec, score_sec))
    print()
    print("[쌍별 판정]")
    for (name, f), label, prob in zip(pairs.items(), labels, probs):
        same = compare(label, f["human"])
        verdict = "비교 불가" if same is None else ("일치" if same else "불일치")
        print("  %s | %s | %s | 자동 %s | 확률 %.4f | 사람 %s | %s" % (
            name, f["doc_id"], f["claim_id"], label_cell(label), prob, f["human"], verdict))
    print()
    print("[갈린 쌍] %s" % (", ".join(n for n, _, _ in diverged) if diverged else "없음"))
    print("출력 파일: %s" % OUT_PATH)


if __name__ == "__main__":
    main()
