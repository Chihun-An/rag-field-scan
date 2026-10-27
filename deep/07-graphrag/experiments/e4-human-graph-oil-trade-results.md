# 2번 사람 그래프 대 에이전트 그래프

2026-10-27. 방법과 예측은 [e4-human-graph-oil-trade-method.md](e4-human-graph-oil-trade-method.md)이고 사람 그래프보다 먼저 커밋했다. A는 사람 그래프(원장 4·11·14·17번), B는 에이전트 그래프에서 같은 원장의 줄만 남긴 것이다. 짝짓기 규칙은 [2번 E4 방법](e4-method-oil-trade.md) 1~7번이다.

## 1. 사람 그래프 형식 검사와 줄 수

```bash
python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py deep/07-graphrag/oil-trade/human-graph.csv
```

```
관계별 줄 수: 원문 용어 2, 품목 분류 3, 요건 4
주어별 줄 수: UMO 0, ULO 9, PPO 0, 그 밖의 주어 0
줄 9개, 위반 0건, 경고 0건
```

```bash
python3 - deep/07-graphrag/oil-trade/human-graph.csv <<'EOF'
# 사람 그래프의 원장별·관계별 줄 수를 센다(값은 출력하지 않음). 표준 라이브러리만 쓴다.
import csv, sys
from collections import Counter
with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))
head, data = rows[0], rows[1:]
ok = [dict(zip(head, r)) for r in data if len(r) == len(head)]
print(f"데이터 줄 수: {len(data)} (칸 수가 맞는 줄 {len(ok)})")
ledgers = ["4", "11", "14", "17"]
rels = ["원문 용어", "품목 분류", "요건"]
led = Counter(r["원장 번호"].strip() for r in ok)
rel = Counter(r["관계"].strip() for r in ok)
both = Counter((r["원장 번호"].strip(), r["관계"].strip()) for r in ok)
print("원장별 줄 수: " + ", ".join(f"{l}번 {led.get(l, 0)}" for l in ledgers)
      + f" / 그 밖의 원장 {sum(v for k, v in led.items() if k not in ledgers)}")
print("관계별 줄 수: " + ", ".join(f"{k} {rel.get(k, 0)}" for k in rels)
      + f" / 그 밖의 관계 {sum(v for k, v in rel.items() if k not in rels)}")
for l in ledgers:
    print(f"원장 {l}번 관계별: " + ", ".join(f"{k} {both.get((l, k), 0)}" for k in rels))
EOF
```

```
데이터 줄 수: 9 (칸 수가 맞는 줄 9)
원장별 줄 수: 4번 0, 11번 2, 14번 4, 17번 3 / 그 밖의 원장 0
관계별 줄 수: 원문 용어 2, 품목 분류 3, 요건 4 / 그 밖의 관계 0
원장 4번 관계별: 원문 용어 0, 품목 분류 0, 요건 0
원장 11번 관계별: 원문 용어 1, 품목 분류 1, 요건 0
원장 14번 관계별: 원문 용어 0, 품목 분류 0, 요건 4
원장 17번 관계별: 원문 용어 1, 품목 분류 2, 요건 0
```

## 2. 사람 대 1회차

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/human-graph.csv deep/07-graphrag/oil-trade/agent-graph-1.csv --ledger 4,11,14,17
```

```
원장 거르기: 4,11,14,17
A 줄 수: 9, B 줄 수: 24 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 3, 후보가 둘 이상이었던 줄 수: A 0, B 0
닫힌 목록 일치율: 1 / 1 (100.0%)
칸별 일치율: 분류 체계 1 / 1 (100.0%), 업무 단계 0 / 0 (해당 없음), 주체 0 / 0 (해당 없음)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 3 / 9 (33.3%) / 관계별: 원문 용어 2 / 2 (100.0%), 품목 분류 1 / 3 (33.3%), 요건 0 / 4 (0.0%)
B 정밀도: 3 / 24 (12.5%) / 관계별: 원문 용어 2 / 3 (66.7%), 품목 분류 1 / 12 (8.3%), 요건 0 / 9 (0.0%)
자카드 지수: 3 / 30 (10.0%)
```

## 3. 사람 대 2회차

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/human-graph.csv deep/07-graphrag/oil-trade/agent-graph-2.csv --ledger 4,11,14,17
```

```
원장 거르기: 4,11,14,17
A 줄 수: 9, B 줄 수: 28 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 3, 후보가 둘 이상이었던 줄 수: A 0, B 0
닫힌 목록 일치율: 1 / 1 (100.0%)
칸별 일치율: 분류 체계 1 / 1 (100.0%), 업무 단계 0 / 0 (해당 없음), 주체 0 / 0 (해당 없음)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 3 / 9 (33.3%) / 관계별: 원문 용어 2 / 2 (100.0%), 품목 분류 1 / 3 (33.3%), 요건 0 / 4 (0.0%)
B 정밀도: 3 / 28 (10.7%) / 관계별: 원문 용어 2 / 5 (40.0%), 품목 분류 1 / 13 (7.7%), 요건 0 / 10 (0.0%)
자카드 지수: 3 / 34 (8.8%)
```
