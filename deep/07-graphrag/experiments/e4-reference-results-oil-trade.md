# E4 기준 그래프 대 에이전트 그래프 (2번 도메인 무역 & 기름)

2026-10-22, 정답 디스크를 연 격리 Claude Code 대화에서 돌렸다(handoff.md 8절 순서). 기준 그래프(reference-triples.csv, 디스크 안)는 대화가 열지 않고 스크립트에 경로만 넘겼다. 방법은 [e4-method-oil-trade.md](e4-method-oil-trade.md)(짝짓기 1~7번)다. A는 기준 그래프, B는 에이전트 그래프다. 이 파일에는 스크립트가 낸 개수·비율과 해시 확인 결과만 적었다. R은 저장소 경로다.

## 1. 기준 그래프 해시 확인

```bash
cd /Volumes/rag-answer-keys/oil-trade && shasum -a 256 -c $R/deep/07-graphrag/oil-trade/answer-key.sha256
```

```
answer-key.md: OK
reference-triples.csv: OK
t5-statement.md: OK
```

## 2. 기준 그래프 형식 검사

```bash
python3 $R/deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py /Volumes/rag-answer-keys/oil-trade/reference-triples.csv | grep -v '별 줄 수:' | sed -E 's/^줄 [0-9]+: //' | sort | uniq -c
```

```
  11 경고: space-only
   1 줄 139개, 위반 0건, 경고 11건
```

## 3. 기준 대 1회차

```bash
python3 $R/deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py /Volumes/rag-answer-keys/oil-trade/reference-triples.csv $R/deep/07-graphrag/oil-trade/agent-graph-1.csv
```

```
A 줄 수: 139, B 줄 수: 34 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 18, 후보가 둘 이상이었던 줄 수: A 2, B 0
닫힌 목록 일치율: 15 / 15 (100.0%)
칸별 일치율: 분류 체계 5 / 5 (100.0%), 업무 단계 5 / 5 (100.0%), 주체 5 / 5 (100.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 18 / 139 (12.9%) / 관계별: 원문 용어 8 / 12 (66.7%), 품목 분류 5 / 22 (22.7%), 요건 5 / 105 (4.8%)
B 정밀도: 18 / 34 (52.9%) / 관계별: 원문 용어 8 / 9 (88.9%), 품목 분류 5 / 13 (38.5%), 요건 5 / 12 (41.7%)
자카드 지수: 18 / 155 (11.6%)
```

## 4. 기준 대 2회차

```bash
python3 $R/deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py /Volumes/rag-answer-keys/oil-trade/reference-triples.csv $R/deep/07-graphrag/oil-trade/agent-graph-2.csv
```

```
A 줄 수: 139, B 줄 수: 38 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 21, 후보가 둘 이상이었던 줄 수: A 2, B 0
닫힌 목록 일치율: 17 / 17 (100.0%)
칸별 일치율: 분류 체계 7 / 7 (100.0%), 업무 단계 5 / 5 (100.0%), 주체 5 / 5 (100.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 21 / 139 (15.1%) / 관계별: 원문 용어 9 / 12 (75.0%), 품목 분류 7 / 22 (31.8%), 요건 5 / 105 (4.8%)
B 정밀도: 21 / 38 (55.3%) / 관계별: 원문 용어 9 / 12 (75.0%), 품목 분류 7 / 14 (50.0%), 요건 5 / 12 (41.7%)
자카드 지수: 21 / 156 (13.5%)
```
