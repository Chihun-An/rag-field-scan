# E5 채점용 A/B 사본과 열쇠 만들기
#
# 하는 일: 도메인 순서(ai-consulting, oil-trade)대로 r = random.Random(20261026)에서 r.random()을 한 번씩 뽑아,
#   0.5보다 작으면 검색만을 A, 아니면 그래프 경유를 A로 한다.
#   각 답 JSON을 읽어 모든 문자열 값에서 "graph.csv"를 먼저, 그다음 "그래프"를 "[가림]"으로 바꾼다.
#   두 답 모두에 똑같이 하고, 다른 글자는 바꾸지 않는다(칸 이름은 그대로 둔다).
#   표준 출력에는 만든 파일 이름과 "완료"만 쓴다. 어느 쪽이 A인지, 바꾼 횟수는 쓰지 않는다.
#   python 표준 라이브러리만 쓴다.
# 입력: deep/07-graphrag/ai-consulting/e5-answers-search.json, e5-answers-graph.json,
#   deep/07-graphrag/oil-trade/e5-answers-search.json, e5-answers-graph.json (원본은 고치지 않는다)
# 출력: Claude outputs/e5-blind/<도메인>-A.json, <도메인>-B.json(UTF-8, 원본과 같은 구조),
#   Claude outputs/e5-blind/key.json(도메인마다 A·B가 어느 방식인지, 파일마다 바꾼 횟수).
#   "Claude outputs/"는 .gitignore에 있어 커밋되지 않는다.
# 실행: python3 deep/07-graphrag/experiments/scripts/make-e5-blind.py

import json
import random
from pathlib import Path

G = Path(__file__).resolve().parent.parent.parent  # deep/07-graphrag
OUT = G.parent.parent / "Claude outputs" / "e5-blind"
DOMAINS = ["ai-consulting", "oil-trade"]
MASK = "[가림]"


def mask(value, counter):
    """모든 문자열 값에서 graph.csv, 그래프 순서로 가린다. counter[0]에 바꾼 횟수를 더한다."""
    if isinstance(value, str):
        n1 = value.count("graph.csv")
        value = value.replace("graph.csv", MASK)
        n2 = value.count("그래프")
        value = value.replace("그래프", MASK)
        counter[0] += n1 + n2
        return value
    if isinstance(value, list):
        return [mask(v, counter) for v in value]
    if isinstance(value, dict):
        return {k: mask(v, counter) for k, v in value.items()}
    return value


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    r = random.Random(20261026)
    key = {}
    for dom in DOMAINS:
        a_method = "search" if r.random() < 0.5 else "graph"
        b_method = "graph" if a_method == "search" else "search"
        key[dom] = {"A": a_method, "B": b_method, "바꾼 횟수": {}}
        for side, method in (("A", a_method), ("B", b_method)):
            data = json.loads((G / dom / f"e5-answers-{method}.json").read_text(encoding="utf-8"))
            counter = [0]
            masked = mask(data, counter)
            name = f"{dom}-{side}.json"
            (OUT / name).write_text(json.dumps(masked, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            key[dom]["바꾼 횟수"][name] = counter[0]
            print(name)
    (OUT / "key.json").write_text(json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("key.json")
    print("완료")


if __name__ == "__main__":
    main()
