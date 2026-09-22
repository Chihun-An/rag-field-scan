# RAG Field Scan

## 결론
규정·품질 문서에 근거를 달아 답하는 AI는 검색 성능보다 '어느 문서의 어느 판에서 왔는지'를 파이프라인 끝까지 잇는 설계가 관건이다.

## 배포 URL
https://chihun-an.github.io/rag-field-scan/

## 출발 질문
규정·품질 문서에 근거를 달아 답하는 AI를 만들려면 무엇을 알아야 할까?

## 문서 목록
- [AGENTS.md](AGENTS.md) — 에이전트 작업 규칙
- [worklog.md](worklog.md) — 작업 기록
- [scope.md](scope.md) — 범위와 깊이 기준
- [field-map.md](field-map.md) — 분야 지도 (10개 영역)
- [sources.md](sources.md) — 출처 모음
- [key-contexts.md](key-contexts.md) — 핵심 맥락 5개
- [process.md](process.md) — 제작 과정
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
