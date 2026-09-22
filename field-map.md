# 분야 지도 (field-map)

범위와 깊이 기준은 [scope.md](scope.md)를 따른다.

| 번호 | 영역 | 한 줄 정의 | 출발 질문과의 연결 | IATF 연결 |
|------|------|-----------|-------------------|-----------|
| 01 | RAG 기본 구조 ([areas/01-rag-basics.md](areas/01-rag-basics.md)) | 질문에 관련된 문서를 찾아 그 내용을 바탕으로 답을 만드는 기본 구성 | 근거를 달아 답하는 시스템의 전체 뼈대 | - |
| 02 | 문서 파싱·청킹 ([areas/02-document-parsing-chunking.md](areas/02-document-parsing-chunking.md)) | 문서를 읽어 검색하기 좋은 조각으로 나누는 과정 | 규정·품질 문서를 어떻게 잘라야 근거가 온전히 남는가 | 문서 식별자, 상호참조 |
| 03 | 검색·리랭킹·벡터 DB ([areas/03-retrieval-vector-db.md](areas/03-retrieval-vector-db.md)) | 질문과 관련된 조각을 찾고 순위를 다듬는 방법과 저장소 | 필요한 근거를 빠뜨리지 않고 찾아내는 일 | 문서 식별자 |
| 04 | 문서 버전·메타데이터 관리 ([areas/04-metadata-versioning.md](areas/04-metadata-versioning.md)) | 문서의 종류·버전·상태 같은 부가 정보를 함께 관리하는 일 | 지금 유효한 문서를 근거로 삼고 있는가 | 문서 식별자, 개정 이력 |
| 05 | 근거 인용·환각 억제 ([areas/05-citation-grounding.md](areas/05-citation-grounding.md)) | 답의 출처를 표시하고 근거 없는 내용을 줄이는 방법 | 근거를 달아 답한다는 요구의 핵심 | 문서 식별자, 개정 이력 |
| 06 | RAG 평가 ([areas/06-rag-evaluation.md](areas/06-rag-evaluation.md)) | 검색과 답변의 품질을 측정하는 방법 | 근거가 맞는 답인지 어떻게 확인하는가 | 개정 이력 (구버전 문서를 근거로 답하는 오류를 평가 항목으로 삼을 수 있음) |
| 07 | GraphRAG·지식 그래프 ([areas/07-graphrag.md](areas/07-graphrag.md)) | 문서 속 개체와 관계를 그래프로 엮어 검색에 활용하는 방식 | 문서 사이의 연결을 따라가는 질문에 대응 | 상호참조 |
| 08 | 에이전트형 RAG·데이터 분석 에이전트 ([areas/08-agentic-rag.md](areas/08-agentic-rag.md)) | 여러 단계로 검색하고 도구를 호출하며 답을 만드는 방식 | 한 번의 검색으로 풀리지 않는 질문 처리 | 상호참조 |
| 09 | 긴 컨텍스트 vs RAG ([areas/09-long-context-vs-rag.md](areas/09-long-context-vs-rag.md)) | 문서를 통째로 넣는 방식과 필요한 부분만 검색하는 방식의 비교 | 문서 규모에 맞는 방식을 어떻게 고르는가 | - |
| 10 | 권한·보안·거버넌스 ([areas/10-security-governance.md](areas/10-security-governance.md)) | 접근 권한, 보안, 운영 통제를 다루는 영역 | 공개하면 안 되는 문서를 안전하게 다루는 일 | 문서 식별자, 개정 이력 |
