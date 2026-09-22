# RAG 기본 구조

## 한 줄 정의

RAG(검색 증강 생성, Retrieval-Augmented Generation)는 질문이 들어오면 관련 문서를 먼저 찾고, 그 내용을 근거로 언어모델이 답을 만드는 방식이다.

## 출발 질문과의 관계

"규정·품질 문서에 근거를 달아 답하는 AI"의 기본 뼈대가 RAG다. 모델이 학습 때 외운 지식만으로 답하지 않고, 실제 문서를 찾아 그 내용을 바탕으로 답하게 만드는 구조이기 때문이다.

## 핵심 개념 3~5개

- 검색기(retriever): 질문과 관련된 문서(조각)를 찾아오는 부분
- 생성기(generator): 찾아온 문서를 참고해 답을 만드는 언어모델
- 인덱스(index): 검색 대상 문서를 미리 정리해 둔 저장소
- 증강(augmentation): 찾아온 문서를 프롬프트에 끼워 넣어 모델에 전달하는 과정
- 근거 문서(context): 답변의 바탕이 되는, 검색으로 찾아온 문서 조각

## 대표 기법·도구

- 원조 구조: Dense Passage Retriever(검색기) + BART(생성기)를 결합한 RAG 모델 (Lewis et al., 2020)
- 실무 구현: LangChain, LlamaIndex 같은 RAG 프레임워크
- 검색 대상 저장: 벡터 DB (자세한 내용은 [03-retrieval-vector-db.md](03-retrieval-vector-db.md))

## 품질 문서에서는?

검색기가 찾아온 문서가 최신 개정판인지, 문서 식별자가 프롬프트와 답변에 남아 나중에 인용을 추적할 수 있는지가 문제가 될 수 있다. (일반적 문제 유형: 문서 식별자, 개정 이력)

## 남은 질문

- 확인 필요: 검색기와 생성기를 따로 학습시키는지, 함께 학습시키는지에 따라 구조가 어떻게 달라지는가

## 출처

- Lewis, P. et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" — https://arxiv.org/abs/2005.11401 (확인: 2026-09-22)

---

[분야 지도](../field-map.md)
