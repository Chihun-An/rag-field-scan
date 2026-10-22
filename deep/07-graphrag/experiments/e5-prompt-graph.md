# E5 답 지시문 — 그래프 경유 (두 도메인 공통)

두 도메인의 "그래프 경유" 답에 이 지시문을 글자 하나 바꾸지 않고 그대로 쓴다. 답을 만들기 전에 커밋했다.

## 작업 폴더

이 폴더에는 schema.md, sources.csv, raw/, graph.csv, questions.md, answer-shape.md만 있다. graph.csv는 raw/의 원문에서 schema.md 형식으로 뽑은 그래프다. 이 폴더 밖의 파일은 열거나 찾지 않는다. 인터넷은 쓰지 않는다.

## 할 일

1. schema.md, answer-shape.md, questions.md, graph.csv를 읽는다.
2. questions.md의 질문 15개(Q1~Q10, T1~T5)에 하나씩 답한다. 먼저 graph.csv에서 찾는다. 그래프로 답이 모자라거나 근거를 확인해야 하면 raw/의 원문을 연다.
   - 원문에 적힌 것만 쓴다. 추론하지 않는다.
   - 근거 문장은 원문 한 곳을 그대로 옮긴다. 떨어진 두 곳을 이어 붙이지 않는다. 근거가 여러 곳이면 answer-shape.md가 정한 방식대로 나눠 적는다.
   - 자료에 없으면 상태를 "자료에 없음"으로, 질문의 전제가 원문과 다르면 "전제가 틀림"으로 쓴다.
3. 답을 이 폴더에 answers.json으로 저장한다. 모양은 answer-shape.md 그대로이고 UTF-8이다.
4. 보고: 쓴 모델 이름, 질문별 상태와 주장 수, 질문별로 쓴 자료("그래프만", "그래프+원문", "원문만" 가운데 하나), 통째로 읽은 파일 번호·일부만 읽은 파일 번호·열지 않은 파일 번호, 판단이 어려웠던 점(질문 번호와 함께 짧게).

## 하지 않을 것

- 이 폴더 밖 파일 열기·검색, 인터넷 사용
- schema.md, sources.csv, raw/, graph.csv, questions.md, answer-shape.md 고치기
