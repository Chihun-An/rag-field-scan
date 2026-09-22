# RAG 평가

## 한 줄 정의

RAG 평가는 검색이 관련 문서를 제대로 찾아왔는지, 생성된 답변이 그 문서에 충실한지를 측정하는 방법이다.

## 출발 질문과의 관계

근거가 맞는 답인지 어떻게 확인하느냐가 이 영역의 질문이다. 검색과 생성 각 단계를 따로, 또 전체를 함께 측정할 방법이 있어야 "근거를 달아 답한다"는 목표를 검증할 수 있다.

## 핵심 개념 3~5개

- 충실성(faithfulness): 답변이 검색된 문서 내용에서 벗어나지 않는 정도
- 답변 관련성(answer relevance): 답변이 실제 질문에 맞게 대답하고 있는 정도
- 문맥 정밀도(context precision): 검색된 문서 중 실제로 필요한 것의 비율을 보는 지표 (Ragas 공식 문서 기준)
- 문맥 재현율(context recall): 필요한 근거를 빠뜨리지 않고 찾아왔는지 보는 지표 (Ragas 공식 문서 기준)
- 기준 답안 없는 평가(reference-free evaluation): 정답 예시 없이도 모델 스스로 품질을 매기는 평가 방식
- 최신성(freshness): 근거로 쓰인 문서가 지금 유효한 버전인지 보는 평가 관점

## 대표 기법·도구

- RAGAS: 충실성·답변 관련성·문맥 정밀도·문맥 재현율 등을 자동으로 측정하는 평가 프레임워크. 2023년 논문에서는 문맥 관련성(context relevance)이라는 이름을 썼고, 현재 공식 문서에서는 문맥 정밀도·문맥 재현율로 나뉘어 있다.
- 사람 평가(human evaluation): 평가자가 직접 답변과 근거를 대조해 점수를 매기는 방식
- 회귀 테스트(regression test): 시스템을 바꿀 때마다 정해진 질문 세트로 품질이 떨어지지 않았는지 확인하는 방식

## 품질 문서에서는?

구버전 문서를 근거로 답하는 오류를 평가 항목으로 따로 넣을 수 있다. 즉 문서가 최신 개정판인지 확인하는 것도 "충실성"과는 별개의 평가 기준으로 다뤄야 한다. (일반적 문제 유형: 개정 이력)

## 남은 질문

- 확인 필요: RAGAS 같은 자동 평가 지표가 한국어 규정 문서에도 그대로 적용 가능한지, 별도 검증이 필요한지

## 출처

- Es, S., James, J., Espinosa-Anke, L. & Schockaert, S., "Ragas: Automated Evaluation of Retrieval Augmented Generation" — https://arxiv.org/abs/2309.15217 (확인: 2026-09-22)
- Ragas, "List of available metrics" 공식 문서 (충실성·답변 관련성·문맥 관련성 지표 이름의 근거) — https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/ (확인: 2026-09-22)

---

[분야 지도](../field-map.md)
