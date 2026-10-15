# 인수인계 (handoff)

새 대화를 시작한 AI(Claude Code, Cowork, 또는 그 자리를 이어받는 다른 AI)가 이 파일 하나로 과제를 이어받기 위한 문서다. 자세한 내용은 링크한 파일에 있다. 다른 AI로 넘길 때는 8절을 먼저 읽는다. 마지막 갱신: 2026-10-15, Cowork(에드워드 요청으로 직접 고침).

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
| 1주차 (10/12~10/18) | E0 저장소 정리 / E1 범위 + 분류 축 / E2 원천 원장 / E3 골든 세트(질문·통제 항목·골든 룰과 검사 스크립트) / progress/week-1.md 4줄, 리즈 저장소 상호 검토 1장 | 10/18(일) 21:00 |
| 2주차 (10/19~10/25) | E4 사람 그래프 vs 에이전트 그래프 / E5 검색만 vs 그래프 경유 답변 비교 / progress/week-2.md 4줄 | 10/25(일) 21:00 |
| 3주차 (10/26~10/31) | E6 내 그래프 뷰어 / E7 발견 정리 / progress/week-3.md 4줄 | 10/31(토) 21:00 |

- 필수선: 10/31까지 다 못 하면 AI 컨설팅은 끝까지, 방산(2번)은 원장·골든 세트·에이전트 그래프·답변 비교까지
- 지켜야 할 규칙(저장소에서 확인한 것):
  - 사람 그래프는 에이전트 결과를 보지 않고 먼저 만든다. 그래서 원장에는 서지 정보만 적고 업무 유형·병목·해결책·고객 산업은 적지 않는다. raw/ 파일 이름도 번호만 쓴다 ([worklog.md](worklog.md) 2026-10-13)
  - 사례 원문(raw/)은 저작권 때문에 올리지 않는다(.gitignore). 해시는 원장에 남긴다
  - 2번 도메인 변경은 2026-10-13 멘토가 승인했다. 무역 & 기름 실무 정보는 올리지 않는다 ([07 README](deep/07-graphrag/README.md), [AGENTS.md](AGENTS.md))
  - 방산 범위 제한(무기 성능·기술 사양·수출 통제)은 방산 도메인 규칙이라 2번에는 해당하지 않고, 대신 AGENTS.md의 무역 & 기름 실무 정보 금지가 적용된다 ([challenge.md](deep/07-graphrag/challenge.md) "꼭 지킬 것", [AGENTS.md](AGENTS.md) "공개 금지")

## 4. 현재 상태 (2026-10-15)

| 단계 | 1번 AI 컨설팅 | 2번 무역 & 기름 | 근거 |
|------|---------------|-----------------|------|
| E0 | 완료(커밋 7b45236, 도메인 공통) | 완료(공통) | [worklog.md](worklog.md) 2026-10-12 |
| E1 | 완료(분류 축 확정) | 완료 | [e1-decisions.md](deep/07-graphrag/e1-decisions.md) |
| E2 | 완료. 원장 17건, 제외 19건(커밋 0d9f7e2) | 완료. 원장 17건, 제외 24건(커밋 5e4c595에 원장 16건·제외 23건, 2026-10-14 원장 관세율표 1건·제외 관세법 본문 1건 추가) | 1번 [sources.csv](deep/07-graphrag/ai-consulting/sources.csv), [excluded.csv](deep/07-graphrag/ai-consulting/excluded.csv) / 2번 [sources.csv](deep/07-graphrag/oil-trade/sources.csv), [excluded.csv](deep/07-graphrag/oil-trade/excluded.csv) |
| E3 골든 세트 | 완료. 스키마([schema.md](deep/07-graphrag/ai-consulting/schema.md))·질문([questions.md](deep/07-graphrag/ai-consulting/questions.md))·기대 답 해시([answer-key.sha256](deep/07-graphrag/ai-consulting/answer-key.sha256))·골든 룰([golden-rules.md](deep/07-graphrag/ai-consulting/golden-rules.md))·예측([predictions.md](deep/07-graphrag/ai-consulting/predictions.md)) 확정 | 완료. 스키마([schema.md](deep/07-graphrag/oil-trade/schema.md))·질문([questions.md](deep/07-graphrag/oil-trade/questions.md))·기대 답 해시([answer-key.sha256](deep/07-graphrag/oil-trade/answer-key.sha256))·골든 룰([golden-rules.md](deep/07-graphrag/oil-trade/golden-rules.md))·예측([predictions.md](deep/07-graphrag/oil-trade/predictions.md)) 확정 | [challenge.md](deep/07-graphrag/challenge.md) |
| E4 사람 그래프 vs 에이전트 그래프 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E5 답변 비교 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E6 그래프 뷰어 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |
| E7 발견 정리 | 대기 | 대기 | [challenge.md](deep/07-graphrag/challenge.md) |

- E2·E3 경위(자세한 것은 [worklog.md](worklog.md) 2026-10-14~15):
  - 2번 E2 후속: 원장에 "별표 자체 개정일" 칸을 더해 9·11~14·17번의 별표 자체 개정일을 적었다(2026-10-14 에드워드 결정. 6·7번 고시 별지·별표는 표시 없음). 판정이 얇은 자료 중 원장 4·5·15번은 포함 근거가 원문에 있음을 2026-10-14 Cowork가 확인했고, 같은 날 에드워드가 그대로 두기로 했다. 제외 표의 석유사업법 시행령과 2022-02-03 보도자료는 2026-10-14 에드워드가 제외로 확정했다. 원장 6·7·9번 법령 번호는 2026-10-14 에드워드가 국가법령정보센터에서 확인했다(일치). 관세율표는 원장 17번으로 넣었다. 관세율표 제27류에는 10단위 세번이 없고 호·소호와 번호 매긴 세분 항목만 있다. 관세법 본문은 품목을 세분한 관세·통계통합품목분류표를 재정경제부장관이 고시한다고 정한다(2026-10-14 Cowork가 관세법 본문에서 확인. 10단위 세번이 그 고시에 있는지는 확인 필요).
  - 1번 E3 골든 세트: 스키마(완료, [schema.md](deep/07-graphrag/ai-consulting/schema.md)) → 질문·통제 항목(완료, [questions.md](deep/07-graphrag/ai-consulting/questions.md)) → 기대 답(완료, 해시 [answer-key.sha256](deep/07-graphrag/ai-consulting/answer-key.sha256)) → 골든 룰과 검사 스크립트(완료, [golden-rules.md](deep/07-graphrag/ai-consulting/golden-rules.md)) → 예측(완료, [predictions.md](deep/07-graphrag/ai-consulting/predictions.md))
  - 2번 E3 골든 세트: 스키마(완료, [schema.md](deep/07-graphrag/oil-trade/schema.md)) → 질문·통제 항목(완료, [questions.md](deep/07-graphrag/oil-trade/questions.md)) → 기대 답(완료, 해시 [answer-key.sha256](deep/07-graphrag/oil-trade/answer-key.sha256)) → 골든 룰과 검사 스크립트(완료, [golden-rules.md](deep/07-graphrag/oil-trade/golden-rules.md)) → 예측(완료, [predictions.md](deep/07-graphrag/oil-trade/predictions.md))
  - 2번 기대 답 노출 기록: 정답을 쓴 격리 대화의 마지막 보고에 정답 일부(Q9의 결과 건수, T1·T3의 근거 설명)가 들어갔고, 같은 대화가 worklog에 원문을 읽은 위치를 적었다(커밋 전에 지움). 2번은 사람 그래프가 필수가 아니어서 다시 시작하지 않고 기록만 남겼다. Q9는 질문을 바꾸지 않고 그대로 둔다(에드워드 결정). 품목 분류에 근거 두 개(원문 용어 근거, 분류 근거)를 함께 적는 방식은 [2번 골든 룰](deep/07-graphrag/oil-trade/golden-rules.md)에서 허용했다

## 5. 다음 할 일

- 1주차 남은 일(점검 10/18(일) 21:00):
  - progress/week-1.md 4줄: 에드워드가 쓴다(이번 주에 한 일, 발견, 막힌 점, 다음 주 계획)
  - 리즈 저장소 상호 검토 1장: 리즈 저장소 주소가 필요하다
- 2주차(E4·E5)에 할 일:
  - E4 1번: 에드워드가 사람 그래프 7건([schema.md](deep/07-graphrag/ai-consulting/schema.md) 9절 대상, 7절 형식)을 에이전트 결과를 보기 전에 만들어 커밋한다. 그다음 에이전트 그래프를 2회 이상 만들고, 일치율은 [1번 예측](deep/07-graphrag/ai-consulting/predictions.md) 4절 기준으로 잰다
  - E4 2번: 사람 그래프는 필수가 아니다. 에이전트 그래프를 기준 그래프(디스크 안)와 [2번 예측](deep/07-graphrag/oil-trade/predictions.md) 5절 기준으로 비교한다
  - E5: 두 도메인 모두 "검색만"과 "그래프 경유"로 Q1~Q10·T1~T5에 답한다. 답 모양은 각 도메인 golden-rules.md 2절이다. 순서는 골든 룰 검사 스크립트 → 판정기(다른 계열 1회 이상, 6절 Codex 판정 격리) → 채점(디스크를 열어 기대 답과 비교)이다
  - 기대 답 확인(에드워드): 1번은 사람 그래프를 커밋한 뒤, 2번은 아무 때나(사람 그래프 없음). 확인할 때도 아래 정답 격리 규칙대로 디스크를 연다
- 남은 작은 일:
  - [07 README](deep/07-graphrag/README.md) 폴더 구조 블록에 e1-decisions.md가 아직 없다(worklog 2026-10-13에 기록된 상태)
  - 2번 통관 단계: 근거 자료를 찾으면 [2번 스키마](deep/07-graphrag/oil-trade/schema.md)에 추가한다(에드워드 예정)
  - 한국 10단위 세번이 관세·통계통합품목분류표(재정경제부장관 고시)에 있는지 확인 필요
- E3 정답 격리 규칙(2026-10-14 확정. 10/13~14 Cowork 대화의 계획 안을 바탕으로 함):
  - 기대 답은 암호를 건 디스크 이미지(~/Documents/rag-answer-keys.dmg, 열면 /Volumes/rag-answer-keys)에 둔다. 저장소에는 해시만 커밋한다. 이유: Codex와 Cowork 모두 에드워드 맥에 접근할 수 있어 저장소 밖에 두는 것만으로는 막을 수 없다
  - 디스크는 기대 답을 쓸 때와 채점할 때만 열고 끝나면 바로 잠근다. 열려 있는 동안 Codex, Cowork, 다른 Claude Code 대화를 쓰지 않는다
  - 암호는 에드워드만 알고, 어떤 대화창에도 치지 않으며 키체인에 저장하지 않는다
  - 기대 답 초안은 정답 격리를 위해 따로 연 Claude Code 대화가 쓴다. Codex와 Cowork는 기대 답을 쓰지 않는다. 기대 답을 쓴 대화는 다시 쓰지 않는다
  - 기대 답을 쓰는 동안 에드워드는 그 대화 내용을 읽지 않고 마지막 요약만 읽는다. 수동 승인 화면에 정답이 보이므로, 그 대화에서만 디스크 안 파일 쓰기를 자동 승인한다(권한 수동 원칙의 예외)
  - 에드워드는 기대 답을 사람 그래프를 커밋한 뒤에 확인한다. 고칠 것이 있으면 새 판으로 만들고 이유와 새 해시를 남긴다
  - 주의: 메인 Claude Code 대화가 자동 모드(승인 없이 도구를 실행)로 돌면 디스크가 열려 있을 때 그 안의 파일도 승인 없이 읽을 수 있다. .claude/settings.local.json에도 "Bash(python3 -)" 허용이 있다(뒤에 입력이 붙은 python3 명령까지 승인 없이 통과시키는지는 확인 필요). 디스크가 열려 있을 때 다른 대화를 쓰지 않는 규칙이 이 때문에 필요하다
  - 예측은 그래프를 만들기 전에 커밋한다

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
- Codex 판정 규칙 초안(E5 때 shared/에 파일로 저장한다):
  1. 붙여 넣은 텍스트만 보고 판정한다
  2. 파일 읽기, 명령 실행, 인터넷 검색을 하지 않는다
  3. 판단할 정보가 부족하면 "정보 부족"이라고 쓴다
  4. 표(번호, 판정, 근거 문장)로만 답한다. 개선 제안이나 의견은 쓰지 않는다
  5. 파일·명령·인터넷을 썼다면 마지막 줄에 밝힌다
  - E5 비교 판정에서는 어느 답이 그래프 경유인지 가리고 A/B 순서를 섞어서 준다
- 규칙:
  - 정답을 본 대화는 다른 작업에 다시 쓰지 않는다
  - 동시 편집 금지
  - worklog에 누가 했는지 적는다
  - handoff.md는 Codex 판정 대화에 주지 않는다
  - 정답 위치를 적지 않는 규칙은 3주 챌린지의 기대 답에 해당한다. 05의 answer-key-04.md는 끝난 실험의 공개 파일이라 링크해도 된다
- Cowork 작업 방식:
  - Cowork는 에드워드 허락 없이 저장소 파일을 직접 고치지 않는다. 고칠 내용은 Claude Code 지시문으로 넘긴다
  - 지시문에는 넣을 문장을 그대로 적는다. "위 내용 그대로" 같은 자리표시를 쓰지 않는다
  - Claude Code 보고를 그대로 믿지 않고, Cowork가 저장소 파일·커밋·배포 사이트를 직접 열어 확인한다

## 7. 더 볼 곳

- 규칙: [AGENTS.md](AGENTS.md) · 기록: [worklog.md](worklog.md) · 발표 요약: [README.md](README.md)
- 05 결론: [deep/05-citation/findings.md](deep/05-citation/findings.md)
- 3주 챌린지: [deep/07-graphrag/README.md](deep/07-graphrag/README.md), [e1-decisions.md](deep/07-graphrag/e1-decisions.md), [ai-consulting/](deep/07-graphrag/ai-consulting/README.md), [shared/](deep/07-graphrag/shared/README.md)

## 8. 다른 AI로 넘길 때 (2026-10-15 추가)

Claude 크레딧이 떨어지는 등으로 다른 AI가 이어받을 때 읽는다. 이 절은 에드워드 요청으로 Cowork가 썼다.

- 먼저 읽을 것: 이 파일, [AGENTS.md](AGENTS.md), [worklog.md](worklog.md)의 끝부분(2026-10-14~15). 정답(기대 답)은 저장소에 없고 암호화 디스크에만 있다
- 역할을 이어받을 때:
  - Cowork 자리(설계, 지시문, 검토)를 맡는 AI는 6절 "Cowork 작업 방식"을 그대로 따른다
  - Claude Code 자리(실행)를 맡는 AI는 AGENTS.md를 그대로 따른다
  - Codex는 6절대로 판정과 감사만 맡고 백업으로 쓰지 않는다. Codex를 다른 자리에 써야 하면 에드워드가 정하고, 그 경우 E5의 다른 계열 판정기를 새로 정한다(2026-10-15 Cowork 제안)
- 이번 주에 굳어진 일하는 순서:
  1. Cowork가 설계를 제안하고 에드워드가 정한다. 판단 기록은 "AI가 제안한 것 / 내가 채택하거나 고친 것 / 그렇게 판단한 이유" 세 항목이고, 이유는 에드워드의 말로 쓴다(보기를 주고 고르게 하면 쉽다)
  2. Cowork가 넣을 문장을 그대로 담은 지시문을 쓰고, 에드워드가 실행 AI에 붙여 넣는다
  3. 실행 AI가 파일을 만들고 worklog에 남긴다. commit·push는 하지 않는다
  4. Cowork가 저장소를 직접 열어 확인한다. 긴 문서는 지시한 문장으로 기대 파일을 만들어 실제 파일과 diff로 대조한다
  5. 에드워드가 commit·push한다. 단계마다 따로 커밋해 커밋 시각이 작업 순서의 증거가 되게 한다
- 정답 디스크를 열 때마다(채점, 기대 답 확인):
  1. 다른 AI 대화(Codex, Cowork, 다른 Claude Code)를 모두 멈춘다
  2. 터미널에서 `hdiutil attach ~/Documents/rag-answer-keys.dmg`를 실행하고 암호를 넣는다(키체인에 저장하지 않는다)
  3. 실행 AI는 새 대화로 열고 작업 폴더를 디스크로 잡는다. 지시문 맨 앞에 "작업 폴더는 /Volumes/rag-answer-keys, 저장소는 ~/Documents/GitHub/rag-field-scan, 저장소 파일은 절대 경로로 읽고 쓴다"를 붙인다
  4. 에드워드는 진행 내용을 읽지 않고 마지막 보고만 읽는다. 지시문에 보고 항목을 정해 두고, 보고와 worklog에 정답 내용이나 원문 위치를 쓰지 말라고 적는다(2번 기대 답 때 둘 다 새었다)
  5. 그 대화를 삭제하고 `hdiutil detach /Volumes/rag-answer-keys`로 잠근 뒤에 다른 AI 대화를 다시 쓴다
- 기대 답은 두 도메인 모두 이미 썼다(해시: [1번](deep/07-graphrag/ai-consulting/answer-key.sha256), [2번](deep/07-graphrag/oil-trade/answer-key.sha256)). 앞으로 디스크를 여는 때는 채점과 에드워드의 기대 답 확인뿐이다
