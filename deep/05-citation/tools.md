# 도구 후보

## 후보 3개

| 도구 | 무엇을 재는가 | 필요한 것 | 장단점 | 저장소 URL | 확인 날짜 |
|------|---------------|-----------|--------|------------|-----------|
| RAGAS | 충실성(faithfulness), 답변 관련성 등 RAG 답변 품질 전반 | LLM API 키 (평가에 LLM judge를 씀) | 장점: 지표 종류가 다양하고 문서화가 잘 돼 있음 / 단점: 대부분의 지표가 사실상 유료 LLM API 키를 필요로 함 | https://github.com/vibrantlabsai/ragas | 2026-09-28 |
| ALCE | 인용 정확도(문장이 인용한 문서로 뒷받침되는지), 유창성, 정답률 | NLI 모델 또는 LLM, 검색 코퍼스 | 장점: 인용 품질을 재는 지표가 구체적임 / 단점: 벤치마크 데이터셋(ASQA·QAMPARI·ELI5) 중심이라 새 문서에 적용하려면 손볼 부분이 많음 | https://github.com/princeton-nlp/ALCE | 2026-09-28 |
| MiniCheck | 문장이 근거 문서로 뒷받침되는지(사실 일치 여부) | 로컬에서 돌아가는 오픈소스 모델(DeBERTa·Flan-T5 계열) | 장점: 유료 LLM API 키 없이 로컬로 실행 가능, GPT-4 수준 정확도를 주장함 / 단점: 한국어 등 다국어 문서에서의 성능은 확인 필요 | https://github.com/Liyan06/MiniCheck | 2026-09-28 |

## 판단

유료 LLM API 키 없이 진행하기로 해서 MiniCheck를 먼저 고른다. RAGAS는 지표 대부분이 LLM judge를 전제로 해 API 키가 사실상 필요하고, ALCE는 벤치마크 데이터셋과 검색 파이프라인을 함께 구성해야 해 2주 안에 준비하기에는 부담이 크다. MiniCheck는 로컬 모델로 문장 단위 사실 일치를 바로 돌려볼 수 있어 이번 실험 범위(질문 5개, 2주)에 맞다.

RAGAS 저장소는 explodinggradients에서 vibrantlabsai로 조직명이 바뀌었다(2026-09-28 확인). 도구 저장소 주소도 출처와 마찬가지로 바뀔 수 있어 확인 날짜를 함께 적는다.

---

[분야 지도](../../field-map.md) · [05 영역 파일](../../areas/05-citation-grounding.md)
