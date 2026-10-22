# 골든 룰 검사 스크립트 시험 (1번 AI 컨설팅, E3)

[check-golden-rules.py](scripts/check-golden-rules.py)가 [골든 룰](../ai-consulting/golden-rules.md) G1~G9를 기대대로 잡는지 시험 파일 세 개로 확인했다. 2026-10-14, Claude Code가 돌렸다.

- 시험 파일: [golden-rules-pass.json](fixtures/golden-rules-pass.json), [golden-rules-fail.json](fixtures/golden-rules-fail.json), [golden-rules-empty.json](fixtures/golden-rules-empty.json)
- 시험 파일에는 공개 정보(원장 제목, sources.csv의 수행 펌)와 일부러 틀린 값("테스트", "기타: 테스트", 원장 18번, "협력", "인수합병 자문", BCG 등)만 썼다. 사례를 분류한 내용(업무 유형·기술·산업·병목·성과의 실제 값)과 정답(기대 답)은 쓰지 않았다.
- 설치한 도구 없음(python 표준 라이브러리만). 실행 환경: macOS, 시스템 python3
- 한 번에 기대대로 나와 스크립트를 고친 일은 없다.

## 1. 실행과 출력

모두 저장소 맨 위에서 돌렸다.

### 통과 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-pass.json
```

종료 코드: 0

```
검사한 질문 5개, 주장 5개
위반 없음
```

### 위반 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-fail.json
```

종료 코드: 1

```
검사한 질문 9개, 주장 8개
위반 10건
질문	주장	규칙	이유
Q10	-	G1	"요약" 칸이 없음
Q5	-	G2	상태가 답함인데 주장이 없음
Q6	1	G3	원장에 없는 번호: 18
Q8	1	G4	근거 문장이 원장 3번 원문에 없음
Q9	1	G5	스키마 6절에 없는 관계: '협력'
Q10	1	G6	"적용 업무"의 목록에 없는 값: '인수합병 자문'
Q6	1	G7	원장 3번의 펌은 McKinsey인데 값은 'BCG'
T1	-	G8	상태가 "자료에 없음"이 아님: '답함'
T1	-	G8	주장이 0개가 아님: 1개
Q1	1	G9	Q1의 주장은 원장 2번이어야 하는데 3
```

### 입력 오류 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-empty.json
```

종료 코드: 2

```
입력 오류: 질문이나 주장을 하나도 읽지 못함(질문 0개, 주장 0개)
```

## 2. 판정 표

| 시험 파일 | 시험 항목 | 걸려야 할 규칙 | 코드 판정 | 사람 판정 |
|-----------|-----------|----------------|-----------|-----------|
| pass | Q5 답함: 원장 3번 수행 McKinsey(근거 = 3번 제목), 원장 7번 수행 Bain(근거 = 7번 제목) | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | Q6 답함: 원장 9번 수행 Deloitte(근거 "원장") | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | Q8 답함: 원장 11번 적용 업무 "기타: 테스트"(근거 = 11번 제목) | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | T1 자료에 없음(주장 없음) | 없음 | 위반 없음 | 에드워드 확인 전 |
| pass | T2 전제가 틀림: 원장 1번 수행 McKinsey(근거 "원장") | 없음 | 위반 없음 | 에드워드 확인 전 |
| fail | "요약" 칸이 없는 항목(Q10, 원장 3번 수행 McKinsey, 근거 "원장") | G1 | G1 | 에드워드 확인 전 |
| fail | Q5 답함인데 주장 없음 | G2 | G2 | 에드워드 확인 전 |
| fail | 원장 18번 수행 McKinsey(근거 "원장") | G3 | G3 | 에드워드 확인 전 |
| fail | 원장 3번 수행 McKinsey(근거 "이 문장은 원문에 없는 테스트 문장이다") | G4 | G4 | 에드워드 확인 전 |
| fail | 원장 3번 관계 "협력", 값 "테스트"(근거 = 3번 제목) | G5 | G5 | 에드워드 확인 전 |
| fail | 원장 3번 적용 업무 "인수합병 자문"(근거 = 3번 제목) | G6 | G6 | 에드워드 확인 전 |
| fail | 원장 3번 수행 BCG(근거 "원장") | G7 | G7 | 에드워드 확인 전 |
| fail | T1 답함, 원장 3번 수행 McKinsey(근거 "원장") | G8 | G8(상태, 주장 수 두 건) | 에드워드 확인 전 |
| fail | Q1 답함, 원장 3번 수행 McKinsey(근거 "원장") | G9 | G9 | 에드워드 확인 전 |
| empty | 빈 목록 [] | 입력 오류(종료 코드 2) | 종료 코드 2 | 에드워드 확인 전 |

- 위반 시험의 각 항목에는 걸려야 할 규칙 말고 다른 규칙이 걸리지 않았다(위 출력에서 항목마다 규칙 하나. T1만 G8이 두 조건으로 두 번 걸림).
- G4 정규화: 원장 7번 제목은 원문에 그대로는 없고(줄바꿈으로 나뉨), 공백·줄바꿈을 한 칸으로 줄인 뒤에는 있다. 3번·11번 제목은 원문에 그대로 있다. 통과 시험의 7번 항목이 정규화를 거쳐 통과한 것을 별도로 확인했다(원문 내용은 출력하지 않음).

## 3. 구현에서 정한 것

- 스키마 확인: 펌·산업·업무 유형·AI 기술·관계 이름 상수가 schema.md 본문에 그대로 있는지 시작할 때 확인하고, 없으면 종료 코드 2로 멈춘다. 이번 시험에서는 모두 있었다.
- 생성형 AI: 스키마 5절의 목록 이름은 "생성형 AI(LLM 포함)"인데, 골든 룰 G9는 Q3 값을 "생성형 AI"로 정한다. 둘을 그대로 따르면 "생성형 AI(LLM 포함)"은 G9에, "생성형 AI"는 G6에 걸린다. G9가 값을 직접 적었으므로 스크립트는 목록 이름을 "생성형 AI"로 보고 괄호는 설명으로 뺐다. 확인 필요(에드워드가 정한다)
- 입력 오류 기준: golden-rules.md 4절 "질문이나 주장을 하나도 읽지 못하면 2"를 글자대로 구현해, 파일 전체에 주장이 0개여도 종료 코드 2로 끝낸다. 그래서 T1·T3·T4 답만 든 파일은 입력 오류가 된다. E5 답 파일은 Q1~Q10을 함께 담으므로 문제가 없을 것으로 본다
- G4 하이픈: 지시대로 줄 끝 하이픈 줄바꿈을 붙여 비교하고, 붙여서 못 찾으면 하이픈을 남긴 정규화로도 한 번 더 본다. 원문 줄 끝 하이픈이 낱말 안의 하이픈(예: AI-powered)일 때 맞는 근거 문장이 G4에 걸리지 않게 하려는 것이다
- G2의 칸 검사는 상태가 "답함"일 때만 한다(golden-rules.md 문구대로). 원장 번호가 비어 있으면 G3, 관계가 비어 있으면 G5를 따로 보고하지 않는다
- G4는 원장 번호가 원장에 있을 때만 본다(번호가 없으면 G3만 보고). 수행 관계에서 근거 문장이 "원장"이면 G4를 보지 않는다

## 4. 정정 뒤 다시 돌린 결과 (2026-10-14)

### 고친 내용

- 생성형 AI 이름: 스키마 5절 이름 그대로 "생성형 AI(LLM 포함)"로 맞춤. golden-rules.md G9의 Q3 값과 스크립트의 AI 기술 목록·G9 값을 바꾸고, 괄호를 설명으로 보고 빼던 주석과 처리를 없앰
- 입력 오류 기준: 종료 코드 2는 질문을 하나도 읽지 못했을 때(그리고 파일·JSON·스키마·원장·raw 오류)만 냄. 주장 0개만으로는 2를 내지 않음. golden-rules.md 4절도 "질문을 하나도 읽지 못하면 2로 끝낸다. 주장이 0개인 답은 G1·G2·G8로 본다."로 바꿈
- G4 문서화: 하이픈을 붙여서 찾지 못하면 하이픈을 남긴 채로 한 번 더 보는 처리(3절에 적었던 것)를 golden-rules.md G4 행에 적음. 스크립트 처리는 그대로
- 시험 파일 추가: [golden-rules-controls-only.json](fixtures/golden-rules-controls-only.json) — T1·T3·T4 세 항목, 모두 상태 "자료에 없음", 주장 빈 목록, 요약 "테스트"

### 실행과 출력

모두 저장소 맨 위에서 돌렸다.

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-pass.json
```

종료 코드: 0

```
검사한 질문 5개, 주장 5개
위반 없음
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-fail.json
```

종료 코드: 1

```
검사한 질문 9개, 주장 8개
위반 10건
질문	주장	규칙	이유
Q10	-	G1	"요약" 칸이 없음
Q5	-	G2	상태가 답함인데 주장이 없음
Q6	1	G3	원장에 없는 번호: 18
Q8	1	G4	근거 문장이 원장 3번 원문에 없음
Q9	1	G5	스키마 6절에 없는 관계: '협력'
Q10	1	G6	"적용 업무"의 목록에 없는 값: '인수합병 자문'
Q6	1	G7	원장 3번의 펌은 McKinsey인데 값은 'BCG'
T1	-	G8	상태가 "자료에 없음"이 아님: '답함'
T1	-	G8	주장이 0개가 아님: 1개
Q1	1	G9	Q1의 주장은 원장 2번이어야 하는데 3
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-empty.json
```

종료 코드: 2

```
입력 오류: 질문을 하나도 읽지 못함(질문 0개)
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-controls-only.json
```

종료 코드: 0

```
검사한 질문 3개, 주장 0개
위반 없음
```

### 판정 표

| 시험 파일 | 시험 항목 | 기대 | 코드 판정 | 사람 판정 |
|-----------|-----------|------|-----------|-----------|
| pass | 1절 판정 표의 pass 다섯 항목 | 위반 없음, 종료 코드 0 | 위반 없음, 종료 코드 0 | 에드워드 확인 전 |
| fail | 1절 판정 표의 fail 아홉 항목(G1~G9 하나씩) | 항목마다 걸려야 할 규칙만, 종료 코드 1 | G1~G9 항목마다 하나씩(T1만 G8 두 조건), 종료 코드 1 | 에드워드 확인 전 |
| empty | 빈 목록 [] | 입력 오류, 종료 코드 2 | 입력 오류(질문 0개), 종료 코드 2 | 에드워드 확인 전 |
| controls-only | T1·T3·T4 자료에 없음, 주장 0개 | 위반 없음, 종료 코드 0 | 위반 없음, 종료 코드 0 | 에드워드 확인 전 |

- pass·fail 출력은 정정 전(1절)과 같다. 바뀐 것은 empty의 오류 문구와, 정정 전에는 입력 오류가 되었을 controls-only가 통과한 것이다
- 시험 파일에는 이번에도 공개 정보(원장 제목, 수행 펌)와 일부러 틀린 값, "테스트"만 썼다

## G4 공백 경고 시험 (2026-10-22, E5 답 전)

e5-method.md 4절대로 G4를 고쳤다: in_raw로 원문에 없을 때, 따옴표를 바꾼 뒤 공백을 모두 지운 근거 문장이 같은 방식으로 공백을 지운 원문에 있으면 위반 대신 "G4 경고(space-only)"로 모은다. 경고가 있으면 위반 목록(또는 "위반 없음") 뒤에 "경고 N건"과 같은 칸의 표를 낸다. 종료 코드는 위반으로만 정한다.

- 시험 파일: [golden-rules-space.json](fixtures/golden-rules-space.json). golden-rules-pass.json의 Q5 첫 주장(원장 3번 수행 McKinsey, 근거 문장 = 3번 제목)에서 근거 문장의 공백만 뺀 주장 1과, 근거 문장이 "이 문장은 원문에 없는 테스트 문장이다"인 주장 2를 담았다.
- 아래 기대는 실행 전에 적었다.

### space 기대 출력

```
검사한 질문 1개, 주장 2개
위반 1건
질문	주장	규칙	이유
Q5	2	G4	근거 문장이 원장 3번 원문에 없음
경고 1건
질문	주장	규칙	이유
Q5	1	G4 경고(space-only)	공백을 모두 지우면 원장 3번 원문에 있음
```

종료 코드 1. 기존 시험 파일(pass, fail, empty, controls-only)은 공백만 다른 근거 문장이 없어 4절(정정 뒤) 출력과 같아야 한다.

### 실행과 출력

모두 저장소 맨 위에서 bash로 돌렸다. 설치한 도구 없음.

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-space.json
```

종료 코드: 1

```
검사한 질문 1개, 주장 2개
위반 1건
질문	주장	규칙	이유
Q5	2	G4	근거 문장이 원장 3번 원문에 없음
경고 1건
질문	주장	규칙	이유
Q5	1	G4 경고(space-only)	공백을 모두 지우면 원장 3번 원문에 있음
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-pass.json
```

종료 코드: 0

```
검사한 질문 5개, 주장 5개
위반 없음
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-fail.json
```

종료 코드: 1

```
검사한 질문 9개, 주장 8개
위반 10건
질문	주장	규칙	이유
Q10	-	G1	"요약" 칸이 없음
Q5	-	G2	상태가 답함인데 주장이 없음
Q6	1	G3	원장에 없는 번호: 18
Q8	1	G4	근거 문장이 원장 3번 원문에 없음
Q9	1	G5	스키마 6절에 없는 관계: '협력'
Q10	1	G6	"적용 업무"의 목록에 없는 값: '인수합병 자문'
Q6	1	G7	원장 3번의 펌은 McKinsey인데 값은 'BCG'
T1	-	G8	상태가 "자료에 없음"이 아님: '답함'
T1	-	G8	주장이 0개가 아님: 1개
Q1	1	G9	Q1의 주장은 원장 2번이어야 하는데 3
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-empty.json
```

종료 코드: 2

```
입력 오류: 질문을 하나도 읽지 못함(질문 0개)
```

```bash
python3 deep/07-graphrag/experiments/scripts/check-golden-rules.py deep/07-graphrag/experiments/fixtures/golden-rules-controls-only.json
```

종료 코드: 0

```
검사한 질문 3개, 주장 0개
위반 없음
```

- 기존 시험 파일(pass, fail, empty, controls-only)의 출력은 4절(정정 뒤) 출력과 글자 단위로 같다(종료 코드 0, 1, 2, 0). 결과가 바뀌지 않았다

### 확인 표 (G4 공백 경고)

| 시험 파일 | 넣은 것 | 기대 | 스크립트 결과 | 사람 확인 |
|-----------|---------|------|---------------|-----------|
| space | 공백만 뺀 근거 문장 주장 1, 원문에 없는 테스트 문장 주장 2 | 경고 1건(G4 경고(space-only)), 위반 1건(G4), 종료 코드 1 | 기대와 글자 단위로 같음, 종료 코드 1 | 에드워드 확인 전 |
| pass·fail·empty·controls-only (다시) | 앞과 같은 파일 | 4절(정정 뒤) 출력과 같음 | 넷 모두 같음 | 에드워드 확인 전 |

- 기대와 다른 결과: 없음
