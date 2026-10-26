# E5 골든 룰 검사 결과 (층위 1)

## ai-consulting search

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/ai-consulting/e5-answers-search.json
```

```
검사한 질문 15개, 주장 245개
위반 1건
질문	주장	규칙	이유
T4	-	G8	상태가 "자료에 없음"이 아님: '전제가 틀림'
```

종료 코드: 1

## ai-consulting graph

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/ai-consulting/e5-answers-graph.json
```

```
검사한 질문 15개, 주장 273개
위반 2건
질문	주장	규칙	이유
T1	-	G8	상태가 "자료에 없음"이 아님: '전제가 틀림'
T4	-	G8	상태가 "자료에 없음"이 아님: '전제가 틀림'
경고 2건
질문	주장	규칙	이유
Q5	11	G4 경고(space-only)	공백을 모두 지우면 원장 6번 원문에 있음
Q9	17	G4 경고(space-only)	공백을 모두 지우면 원장 6번 원문에 있음
```

종료 코드: 1

## oil-trade search

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py deep/07-graphrag/oil-trade/e5-answers-search.json
```

```
검사한 질문 15개, 주장 255개, 근거 358개
위반 5건
질문	주장	근거	규칙	이유
T4	-	-	G8	상태가 "자료에 없음"이 아님: '전제가 틀림'
Q1	1	2	G9	Q1의 근거는 원장 4번이어야 하는데 5
Q1	1	2	G9	Q1의 근거 위치에 "제7조"가 없음: '시행령 제5조제1항'
Q1	2	2	G9	Q1의 근거는 원장 4번이어야 하는데 5
Q1	2	2	G9	Q1의 근거 위치에 "제7조"가 없음: '시행령 제5조제2항'
```

종료 코드: 1

## oil-trade graph

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py deep/07-graphrag/oil-trade/e5-answers-graph.json
```

```
검사한 질문 15개, 주장 216개, 근거 248개
위반 2건
질문	주장	근거	규칙	이유
Q5	-	-	G2	상태가 답함인데 주장이 없음
T4	-	-	G8	상태가 "자료에 없음"이 아님: '전제가 틀림'
경고 45건
질문	주장	근거	규칙	이유
Q4	15	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	16	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	17	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	18	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	19	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	20	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	21	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q4	23	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q6	1	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	2	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	3	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	4	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	5	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	6	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	7	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	8	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	13	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	14	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	15	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	16	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	17	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	18	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	19	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q6	20	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q7	1	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q7	2	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q7	3	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q8	1	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q8	2	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q8	3	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q9	1	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q9	2	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q9	5	1	G4 경고(space-only)	공백을 모두 지우면 원장 14번 원문에 있음
Q9	7	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	4	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	5	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	6	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	7	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	8	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	9	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	10	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	11	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	12	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	13	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
Q10	14	1	G4 경고(space-only)	공백을 모두 지우면 원장 11번 원문에 있음
```

종료 코드: 1
