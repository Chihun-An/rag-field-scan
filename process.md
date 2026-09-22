# 제작 과정 — 어떻게 만들고 어떻게 확인했는가

## 1. 한 줄 요약

사람(에드워드)이 지시·검토·승인을 맡고, Claude Code가 파일 작업을, Claude Cowork가 계획 수립과 교차 토론·검토를 맡아, GitHub Desktop으로 commit·push해 만들었다.

## 2. 도구별 역할

| 도구 | 역할 |
|------|------|
| Claude Code | 파일 작업(문서 작성·수정), worklog.md 기록 |
| Claude Cowork | 계획 수립, ChatGPT·Gemini와 교차 토론, 검토. 9/20 새벽에는 사용자 승인을 받아 Pages 설정과 배포 URL 기록을 대신함 |
| GitHub Desktop | commit·push |
| 사람(에드워드) | 지시, 검토, 승인, 출처 일부 직접 확인 |

## 3. 작업 순서

- 9/19 밤~9/20: 도구 개통(Codex 재로그인 시도 후 Claude Code 선택) → 저장소 Clone, AGENTS.md·README.md 작성 → GitHub Pages 배포(설정 9/20 00:19, 확인 9/20 00:21)
- 9/21: 멘토 피드백 반영(worklog 표 렌더링 수정, AGENTS.md에 적용 범위 항목 추가) → 범위(scope.md)와 분야 지도(field-map.md) 작성
- 9/22: 영역 파일 10개(areas/01~10) 작성 → 출처 목록(sources.md) 작성 → 핵심 맥락 5개(key-contexts.md) 작성

## 4. 확인 방법

sources.md에 실린 출처 14건 중 5건은 사람이 직접 링크를 열어 문장과 대조했다: 01(arXiv:2005.11401), 04(semver.org), 06(docs.ragas.io), 09(arXiv:2307.03172), 10(genai.owasp.org). 나머지 중 8건은 Claude(Cowork)가 열어 확인했고, 1건(04 DCMI Metadata Terms)은 아직 미확인 상태로 남아 있다. 자세한 목록은 [출처 목록](sources.md)에 있다.

## 5. 에이전트가 틀린 순간

| 무엇이 틀렸나 | 어떻게 발견했나 | 어떻게 고쳤나 |
|---------------|------------------|----------------|
| worklog 수정 1 이후 "이번 수정은 만든·고친 파일 칸에 추가하지 않았다"고 보고함. AGENTS.md의 "파일을 고칠 때마다 worklog에 기록" 규칙과 어긋남 | Claude Code의 완료 보고를 읽고 AGENTS.md 규칙과 대조함(Claude Cowork가 먼저 짚음) | 다음 지시에 "규칙대로 수정 기록도 남길 것"을 넣음 → 수정 2에서 반영된 것을 확인 |
| areas/06-rag-evaluation.md가 RAGAS 논문(arXiv:2309.15217) 초록을 출처로 충실성·답변 관련성·문맥 관련성 지표 이름을 적었으나, 초록에는 그 이름이 나열돼 있지 않음 | Claude Cowork가 arXiv 초록을 직접 열어 지표 이름이 없음을 확인 | RAGAS 공식 문서(docs.ragas.io)를 출처로 추가하고, 논문과 공식 문서의 지표 이름 차이(문맥 관련성 vs 문맥 정밀도·재현율)를 구분해 표기 |
| areas/10-security-governance.md의 OWASP 출처 URL(PDF)이 404로 연결되지 않음 | Claude Cowork가 출처 URL을 직접 열었을 때 404가 떠서 발견 | 공식 페이지(genai.owasp.org/llm-top-10)로 교체하고, 2026년판이 이미 공개돼 있다는 사실을 함께 표기 |

## 6. 규칙이 바뀐 지점

이 항목은 9/21 멘토 피드백에서 "에이전트를 여러 개 쓸 때 규칙이 어디까지 적용되는지 정리해 두라"는 지적을 받아 추가했다. Claude Cowork가 사용자 승인을 받아 GitHub Pages 설정을 대신하고, 사용자 승인을 받아 README·worklog를 대신 작성하고, 다음 날 사용자가 검토해 확정한 일(9/20 00:22 작성, 9/21 확정)이 있었다. 에이전트가 Claude Code 하나가 아니라 여러 개로 늘어나면서, 같은 작업 규칙이 모든 에이전트에 똑같이 적용되는지를 분명히 할 필요가 생겼다. 그래서 AGENTS.md에 "적용 범위(에이전트가 여러 개일 때)" 항목을 추가해, 파일 작업은 에이전트가 하되 commit·push·설정 변경·배포는 사람이 하고, 사람이 건건이 승인한 경우에만 에이전트가 대신할 수 있으며 그 사실을 worklog.md에 남기도록 못박았다.

## 7. 다시 한다면

- 지시를 보내기 전에 `[ ]` 자리표시자를 다 채우거나, 비워 둘 값을 명확히 표시한다. (지시문의 자리표시자를 채우지 않고 보내 템플릿 문구가 worklog에 그대로 커밋된 적이 있었다.)
- 출처 URL을 넣는 시점에 바로 링크를 열어 확인하는 절차를 처음부터 둔다. (LangChain 리다이렉트, Dublin Core 구버전 안내, OWASP 404가 나중에 따로따로 발견돼 여러 번 고쳐야 했다.)
- 저장소를 Clone한 직후 GitHub Desktop 계정과 로컬 Git 설정부터 확인하는 것을 첫 단계로 못박는다. ("write access 없음" 경고와 "misattributed" 경고가 각각 다른 시점에 발생했다.)

---

[작업 기록](worklog.md) · [출처 목록](sources.md) · [핵심 맥락](key-contexts.md)
