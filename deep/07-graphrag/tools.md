# 도구 후보

## 후보 3개

| 도구 | 설명 | 필요한 것 | 장단점 | 저장소 URL | 확인 날짜 |
|------|------|-----------|--------|------------|-----------|
| Microsoft GraphRAG | LLM로 지식 그래프를 추출하고, 커뮤니티 단위로 요약해 검색·질의에 쓰는 원조 구현체 | LLM API 키, 인덱싱에 드는 컴퓨팅 비용 | 장점: 원 논문(Edge et al., 2024)의 구현체라 커뮤니티 요약 기능이 충실함 / 단점: 인덱싱 비용이 크고 프롬프트를 직접 튜닝해야 함 | https://github.com/microsoft/graphrag | 2026-09-28 |
| LightRAG | 그래프 구조와 벡터 임베딩을 함께 쓰는 경량 GraphRAG 프레임워크 | LLM API 키 | 장점: 가볍고 빠르며, 개체 단위·주제 단위 이중 검색을 지원함 / 단점: Microsoft GraphRAG보다 나온 지 얼마 안 돼 사례가 적음 | https://github.com/HKUDS/LightRAG | 2026-09-28 |
| Neo4j LLM Graph Builder | 업로드한 비정형 문서를 Neo4j 그래프로 자동 변환해 주는 애플리케이션 | Neo4j 데이터베이스(APOC 포함), LLM API 키 | 장점: GUI를 제공하고 Neo4j 생태계와 바로 연결됨 / 단점: Neo4j DB를 별도로 운영해야 함 | https://github.com/neo4j-labs/llm-graph-builder | 2026-09-28 |

## 고를 때 볼 기준

설치·운영 난이도, LLM API 비용, 커뮤니티 요약처럼 전역 질문(펌 간 비교 같은)에 답하는 기능이 있는지, 리포트 수가 많지 않을 때도 그래프가 의미 있게 나오는지를 볼 계획이다. 어느 도구를 고를지는 아직 정하지 않았다.

---

[분야 지도](../../field-map.md) · [07 영역 파일](../../areas/07-graphrag.md)
