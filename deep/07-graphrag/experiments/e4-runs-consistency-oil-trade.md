# E4 회차끼리 일관성 (2번 도메인 무역 & 기름)

2026-10-22, 에이전트 그래프 1회차(oil-trade/agent-graph-1.csv)와 2회차(oil-trade/agent-graph-2.csv)를 [compare-graphs-oil-trade.py](scripts/compare-graphs-oil-trade.py)로 비교했다. 방법은 [e4-method-oil-trade.md](e4-method-oil-trade.md) "회차끼리 일관성"이다(짝짓기 7번까지 적용). 기준 그래프를 쓰지 않으므로 디스크를 열지 않았다. A는 1회차, B는 2회차다.

- 짝짓기 7번을 더하기 전에 Cowork가 같은 비교를 돌린 결과: 짝 23, 자카드 23/49(46.9%), 품목 분류 줄 짝 4/13(1회차 기준). 이 결과를 보고 짝짓기 7번을 더했다(방법 파일 끝 "추가" 문단).

## 결과

```bash
python3 deep/07-graphrag/experiments/scripts/compare-graphs-oil-trade.py deep/07-graphrag/oil-trade/agent-graph-1.csv deep/07-graphrag/oil-trade/agent-graph-2.csv
```

```
A 줄 수: 34, B 줄 수: 38 (칸 수가 틀려 뺀 줄: A 0, B 0)
짝 수: 30, 후보가 둘 이상이었던 줄 수: A 3, B 2
닫힌 목록 일치율: 31 / 31 (100.0%)
칸별 일치율: 분류 체계 11 / 11 (100.0%), 업무 단계 10 / 10 (100.0%), 주체 10 / 10 (100.0%)
뺀 칸 수: 양쪽 모두 기타 0, 양쪽 빈 칸 0
A 재현율: 30 / 34 (88.2%) / 관계별: 원문 용어 9 / 9 (100.0%), 품목 분류 11 / 13 (84.6%), 요건 10 / 12 (83.3%)
B 정밀도: 30 / 38 (78.9%) / 관계별: 원문 용어 9 / 12 (75.0%), 품목 분류 11 / 14 (78.6%), 요건 10 / 12 (83.3%)
자카드 지수: 30 / 42 (71.4%)
```
