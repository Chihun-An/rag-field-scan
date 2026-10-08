# RAG Field Scan

## 결론
규정·품질 문서에 근거를 달아 답하는 AI는 검색 성능보다 '어느 문서의 어느 판에서 왔는지'를 파이프라인 끝까지 잇는 설계가 관건이다.

## 배포 URL
https://chihun-an.github.io/rag-field-scan/

## 출발 질문
규정·품질 문서에 근거를 달아 답하는 AI를 만들려면 무엇을 알아야 할까?

## 2026-10-11 발표 요약

- [무엇을 했나](#무엇을-했나)
- [발견 1 — 번호가 맞는 것과 내용이 맞는 것은 다르다](#발견-1--번호가-맞는-것과-내용이-맞는-것은-다르다)
- [발견 2 — 근거를 어디서 자르느냐가 판정을 바꾼다](#발견-2--근거를-어디서-자르느냐가-판정을-바꾼다)
- [발견 3 — 새 입력에서 도구가 조용히 실패했다](#발견-3--새-입력에서-도구가-조용히-실패했다)
- [빗나간 예측](#빗나간-예측)
- [07 GraphRAG](#07-graphrag)
- [한계](#한계)
- [만든 에이전트와 스크립트](#만든-에이전트와-스크립트)

### 무엇을 했나

법령 발췌본에 인용 강제 프롬프트로 답하게 하고, 인용이 맞는지를 두 층위로 쟀다. 층위 1은 조항 번호가 실재하는지(규칙 기반 스크립트), 층위 2는 그 조항이 주장을 뒷받침하는지(citation-judge 서브에이전트)를 본다.

| 실험 | 자료 | 질문 수 | 쌍·항목 수 | 핵심 결과 |
|------|------|---------|------------|-----------|
| 01 | 산업안전보건법 발췌 | 5 (Q1~Q5) | 층위 1 인용 항목 29건, 층위 2 쌍 8개(호출 8회) | 층위 2와 사람 판정 일치 7, 불일치 1(P7). Q5 내용 오류를 층위 2가 잡음 |
| 02 | 산업안전보건법 발췌 | 실험 01 Q2의 주장 1개 | 쌍 3개 × 3회(호출 9회) | 근거에 조 제목을 더하자 뒷받침됨으로 뒤집힘 |
| 03 | 산업안전보건법 발췌 | 실험 01 Q2의 주장 1개 | 쌍 2개 × 3회(호출 6회) | 정의문(제2항)을 더하면 뒤집히고, 명칭만 있는 제3항은 뒤집히지 않음 |
| 04 | 개인정보 보호법 발췌 | 2 (Q6, Q7) | 층위 1 인용 항목 16건, 층위 2 쌍 34개(호출 46회), 사람 판정 표본 17건 | 절차는 재사용, 스크립트는 깨짐. 표본 17건 중 일치 14, 같은 쪽 1, 불일치 2 |

출처: [findings.md](deep/05-citation/findings.md), [results-01.md](deep/05-citation/experiments/results-01.md), [results-02.md](deep/05-citation/experiments/results-02.md), [results-03.md](deep/05-citation/experiments/results-03.md), [results-04.md](deep/05-citation/experiments/results-04.md), [results-04-layer2.md](deep/05-citation/experiments/results-04-layer2.md) · [목차로](#2026-10-11-발표-요약)

### 발견 1 — 번호가 맞는 것과 내용이 맞는 것은 다르다

실험 01 Q5에서 답변은 제42조 제2항을 "작성·제출·심사"로 설명했다. 원문 제2항은 자격을 갖춘 자의 의견을 들어야 한다는 의견 청취 의무다.

- 층위 1: Q5가 인용한 제42조 제1항~제6항 6건이 모두 "실재함". 제42조 제2항도 통과했다
- 사람 판정: "일부". 제2항의 내용 설명이 원문과 다름
- 층위 2: 같은 주장을 P1(제2항만)과 P2(제1항+제2항) 모두 "뒷받침 안 됨"으로 판정. 사람 판정과 같음

출처: [findings.md](deep/05-citation/findings.md) 발견 1, [results-01.md](deep/05-citation/experiments/results-01.md), [results-01-layer1.md](deep/05-citation/experiments/results-01-layer1.md), [results-01-layer2.md](deep/05-citation/experiments/results-01-layer2.md) · [목차로](#2026-10-11-발표-요약)

### 발견 2 — 근거를 어디서 자르느냐가 판정을 바꾼다

주장은 모두 "안전보건관리책임자는 사업장의 산업재해 예방계획의 수립에 관한 사항을 총괄하여 관리해야 한다"이고, 건넨 근거 범위만 다르다.

| 쌍 | 근거 범위 | "안전보건관리책임자"가 건넨 조각에 있는가 | 판정 (3회) | 출처 |
|----|-----------|------------------------------------------|------------|------|
| P7 | 제1호 | 없음 | 뒷받침 안 됨 ×3 | 실험 01(1회), 실험 02(3회) |
| P9 | 제1항 본문+제1호 | 없음 | 뒷받침 안 됨 ×3 | 실험 02 |
| P10 | 조 제목+제1항 본문+제1호 | 있음(조 제목) | 뒷받침됨 ×3 | 실험 02 |
| P11 | 제1항 본문+제1호+제2항 | 있음(제2항 정의문) | 뒷받침됨 ×3 | 실험 03 |
| P12 | 제1항 본문+제1호+제3항 | 있음(제3항, 정의 없음) | 뒷받침 안 됨 ×3 | 실험 03 |

명칭이 글자로 들어와도 뒤집히지 않았고, 명칭과 의무를 잇는 문장이 있어야 뒤집혔다.

출처: [results-03.md](deep/05-citation/experiments/results-03.md) "무엇이 판정을 바꿨는가", [findings.md](deep/05-citation/findings.md) 발견 2 · [목차로](#2026-10-11-발표-요약)

### 발견 3 — 새 입력에서 도구가 조용히 실패했다

실험 04에서 고치기 전 층위 1 스크립트를 개인정보 보호법 입력에 돌린 첫 실행이다.

- 종료 코드 0. 파이썬 예외나 "오류:" 문구가 없었다
- 대조 단계에 간 인용 항목은 0건이었다(Q6 파싱 실패 1건, Q7 인용 항목 0건)
- Q6의 실패 사유로 "('실제 인용 조항:' 줄 없음)"을 냈는데 사실이 아니었다. 줄은 있었다
- 실험 01에서 같은 스크립트는 인용 항목 29건을 대조하고 "파싱 실패 0"에 종료 코드 0이었다. 두 실행은 종료 코드와 오류 문구만으로는 구별되지 않았다

고친 스크립트는 인용 항목이 0건이거나 파싱 실패가 절반 이상이면 경고를 내고 종료 코드 2로 끝난다.

출처: [results-04.md](deep/05-citation/experiments/results-04.md) "층위 1 첫 실행", [findings.md](deep/05-citation/findings.md) 발견 6 · [목차로](#2026-10-11-발표-요약)

### 빗나간 예측

- 예측 [A](판정 전): Q6 답변의 호 인용은 층위 2에서 "뒷받침 안 됨"이 다수 나올 것이다. 실험 02·03의 P7과 같은 구조다
- 전제부터 맞지 않았다: Q6 답변에는 호 단위 인용이 하나도 없었다(항 단위 [제15조 제1항]만). 그래서 사람이 같은 주장에 근거만 바꾼 3칸 사다리(항 전체 / 본문+호 / 호만)를 만들어 시험했다
- 결과: 6칸 모두 뒷받침됨. 호만 줘도 뒷받침됨이 나왔다
- 빗나간 이유: P7의 주장에는 호 한 줄에 없는 주체와 의무가 있었다. 실험 04의 주장은 그 호의 내용을 되풀이한 것이었다
- 그래서 좁힌 결론: 근거 범위가 판정을 바꾸는 것은 주장이 그 범위 밖의 요소를 담고 있을 때다

출처: [findings.md](deep/05-citation/findings.md) 발견 9·빗나간 가설, [pairs-04-ko.md](deep/05-citation/experiments/pairs-04-ko.md), [results-04-layer2.md](deep/05-citation/experiments/results-04-layer2.md) · [목차로](#2026-10-11-발표-요약)

### 07 GraphRAG

- 주제: McKinsey·BCG·Bain(MBB) 공개 리포트로 만드는 "산업 × 펌별 관점 비교" 그래프
- 왜 이 주제와 개체·관계인가(에드워드의 설명 요지): 원래 궁금했던 MBB 채용 쪽 자료는 1차 자료가 거의 없고 공개 저장소에 올릴 수 없다. 리포트는 URL·제목·날짜가 분명한 공개 자료라 05의 검증 절차를 붙일 수 있다. "근거 유형"을 노드로 넣은 것이 핵심이다. 유형마다 원출처로 되짚을 수 있는 정도가 다르다
- 근거 유형 다섯 가지: 자체 설문, 사례 연구, 자체 지수·추정, 공개 통계 인용, 출처 미상
- 도구 셋이 지금 안 되는 이유(유료 API 키 없음, Apple M1·메모리 8GB·디스크 3.6~3.7GiB, 2026-10-07)
  - MS GraphRAG: 로컬 모델 경로는 있으나, 이 하드웨어에 올릴 모델이 요구하는 JSON 출력을 안정적으로 내는지 확인하지 않음
  - LightRAG: README의 권장 최소 모델(30.5B, BF16)이 디스크·메모리를 넘음
  - Neo4j LLM Graph Builder: Ollama 경로는 있으나 필요한 모델 크기가 명시돼 있지 않음. 슬라이드형 자료에 덜 적합하다고 명시
- 조건부 2단계: 1단계(지금)는 리포트 15~20건을 사람이 읽고 손으로 그래프를 만들어 규칙 기반 조회로 답해 본다. 2단계는 API 키나 로컬 모델용 하드웨어가 생기거나 작은 로컬 모델로 추출이 되는지 확인되면, 자동 추출과 비교한다

출처: [deep/07-graphrag/plan.md](deep/07-graphrag/plan.md) · [목차로](#2026-10-11-발표-요약)

### 한계

- 판정기(citation-judge)는 답변을 만든 것과 같은 모델 계열이다. 자기 답을 관대하게 볼 편향이 있을 수 있다
- 실험 04 사람 판정 표본 17건은 오류가 나올 만한 쌍에 몰려 있어, 사람 판정과 자동 판정의 일치율을 쌍 34건 전체에 대해 말할 수 없다
- 실험 04 사람 판정은 Claude Cowork의 판정을 본 뒤에 이뤄졌다. 완전히 독립된 판정이 아니다
- P29에서 같은 입력의 자동 판정 3회가 갈렸다(뒷받침 안 됨, 뒷받침 안 됨, 뒷받침됨). 1회만 돌린 쌍의 값은 재현을 보장할 수 없다

출처: [findings.md](deep/05-citation/findings.md) 한계 1·8·9·11, 발견 12 · [목차로](#2026-10-11-발표-요약)

### 만든 에이전트와 스크립트

| 이름 | 종류 | 하는 일 | 호출·실행 |
|------|------|---------|-----------|
| citation-judge | 서브에이전트 | 조문과 주장 한 쌍에 대해 뒷받침 여부만 판정한다 | 69회(실험 01 8, 02 9, 03 6, 04 46) |
| answer-writer | 서브에이전트 | 법령 발췌 원문과 질문 하나에 대해, 원문만 근거로 인용을 달아 답한다 | 2회(실험 04 Q6·Q7) |
| check-article-numbers.py | 스크립트 | 답변이 인용한 조항 번호가 발췌본에 실재하는지 대조한다(층위 1) | 실험 01·04 층위 1 결과를 냄 |
| extract-doc-text.py | 스크립트 | 판정 쌍의 doc_ref에 해당하는 조문 원문을 발췌본에서 뽑는다 | 실험 01~04 층위 2 입력을 냄 |
| split-answer-sentences.py | 스크립트 | 답변 원문을 문장 단위로 기계적으로 나눠 층위 2 판정 쌍을 만든다 | 실험 04 쌍 28건을 냄 |
| run-minicheck.py | 스크립트 | MiniCheck로 층위 2를 돌리려 한 미사용 기록. 끝까지 실행되지 않았다 | 1회 실행, 실패(accelerate 누락) |

출처: [.claude/agents/](.claude/agents/), [deep/05-citation/experiments/scripts/](deep/05-citation/experiments/scripts/), [results-01-layer2.md](deep/05-citation/experiments/results-01-layer2.md), [results-02.md](deep/05-citation/experiments/results-02.md), [results-03.md](deep/05-citation/experiments/results-03.md), [results-04-layer2.md](deep/05-citation/experiments/results-04-layer2.md), [results-04.md](deep/05-citation/experiments/results-04.md) · [목차로](#2026-10-11-발표-요약)

## 문서 목록
- [AGENTS.md](AGENTS.md) — 에이전트 작업 규칙
- [worklog.md](worklog.md) — 작업 기록
- [scope.md](scope.md) — 범위와 깊이 기준
- [field-map.md](field-map.md) — 분야 지도 (10개 영역)
- [sources.md](sources.md) — 출처 모음
- [key-contexts.md](key-contexts.md) — 핵심 맥락 5개
- [process.md](process.md) — 제작 과정
- [deep/README.md](deep/README.md) — 2주 깊이 파기
- 영역 파일 10개
  - [areas/01-rag-basics.md](areas/01-rag-basics.md) — RAG 기본 구조
  - [areas/02-document-parsing-chunking.md](areas/02-document-parsing-chunking.md) — 문서 파싱·청킹
  - [areas/03-retrieval-vector-db.md](areas/03-retrieval-vector-db.md) — 검색·리랭킹·벡터 DB
  - [areas/04-metadata-versioning.md](areas/04-metadata-versioning.md) — 문서 버전·메타데이터 관리
  - [areas/05-citation-grounding.md](areas/05-citation-grounding.md) — 근거 인용·환각 억제
  - [areas/06-rag-evaluation.md](areas/06-rag-evaluation.md) — RAG 평가
  - [areas/07-graphrag.md](areas/07-graphrag.md) — GraphRAG·지식 그래프
  - [areas/08-agentic-rag.md](areas/08-agentic-rag.md) — 에이전트형 RAG·데이터 분석 에이전트
  - [areas/09-long-context-vs-rag.md](areas/09-long-context-vs-rag.md) — 긴 컨텍스트 vs RAG
  - [areas/10-security-governance.md](areas/10-security-governance.md) — 권한·보안·거버넌스
