# 2번 사람 그래프 v2 대 에이전트 그래프

2026-10-27. 방법과 예측은 [e4-human-graph-oil-trade-method.md](e4-human-graph-oil-trade-method.md) 6절이고 v2보다 먼저 커밋했다(e5606f3). v2는 v1 9줄에 줄 16줄을 더한 것이다(2efe82a). A는 v2 전체 또는 추가한 줄만, B는 에이전트 그래프에서 원장 4·11·14·17번 줄만 남긴 것이다. 짝짓기 규칙은 [2번 E4 방법](e4-method-oil-trade.md) 1~7번이다. v1 결과는 [e4-human-graph-oil-trade-results.md](e4-human-graph-oil-trade-results.md)이다.

## 1. 추가한 줄만 떼어 내기

```bash
python3 - <<'EOF'
# v2에서 v1 9줄(앞부분, 순서 그대로)을 뺀 나머지를 human-graph-v2-added.csv로 쓴다. 표준 라이브러리만 쓴다.
import csv, io
d = "deep/07-graphrag/oil-trade/"
v1 = list(csv.reader(open(d + "human-graph.csv", encoding="utf-8-sig", newline="")))
v2 = list(csv.reader(open(d + "human-graph-v2.csv", encoding="utf-8-sig", newline="")))
assert v2[:len(v1)] == v1, "v1 줄이 v2 앞부분에 그대로 있지 않음"
out = [v2[0]] + v2[len(v1):]
buf = io.StringIO(); csv.writer(buf, lineterminator="\r\n").writerows(out)
open(d + "human-graph-v2-added.csv", "w", encoding="utf-8", newline="").write(buf.getvalue())
print(f"v1 줄이 v2 앞부분에 그대로 있음: True / 추가한 줄: {len(out) - 1}")
EOF
```

```
v1 줄이 v2 앞부분에 그대로 있음: True / 추가한 줄: 16
```

## 2. 형식 검사: v2 전체

```bash
python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py deep/07-graphrag/oil-trade/human-graph-v2.csv
```

```
관계별 줄 수: 원문 용어 5, 품목 분류 4, 요건 16
주어별 줄 수: UMO 3, ULO 10, PPO 12, 그 밖의 주어 0
줄 25개, 위반 0건, 경고 0건
```

## 3. 형식 검사: 추가한 줄만

```bash
python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py deep/07-graphrag/oil-trade/human-graph-v2-added.csv
```

```
관계별 줄 수: 원문 용어 3, 품목 분류 1, 요건 12
주어별 줄 수: UMO 3, ULO 1, PPO 12, 그 밖의 주어 0
줄 16개, 위반 0건, 경고 0건
```

## 4. 추가한 줄의 원장별 줄 수

```bash
python3 - deep/07-graphrag/oil-trade/human-graph-v2-added.csv <<'EOF'
# 추가한 줄의 원장별·주어·관계별 줄 수를 센다(값은 출력하지 않음). 표준 라이브러리만 쓴다.
import csv, sys
from collections import Counter
with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
    rows = list(csv.reader(f))
head, data = rows[0], [dict(zip(rows[0], r)) for r in rows[1:]]
for l in ["4", "11", "14", "17"]:
    c = Counter((r["주어"].strip(), r["관계"].strip()) for r in data if r["원장 번호"].strip() == l)
    print(f"원장 {l}번: " + (", ".join(f"{s} {k} {v}" for (s, k), v in sorted(c.items())) or "0줄"))
EOF
```

```
원장 4번: 0줄
원장 11번: UMO 원문 용어 2, UMO 품목 분류 1
원장 14번: PPO 요건 11, PPO 원문 용어 1, ULO 요건 1
원장 17번: 0줄
```

## 5. v2 전체 대 1회차

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/human-graph-v2.csv deep/07-graphrag/oil-trade/agent-graph-1.csv --ledger 4,11,14,17
```

```
원장 거르기: 4,11,14,17
A 줄 수: 25, B 줄 수: 24 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 6, 후보가 둘 이상이었던 줄 수: A 0, B 0
닫힌 목록 일치율: 3 / 5 (60.0%)
칸별 일치율: 분류 체계 1 / 1 (100.0%), 업무 단계 2 / 2 (100.0%), 주체 0 / 2 (0.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 6 / 25 (24.0%) / 관계별: 원문 용어 3 / 5 (60.0%), 품목 분류 1 / 4 (25.0%), 요건 2 / 16 (12.5%)
B 정밀도: 6 / 24 (25.0%) / 관계별: 원문 용어 3 / 3 (100.0%), 품목 분류 1 / 12 (8.3%), 요건 2 / 9 (22.2%)
자카드 지수: 6 / 43 (14.0%)
```

## 6. v2 전체 대 2회차

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/human-graph-v2.csv deep/07-graphrag/oil-trade/agent-graph-2.csv --ledger 4,11,14,17
```

```
원장 거르기: 4,11,14,17
A 줄 수: 25, B 줄 수: 28 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 7, 후보가 둘 이상이었던 줄 수: A 0, B 1
닫힌 목록 일치율: 3 / 5 (60.0%)
칸별 일치율: 분류 체계 1 / 1 (100.0%), 업무 단계 2 / 2 (100.0%), 주체 0 / 2 (0.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 7 / 25 (28.0%) / 관계별: 원문 용어 4 / 5 (80.0%), 품목 분류 1 / 4 (25.0%), 요건 2 / 16 (12.5%)
B 정밀도: 7 / 28 (25.0%) / 관계별: 원문 용어 4 / 5 (80.0%), 품목 분류 1 / 13 (7.7%), 요건 2 / 10 (20.0%)
자카드 지수: 7 / 46 (15.2%)
```

## 7. 추가한 줄만 대 1회차

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/human-graph-v2-added.csv deep/07-graphrag/oil-trade/agent-graph-1.csv --ledger 4,11,14,17
```

```
원장 거르기: 4,11,14,17
A 줄 수: 16, B 줄 수: 24 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 3, 후보가 둘 이상이었던 줄 수: A 0, B 0
닫힌 목록 일치율: 2 / 4 (50.0%)
칸별 일치율: 분류 체계 0 / 0 (해당 없음), 업무 단계 2 / 2 (100.0%), 주체 0 / 2 (0.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 3 / 16 (18.8%) / 관계별: 원문 용어 1 / 3 (33.3%), 품목 분류 0 / 1 (0.0%), 요건 2 / 12 (16.7%)
B 정밀도: 3 / 24 (12.5%) / 관계별: 원문 용어 1 / 3 (33.3%), 품목 분류 0 / 12 (0.0%), 요건 2 / 9 (22.2%)
자카드 지수: 3 / 37 (8.1%)
```

## 8. 추가한 줄만 대 2회차

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/human-graph-v2-added.csv deep/07-graphrag/oil-trade/agent-graph-2.csv --ledger 4,11,14,17
```

```
원장 거르기: 4,11,14,17
A 줄 수: 16, B 줄 수: 28 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 4, 후보가 둘 이상이었던 줄 수: A 0, B 1
닫힌 목록 일치율: 2 / 4 (50.0%)
칸별 일치율: 분류 체계 0 / 0 (해당 없음), 업무 단계 2 / 2 (100.0%), 주체 0 / 2 (0.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 4 / 16 (25.0%) / 관계별: 원문 용어 2 / 3 (66.7%), 품목 분류 0 / 1 (0.0%), 요건 2 / 12 (16.7%)
B 정밀도: 4 / 28 (14.3%) / 관계별: 원문 용어 2 / 5 (40.0%), 품목 분류 0 / 13 (0.0%), 요건 2 / 10 (20.0%)
자카드 지수: 4 / 40 (10.0%)
```
