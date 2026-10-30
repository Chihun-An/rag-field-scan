# 2번 도메인 — 무역 & 기름

3주 챌린지(두 도메인 GraphRAG)의 2번 도메인 작업 공간이다. 지금 다루는 제품은 UMO, ULO, PPO다.
이 도메인으로 바꾸는 것은 2026-10-13 멘토가 승인했다(2026-10-12 요청). 경위는 [07 README](../README.md)에 있다.
실무 정보(거래처, 가격, 계약 조건, 받은 서류)는 이 폴더에 두지 않는다([AGENTS.md](../../../AGENTS.md) "공개 금지").
그래프 스키마(E3): [schema.md](schema.md)
골든 세트 질문(E3): [questions.md](questions.md)
골든 룰(E3): [golden-rules.md](golden-rules.md)
예측(E3): [predictions.md](predictions.md)
원천 원장(E2): [sources.csv](sources.csv), 제외 목록: [excluded.csv](excluded.csv). 원문(raw/)은 저작권 때문에 올리지 않는다.
기대 답 해시(E3): [answer-key.sha256](answer-key.sha256). 기대 답은 저장소 밖에 둔다.
사람 그래프(E4): [human-graph.csv](human-graph.csv)(v1, 원장 4편 9줄), [human-graph-v2.csv](human-graph-v2.csv)(보조, 결과를 본 뒤 16줄 추가), [human-graph-v2-added.csv](human-graph-v2-added.csv)(v2에서 더한 줄만)
에이전트 그래프(E4): [agent-graph-1.csv](agent-graph-1.csv), [agent-graph-2.csv](agent-graph-2.csv). 기준 그래프는 정답 격리 때문에 저장소 밖에 둔다.
E5 답: [e5-answers-search.json](e5-answers-search.json), [e5-answers-graph.json](e5-answers-graph.json)
실험 방법과 결과: [experiments/](../experiments/)
