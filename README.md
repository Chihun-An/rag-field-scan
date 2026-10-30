# RAG Field Scan

## 결론
규정·품질 문서에 근거를 달아 답하는 AI는 검색 성능보다 '어느 문서의 어느 판에서 왔는지'를 파이프라인 끝까지 잇는 설계가 관건이다.

## 배포 URL
https://chihun-an.github.io/rag-field-scan/

그래프 뷰어(3주 챌린지 E6): https://chihun-an.github.io/rag-field-scan/deep/07-graphrag/viewer/

## 출발 질문
규정·품질 문서에 근거를 달아 답하는 AI를 만들려면 무엇을 알아야 할까?

## 3주 챌린지 최종 점검 (2026-10-31)

멘토님이 10/31(토) 21:00에 보시는 것을 기준으로, 과제에서 요구한 것과 지난 점검(10/26)의 피드백마다 무엇을 했고 어디서 보면 되는지 정리했다. 과제 원문은 [challenge.md](deep/07-graphrag/challenge.md)이고, 2번 도메인은 2026-10-13 멘토 승인으로 방산에서 무역 & 기름(UMO·ULO·PPO)으로 바꿨다. 발견과 숫자의 자세한 내용은 [findings.md](deep/07-graphrag/findings.md)에 있다.

- [한눈에](#한눈에)
- [과제 요구 사항과 한 것](#과제-요구-사항과-한-것)
- [지난 점검 피드백에 한 것](#지난-점검-피드백에-한-것)
- [일한 방식](#일한-방식)
- [주요 발견 — 그래프 경유 답은 근거가 덜 탄탄했다](#주요-발견--그래프-경유-답은-근거가-덜-탄탄했다)
- [그 밖의 발견](#그-밖의-발견)
- [예측 대 실제](#예측-대-실제)
- [그래프 뷰어](#그래프-뷰어)
- [3주 챌린지의 한계](#3주-챌린지의-한계)
- [만든 스크립트](#만든-스크립트)

### 한눈에

1. **질문:** 자료가 많은 도메인(1번 AI 컨설팅)과 적은 도메인(2번 무역 & 기름)에 GraphRAG를 하나씩 만들면, 그래프는 언제 도움이 될까? 원장(원천 자료 목록)은 도메인마다 17건이다.
2. **답:** 자료가 다 읽을 수 없을 만큼 많고, 그래프를 만드는 규칙이 질문에 필요한 연결을 담을 때 도움이 된다. 이번에는 둘 다 아니었고, 그래서 그래프 경유 답과 검색만 답의 점수가 비슷했다(1번 87.1% 대 87.1%, 2번 87.0% 대 91.6%).
3. **주요 발견:** 그래프 경유 답은 점수는 비슷했지만 근거가 덜 탄탄했다. 근거가 주장을 뒷받침하는 비율이 1번 79.6% → 73.0%, 2번 73.6% → 64.0%로 낮았다.
4. **에이전트 그래프는 정확했지만 좁았다:** 2번에서 짝 지은 줄은 분류 값이 모두 같았지만, 기준 그래프의 요건 105줄 중 5줄만 찾았고 표본 20줄을 직접 분류하니 19줄이 정말 놓친 사실이었다. 무역 법령 요건은 사람도 이 규칙으로는 넣지 못했다. 그래프가 담는 범위는 모델보다 규칙이 정했다.
5. **같은 저울:** 사람 그래프 기준으로 재면 에이전트가 찾은 비율이 1번 72.2%, 2번 33.3%였다. 다만 2번은 짝짓기 방식 탓이 커서, 짝이 안 된 사람 요건 14줄을 직접 분류하니 놓친 사실은 0줄이었다.

[목차로](#3주-챌린지-최종-점검-2026-10-31)

### 과제 요구 사항과 한 것

과제 원문의 요구를 주차별로 옮기고, 한 것과 보는 곳을 붙였다. 시각은 커밋 시각이다.

**1주차 (점검 10/18 21:00)**

| 요구 | 한 것 | 보는 곳 |
|------|-------|---------|
| E0 저장소 정리(.DS_Store 3개·빈 .Rhistory 지우고 .gitignore에 추가) | 저장소에서 빼고 .gitignore에 넣었다(10/12) | 커밋 [7b45236](https://github.com/Chihun-An/rag-field-scan/commit/7b45236), [.gitignore](.gitignore) |
| E1 두 도메인 범위 + 분류 축, 3줄 판단 기록 | 1번은 펌 7곳(McKinsey·BCG·Bain·Deloitte·PwC·EY·KPMG)의 공개 AI 도입 사례, 2번은 UMO·ULO·PPO의 품목 분류·규제·수출입 절차(한국 법령, 바젤협약, HS 코드). 분류 축은 두 도메인 모두 업무 유형. 판단 기록(AI 제안 / 내 선택 / 이유) 있음 | [e1-decisions.md](deep/07-graphrag/e1-decisions.md) |
| E2 원천 원장(AI 컨설팅 15건+, 방산 10건+, 찾았지만 못 쓴 자료도 세기) | 1번 원장 17건·제외 19건(10/13), 2번 원장 17건·제외 24건(10/14). 원문은 저작권 때문에 올리지 않고 해시를 원장에 적었다 | 1번 [원장](deep/07-graphrag/ai-consulting/sources.csv)·[제외](deep/07-graphrag/ai-consulting/excluded.csv), 2번 [원장](deep/07-graphrag/oil-trade/sources.csv)·[제외](deep/07-graphrag/oil-trade/excluded.csv) · 커밋 [0d9f7e2](https://github.com/Chihun-An/rag-field-scan/commit/0d9f7e2), [5e4c595](https://github.com/Chihun-An/rag-field-scan/commit/5e4c595) |
| E3 골든 세트를 그래프보다 먼저(질문 8~10 + 통제 4~5 + 골든 룰 6~10 + 검사 스크립트) | 도메인마다 질문 10개 + 통제 항목 5개 + 골든 룰 G1~G9 + 검사 스크립트. 기대 답은 암호 디스크(저장소 밖)에 두고 해시만 커밋(1번 10/14 16:33). 예측도 그래프 전에 커밋 | 1번 [질문](deep/07-graphrag/ai-consulting/questions.md)·[골든 룰](deep/07-graphrag/ai-consulting/golden-rules.md)·[예측](deep/07-graphrag/ai-consulting/predictions.md), 2번 [질문](deep/07-graphrag/oil-trade/questions.md)·[골든 룰](deep/07-graphrag/oil-trade/golden-rules.md)·[예측](deep/07-graphrag/oil-trade/predictions.md) · [검사 스크립트](deep/07-graphrag/experiments/scripts/) · 커밋 [b847eaf](https://github.com/Chihun-An/rag-field-scan/commit/b847eaf) |
| progress/week-1.md 4줄 · 리즈 저장소 상호 검토 1장 | 10/15, 10/16 | [week-1.md](progress/week-1.md), [상호 검토](progress/review-liz-week-1.md) |

**2주차 (점검 10/25 21:00)**

| 요구 | 한 것 | 보는 곳 |
|------|-------|---------|
| E4 사람 그래프(AI 컨설팅 6건+, 먼저·독립적으로) vs 에이전트 그래프(2회+) → 정밀도·재현율 | 1번: 사람 그래프 7건(10/22 10:36) → 에이전트 그래프 2회(12:08, 13:29). 닫힌 목록 재현율 72.2%·정밀도 89.7%·86.7%, 열린 값 재현율 78.3%·73.9%. 에이전트는 Claude Code를 추출기로, 회차마다 저장소 밖 새 폴더·새 대화. 2번: 에이전트 그래프 2회를 기준 그래프와 비교해 재현율 12.9%·15.1%, 정밀도 52.9%·55.3% | 1번 [닫힌 목록](deep/07-graphrag/experiments/e4-closed-results.md)·[열린 값 1회차](deep/07-graphrag/experiments/e4-open-results-run1.md)·[2회차](deep/07-graphrag/experiments/e4-open-results-run2.md), 2번 [기준 비교](deep/07-graphrag/experiments/e4-reference-results-oil-trade.md) · 커밋 [065cf33](https://github.com/Chihun-An/rag-field-scan/commit/065cf33) → [b173c20](https://github.com/Chihun-An/rag-field-scan/commit/b173c20) → [ed2203d](https://github.com/Chihun-An/rag-field-scan/commit/ed2203d) |
| E5 검색만 vs 그래프 경유, 05의 2층 검증 그대로 + 다른 계열 판정기 1회 이상 | 두 도메인 × 두 방식 답 4개. 층위 1은 골든 룰 검사, 층위 2는 citation-judge(판정 단위 414개). 다른 계열 판정기 Codex로 40개. 채점은 두 답을 A/B로 가린 채 했다. 점수 1번 87.1% 대 87.1%, 2번 87.0% 대 91.6% | [방법](deep/07-graphrag/experiments/e5-method.md) · [골든 룰 검사](deep/07-graphrag/experiments/e5-golden-rules-results.md) · [판정](deep/07-graphrag/experiments/e5-judge-results.md) · [채점](deep/07-graphrag/experiments/e5-score-results.md) · [사람 판정 비교](deep/07-graphrag/experiments/e5-human-judge-results.md) |
| progress/week-2.md 4줄 | 10/26 13:39(점검 시각 뒤에 씀) | [week-2.md](progress/week-2.md) |

**3주차 (최종 점검 10/31 21:00)**

| 요구 | 한 것 | 보는 곳 |
|------|-------|---------|
| E6 내 그래프 뷰어(오픈소스 JS 라이브러리, 정적 HTML, GitHub Pages, 도메인 전환·종류별 색·클릭하면 출처 패널·필터) | Cytoscape.js·PapaParse로 만든 HTML 한 파일을 GitHub Pages에 올렸다. 네 기능 모두 있고, 열로 정렬·누른 노드와 이웃만 밝게·1번 사람/에이전트 그래프 전환을 더했다(10/27) | [뷰어(배포)](https://chihun-an.github.io/rag-field-scan/deep/07-graphrag/viewer/) · [index.html](deep/07-graphrag/viewer/index.html) · 커밋 [852cbea](https://github.com/Chihun-An/rag-field-scan/commit/852cbea), [95d405a](https://github.com/Chihun-An/rag-field-scan/commit/95d405a) |
| E7 발견 정리(먼저 적은 예측 vs 실제 · 방산 보완) | 예측 대 실제는 findings 2절, 2번 보완(저울 점검, 사람 그래프 v1·v2, 요건 줄 진단)은 3·6절 | [findings.md](deep/07-graphrag/findings.md) |
| progress/week-3.md 4줄 | 있음 | [week-3.md](progress/week-3.md) |

**꼭 지킬 것**

| 요구 | 한 것 | 보는 곳 |
|------|-------|---------|
| 정답은 메인 세션까지 도구 수준에서 막거나 저장소 밖에 둔다. 뚫리면 기록하고 다시 시작 | 기대 답은 암호 디스크(저장소 밖)에 두고 해시만 커밋. 디스크를 여는 동안 다른 AI 대화를 쓰지 않음. 에이전트 그래프와 답은 저장소 밖 격리 폴더·새 대화에서 만듦. 샌 일 2건(10/15 기대 답 일부, 10/26 채점 대화의 출력)은 기록함 | [findings 5절](deep/07-graphrag/findings.md#5-한계) · [handoff 5절](handoff.md) · [worklog.md](worklog.md) |
| 방산은 공개 자료만(무기 성능·기술 사양·수출 통제는 범위 밖) | 2번을 무역 & 기름으로 바꿔 해당 없음. 대신 무역 실무 정보(거래처·가격·계약 조건·받은 서류)는 올리지 않음 | [challenge.md 변경 기록](deep/07-graphrag/challenge.md) · [AGENTS.md](AGENTS.md) |
| 필수선(AI 컨설팅은 끝까지, 방산은 원장·골든 세트·에이전트 그래프·답변 비교까지) | 두 도메인 모두 E0~E7을 마쳤다 | [handoff 4절](handoff.md) |
| 스터디로 끝내지 말고 지금 하는 일과의 연결 | "검증하는 습관"(결과 전에 규칙 커밋, 자동 판정을 사람과 대어 보기, 틀린 예측 남기기). 2번은 기름 무역 일을 단계별로 알려 줄 특화 에이전트의 출발점 | [findings 7절](deep/07-graphrag/findings.md#7-지금-하는-일과의-연결) · [E1 판단 기록](deep/07-graphrag/e1-decisions.md) |

[목차로](#3주-챌린지-최종-점검-2026-10-31)

### 지난 점검 피드백에 한 것

10/26에 받은 1·2주차 점검(10/22 16:48 커밋까지)의 피드백이다.

| 피드백 | 한 것 | 보는 곳 |
|--------|-------|---------|
| 두 도메인의 저울 맞추기: 기준 그래프 요건 20줄쯤을 "놓친 사실 / 단위만 다른 것"으로 나누거나, 2번에도 사람 그래프 3~4건 | 둘 다 했다. ① 저울 점검: 기준 그래프 요건 20줄 중 놓친 사실 19, 같은 사실 1, 단위만 다름 0 → 기준 그래프가 잘게 쪼갠 게 아니라 에이전트가 정말 놓쳤다. ② 2번 사람 그래프(원장 4편, 9줄): 재현율 33.3%, 원장 4번(폐기물국가간이동법)은 사람도 0줄. ③ 짝이 안 된 사람 요건 14줄 진단: 놓친 사실 0 → 사람 기준 숫자가 낮은 것은 주로 짝짓기 방식 탓. 모두 방법과 예측을 먼저 커밋했다 | [저울 점검 방법](deep/07-graphrag/experiments/e4-scale-check-oil-trade-method.md)·[결과](deep/07-graphrag/experiments/e4-scale-check-oil-trade.md) · [사람 그래프 방법](deep/07-graphrag/experiments/e4-human-graph-oil-trade-method.md)·[v1 결과](deep/07-graphrag/experiments/e4-human-graph-oil-trade-results.md)·[v2 결과](deep/07-graphrag/experiments/e4-human-graph-v2-oil-trade-results.md) · [진단 방법](deep/07-graphrag/experiments/e4-human-req-diagnosis-oil-trade-method.md)·[결과](deep/07-graphrag/experiments/e4-human-req-diagnosis-oil-trade.md) · 커밋 [a9b6aba](https://github.com/Chihun-An/rag-field-scan/commit/a9b6aba) → [705971a](https://github.com/Chihun-An/rag-field-scan/commit/705971a), [b4c00b9](https://github.com/Chihun-An/rag-field-scan/commit/b4c00b9) → [f62b752](https://github.com/Chihun-An/rag-field-scan/commit/f62b752), [3c9a258](https://github.com/Chihun-An/rag-field-scan/commit/3c9a258) → [611c167](https://github.com/Chihun-An/rag-field-scan/commit/611c167) |
| 10/25 21:00 전에 E5 답변 비교 + week-2.md | 늦었다. 방법·지시문은 10/22에 먼저 커밋했고([09af470](https://github.com/Chihun-An/rag-field-scan/commit/09af470)), 답·판정·채점과 week-2.md는 10/26에 했다 | 커밋 [4000bb0](https://github.com/Chihun-An/rag-field-scan/commit/4000bb0), [aabc3d2](https://github.com/Chihun-An/rag-field-scan/commit/aabc3d2) |
| 사람 판정은 자동 판정을 보기 전에 | 40개를 citation-judge의 단위별 판정을 보기 전에 했지만, Codex 판정은 화면에서 본 뒤였다(한계에 적음). 사람 대 각 판정기 67.5%, Codex 대 citation-judge 80.0% | [사람 판정 비교](deep/07-graphrag/experiments/e5-human-judge-results.md) |
| 다른 계열 판정기 1회 이상 | Codex로 40개(A/B를 섞어, 빈 폴더에서) | [Codex 판정](deep/07-graphrag/experiments/e5-codex-output.md) |
| E5가 끝나면 E6 뷰어 뼈대(도메인 전환, 클릭하면 출처 패널)부터 | 10/27 09:07 뼈대, 09:41 읽기 쉽게 고친 판 | 커밋 [852cbea](https://github.com/Chihun-An/rag-field-scan/commit/852cbea), [95d405a](https://github.com/Chihun-An/rag-field-scan/commit/95d405a) |
| 시간이 모자라면 필수선 순서로 | 모자라지 않아 두 도메인 모두 끝까지 했다 | [handoff 4절](handoff.md) |

[목차로](#3주-챌린지-최종-점검-2026-10-31)

### 일한 방식

**역할.** 에드워드가 지휘·결정·사람 그래프·커밋을, Cowork가 단계 설계·지시문·검토를, Claude Code가 실행을, Codex가 판정만 맡았다. Codex를 넣은 것은 10-11 발표 때 멘토가 "웹 AI끼리 토론시키기보다 데스크톱 AI끼리 일을 시키라"고 조언해서다.

**결과보다 먼저 커밋.** 예측, 방법, 지시문, 짝짓기 규칙은 결과를 보기 전에 커밋했다. 커밋 시각이 순서의 증거다. 예: E5 방법과 지시문(09af470), 2번 사람 그래프 방법과 예측(b4c00b9) → 사람 그래프(f62b752) → 비교. 결과를 본 뒤에 고친 것은 따로 표시했다(2번 사람 그래프 v2).

**정답 격리.** 기대 답은 암호를 건 디스크 이미지에 두고 저장소에는 해시만 올렸다. 디스크는 기대 답을 쓸 때와 채점할 때만 열었고, 열려 있는 동안 다른 AI 대화는 쓰지 않았다. 에이전트 그래프와 답은 저장소 밖 격리 폴더에서 새 대화로 만들었다. 새어 나간 것 두 건은 고치지 않고 기록했다(한계 참고).

**판단 기록.** 단계마다 "AI가 제안한 것 / 내가 채택하거나 고친 것 / 그렇게 판단한 이유"를 남겼다. 이유를 따로 고르지 않은 것은 그렇게 적었다.

출처: [handoff.md](handoff.md) 5·6절, [findings.md](deep/07-graphrag/findings.md) 8절, [worklog.md](worklog.md) 2026-10-13·26·27 · [목차로](#3주-챌린지-최종-점검-2026-10-31)

### 주요 발견 — 그래프 경유 답은 근거가 덜 탄탄했다

| | 1번 검색만 → 그래프 경유 | 2번 검색만 → 그래프 경유 |
|---|---|---|
| 채점(기대 답 항목 재현율) | 87.1% → 87.1% | 87.0% → 91.6% |
| 뒷받침됨 비율(citation-judge) | 79.6% → 73.0% | 73.6% → 64.0% |
| 틀린 항목(기대 답에 없는 항목) | 20 → 23 | 21 → 48 |

- 점수는 비슷했지만 그래프 경유 답의 주장은 근거가 덜 받쳐 줬다. 10-11 발표의 발견 1("번호가 맞는 것과 내용이 맞는 것은 다르다")과 같은 방향이다. 점수만 보면 보이지 않고, 근거를 따로 판정해야 보인다.
- 2번 그래프 경유 답은 그래프에 무역 요건이 없어 15문항 중 14문항에서 원문도 함께 봤다. 그래서 +4.5%p를 그래프 덕분으로 보기 어렵다.

출처: [findings.md](deep/07-graphrag/findings.md) 1·4절, [e5-score-results.md](deep/07-graphrag/experiments/e5-score-results.md), [e5-judge-results.md](deep/07-graphrag/experiments/e5-judge-results.md) · [목차로](#3주-챌린지-최종-점검-2026-10-31)

### 그 밖의 발견

- **에이전트 그래프는 정확했지만 좁았다(2번).** 짝 지은 줄의 분류 값은 모두 같았다(기준 그래프와 15/15·17/17, 사람 그래프와 1/1). 그런데 찾은 비율은 기준 그래프의 12.9%·15.1%(요건은 105줄 중 5줄), 사람 그래프 v1의 33.3%, 결과를 본 뒤 16줄을 더한 v2의 24.0%·28.0%였다. 다만 사람 그래프 쪽은 짝이 안 된 요건 14줄을 에드워드가 분류하니 놓친 사실 0, 같은 사실이지만 주어가 다름 4(사람 ULO, 에이전트 폐윤활유), 근거 문장이 다름 4, 판단 어려움 6이어서, 낮은 숫자는 주로 짝짓기 방식 탓이었다. 기준 그래프 요건 20줄을 에드워드가 분류하니 놓친 사실이 19였다. 제품을 바젤 코드나 수출입 폐기물 구분에 이으려면 두 문서를 엮어야 하는데, 스키마는 한 줄에 근거 하나만 허용했다. 사람 그래프도 v1·v2 모두 원장 4번(폐기물국가간이동법)에서 한 줄도 없었다. 무역 법령 요건이 빠진 것은 에이전트만이 아니라 규칙의 한계다.
- **같은 저울로 재니 두 도메인의 숫자가 달랐다.** 사람 줄 중 에이전트에도 있는 비율이 1번 72.2%(26/36), 2번 33.3%(3/9)였고, 에이전트 줄 중 사람에게도 있는 비율은 1번 89.7%·86.7%, 2번 12.5%·10.7%였다. 다만 1번은 사례 번호·관계·값으로, 2번은 근거 문장으로 짝을 지어 방식이 같지 않고, 2번 사람 그래프는 원장 4편·9줄로 작다. 2번 숫자는 짝짓기 방식 때문에 낮게 나온 몫이 커서(놓친 사실 0/14), 두 도메인에서 에이전트가 뽑은 사실의 차이로 읽으면 안 된다.
- **AI 판정기끼리는 맞고, 사람과는 덜 맞았다.** 표본 40개에서 Codex 대 citation-judge는 80.0%, 사람 대 각각은 67.5%였다. 사람이 "뒷받침됨"으로 본 29개 중 8개를 AI 둘은 다르게 봤다.
- **그래프가 질문에 맞으면 원문을 덜 읽었다.** 1번 그래프 경유 답은 15문항 중 11문항을 그래프만으로 답했고, 검색만 답은 17편을 다 읽었다. 점수는 같았다.
- **측정 규칙이 숫자를 흔들었다.** 2번 회차끼리 자카드 지수(두 그래프의 겹침)가 짝짓기 규칙 하나로 46.9%에서 71.4%로 바뀌었다. 원문 PDF의 낱말 중간 공백 때문에 형식 검사와 짝짓기를 고쳤다(모두 기준과 비교하기 전, 방법 파일에 기록).

출처: [findings.md](deep/07-graphrag/findings.md) 3·4·6절, [e4-reference-results-oil-trade.md](deep/07-graphrag/experiments/e4-reference-results-oil-trade.md), [e4-scale-check-oil-trade.md](deep/07-graphrag/experiments/e4-scale-check-oil-trade.md), [e4-closed-results.md](deep/07-graphrag/experiments/e4-closed-results.md), [e4-human-graph-oil-trade-results.md](deep/07-graphrag/experiments/e4-human-graph-oil-trade-results.md), [e4-human-graph-v2-oil-trade-results.md](deep/07-graphrag/experiments/e4-human-graph-v2-oil-trade-results.md), [e4-human-req-diagnosis-oil-trade.md](deep/07-graphrag/experiments/e4-human-req-diagnosis-oil-trade.md), [e5-human-judge-results.md](deep/07-graphrag/experiments/e5-human-judge-results.md), [e4-method-oil-trade.md](deep/07-graphrag/experiments/e4-method-oil-trade.md) · [목차로](#3주-챌린지-최종-점검-2026-10-31)

### 예측 대 실제

| 예측 | 실제 |
|------|------|
| E5: 그래프 경유가 B~E 종류(모으기·세기·이어 찾기·비교)에서 더 나음 | 두 도메인 모두 다섯 종류 다 "비슷". 맞은 것은 A(문서 하나 안의 사실) "비슷"뿐 |
| 그래프 효과는 2번이 더 큼 | 비슷(2번 +4.5%p, 1번 0.0%p) |
| 1번 E4 닫힌 목록 일치율 85% | 72.2% |
| 2번 사람 그래프 재현율 80% 이상 | 33.3% |
| 2번 사람 그래프의 원장 4번 줄 0줄 | 맞음(0줄) |
| 사람 그래프 v2에 추가한 줄 중 짝은 절반 미만 | 맞음(18.8%·25.0%) |
| 짝이 안 된 사람 요건 줄 중 놓친 사실은 절반 이상 | 0/14 |

출처: [findings.md](deep/07-graphrag/findings.md) 2절, [1번 예측](deep/07-graphrag/ai-consulting/predictions.md), [2번 예측](deep/07-graphrag/oil-trade/predictions.md), [사람 그래프 방법](deep/07-graphrag/experiments/e4-human-graph-oil-trade-method.md) · [목차로](#3주-챌린지-최종-점검-2026-10-31)

### 그래프 뷰어

배포: https://chihun-an.github.io/rag-field-scan/deep/07-graphrag/viewer/

- 두 도메인을 바꿔 보고, 1번은 에이전트 그래프와 사람 그래프를 바꿔 볼 수 있다. 2번 기준 그래프는 정답 격리 때문에 넣지 않았다.
- 노드는 종류별 색, 누르면 출처 패널에 근거 문장과 원장 번호가 나온다. 관계 필터, 열로 정렬, 누른 노드와 이웃만 밝게 보기가 있다.
- 1번 그래프는 노드가 147개라 처음 판은 읽기 힘들었다. 그래서 열로 정렬하고 누른 것만 밝게 보이게 고쳤다.
- 저장소의 CSV를 그대로 읽는 HTML 한 파일이다.

출처: [viewer/index.html](deep/07-graphrag/viewer/index.html), [week-3.md](progress/week-3.md) · [목차로](#3주-챌린지-최종-점검-2026-10-31)

### 3주 챌린지의 한계

- 원장이 도메인마다 17건이고 질문은 종류마다 2개다. "자료가 많을 때 그래프가 도움이 된다"는 시험하지 못한 가설이다.
- 그래프 추출, 답, citation-judge, 채점이 모두 Claude 계열이다. 다른 계열(Codex) 판정은 40개뿐이다.
- 사람 판정 40개는 Codex 판정을 화면에서 본 뒤에 했다.
- 2번 사람 그래프는 작고(9줄), 에드워드가 뷰어 화면으로 에이전트 그래프 모양을 미리 봤다. v2는 결과를 들은 뒤에 만들었다. 짝이 안 된 사람 요건 14줄의 진단은 에드워드 한 명이 1회차와만 대 본 것이고, 6줄은 판단 어려움이었다.
- 2번 기대 답 일부가 격리 대화의 보고로 샜고(10-15), 채점 세션에서 격리 대화가 기준 그래프 몇몇 열의 값 목록을 자기 출력에 찍었다. 둘 다 worklog에 기록했다.

출처: [findings.md](deep/07-graphrag/findings.md) 5절, [worklog.md](worklog.md) · [목차로](#3주-챌린지-최종-점검-2026-10-31)

### 만든 스크립트

07에서 새로 만든 스크립트다. 서브에이전트는 10-11 발표의 citation-judge를 그대로 썼다.

| 이름 | 하는 일 |
|------|---------|
| check-graph-csv.py, check-graph-csv-oil-trade.py | 그래프 CSV가 스키마의 형식 규칙을 지키는지 검사한다 |
| check-golden-rules.py, check-golden-rules-oil-trade.py | E5 답이 골든 룰 G1~G9를 지키는지 검사한다 |
| compare-graphs.py, compare-graphs-oil-trade.py | 두 그래프를 짝짓고 일치율·재현율·정밀도·자카드 지수를 낸다 |
| build-e5-judge-units.py | E5 답에서 판정 단위와 Codex 표본을 뽑는다 |
| summarize-e5-judge.py | 판정 결과를 센다 |
| compare-e5-human-judge.py | 사람 판정을 citation-judge·Codex 판정과 대 본다 |
| make-e5-blind.py | 채점용으로 두 답을 A/B로 가린 사본과 열쇠를 만든다 |
| score-e5.py | 채점 표를 열쇠로 방식에 잇고 점수를 낸다 |

출처: [deep/07-graphrag/experiments/scripts/](deep/07-graphrag/experiments/scripts/) · [목차로](#3주-챌린지-최종-점검-2026-10-31)

## 2026-10-11 발표 요약

- [무엇을 했나](#무엇을-했나)
- [작업 방식](#작업-방식)
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

### 작업 방식

지시 설계, 정답표 격리, 판단 기록 세 가지다. 멘토 피드백 ①②③에 대한 답이기도 하다.

**① 지시 방식.** 2026-10-06 지시 6(층위 1 스크립트 수정)은 완료 기준 7개를 주고 방법은 Claude Code가 정하게 했으며, 회귀 검사가 다르면 보고하고 멈추는 중단 조건을 걸었다. 지시 9(층위 2)는 완료 기준 6개와 "통제군 C3가 뒷받침됨이면 결과 파일을 쓰지 않고 보고"라는 중단 조건을 줬다(완료 기준 개수가 worklog에 적힌 지시는 이 둘이다). 사람이 개입한 자리: Claude Code가 회귀 차이(실험 01 출력에 목 표가 생김)를 보고하고 멈추자, 에드워드가 지시 7에서 1번(받아들임)을 채택했다.

**② 정답표 격리.** 기대 답은 answer-key-04.md로 파일을 나눴고, 두 서브에이전트(answer-writer, citation-judge)는 파일 읽기 도구를 도구 수준에서 막았다. 메인 세션은 규칙으로만 막혀 있었다. 2026-10-06 11:02 세션에서 Claude Code가 빈 틀이던 answer-key-04.md를 읽었고(에이전트 오류), 같은 세션 11:28 에드워드가 기대 답을 대화창에 붙여 넣는 경로로 메인 세션에 노출됐다. 그 세션은 버리고 13:17 새 세션에서 3단계를 다시 시작했다. 두 서브에이전트는 영향받지 않았다.

**③ AI 제안 / 내 선택 / 이유.** [worklog.md "판단 기록" 절](worklog.md#판단-기록--ai-제안--내-선택--이유-멘토-피드백-)(에드워드 작성). "대상 장면은 2026-10-04 MiniCheck를 접고 서브에이전트로 바꾼 결정이다."

- AI가 제안한 것: "Cowork가 네 가지를 제시했다. (1) Claude Code를 판정기로 쓰기 (2) Claude Code 먼저 하고 MiniCheck 나중에 (3) MiniCheck를 더 작은 모델(roberta-large, 1.42GB)로 계속 (4) 거기서 멈추고 findings 정리."
- 내가 채택하거나 고친 것: "(1)을 골랐다. 그리고 Cowork가 제안하지 않은 것을 추가로 물었다 — 이미 설치한 MiniCheck 가상환경을 지우라는 지시도 있어야 하지 않느냐."
- 그렇게 판단한 이유: "저장용량이 부족했다. roberta-large로 줄여도 결국 용량을 쓰는 건 같아서, 아예 설치가 필요 없는 쪽으로 갔다."

출처: [worklog.md](worklog.md) 2026-10-06 "Claude Code에 준 지시"·"문제와 대처", ["판단 기록" 절](worklog.md#판단-기록--ai-제안--내-선택--이유-멘토-피드백-), [findings.md](deep/05-citation/findings.md) 한계 10 · [목차로](#2026-10-11-발표-요약)

### 발견 1 — 번호가 맞는 것과 내용이 맞는 것은 다르다

실험 01의 다섯 번째 질문(Q5)은 "이 문서에 유해위험방지계획서 미제출 시 과태료 금액이 나와 있는가?"였다. 기대 답은 "문서에 없음"이다. 과태료 조항은 발췌 범위(제2조, 제15조~제17조, 제36조~제42조) 밖이다. 답변은 "나와 있지 않다"고 맞게 답했고, 근거 부재를 보이려고 제42조 제1항~제6항을 인용했다.

실험 01 Q5에서 답변은 제42조 제2항을 "작성·제출·심사"로 설명했다. 원문 제2항은 자격을 갖춘 자의 의견을 들어야 한다는 의견 청취 의무다.

- 층위 1: Q5가 인용한 제42조 제1항~제6항 6건이 모두 "실재함". 제42조 제2항도 통과했다
- 사람 판정: "일부". 제2항의 내용 설명이 원문과 다름
- 층위 2: 같은 주장을 P1(제2항만)과 P2(제1항+제2항) 모두 "뒷받침 안 됨"으로 판정. 사람 판정과 같음

출처: [findings.md](deep/05-citation/findings.md) 발견 1, [results-01.md](deep/05-citation/experiments/results-01.md), [results-01-layer1.md](deep/05-citation/experiments/results-01-layer1.md), [results-01-layer2.md](deep/05-citation/experiments/results-01-layer2.md) · [목차로](#2026-10-11-발표-요약)

### 발견 2 — 근거를 어디서 자르느냐가 판정을 바꾼다

이 주장(P7)은 실험 01 Q2(안전보건관리책임자의 업무)의 답변에서 나왔다. 사람 판정은 "맞음", 층위 2는 "뒷받침 안 됨"으로 갈렸다. P7에 건넨 조각은 제15조 제1항 제1호 한 줄 "1. 사업장의 산업재해 예방계획의 수립에 관한 사항"이다. 그 한 줄에는 주체(안전보건관리책임자)도 의무(총괄하여 관리)도 없다.

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

#### 원인

0건이 된 원인:

- Q6: 답변 안에 "## "로 시작하는 줄이 있어, 스크립트가 Q6 절이 거기서 끝난 것으로 읽었다. 그래서 인용 줄을 못 찾고 "줄 없음"이라는 사실과 다른 사유를 냈다
- Q7: "실제 인용 조항:" 줄은 있었으나 값이 그 줄이 아니라 바로 아래 "- " 목록에 있었다. 그래서 0건

구조를 틀리게 읽은 원인:

- 제28조의2·제28조의3을 조로 알아보지 못해 제18조에 붙였다. 그 결과 터미널에 `제18조(개인정보의 목적 외 이용ㆍ제공 제한): 항 10개 ①②③④⑤①②①②③ / 호 15개 ②: 1~10 / ③: 1~5`가 찍혔다. 경고는 없었다

고친 스크립트는 인용 항목이 0건이거나 파싱 실패가 절반 이상이면 경고를 내고 종료 코드 2로 끝난다.

출처: [results-04.md](deep/05-citation/experiments/results-04.md) "층위 1 첫 실행", [findings.md](deep/05-citation/findings.md) 발견 6 · [목차로](#2026-10-11-발표-요약)

### 빗나간 예측

- 예측 A(판정 전): Q6 답변의 호 인용은 층위 2에서 "뒷받침 안 됨"이 다수 나올 것이다. 실험 02·03의 P7과 같은 구조다
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
- [handoff.md](handoff.md) — 인수인계 (새 대화에서 먼저 읽는 문서)
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
