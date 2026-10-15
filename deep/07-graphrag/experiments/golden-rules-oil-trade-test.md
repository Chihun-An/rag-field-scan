# 골든 룰 검사 스크립트 시험 (2번 무역 & 기름, E3)

[check-golden-rules-oil-trade.py](scripts/check-golden-rules-oil-trade.py)가 [2번 골든 룰](../oil-trade/golden-rules.md) G1~G9를 기대대로 잡는지 시험 파일 네 개로 확인했다. 2026-10-15, Claude Code가 돌렸다.

- 시험 파일: [oil-trade-golden-rules-pass.json](fixtures/oil-trade-golden-rules-pass.json), [oil-trade-golden-rules-fail.json](fixtures/oil-trade-golden-rules-fail.json), [oil-trade-golden-rules-empty.json](fixtures/oil-trade-golden-rules-empty.json), [oil-trade-golden-rules-controls-only.json](fixtures/oil-trade-golden-rules-controls-only.json)
- 시험 파일에는 원장 제목(sources.csv 4·5·8번), 원문 머리줄(ot-17.txt에서 글자가 있는 첫 줄 "■ 관세법 [별표] <개정 2022. 12. 31.>"), 일부러 틀린 값(원장 18번, "협력", "통관", 비어 있는 분류 체계, 주어 UMO 등), "테스트"·"기타: 테스트"·"테스트 분류 값" 같은 문자열만 썼다. 실제 분류·요건·업무 단계 값을 원문에서 찾아 쓰지 않았고, 정답(기대 답)은 보지 않았다.
- 설치한 도구 없음(python 표준 라이브러리만). 1번 스크립트(check-golden-rules.py)와 1번 시험 파일은 고치지 않았다.
- 기대: pass 0, fail 1(G1~G9가 하나씩), empty 2, controls-only 0. 처음 돌린 결과가 기대와 같아 스크립트를 고친 일은 없다.

## 1. 실행과 출력

모두 저장소 맨 위에서 돌렸다.

### 통과 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-golden-rules-pass.json
```

종료 코드: 0

```
검사한 질문 7개, 주장 3개, 근거 4개
위반 없음
```

### 위반 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-golden-rules-fail.json
```

종료 코드: 1

```
검사한 질문 9개, 주장 8개, 근거 9개
위반 11건
질문	주장	근거	규칙	이유
Q10	-	-	G1	"요약" 칸이 없음
Q5	-	-	G2	상태가 답함인데 주장이 없음
Q6	1	1	G3	원장에 없는 번호: 18
Q6	1	1	G4	근거 문장이 원장 4번 원문에 없음
Q6	1	-	G5	스키마 2절에 없는 관계: '협력'
Q6	1	-	G6	"업무 단계"의 목록에 없는 값: '통관'
Q6	1	-	G7	품목 분류인데 "분류 체계"가 비어 있음
Q6	1	-	G7	품목 분류인데 "업무 단계"가 채워져 있음: '기타: 테스트'
T1	-	-	G8	상태가 "자료에 없음"이 아님: '답함'
T1	-	-	G8	주장이 0개가 아님: 1개
Q2	1	-	G9	Q2의 주장은 주어가 ULO여야 하는데 'UMO'
```

### 입력 오류 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-golden-rules-empty.json
```

종료 코드: 2

```
입력 오류: 질문을 하나도 읽지 못함(질문 0개)
```

### 통제 항목만 든 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-golden-rules-controls-only.json
```

종료 코드: 0

```
검사한 질문 3개, 주장 0개, 근거 0개
위반 없음
```

## 2. 판정 표

| 시험 파일 | 시험 항목 | 걸려야 할 규칙 | 코드 판정 | 사람 판정 |
|-----------|-----------|----------------|-----------|-----------|
| pass | Q1 답함: 주어 "테스트 분류 값", 요건, 업무 단계·주체 "기타: 테스트", 근거 원장 4번 "제7조"(근거 문장 = 4번 제목) | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | Q2 답함: 주어 ULO, 품목 분류, 분류 체계 "기타: 테스트", 근거 두 개(원장 17번 머리줄, 원장 5번 제목) | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | Q5 답함: 주어 PPO, 원문 용어, 세 칸 빈 문자열, 근거 원장 8번 제목 | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | T1·T3·T4 자료에 없음, T2 전제가 틀림(모두 주장 없음) | 없음 | 위반 없음 | 에드워드 확인 전 |
| fail | "요약" 칸이 없는 항목(Q10) | G1 | G1 | 에드워드 확인 전 |
| fail | Q5 답함인데 주장 없음 | G2 | G2 | 에드워드 확인 전 |
| fail | 근거의 원장 번호 18 | G3 | G3 | 에드워드 확인 전 |
| fail | 원장 4번, 근거 문장 "이 문장은 원문에 없는 테스트 문장이다" | G4 | G4 | 에드워드 확인 전 |
| fail | 관계 "협력" | G5 | G5 | 에드워드 확인 전 |
| fail | 요건인데 업무 단계 "통관" | G6 | G6 | 에드워드 확인 전 |
| fail | 품목 분류인데 분류 체계가 비어 있고 업무 단계가 "기타: 테스트" | G7 | G7(두 조건으로 두 건) | 에드워드 확인 전 |
| fail | T1 답함, 주장 하나 | G8 | G8(상태, 주장 수 두 건) | 에드워드 확인 전 |
| fail | Q2 답함, 주어 UMO(나머지는 통과용 Q2와 같음) | G9 | G9 | 에드워드 확인 전 |
| empty | 빈 목록 [] | 입력 오류(종료 코드 2) | 종료 코드 2 | 에드워드 확인 전 |
| controls-only | T1·T3·T4 자료에 없음, 주장 0개 | 위반 없음, 종료 코드 0 | 위반 없음, 종료 코드 0 | 에드워드 확인 전 |

- 위반 시험의 각 항목에는 걸려야 할 규칙 말고 다른 규칙이 걸리지 않았다. G7과 G8만 한 항목에서 두 조건이 함께 걸렸다.

## 3. 구현에서 정한 것

- 스키마 확인: 제품·분류 체계·업무 단계·주체·관계 이름 상수가 oil-trade/schema.md 본문에 그대로 있는지 시작할 때 확인한다. 분류 체계 "HS(관세율표·WCO)"는 1번의 "생성형 AI(LLM 포함)" 정정과 같이 스키마 3절 표기를 괄호까지 그대로 목록 이름으로 썼다
- G1: 주장의 일곱 칸이 없거나 근거가 목록이 아니면 G1. 근거 안의 세 칸(원장 번호·위치·근거 문장)이 비었는지는 G2로 본다(상태가 "답함"일 때만, golden-rules.md 문구대로)
- G4는 원장 번호가 원장에 있을 때만 본다(번호가 없으면 G3만 보고). 정규화와 하이픈 처리는 1번 스크립트와 같은 함수다
- G7은 관계가 원문 용어·품목 분류·요건일 때만 본다(관계가 스키마에 없으면 G5만 보고)
- G9의 Q1 조건 가운데 "관계가 요건"은 주장 단위로, "원장 4번·위치에 제7조"는 근거 단위로 보고한다. Q2의 "원장 17번이 하나 이상"은 주장 단위로 본다
