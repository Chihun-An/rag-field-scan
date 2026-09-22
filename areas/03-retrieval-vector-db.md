# 검색·리랭킹·벡터 DB

## 한 줄 정의

질문과 의미적으로 가까운 문서 조각을 찾아 순위를 매기는 과정(검색·리랭킹)과, 그 조각들을 미리 벡터로 바꿔 저장해 두는 저장소(벡터 DB)를 함께 다루는 영역이다.

## 출발 질문과의 관계

필요한 근거 문서를 빠뜨리지 않고, 관련 없는 문서는 섞이지 않게 찾아내는 능력이 답의 정확도를 좌우한다.

## 핵심 개념 3~5개

- 임베딩(embedding): 문장을 의미를 담은 숫자 벡터로 바꾼 것
- 유사도 검색(similarity search): 벡터끼리의 거리로 의미가 가까운 문서를 찾는 방법
- 근사 최근접 이웃(ANN, Approximate Nearest Neighbor): 모든 문서와 비교하지 않고 빠르게 가까운 문서를 찾는 방법
- 리랭킹(reranking): 1차로 찾아온 후보들을 더 정밀한 기준으로 다시 순위를 매기는 단계
- 벡터 인덱스: 벡터를 빠르게 찾을 수 있도록 미리 구성해 둔 자료구조

## 대표 기법·도구

- HNSW(Hierarchical Navigable Small World): 여러 층으로 이루어진 그래프를 이용해 근사 최근접 이웃을 빠르게 찾는 대표적 알고리즘
- 교차 인코더(cross-encoder) 기반 리랭커: 질문과 문서를 함께 넣어 더 정밀하게 관련도를 매기는 방식
- 벡터 DB: 벡터 인덱스와 문서 원문·메타데이터를 함께 저장·검색하는 저장소 (scope.md에 따라 특정 제품 비교는 다루지 않음)
- 키워드 검색(BM25): 단어의 등장 빈도와 문서 길이를 바탕으로 관련도를 계산하는 전통적 검색 방식
- 하이브리드 검색: 벡터 검색(의미 기반)과 키워드 검색(BM25 등)을 함께 써서 서로의 약점을 보완하는 방식

## 품질 문서에서는?

검색 결과가 어떤 문서·개정판에서 나온 조각인지 식별자로 추적할 수 있어야 근거로 쓸 수 있다. (일반적 문제 유형: 문서 식별자)

## 남은 질문

- 확인 필요: 규정·품질 문서처럼 조항 간 유사도가 높은 문서에서 벡터 검색만으로 충분한지, 아니면 키워드 검색과 함께 써야 하는지

## 출처

- Malkov, Y. A. & Yashunin, D. A., "Efficient and Robust Approximate Nearest Neighbor Search Using Hierarchical Navigable Small World Graphs" — https://arxiv.org/abs/1603.09320 (확인: 2026-09-22)
- Robertson, S. & Zaragoza, H., "The Probabilistic Relevance Framework: BM25 and Beyond" — https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf (확인: 2026-09-22)

---

[분야 지도](../field-map.md)
