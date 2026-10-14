# 인수인계 (handoff)

새 대화를 시작한 Claude 쪽 AI(Claude Code, Cowork)가 이 파일 하나로 과제를 이어받기 위한 문서다. 자세한 내용은 링크한 파일에 있다. 마지막 갱신: 2026-10-14, Claude Code.

## 1. 이 저장소가 무엇인가

- "AI·데이터 분석 × RAG" 분야를 넓게 훑어 정리하는 공개 리서치 저장소다. 출발 질문: 규정·품질 문서에 근거를 달아 답하는 AI를 만들려면 무엇을 알아야 할까? ([AGENTS.md](AGENTS.md), [scope.md](scope.md))
- 배포: https://chihun-an.github.io/rag-field-scan/ ([README.md](README.md))
- 멘토 프로그램 원칙 (원문은 저장소에 없음):
  - 넓게 훑은 뒤 주제 2개를 깊게 판다 (2차 과제 안내)
  - Claude Code 데스크톱 모드로 일하고, 권한은 수동으로 두어 바뀌는 내용을 확인한 뒤 승인한다 (2차 과제 안내)
  - 멘토가 매주 저장소를 확인하고, 커밋 시각이 작업 순서의 증거가 된다 (3주 챌린지 안내)
  - 웹 AI끼리 토론시키기보다 데스크톱 AI끼리 일을 시키는 게 낫다 (10/11 발표 때 멘토 조언, 에드워드가 전함)

## 2. 지금까지의 흐름

- **1차 과제 (2026-09-19 ~ 09-22)**: 분야를 10개 영역으로 나눠 영역 파일 10개, 출처 14건, 핵심 맥락 5개, 제작 과정을 썼다 ([field-map.md](field-map.md), [sources.md](sources.md), [key-contexts.md](key-contexts.md), [process.md](process.md))
- **2차 과제 (2주 깊이 파기, 2026-10-11 발표)**: [deep/README.md](deep/README.md)
  - 05 목표: 문장 단위 귀속 평가, 인용 강제 프롬프트, 사후 검증을 개념이 아니라 실제로 돌려, "전문용어가 많고 조항끼리 참조하는 문서에서도 자동 귀속 평가가 잘 맞을까"를 작은 실험으로 확인한다
  - 07 목표: 주제를 하나 정해 GraphRAG 계획을 세운다(주제와 이유, 참고 자료, B2B·B2C·B2G 중 어디에 쓰일지, 데이터 수집, 개체와 관계)
  - 공통 목표: 두 주제를 이어서, 근거를 교차 확인하고 환각을 줄이는 엔진을 나만의 에이전트로 만든다. 3주 챌린지 E5에서 05의 2층 검증을 07 GraphRAG 답변에 그대로 쓰는 것이 이 흐름이다
  - (위 세 줄의 출처: 2차 과제 안내 요약, 원문은 저장소에 없음)
  - 05 근거 인용 실험 방법: 법령 발췌본에 인용 강제 프롬프트로 답하게 하고, 층위 1(조항 번호가 실재하는가, 규칙 기반 스크립트)과 층위 2(조항이 주장을 뒷받침하는가, citation-judge 서브에이전트)로 쟀다
  - 규모: 실험 01 질문 5개·층위 1 인용 항목 29건·층위 2 쌍 8개 / 02 호출 9회 / 03 호출 6회 / 04 질문 2개·층위 1 16건·쌍 34건·호출 46회·사람 판정 표본 17건(일치 14, 같은 쪽 1, 불일치 2). 재료는 01~03 산업안전보건법, 04 개인정보 보호법 발췌 ([findings.md](deep/05-citation/findings.md) "무엇을 했나", [results-04.md](deep/05-citation/experiments/results-04.md))
  - 주요 발견: 번호가 맞는 것과 내용이 맞는 것은 다르다. 근거를 어디서 자르느냐가 판정을 바꾸며, 주장이 건넨 조각 밖의 요소(주체·명칭)를 담을 때 그렇다. 새 입력에서 층위 1 스크립트가 종료 코드 0으로 조용히 실패했다 ([findings.md](deep/05-citation/findings.md) 발견 1·2·6·9)
  - 정답 격리 사고: 2026-10-06 11:02 세션에서 Claude Code가 빈 틀이던 기대 답 파일을 읽었고(에이전트 오류), 같은 세션 11:28 에드워드가 기대 답을 대화창에 붙여 넣어 메인 세션에 노출됐다. 그 세션은 버리고 13:17 새 세션에서 다시 시작했다. 서브에이전트 둘은 파일 읽기 도구가 막혀 있어 영향받지 않았다 ([findings.md](deep/05-citation/findings.md) 한계 10, [worklog.md](worklog.md) 2026-10-06)
  - 한계: 판정기와 답변 생성기가 같은 모델 계열이다. 사람 판정 표본이 오류 날 만한 쌍에 몰려 있다. 실험 04 사람 판정은 Cowork 판정을 본 뒤에 했다. P29에서 같은 입력의 자동 판정 3회가 갈렸다 ([findings.md](deep/05-citation/findings.md) 한계)
  - 07 계획: MBB 공개 리포트로 "산업 × 펌별 관점 비교" 그래프. 도구 셋(MS GraphRAG, LightRAG, Neo4j LLM Graph Builder)은 유료 API 키 없음·하드웨어 제약으로 지금 안 돼, 1단계는 손으로 그래프를 만들고 2단계는 조건이 생기면 자동 추출과 비교하는 조건부 2단계로 정했다 ([plan.md](deep/07-graphrag/plan.md) 7절). 3주 챌린지 계획이 아니다
- **3주 챌린지 (2026-10-12 시작)**: 두 도메인 GraphRAG. 작업 공간은 [deep/07-graphrag/](deep/07-graphrag/README.md)

## 3. 3주 챌린지

과제 정의 전체: [challenge.md](deep/07-graphrag/challenge.md)

- 핵심 질문: 자료가 많은 도메인(AI 컨설팅)과 적은 도메인(방산)에 GraphRAG를 하나씩 만들면, 그래프는 언제 도움이 될까? 에드워드 자신의 숫자로 답한다
- 두 도메인: 1번 AI 컨설팅(컨설팅 펌이 공개한 AI 도입 사례, McKinsey·BCG·Bain·Deloitte·PwC·EY·KPMG), 2번 무역 & 기름(UMO, ULO, PPO. 원래 방산, 2026-10-13 멘토 승인으로 변경) ([e1-decisions.md](deep/07-graphrag/e1-decisions.md))
- 단계와 마감:

| 주차 | 단계 | 점검 |
|------|------|------|
| 1주차 (10/12~10/18) | E0 저장소 정리 / E1 범위 + 분류 축 / E2 원천 원장 / E3 골든 세트(질문·통제 항목·골든 룰과 검사 스크립트) | 10/18(일) 21:00 |
| 2주차 (10/19~10/25) | E4 사람 그래프 vs 에이전트 그래프 / E5 검색만 vs 그래프 경유 답변 비교 | 10/25(일) 21:00 |
| 3주차 (10/26~10/31) | E6 내 그래프 뷰어 / E7 발견 정리 | 10/31(토) 21:00 |

- 필수선: 10/31까지 다 못 하면 AI 컨설팅은 끝까지, 방산(2번)은 원장·골든 세트·에이전트 그래프·답변 비교까지
- 지켜야 할 규칙(저장소에서 확인한 것):
  - 사람 그래프는 에이전트 결과를 보지 않고 먼저 만든다. 그래서 원장에는 서지 정보만 적고 업무 유형·병목·해결책·고객 산업은 적지 않는다. raw/ 파일 이름도 번호만 쓴다 ([worklog.md](worklog.md) 2026-10-13)
  - 사례 원문(raw/)은 저작권 때문에 올리지 않는다(.gitignore). 해시는 원장에 남긴다
  - 2번 도메인 변경은 2026-10-13 멘토가 승인했다. 무역 & 기름 실무 정보는 올리지 않는다 ([07 README](deep/07-graphrag/README.md), [AGENTS.md](AGENTS.md))
  - 방산 범위 제한(무기 성능·기술 사양·수출 통제)은 방산 도메인 규칙이라 2번에는 해당하지 않고, 대신 AGENTS.md의 무역 & 기름 실무 정보 금지가 적용된다 ([challenge.md](deep/07-graphrag/challenge.md) "꼭 지킬 것", [AGENTS.md](AGENTS.md) "공개 금지")

## 4. 현재 상태 (2026-10-14)

| 단계 | 1번 AI 컨설팅 | 2번 무역 & 기름 | 근거 |
|------|---------------|-----------------|------|
| E0 | 완료(커밋 7b45236, 도메인 공통) | 완료(공통) | [worklog.md](worklog.md) 2026-10-12 |
| E1 | 완료(분류 축 확정) | 완료 | [e1-decisions.md](deep/07-graphrag/e1-decisions.md) |
| E2 | 완료. 원장 17건, 제외 19건(커밋 0d9f7e2) | 대기 | [sources.csv](deep/07-graphrag/ai-consulting/sources.csv), [excluded.csv](deep/07-graphrag/ai-consulting/excluded.csv) |
| E3 골든 세트 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E4 사람 그래프 vs 에이전트 그래프 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E5 답변 비교 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E6 그래프 뷰어 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E7 발견 정리 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |

## 5. 다음 할 일

- 2번 E2(원장 10건 이상, 찾았지만 못 쓴 자료도 셈) → 두 도메인 E3 골든 세트
- 1번 E3 골든 세트: 스키마 → 질문·통제 항목 → 기대 답 → 골든 룰과 검사 스크립트 → 예측
- [07 README](deep/07-graphrag/README.md) 폴더 구조 블록에 e1-decisions.md가 아직 없다(worklog 2026-10-13에 기록된 상태)

## 6. 역할과 규칙

| 누가 | 맡는 것 |
|------|---------|
| 에드워드 | 지휘, 결정, 사람 그래프, 정답 확인, commit·push |
| Cowork | 단계 설계, 지시문 작성, 결과 검토 |
| Claude Code | 주 실행 |
| Codex | 판정과 감사만: E5 다른 계열 판정, E4 그래프 맞춰보기 판정, 필요할 때 골든 룰 검사 스크립트 감사 |

- Codex에게는 조언·설계·계획 검토·생성을 맡기지 않는다. 백업으로 쓰지 않는다. 결과는 통과/실패와 근거로만 받는다
- Codex를 합류시킨 이유: 멘토님이 웹 AI끼리 토론시키는 것보다 데스크톱 AI끼리 일을 시키는 게 낫다고 조언해서, 이를 연습하기 위함 ([worklog.md](worklog.md) 2026-10-13 "판단 기록 — Codex의 역할")
- Codex 판정 격리:
  - 판정 대화에는 프로젝트 폴더를 연결하지 않는다
  - 판정 규칙을 매 지시문 맨 위에 붙인다
  - Codex 메모리는 꺼져 있다(2026-10-13 에드워드 확인). Codex 맞춤 지시는 비워 둔다
  - 판정이 끝나면 Codex 화면에 파일·명령 사용 기록이 없는지 확인한다
- 규칙:
  - 정답을 본 대화는 다른 작업에 다시 쓰지 않는다
  - 동시 편집 금지
  - worklog에 누가 했는지 적는다
  - handoff.md는 Codex 판정 대화에 주지 않는다
  - 정답 위치를 적지 않는 규칙은 3주 챌린지의 기대 답에 해당한다. 05의 answer-key-04.md는 끝난 실험의 공개 파일이라 링크해도 된다

## 7. 더 볼 곳

- 규칙: [AGENTS.md](AGENTS.md) · 기록: [worklog.md](worklog.md) · 발표 요약: [README.md](README.md)
- 05 결론: [deep/05-citation/findings.md](deep/05-citation/findings.md)
- 3주 챌린지: [deep/07-graphrag/README.md](deep/07-graphrag/README.md), [e1-decisions.md](deep/07-graphrag/e1-decisions.md), [ai-consulting/](deep/07-graphrag/ai-consulting/README.md), [shared/](deep/07-graphrag/shared/README.md)
