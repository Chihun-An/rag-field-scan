# worklog

## 2026-09-19 ~ 09-20

### 목표
도구 개통 + 빈 저장소 배포, 9/20 21:00 공유용 GitHub Pages URL 확보

### 시작·종료 시각

- 시작: 2026-09-19 23:40경
- 종료: 2026-09-20 00:20경 (이후 Pages 설정·URL 기록은 Claude Cowork가 대신함)

### 환경

- macOS, Claude Code 데스크톱 (파일 작업)
- GitHub Desktop (commit·push)
- Claude Cowork (계획 수립, ChatGPT·Gemini와 교차 토론, Pages 설정·URL 기록 대행)

### Codex 시도 결과

| 시각 | 결과 | 오류 문구 | 선택 | 이유 |
|------|------|-----------|------|------|
| 9/19 밤 | 재로그인 성공 | | Claude Code | 파일이 바뀌기 전에 변경 내용을 화면에서 보고 승인할 수 있어서 |

재로그인 성공. 다만 파일이 바뀌기 전에 변경 내용을 보고 승인할 수 있어서 Claude Code를 선택해 진행.

### Claude Code에 준 지시

1. README.md를 다음 구조로 수정: 제목(RAG Field Scan), 결론 한 줄(작성 중), 배포 URL(배포 후 추가), 출발 질문, 문서 목록(AGENTS.md, worklog.md 링크, 나머지 문서는 9/21 이후 추가 예정 표시).
2. worklog.md를 만들고 2026-09-19 항목을 정해진 틀로 작성. 알려주지 않은 값은 비워 둠.
3. 사실이나 출처를 지어내지 않고, commit·push는 하지 않음.
4. 작업 후 실제로 읽은 파일과 만들거나 고친 파일을 나눠서 보고.

### 읽은 파일

- AGENTS.md
- README.md

### 만든·고친 파일

- AGENTS.md: Claude가 초안을 제안했고, 내가 검토해서 확정함
- README.md: 고침
- worklog.md: 만듦
- worklog.md: 수정 1 (2026-09-20) — 항목 날짜를 "2026-09-19 ~ 09-20"으로 변경, 목표·시작/종료 시각·Codex 시도 결과·문제와 대처·다음 작업 채움
- worklog.md: 수정 2 (2026-09-20) — 시작 시각·선호 이유 자리표시자 교체, Codex 시도 결과 표 채움(선택·이유 열 추가), 이 기록 추가
- README.md, worklog.md: 수정 3 (2026-09-20 00:22, Claude Cowork) — 사용자 승인을 받아 대행 작성. 이후 9/21 사용자가 내용을 검토하고, 남은 자리표시자를 사용자가 정한 값(시작 시각, 도구 선택 이유)으로 채우도록 지시해 확정함. commit·push는 사용자가 직접 수행. README에 배포 URL 기록, worklog에 커밋·Pages URL·문제와 대처·에이전트 오류 후보 기록, 남은 자리표시자를 "확인 필요"로 표시
- worklog.md: 수정 4 (2026-09-21, Claude Code) — Codex 시도 결과의 이유 칸과 아래 문장을 "선호도 이유"로 교체. commit·push는 하지 않음
- worklog.md: 수정 5 (2026-09-21, Claude Code) — 시작 시각을 "2026-09-19 23:40경"으로, Codex 시도 결과의 이유 칸과 아래 문장을 실제 이유 문장으로 교체, "내가 검토한 것"에 두 줄 추가. commit·push는 하지 않음
- worklog.md: 수정 6 (2026-09-21, Claude Code) — "다음 작업"을 9/21~9/25 일정으로 교체, "문제와 대처"의 자리표시자 항목 끝에 "→ 9/21에 실제 값으로 채움" 추가. commit·push는 하지 않음
- worklog.md: 수정 7 (2026-09-21, Claude Code) — 제목 바로 뒤에 목록·표가 붙어 있던 12곳(Codex 시도 결과 포함)에 빈 줄 추가. 제목 뒤가 일반 문장인 "목표"는 그대로 둠. commit·push는 하지 않음
- AGENTS.md: 수정 (2026-09-21, Claude Code) — 맨 끝에 "적용 범위 (에이전트가 여러 개일 때)" 항목 추가. commit·push는 하지 않음

### 내가 검토한 것

- AGENTS.md 초안 (Claude가 제안, 내가 검토해 확정)
- Claude Code 변경안을 수동 모드에서 하나씩 확인하고 승인
- GitHub Desktop에서 커밋 전 diff 확인

### 커밋

- 52094ca Initial commit (GitHub 웹에서 저장소 생성, README 자동 생성)
- 4a9c867 AGENTS.md (GitHub 웹에서 직접 작성)
- 2b1fb57 Create skeleton with Claude Code (GitHub Desktop, 작성자 Edward + noreply 이메일)

### Pages URL

- https://chihun-an.github.io/rag-field-scan/
- 설정: 2026-09-20 00:19, Settings → Pages → Deploy from a branch → main / (root). 사용자 승인을 받아 Claude Cowork가 브라우저로 설정함
- 확인: 2026-09-20 00:21, 첫 페이지와 AGENTS.html·worklog.html 링크 모두 정상(200)

### 문제와 대처

- GitHub Desktop을 새로 설치해야 하는 줄 알았으나 이미 설치돼 있었고 다른 저장소가 열려 있었음 → rag-field-scan을 새로 Clone
- 저장소 폴더를 기존 작업 폴더(RAG_Assignment)와 혼동 → GitHub Desktop의 Show in Finder로 위치 확인
- 실명 노출을 막으려고 저장소 로컬 Git 설정을 Edward + GitHub noreply 이메일로 지정
- Claude Code의 GitHub 계정 연결 제안은 거절 (commit·push는 사람이 GitHub Desktop으로 함)
- 권한 모드는 '수동'으로 두고, 변경마다 내용을 확인한 뒤 승인함
- GitHub Desktop이 다른 계정으로 로그인돼 있어 "write access 없음" 경고 → 로그아웃 후 저장소 소유 계정으로 다시 로그인
- 커밋 직전 "misattributed" 경고: 로컬 Git 설정이 저장되지 않아 전역 설정 이메일이 쓰이려 함 → Update Email(전역 변경) 대신 Repository Settings에서 로컬 설정 저장
- 지시문의 [ ] 자리표시자를 채우지 않고 보내, 템플릿 문구가 worklog에 그대로 들어간 채 커밋됨 → "확인 필요"로 표시해 두고 다음 커밋에서 실제 값으로 수정 예정 → 9/21에 실제 값으로 채움

### 에이전트가 틀린 순간 (후보)

- 무엇이 틀렸나: 수정 1 뒤 Claude Code가 "이번 수정은 만든·고친 파일 칸에 추가하지 않았다"고 보고함. AGENTS.md의 "파일을 고칠 때마다 worklog에 기록" 규칙과 어긋남 (사용자 지시를 좁게 따르느라 규칙을 놓침)
- 어떻게 잡았나: Claude Code의 완료 보고를 읽고 AGENTS.md 규칙과 대조함 (Claude Cowork가 먼저 짚음)
- 어떻게 고쳤나: 다음 지시에 "규칙대로 수정 기록도 남길 것"을 넣음 → 수정 2에서 수정 1·2 기록이 추가된 것을 GitHub Desktop diff로 확인

### 다음 작업

- 9/21: commit·push → 배포 URL 카톡 공유(9/20 21:00 마감 대비 지연) → 범위·영역 8~12개 확정, 분야 지도
- 9/22~23: 영역 파일 작성, 출처 수집
- 9/24: 핵심 맥락 5, 출처 목록, 출처 5개 직접 확인
- 9/25 21:00: 제작 과정 1장, README 결론 한 줄, 최종 URL 공유

## 2026-09-21

### 목표

범위(scope.md)와 분야 지도(field-map.md) 작성

### 시작·종료 시각

- 시작: 2026-09-21 10:40경
- 종료: 2026-09-21 15:00경

### 환경

- macOS, Claude Code 데스크톱

### Claude Code에 준 지시

1. scope.md와 field-map.md를 새로 만들 것. AGENTS.md 규칙을 지키고 commit·push는 하지 않음.
2. scope.md: 출발 질문, 다루는 것, 다루지 않는 것, 깊이 기준(영역당 1쪽), 출처 기준.
3. field-map.md: 10개 영역 표(번호 | 영역 | 한 줄 정의 | 출발 질문과의 연결 | IATF 연결), 표 앞뒤 빈 줄, 표 아래에 "영역 파일은 9/22~23에 작성 예정" 한 줄. IATF 연결 칸에는 문서 식별자·상호참조·개정 이력 중 해당되는 것만 적고 사내 문서 내용은 쓰지 않음.
4. README.md 문서 목록에 scope.md, field-map.md 링크 추가. worklog.md에 2026-09-21 항목 추가. 사실이나 출처는 지어내지 않음.
5. 검토 후 수정 지시: field-map IATF 연결 칸 06·10 채우기, scope.md '다루는 것' 문장 보완, 오늘 항목의 시각·검토 내용·커밋·문제와 대처 채우고 Codex 표 빼기

### 읽은 파일

- AGENTS.md
- README.md
- worklog.md

### 만든·고친 파일

- scope.md: 만듦
- field-map.md: 만듦. 영역 파일 경로(areas/…)는 아직 없는 파일이라 링크가 아닌 텍스트로 적음. "한 줄 정의"·"출발 질문과의 연결"·"IATF 연결" 칸의 문구는 Claude가 쓴 초안이며 출처를 붙이지 않았음(검토 필요)
- README.md: 문서 목록에 scope.md, field-map.md 링크 추가
- worklog.md: 2026-09-21 항목 추가
- field-map.md: 수정 (2026-09-21, Claude Code) — 06 RAG 평가의 IATF 연결 칸에 "개정 이력 (…)", 10 권한·보안·거버넌스에 "문서 식별자, 개정 이력" 기입. 01·09는 "-" 유지. commit·push는 하지 않음
- scope.md: 수정 (2026-09-21, Claude Code) — "다루는 것"에 10개 영역 문장과 field-map.md 링크 한 줄 추가. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-21, Claude Code) — 오늘 항목의 시작·종료 시각, 내가 검토한 것, 커밋, 문제와 대처, 다음 작업을 채우고 Codex 시도 결과 표를 뺌. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-21, Claude Code) — 오늘 항목의 Pages URL 칸에 "변경 없음 (동일 URL: …)" 추가, "Claude Code에 준 지시"에 5번 항목 추가. commit·push는 하지 않음

### 내가 검토한 것

- field-map의 영역 정의와 IATF 연결 칸을 검토하고 06·10을 채우도록 지시
- scope.md 범위 문장 보완 지시

### 커밋

- 46e2b95 Fix worklog table and add agent scope rule (배포 확인 11:26)

### Pages URL

- 변경 없음 (동일 URL: https://chihun-an.github.io/rag-field-scan/)

### 문제와 대처

- 배포 후에도 브라우저에 옛 페이지가 보임 → 캐시 문제였고 강력 새로고침으로 확인

### 다음 작업

- 9/22~23 영역 파일 10개 작성, 영역마다 1차 출처 1개

## 2026-09-22

### 목표

areas 폴더 생성, 영역 파일 4개 작성 (01~04) + 영역 파일 3개 작성 (05~07) + 영역 파일 3개 작성 (08~10, 완결) + 링크 정리, sources.md 작성 + key-contexts.md 작성 + process.md 작성

### 시작·종료 시각

- 시작: 2026-09-22 09:20경
- 종료: 2026-09-22 11:04경

### 환경

- macOS, Claude Code 데스크톱

### Claude Code에 준 지시

1. AGENTS.md, scope.md, field-map.md를 먼저 읽고 규칙과 틀을 따라 areas/01~04 파일 작성. commit·push는 하지 않음.
2. 각 파일은 scope.md의 깊이 기준(한 줄 정의 / 출발 질문과의 관계 / 핵심 개념 3~5개 / 대표 기법·도구 / 품질 문서에서는? / 남은 질문 / 출처) 그대로 따름.
3. 분량은 영역당 1쪽, 처음 보는 사람 기준으로 쉽게 작성.
4. 출처는 웹 검색으로 직접 찾은 1차 자료를 영역당 1개 이상, "제목 — URL (확인: 2026-09-22)" 형식으로. URL을 지어내지 않고, 확실하지 않으면 "확인 필요"로 표시.
5. "품질 문서에서는?"에는 사내 문서 내용·회사명 없이 문서 식별자·상호참조·개정 이력 같은 일반적 문제 유형으로만 작성.
6. 각 파일 맨 아래에 [분야 지도](../field-map.md) 링크 추가. 제목 바로 뒤에 목록·표가 오면 빈 줄 추가.
7. AGENTS.md, scope.md, field-map.md를 먼저 읽고 규칙과 틀을 따라 areas/05~07 파일 작성. 01~04와 같은 7항목 구성, 출처 기준, 표기 규칙을 그대로 적용. 06에는 field-map대로 "구버전 문서를 근거로 답하는 오류를 평가 항목으로 삼는" 관점을 한 줄 넣음.
8. AGENTS.md, scope.md, field-map.md를 먼저 읽고 01~07과 같은 틀로 areas/08~10 파일 작성. 08은 다단계 검색·도구 호출과 정형 데이터 분석을 함께 다룸. 09는 긴 입력에서 중간 정보를 놓치는 현상을 한 줄 넣음. 10은 접근 권한 분리, 감사 추적, 개인정보·기밀 문서 취급을 다룸. 출처는 논문 초록에 없는 세부 내용이면 공식 문서를 함께 달고, 리다이렉트되면 최종 주소로 적음.
9. field-map.md 표의 영역 파일 경로를 실제 링크로 교체하고, "영역 파일은 9/22~23에 작성 예정" 문장 삭제. README.md 문서 목록에 영역 파일 10개 링크와 sources.md 링크 추가.
10. sources.md 신규 작성: areas/01~10 출처를 표(영역·출처 제목·URL·확인 날짜·확인자)로 모음. 확인자는 semver.org(04)·genai.owasp.org(10)는 "에드워드", worklog에 Claude(Cowork)가 열어 확인했다고 기록된 것은 "Claude(Cowork) 확인", 그 외 확인 기록이 없는 것은 "미확인"으로 표시.
11. AGENTS.md, scope.md, field-map.md, sources.md를 먼저 읽고 areas/01~10 전부를 읽은 뒤 key-contexts.md 신규 작성: 10개 영역을 관통하는 핵심 맥락 5개(제목/설명 3~5문장/근거 영역 2개 이상/출발 질문에 주는 답), 그중 최소 2개는 품질·규정 문서 조건에서 특별히 중요한 맥락. 새 사실·출처를 만들지 않고 영역 파일 내용만 근거로 사용. README.md에 링크 추가.
12. AGENTS.md와 worklog.md 전체를 먼저 읽고 process.md 신규 작성: worklog에 기록된 사실만 근거로, 한 줄 요약/도구별 역할 표/작업 순서/확인 방법(sources.md 링크)/에이전트가 틀린 순간 3건 표/규칙이 바뀐 지점/다시 한다면 3개. worklog에 없는 사실은 만들지 않음. README.md에 링크 추가.

### 읽은 파일

- AGENTS.md
- scope.md
- field-map.md
- worklog.md
- README.md
- sources.md
- areas/01-rag-basics.md ~ areas/10-security-governance.md (10개, sources.md·key-contexts.md 작성을 위해 다시 읽음)
- worklog.md 전체 (process.md 작성을 위해 다시 읽음)

### 만든·고친 파일

- areas/01-rag-basics.md: 만듦. 출처 1개(Lewis et al., arXiv:2005.11401)를 웹 검색으로 확인해 넣음. "남은 질문"은 확인 필요로 표시
- areas/02-document-parsing-chunking.md: 만듦. 출처 1개(LangChain 공식 문서)를 웹 검색으로 확인해 넣음. "남은 질문"은 확인 필요로 표시
- areas/03-retrieval-vector-db.md: 만듦. 출처 1개(Malkov & Yashunin, HNSW 논문, arXiv:1603.09320)를 웹 검색으로 확인해 넣음. 벡터 DB 제품명은 scope.md에 따라 쓰지 않음. "남은 질문"은 확인 필요로 표시
- areas/04-metadata-versioning.md: 만듦. 출처 2개(Dublin Core 공식 문서, semver.org)를 웹 검색으로 확인해 넣음. "남은 질문"은 확인 필요로 표시
- worklog.md: 2026-09-22 항목 추가
- areas/02-document-parsing-chunking.md: 수정 (2026-09-22, Claude Code) — LangChain 출처 URL을 리다이렉트 전 옛 주소에서 https://reference.langchain.com/python/langchain-text-splitters/character/RecursiveCharacterTextSplitter 로 교체. commit·push는 하지 않음
- areas/04-metadata-versioning.md: 수정 (2026-09-22, Claude Code) — Dublin Core 출처를 "1.1 원문(현재는 DCMI Metadata Terms 참고 권장)"으로 표시하고, DCMI Metadata Terms 출처를 추가. commit·push는 하지 않음
- areas/03-retrieval-vector-db.md: 수정 (2026-09-22, Claude Code) — "대표 기법·도구"에 키워드 검색(BM25), 하이브리드 검색 한 줄씩 추가. BM25 출처로 Robertson & Zaragoza 논문(웹 검색으로 확인)을 추가. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — 2026-09-22 항목의 시작 시각, 내가 검토한 것, 문제와 대처, 다음 작업, Pages URL을 채움. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — "내가 검토한 것"에 출처 3건 직접 대조, BM25·Dublin Core 확인 주체(Claude Cowork) 두 줄 추가. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — "내가 검토한 것"에 semver.org 직접 확인(에드워드), 출처 확인(Claude Cowork) 두 줄 추가. commit·push는 하지 않음
- areas/05-citation-grounding.md: 만듦. 출처 1개(Rashkin et al., "Measuring Attribution in Natural Language Generation Models", arXiv:2112.12870)를 웹 검색으로 확인해 넣음. "남은 질문"은 확인 필요로 표시
- areas/06-rag-evaluation.md: 만듦. 출처 1개(Es et al., "Ragas", arXiv:2309.15217)를 웹 검색으로 확인해 넣음. field-map대로 "구버전 문서 근거 오류"를 평가 항목 관점으로 "품질 문서에서는?"에 넣음. "남은 질문"은 확인 필요로 표시
- areas/07-graphrag.md: 만듦. 출처 1개(Edge et al., "From Local to Global: A Graph RAG Approach to Query-Focused Summarization", arXiv:2404.16130)를 웹 검색으로 확인해 넣음. "남은 질문"은 확인 필요로 표시
- worklog.md: 2026-09-22 항목에 영역 05~07 작성 기록 추가 (이 기록)
- areas/06-rag-evaluation.md: 수정 (2026-09-22, Claude Code) — 지표 이름(충실성·답변 관련성·문맥 관련성)의 근거로 RAGAS 공식 문서 출처를 웹 검색으로 찾아 추가. commit·push는 하지 않음
- areas/06-rag-evaluation.md: 수정 (2026-09-22, Claude Code) — "핵심 개념"의 문맥 관련성을 문맥 정밀도·문맥 재현율 두 항목으로 교체, "대표 기법·도구"의 RAGAS 줄에 논문·공식 문서 간 지표 이름 차이 설명 추가. commit·push는 하지 않음
- areas/08-agentic-rag.md: 만듦. 출처 1개(Yao et al., "ReAct", arXiv:2210.03629)를 웹 검색으로 확인해 넣음. 다단계 검색·도구 호출·정형 데이터 분석을 함께 다룸. "남은 질문"은 확인 필요로 표시
- areas/09-long-context-vs-rag.md: 만듦. 출처 1개(Liu et al., "Lost in the Middle", arXiv:2307.03172)를 웹 검색으로 확인해 넣음. 긴 입력에서 중간 정보를 놓치는 현상을 핵심 개념과 "품질 문서에서는?"에 넣음. "남은 질문"은 확인 필요로 표시
- areas/10-security-governance.md: 만듦. 출처 1개(OWASP Top 10 for LLM Applications 2025 공식 PDF, 민감정보 노출 항목)를 웹 검색으로 확인해 넣음. 접근 권한 분리·감사 추적·민감정보 노출을 다룸. "남은 질문"은 확인 필요로 표시
- worklog.md: 2026-09-22 항목에 영역 08~10 작성 기록 추가, "다음 작업"을 9/24 일정으로 갱신 (이 기록)
- areas/10-security-governance.md: 수정 (2026-09-22, Claude Code) — OWASP 출처 URL을 404 PDF에서 공식 페이지(genai.owasp.org/llm-top-10)로 교체하고 2026년판 존재를 알리는 한 줄 추가, "품질 문서에서는?"에 출처 판본 표기 관련 한 줄 추가. commit·push는 하지 않음
- field-map.md: 수정 (2026-09-22, Claude Code) — 표의 영역 파일 경로 10개를 실제 링크로 교체, "영역 파일은 9/22~23에 작성 예정" 문장 삭제. commit·push는 하지 않음
- README.md: 수정 (2026-09-22, Claude Code) — 문서 목록에 영역 파일 10개 링크와 sources.md 링크 추가. commit·push는 하지 않음
- sources.md: 만듦 (2026-09-22, Claude Code) — areas/01~10 출처 14건을 표로 정리. 확인자는 worklog 기록을 근거로 에드워드/Claude(Cowork) 확인/미확인으로 구분. commit·push는 하지 않음
- worklog.md: 2026-09-22 항목에 링크 정리·sources.md 작성 기록 추가 (이 기록)
- sources.md: 수정 (2026-09-22, Claude Code) — 확인자 칸 재정리: 01·06(docs.ragas.io)·09를 "에드워드"로, 02·05·06(논문)·07·08을 "Claude(Cowork) 확인"으로 변경, 04 DCMI Metadata Terms는 "미확인" 유지. 표 아래에 확인자 표기 설명 한 줄 추가. commit·push는 하지 않음
- worklog.md: 2026-09-22 항목 "내가 검토한 것"에 에드워드의 직접 확인 3건(arXiv 2005.11401, arXiv 2307.03172, docs.ragas.io) 기록 추가 (이 기록)
- key-contexts.md: 만듦 (2026-09-22, Claude Code) — AGENTS.md, scope.md, field-map.md, sources.md와 areas/01~10 전부를 읽고 핵심 맥락 5개 작성. 새 사실·출처 없이 영역 파일 내용만 근거로 사용. 맥락 1(문서 식별자·상호참조), 2(최신 버전만 근거), 5(투명성·통제 긴장)는 품질·규정 문서 조건에서 특별히 중요한 맥락으로 표시. commit·push는 하지 않음
- README.md: 수정 (2026-09-22, Claude Code) — 문서 목록에 key-contexts.md 링크 추가. commit·push는 하지 않음
- worklog.md: 2026-09-22 항목에 key-contexts.md 작성 기록 추가 (이 기록)
- key-contexts.md: 수정 (2026-09-22, Claude Code) — 1번·2번 설명 끝에 한 줄씩 추가해 두 맥락의 차이("출처의 연결" vs "출처의 시점")를 명시. commit·push는 하지 않음
- worklog.md: 2026-09-22 항목에 key-contexts.md 1·2번 구분 문장 추가 기록 (이 기록)
- process.md: 만듦 (2026-09-22, Claude Code) — AGENTS.md와 worklog.md 전체를 읽고, worklog에 기록된 사실만 근거로 제작 과정 작성. 한 줄 요약, 도구별 역할 표, 작업 순서, 확인 방법(sources.md 링크), 에이전트가 틀린 순간 3건 표, 규칙이 바뀐 지점, 다시 한다면 3개로 구성. commit·push는 하지 않음
- README.md: 수정 (2026-09-22, Claude Code) — 문서 목록에 process.md 링크 추가. commit·push는 하지 않음
- worklog.md: 2026-09-22 항목에 process.md 작성 기록 추가 (이 기록)
- process.md: 수정 (2026-09-22, Claude Code) — "3. 작업 순서"의 9/21 줄에 멘토 피드백 반영 내용 추가, "5. 에이전트가 틀린 순간" 2·3행의 "어떻게 발견했나"에 발견 주체(Claude Cowork) 명시, "6. 규칙이 바뀐 지점" 앞에 9/21 멘토 피드백 계기 문장 추가. commit·push는 하지 않음
- worklog.md: 2026-09-22 항목에 process.md 수정 기록 추가 (이 기록)
- README.md: 수정 (2026-09-22, Claude Code) — "결론" 항목을 한 줄 결론 문장으로 교체. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — 2026-09-22 항목의 종료 시각을 "2026-09-22 11:04경"(시스템 시각)으로 채움, 맨 아래 "전체 요약" 항목 추가. commit·push는 하지 않음
- README.md: 수정 (2026-09-22, Claude Code) — 문서 목록 맨 아래 "나머지 문서: 9/21 이후 추가 예정" 줄 삭제. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — 2026-09-22 항목 "다음 작업"을 9/25~9/26 일정과 선택 도전 항목으로 교체. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — 9/19~20 항목 "수정 3"의 대행 작업 설명에 사용자 승인과 9/21 검토·확정 사실을 반영해 표현을 다듬음. 사실 변경 없음. commit·push는 하지 않음
- process.md: 수정 (2026-09-22, Claude Code) — "6. 규칙이 바뀐 지점"의 대행 작업 설명을 사용자 승인·검토 확정 표현으로 다듬음. 사실 변경 없음. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — 9/19~20 항목 "수정 3"의 중복된 "commit·push는 하지 않음" 문구를 삭제(앞에 이미 "commit·push는 사용자가 직접 수행"이 있음). 사실 변경 없음. commit·push는 하지 않음
- worklog.md: 수정 (2026-09-22, Claude Code) — "만든·고친 파일" 두 줄에서 옛 문장 인용을 빼고 무엇을 다듬었는지만 남김. commit·push는 하지 않음
- process.md: 수정 (2026-09-22, Claude Code) — "6. 규칙이 바뀐 지점" 두 번째 문장을 더 간결한 표현으로 다듬음. 사실 변경 없음. commit·push는 하지 않음

### 내가 검토한 것

- 영역 파일 4개의 출처 URL을 열어 확인. LangChain 문서 주소 변경과 Dublin Core 구버전 안내를 발견해 수정 지시
- 출처 3건(arXiv 2005.11401, arXiv 1603.09320, semver.org)을 직접 열어 파일 문장과 대조함
- BM25 출처 PDF와 Dublin Core 구버전 안내는 Claude(Cowork)가 열어 확인함
- 출처 직접 확인(2026-09-22, 에드워드): semver.org의 MAJOR/MINOR/PATCH 설명이 04 파일 문장과 일치함을 확인
- 출처 확인(2026-09-22, Claude Cowork): arXiv 2005.11401, arXiv 1603.09320, BM25 PDF(staff.city.ac.uk), Dublin Core DCES 구버전 안내
- 출처 직접 확인(2026-09-22, 에드워드): arXiv 2005.11401 제목, arXiv 2307.03172 초록의 중간 정보 손실 서술, docs.ragas.io 지표 목록

### 커밋

-

### Pages URL

- 변경 없음

### 문제와 대처

- 출처 URL 1건이 리다이렉트되고 1건이 구버전 안내를 달고 있었음 → 새 주소와 최신 명세로 교체
- 06 파일이 RAGAS 지표 이름을 논문 초록 근거로 적었으나 초록에는 지표 이름이 없음을 확인 → 공식 문서를 출처로 추가
- RAGAS 지표 이름이 논문(문맥 관련성)과 현재 공식 문서(문맥 정밀도·문맥 재현율)에서 다름을 확인 → 양쪽을 구분해 표기
- 10 영역 OWASP 출처 PDF 주소가 404였음 → 공식 페이지로 교체하고, 2026년판이 이미 공개된 사실을 함께 표기

### 다음 작업

- 9/25 21:00: 최종 URL 공유
- 9/26 09:00: 5분 발표 (자료는 README·key-contexts·process 기준)
- 남은 선택 도전: 영역 md로 키워드 검색 RAG 만들기 (필수 완료 후)

## 전체 요약

- 기간: 2026-09-19 ~ 09-22
- 만든 문서: README, AGENTS.md, scope.md, field-map.md, areas/01~10, sources.md, key-contexts.md, process.md, worklog.md
- 출처: 14건 (사람 직접 확인 5건, Claude Cowork 확인 8건, 미확인 1건)
- 에이전트 오류 기록: 3건
- 배포 URL: https://chihun-an.github.io/rag-field-scan/

## 2026-09-28

### 목표

2주 깊이 파기 준비: deep/README.md 주제 확정, deep/05-citation/·deep/07-graphrag/ 작성

### 시작·종료 시각

- 시작: 2026-09-28 15:10경
- 종료: 2026-09-28 15:11경

### 환경

- macOS, Claude Code 데스크톱

### Claude Code에 준 지시

1. AGENTS.md, README.md, deep/README.md, areas/05-citation-grounding.md, areas/07-graphrag.md를 먼저 읽을 것. commit·push는 하지 않음.
2. deep/04-versioning 폴더가 있으면 deep/07-graphrag로 이름 변경(안의 내용은 새로 씀).
3. deep/README.md의 주제 2개를 05(근거 인용·환각 억제, 실험)와 07(GraphRAG, 계획)로 정하고 각 목표를 적음.
4. deep/05-citation/ 작성: questions.md(실험 질문 5개), tools.md(RAGAS·ALCE·MiniCheck 비교표와 MiniCheck를 먼저 고르는 판단), data.md(한국 법령·EU AI Act 재료 계획, IATF 원문 비공개 원칙), papers.md(AIS·ALCE·RARR 논문 표, 출처는 웹 검색으로 확인).
5. deep/07-graphrag/ 작성: plan.md(주제/참고자료/활용처/데이터 수집/개체·관계 설계 + 답하고 싶은 질문 3개), tools.md(Microsoft GraphRAG·LightRAG·Neo4j LLM Graph Builder 비교표, 선택 기준만 적고 선택은 비움), papers.md(GraphRAG·LightRAG·Graph RAG 서베이 논문 표).
6. URL은 웹 검색으로 실제 확인한 것만, 리다이렉트되면 최종 주소로. 표 앞뒤·제목 뒤 빈 줄. README.md 문서 목록에 deep/README.md 링크 추가. worklog에 오늘 항목 기록.

### 읽은 파일

- AGENTS.md
- README.md
- areas/05-citation-grounding.md
- areas/07-graphrag.md
- (deep/README.md는 이 저장소에 존재하지 않아 읽지 못함 — 아래 "문제와 대처" 참고)

### 만든·고친 파일

- deep/README.md: 만듦(이미 있던 파일을 고친 것이 아니라 새로 만듦)
- deep/05-citation/questions.md: 만듦
- deep/05-citation/tools.md: 만듦. RAGAS·ALCE·MiniCheck 저장소 URL을 웹 검색으로 확인해 넣음
- deep/05-citation/data.md: 만듦. 국가법령정보센터·EUR-Lex(EU AI Act) URL을 웹 검색으로 확인해 넣음
- deep/05-citation/papers.md: 만듦. Rashkin et al.(AIS)·Gao et al.(ALCE)·Gao et al.(RARR) 출처를 웹 검색으로 확인해 넣음
- deep/07-graphrag/plan.md: 만듦. McKinsey Global Institute·BCG Henderson Institute·Bain 인사이트 페이지 URL을 웹 검색으로 확인해 넣음
- deep/07-graphrag/tools.md: 만듦. Microsoft GraphRAG·LightRAG·Neo4j LLM Graph Builder 저장소 URL을 웹 검색으로 확인해 넣음. 도구 선택은 비워 둠
- deep/07-graphrag/papers.md: 만듦. Edge et al.(GraphRAG)·Guo et al.(LightRAG)·Peng et al.(서베이) 출처를 웹 검색으로 확인해 넣음
- README.md: 문서 목록에 deep/README.md 링크 추가
- deep/05-citation/tools.md: 수정 (2026-09-28, Claude Code) — RAGAS 저장소 URL을 explodinggradients/ragas에서 vibrantlabsai/ragas로 교체, 판단 아래에 조직명 변경 사실 한 줄 추가. commit·push는 하지 않음
- deep/05-citation/papers.md: 수정 (2026-09-28, Claude Code) — RARR 연도 표기를 "2023"에서 "2022(arXiv) / 2023(ACL)"로 정정. commit·push는 하지 않음
- worklog.md: 오늘 항목 "내가 검토한 것"·"문제와 대처"에 RAGAS 저장소 조직명 변경, RARR 연도 오류 관련 기록 추가 (이 기록)

### 내가 검토한 것

- 출처 확인(2026-09-28, Claude Cowork): 논문 6건의 arXiv 주소를 열어 제목·저자·연도를 대조. RAGAS 저장소 조직명 변경과 RARR 연도 표기 오류를 발견해 수정 지시

### 커밋

-

### Pages URL

- 변경 없음

### 문제와 대처

- 지시문은 deep/README.md와 deep/04-versioning 폴더가 이미 있다고 전제했으나, 이 저장소에는 deep/ 폴더 자체가 없었음(git log·작업 폴더 모두 확인). → deep/04-versioning 이름 변경은 건너뛰고, deep/README.md는 "고치는" 대신 지시받은 두 주제로 새로 만듦. 사람에게 이 사실을 알림.
- deep/05-citation/tools.md의 RAGAS 저장소 URL(explodinggradients/ragas)이 vibrantlabsai/ragas로 조직명이 바뀌어 있었음 → 새 주소로 교체하고, 저장소 주소도 확인 날짜와 함께 적어야 한다는 점을 표 아래에 남김
- deep/05-citation/papers.md의 RARR 연도를 "2023"으로만 적었으나 arXiv 제출은 2022년 10월, ACL 발표는 2023년으로 갈림 → "2022(arXiv) / 2023(ACL)"로 정정

### 다음 작업

- deep/05-citation 실험 실행(MiniCheck로 questions.md 5개 질문 확인)
- deep/07-graphrag 도구 3개 중 하나 선택

## 2026-09-29

### 목표

deep/05-citation 실험 재료로 산업안전보건법 조문을 국가법령정보센터에서 받아 저장 + 실험 설계 파일(design-01.md) 작성

### 시작·종료 시각

- 시작: 2026-09-29 09:20경
- 종료: 2026-09-29 09:26경

### 환경

- macOS, Claude Code 데스크톱 (Claude 내장 브라우저로 국가법령정보센터 페이지를 열어 본문 텍스트를 가져옴)

### Claude Code에 준 지시

1. 국가법령정보센터 산업안전보건법 본문 페이지(URL은 아래 데이터 출처 참고)를 가져올 것. commit·push는 하지 않음.
2. 거기서 제2조(정의), 제15조~제17조, 제36조~제42조만 뽑아 deep/05-citation/data/sanan-law.md로 저장.
3. 파일 맨 위에 출처·시행일·법률 번호·URL·수집일·범위를 적은 머리말을 넣고, 조 번호·조 제목·항 번호(①②③)·호 번호는 원문 그대로 유지. 사이트 메뉴·버튼 문구·별표·서식 링크는 빼고, 본문을 요약·수정하지 않고 그대로 옮김.
4. 저장 후 실제로 들어간 조문 번호 목록과, 조문별 다른 조문 참조 표현 개수를 확인해 상위 5개를 보고.
5. worklog.md에 오늘 항목을 만들어 이번 작업, 데이터 출처, 수집 방법을 기록.
6. deep/05-citation/questions.md, data/sanan-law.md, deep/README.md를 먼저 읽고 deep/05-citation/experiments/design-01.md 작성: 실험 목적, 재료(출처·시행일 포함), 질문 5개(Q1 단일 조항, Q2 상호참조 1단계, Q3 상호참조 2단계, Q4 다른 법률로 넘어감, Q5 없는 내용 — 각각 무엇을 보려는지·기대 답·기대 근거 조항), 측정 방법 표 틀(값은 비움), 판정 기준, 아직 안 정한 것. 기대 답은 저장된 원문에서 확인한 내용만 쓰고 원문에 없으면 "문서에 없음"으로 표시. worklog.md 오늘 항목에 기록.
7. deep/05-citation/data.md를 deep/05-citation/data-plan.md로 이름 변경(같은 폴더의 data/ 폴더와 구분). 저장소 전체에서 이 파일을 가리키는 링크가 있으면 새 이름으로 수정. worklog.md 오늘 항목에 기록.
8. deep/05-citation/experiments/design-01.md와 tools.md를 먼저 읽고, design-01.md의 "[6] 아직 안 정한 것"을 "[6] 실행 방법"으로 바꿔 답 생성 모델·인용 강제 프롬프트·판정 방법·실행 순서를 채움. worklog.md 오늘 항목에 기록.
9. deep/05-citation/data/sanan-law.md와 experiments/design-01.md를 읽고, design-01.md [6]의 인용 강제 프롬프트를 그대로 적용해 Q1~Q5에 답함(design-01.md의 기대 답을 먼저 보지 않고 sanan-law.md만 근거로 답을 만든 뒤, 기록 단계에서 기대 답과 비교). deep/05-citation/experiments/results-01.md를 만들어 질문·기대 답·기대 근거 조항·실제 답변 전문·실제 인용 조항·조항 일치·사람 판정(빈칸)·자동 판정(빈칸)·메모를 지정된 형식으로 기록. 답변은 요약하거나 고치지 않고 그대로 남김. worklog.md 오늘 항목에 기록.

### 읽은 파일

- AGENTS.md
- README.md
- worklog.md
- deep/05-citation/questions.md
- deep/05-citation/data/sanan-law.md
- deep/README.md
- deep/05-citation/experiments/design-01.md
- deep/05-citation/tools.md
- deep/05-citation/data/sanan-law.md (재확인, 답변 생성 전)
- deep/05-citation/experiments/design-01.md (재확인, 프롬프트 문구 확인)

### 만든·고친 파일

- deep/05-citation/data/sanan-law.md: 만듦. 국가법령정보센터 산업안전보건법(시행 2026. 8. 1., 법률 제21374호) 본문 페이지를 Claude 내장 브라우저로 열어 제2조, 제15조~제17조, 제36조~제42조를 그대로 옮김. 요약·수정 없음. 출처·시행일·법률번호·URL·수집일·범위를 머리말에 기록
- worklog.md: 2026-09-29 항목 추가 (이 기록)
- deep/05-citation/experiments/design-01.md: 만듦. Q1~Q5 각각의 기대 답·기대 근거 조항을 sanan-law.md 원문과 대조해 적음(지어내지 않음). 측정 방법 표는 틀만 만들고 값은 비움. commit·push는 하지 않음
- worklog.md: 2026-09-29 항목에 실험 설계 파일 작성 기록 추가 (이 기록)
- deep/05-citation/data.md → deep/05-citation/data-plan.md: 이름 변경 (2026-09-29, Claude Code) — 같은 폴더의 data/ 폴더(법령 원문)와 헷갈려서 데이터 수집 계획 문서만 data-plan.md로 구분함. 저장소 전체를 검색했으나 이 파일을 가리키는 마크다운 링크는 없었음(deep/README.md는 05-citation/ 폴더 단위로만 링크). 파일 내용은 그대로. commit·push는 하지 않음
- worklog.md: 2026-09-29 항목에 data.md → data-plan.md 이름 변경 기록 추가 (이 기록)
- deep/05-citation/experiments/design-01.md: 수정 (2026-09-29, Claude Code) — "[6] 아직 안 정한 것"을 "[6] 실행 방법"으로 바꾸고, 답 생성 모델(Claude Code, 한계 포함)·인용 강제 프롬프트 문구·판정 방법(사람 1차, MiniCheck 2차)·실행 순서(results-01.md 기록)를 채움. commit·push는 하지 않음
- worklog.md: 2026-09-29 항목에 design-01.md [6] 채운 기록 추가 (이 기록)
- deep/05-citation/experiments/results-01.md: 만듦. design-01.md [6]의 인용 강제 프롬프트로 Q1~Q5에 답하고, sanan-law.md 원문 대조 결과 조항 일치는 맞음 4개(Q1~Q4)·일부 1개(Q5)로 나옴. 사람 판정·자동 판정 칸은 비워 둠. commit·push는 하지 않음
- worklog.md: 2026-09-29 항목에 실험 실행(results-01.md) 기록 추가 (이 기록)

### 데이터 출처와 수집 방법

- 출처: 국가법령정보센터, 산업안전보건법 [시행 2026. 8. 1.] [법률 제21374호, 2026. 2. 19., 일부개정]
- URL: https://www.law.go.kr/LSW//lsInfoP.do?lsiSeq=283449&chrClsCd=010202&urlMode=lsInfoP&efYd=20260801&ancYnChk=0
- 수집 방법: Claude 내장 브라우저(Claude Browser)로 위 URL을 열어 페이지의 본문 텍스트를 가져온 뒤, 사이트 메뉴·부처 연락처·조문 목차 등 본문이 아닌 부분을 제외하고 제2조·제15조~제17조·제36조~제42조 구간만 그대로 추출
- 수집일: 2026-09-29
- IATF 내규 원문은 이 작업에 쓰지 않았고, 이번에 받은 자료는 공개된 법령 원문이라 저장소에 그대로 저장함

### 내가 검토한 것

-

### 커밋

-

### Pages URL

- 변경 없음

### 문제와 대처

-

### 다음 작업

- deep/05-citation 실험 재료로 EU AI Act 발췌 추가
- results-01.md 사람 판정 채우기 (에드워드)
- MiniCheck 설치 후 results-01.md 자동 판정 채우기
- Q5(조항 일치 "일부")처럼 "없음" 답변에 근거 조항을 붙이는 방식이 맞는지 findings에 정리

## 2026-10-04

### 목표

deep/05-citation 실험 결과(results-01.md)에 사람 판정 기록 + 실험 코드 규칙을 AGENTS.md에 추가 + 층위 1 자동 판정(조항 번호 실재 여부) 스크립트 작성·실행 + 층위 2 판정 쌍 파일(pairs-01.md) 작성 + MiniCheck 설치(성공)·층위 2 실행 시도(실패, accelerate 없음)

### 시작·종료 시각

- 시작:
- 종료:

### 환경

- macOS, Claude Code 데스크톱

### Claude Code에 준 지시

1. results-01.md의 Q1~Q5 "사람 판정" 칸을 사용자가 정해 준 문장으로 채움. commit·push는 하지 않음.
2. "## 요약" 아래에 "사람 판정 요약"(맞음 4건·일부 1건, 발견한 오류 1건, 판정자, 확인 방법)을 추가.
3. 같은 위치에 "이번 오류의 성격" 항목을 추가(지금까지의 출처 문제와 달리, 실재하는 조항의 내용을 잘못 설명한 오류).
4. worklog.md에 오늘 항목을 만들어 이번 작업을 기록하고, "내가 검토한 것"에 사람 판정 수행 사실과 발견한 오류를 적음.
5. AGENTS.md "작업 방식"에 실험 코드 예외 규칙(deep/<영역>/experiments/scripts/, 영문 소문자·하이픈 파일명)을 추가하고, 맨 아래에 "## 실험 코드" 절(코드 위치, 맨 위 주석, 결과는 .md로 기록, 자동 판정과 사람 판정 열 분리, 도구 설치 기록, 공개 금지 적용)을 추가. 코드를 만들기 전에 규칙부터 고치는 것. worklog.md 오늘 항목에 기록. commit·push는 하지 않음.

6. 새 "## 실험 코드" 규칙에 따라 deep/05-citation/experiments/scripts/check-article-numbers.py 작성(표준 라이브러리만 사용, 맨 위 한국어 주석에 하는 일·입력·출력). 입력은 data/sanan-law.md와 experiments/results-01.md, 출력은 experiments/results-01-layer1.md. 발췌본에서 조·항·호 목록을 만들고, results-01.md 각 Q의 "실제 인용 조항:" 줄을 개별 (조, 항, 호)로 펼쳐 "실재함 / 발췌 범위 밖 / 다른 법률 / 파싱 실패"로 판정. 규칙에 안 맞는 표기는 조용히 버리지 않고 파싱 실패로 출력. results-01.md의 사람 판정·자동 판정 칸은 건드리지 않음. 실제로 실행해 터미널 출력을 보고, 결과가 예상과 다르면 코드를 고치기 전에 먼저 보고. commit·push는 하지 않음.
7. 이 작업을 기록하고, "다음 작업"의 "MiniCheck 자동 판정 코드" 줄을 "자동 판정을 두 층위로 나눔" 문장으로 고침.
8. deep/05-citation/experiments/pairs-01.md를 사용자가 준 내용 그대로 새로 만듦(한 글자도 바꾸지 않음). 번역문은 사람이 원문과 대조해 확정한 것이라 다듬거나 교정하지 않고, P1·P2·P8의 claim_en은 의도적으로 원문과 다른 서술이므로 그대로 둠. P3·P8의 "(same as P2)"도 스크립트가 P2 값을 가져다 쓰도록 그대로 둠. commit·push는 하지 않음.

9. 층위 2 자동 판정을 MiniCheck로 돌림. (1) 저장소 밖 가상환경 ~/.venvs/minicheck를 만들고 `pip install "minicheck @ git+https://github.com/Liyan06/MiniCheck.git@main"`로 설치([llm] 추가 의존성은 설치하지 않음), 모델 가중치는 저장소 안에 두지 않고 cache_dir=~/.cache/minicheck-ckpts 사용, .gitignore에 ckpts/ 와 *.pt 추가. 설치 명령·성공 여부·실패 시 오류 문구를 기록하고 실패하면 멈추고 보고. (2) deep/05-citation/experiments/scripts/run-minicheck.py 작성: 입력 pairs-01.md, 출력 results-01-layer2.md, "(same as P2)"는 P2 값 사용, flan-t5-large, scorer.score로 전체 쌍 한 번에 판정, 쌍별 자동 판정·확률·사람 판정·일치 여부 표와 갈린 쌍·한계 절 포함. results-01.md 사람 판정 칸과 pairs-01.md의 human 값은 건드리지 않음. 실행해 터미널 출력을 보고하고, 예상과 다른 결과가 나오면 코드를 고치기 전에 먼저 보고. commit·push는 하지 않음.

### 읽은 파일

- deep/05-citation/experiments/results-01.md
- worklog.md (끝부분)
- deep/05-citation/experiments/pairs-01.md (run-minicheck.py 입력, 실행 시 읽음)
- ~/.venvs/minicheck/.../minicheck/minicheck.py, inference.py (설치된 MiniCheck의 실제 API와 장치 설정 확인용, 저장소 밖 파일)
- git status (작업 폴더 상태 확인)
- AGENTS.md
- README.md
- deep/05-citation/data/sanan-law.md (스크립트 입력, 형식 확인 및 실행 시 읽음)
- deep/05-citation/experiments/results-01-layer1.md (스크립트가 만든 출력 확인)

### 만든·고친 파일

- deep/05-citation/experiments/results-01.md: 수정 (2026-10-04, Claude Code) — Q1~Q5 "사람 판정" 칸 채움, "요약" 아래에 "사람 판정 요약"과 "이번 오류의 성격" 추가. 자동 판정 칸과 기존 "조항 일치"·"메모"는 그대로 둠. commit·push는 하지 않음
- worklog.md: 2026-10-04 항목 추가 (이 기록)
- deep/05-citation/experiments/results-01.md: 수정 (2026-10-04, Claude Code) — Q5 메모 끝에 "일부" 판정이 조항 일치(인용 방식 차이)와 사람 판정(내용 오류) 두 층위에서 각각 나왔다는 설명 한 단락 추가. commit·push는 하지 않음
- worklog.md: 2026-10-04 항목에 Q5 메모 추가 기록 (이 기록)
- AGENTS.md: 수정 (2026-10-04, Claude Code) — "작업 방식"에 "실험에 쓰는 코드는 예외로 deep/<영역>/experiments/scripts/ 아래에 둔다…" 줄 추가, 맨 아래에 "## 실험 코드" 절(6개 항목) 추가. commit·push는 하지 않음
- worklog.md: 2026-10-04 항목에 AGENTS.md 실험 코드 규칙 추가 기록 (이 기록)
- deep/05-citation/experiments/scripts/check-article-numbers.py: 만듦 (2026-10-04, Claude Code) — 층위 1 자동 판정 스크립트. 표준 라이브러리만 사용(설치 없음). commit·push는 하지 않음
- deep/05-citation/experiments/results-01-layer1.md: 만듦 (2026-10-04 20:48 실행, Python 3.13.3) — 스크립트 출력. 발췌본 11개 조 파싱 결과와 인용 항목 29건 판정(실재함 21 / 발췌 범위 밖 7 / 다른 법률 1 / 파싱 실패 0). 실행 결과는 코드를 돌리기 전에 예상한 값과 같았음. results-01.md는 읽기만 했고 수정하지 않음. commit·push는 하지 않음
- worklog.md: 2026-10-04 항목에 층위 1 스크립트 작성·실행 기록 추가, "다음 작업" 줄 수정 (이 기록)
- deep/05-citation/experiments/pairs-01.md: 만듦 (2026-10-04, Claude Code) — 층위 2에서 MiniCheck에 넣을 (문서, 주장) 쌍 P1~P8과 번역 원칙. 사용자가 준 내용을 그대로 옮김(수정·교정 없음). commit·push는 하지 않음
- worklog.md: 2026-10-04 항목에 pairs-01.md 작성 기록 추가 (이 기록)
- .gitignore: 만듦 (2026-10-04, Claude Code) — 파일이 없어서 새로 만들고 `ckpts/`, `*.pt`를 추가(모델 가중치가 저장소에 들어가지 않게 함). commit·push는 하지 않음
- deep/05-citation/experiments/scripts/run-minicheck.py: 만듦 (2026-10-04, Claude Code) — 층위 2 자동 판정 스크립트. pairs-01.md 파싱·"(same as P2)" 치환까지는 실행에서 정상 통과했고, 모델을 불러오는 단계에서 실패함(아래 "문제와 대처"). commit·push는 하지 않음
- (만들지 못한 파일) deep/05-citation/experiments/results-01-layer2.md: 스크립트가 모델 불러오기 단계에서 실패해 아직 생성되지 않음
- worklog.md: 2026-10-04 항목에 MiniCheck 설치·실행 시도 기록 추가 (이 기록)

### 내가 검토한 것

- 사람 판정 수행(에드워드): results-01.md의 Q1~Q5 답변을 data/sanan-law.md 원문과 한 건씩 대조해 맞음 4건(Q1~Q4), 일부 1건(Q5)으로 판정
- 발견한 오류 1건(Q5): 인용한 제42조 제2항은 실재하나, 답변이 제1항·제2항을 묶어 "작성·제출·심사"로 설명한 부분이 원문과 다름. 원문 제2항은 건설공사 착공 시 건설안전 분야 자격자의 의견을 들어야 한다는 의견 청취 의무임
- Claude Cowork가 독립적으로 같은 대조를 수행해 동일한 결과를 냄(사용자가 전한 내용)

### 커밋

-

### Pages URL

- 변경 없음

### 문제와 대처

- Q5 답변이 제42조 제2항의 내용을 잘못 설명함(인용 조항 번호는 실재) → 사람 판정 칸과 "이번 오류의 성격"에 그대로 기록하고 답변 본문은 고치지 않음(틀린 답도 실험 결과로 보존). 자동 판정기가 같은 조 안의 다른 항 내용과 섞어 "뒷받침됨"으로 볼 가능성이 있어, MiniCheck 자동 판정 때 사람 판정과 갈리는지 확인할 예정
- 05 심화 실험에 파이썬 코드를 쓰게 되면서, AGENTS.md의 "모든 문서는 Markdown(.md)으로 쓴다" 규칙이 코드 파일이라는 새 상황을 담지 못함 → 코드를 만들기 전에 규칙부터 고침(코드 위치·파일명 예외, "## 실험 코드" 절 추가). 코드 파일은 아직 만들지 않음

### MiniCheck 설치·실행 기록

- 가상환경: ~/.venvs/minicheck (저장소 밖, 파이썬 3.13.3, 용량 약 1.1GB)
- 설치 명령: `python3 -m venv ~/.venvs/minicheck` → `pip install "minicheck @ git+https://github.com/Liyan06/MiniCheck.git@main"`
- 설치 결과: 성공(종료 코드 0), pip install 약 88초(2026-10-04 21:02:51 ~ 21:04:19 +0900). minicheck 0.1.0, torch 2.14.1, transformers 5.18.0 등이 함께 설치됨. pip 업데이트 안내(25.0.1 -> 26.2.1)는 오류가 아님
- 실행 명령: `~/.venvs/minicheck/bin/python deep/05-citation/experiments/scripts/run-minicheck.py`
- 실행 결과: 실패(종료 코드 1). 모델을 불러오는 `MiniCheck(model_name='flan-t5-large', cache_dir=...)` 단계에서 오류. 모델 가중치는 아직 내려받기 전이라 ~/.cache/minicheck-ckpts는 12KB
- 오류 문구(마지막 줄 그대로): `ValueError: Using a `device_map`, `tp_plan`, `torch.device` context manager or setting `torch.set_default_device(device)` requires `accelerate`. You can install it with `pip install accelerate``
- 원인: 설치된 minicheck의 inference.py가 `from_pretrained(..., device_map="auto")`를 쓰는데, 지시한 설치 명령으로는 `accelerate` 패키지가 함께 설치되지 않음
- 디스크 여유: 설치 후 약 7.2GiB(모델 가중치 약 3GB 예정)

### 다음 작업

- accelerate 설치 여부를 사람이 결정(지시한 설치 명령 밖의 추가 설치라 먼저 보고) → 승인되면 설치 후 run-minicheck.py 다시 실행해 results-01-layer2.md 생성
- 자동 판정을 두 층위로 나눔: 층위 1 조항 번호 대조(규칙 기반, 한국어 그대로) → 층위 2 MiniCheck 내용 뒷받침 판정(영어 번역 쌍 필요)
- deep/05-citation 실험 재료로 EU AI Act 발췌 추가
- MiniCheck 설치 후 results-01.md 자동 판정 채우기
- 자동 판정과 사람 판정이 갈리는 질문(특히 Q5) 정리 → findings 작성
- "없음" 답변에 근거 조항을 붙이는 방식이 맞는지 findings에 정리

## 2026-10-05

### 목표

MiniCheck 경로를 접고 설치물 정리, 한국어 원문 판정 쌍(pairs-01-ko.md)과 판정 서브에이전트(citation-judge) 준비, 층위 2 판정 실행

### 시작·종료 시각

- 시작:
- 종료:

### 환경

- macOS, Claude Code 데스크톱 (Claude Code 2.1.274), Python 3.13.3

### Claude Code에 준 지시

1. [A] MiniCheck 설치물 정리(저장소 밖만): 지우기 전에 용량 측정 → `~/.venvs/minicheck`, `~/.cache/minicheck-ckpts`만 삭제(삭제는 에드워드가 승인) → 여유 용량 보고. `~/.cache/pip`은 지우지 않고 용량만 보고. 저장소 안 파일은 지우지 않고 run-minicheck.py와 pairs-01.md에 "[미사용 기록]" 머리말만 붙임.
2. [B] pairs-01-ko.md를 지정한 내용 그대로 만듦(조문 원문은 적지 않고 data/sanan-law.md에서 뽑아 씀).
3. [C] .claude/agents/citation-judge.md 만들기(프런트매터 형식은 Claude Code가 기대하는 형식을 확인해 맞춤).
4. [D] extract-doc-text.py로 조문 원문 8개를 뽑아 확인 → 쌍마다 citation-judge를 한 번씩(총 8회) 호출. 서브에이전트에는 조문 원문과 claim_ko만 넘기고 human·hypothesis·P 번호는 넘기지 않음. 판정이 끝난 뒤에 human과 비교. P8이 "뒷받침됨"이거나 P5가 "뒷받침 안 됨"이면 결과 파일을 쓰지 않고 즉시 보고.
5. [E] results-01-layer2.md 작성, results-01.md "자동 판정" 칸에 "층위 1: 값 / 층위 2: 값" 기록(사람 판정 칸·pairs의 human 값은 건드리지 않음).
6. [F] worklog에 2026-10-05 항목 기록. commit·push는 하지 않음.
7. (세 번째 세션) 층위 2 자동 판정 마무리: extract-doc-text.py 실행 → citation-judge 8회 호출(조문 원문과 claim_ko만 넘김) → 중단 조건(P8 뒷받침됨, P5 뒷받침 안 됨) 확인 → 8개가 끝난 뒤 human과 비교 → results-01-layer2.md 작성(판정 방식, 도구 수준 격리 설계, 세 번째 세션에서야 실행된 경위, 조문 원문 8개, 판정 표, 갈린 쌍, P1·P2 비교, 한계 3개) → results-01.md "자동 판정" 칸을 "층위 1: 값 / 층위 2: 값"으로 채움 → worklog에 판정 실행과 "반복 작업 자동화" 기록. citation-judge.md 프런트매터는 고치지 않음. commit·push는 하지 않음.
8. (실험 02 첫 지시) P7 불일치가 근거를 자른 범위 때문인지 확인: pairs-02-ko.md에 P9(제15조 제1항 본문+제1호) 작성 → extract-doc-text.py가 "본문"을 처리하게 고치고 실행해 뽑힌 원문을 먼저 보고 → P7·P9 각 3회 판정 → results-02.md 작성. 원문 보고 단계에서 P9 가설과 원문이 어긋나 판정 전에 멈추고 보고함(아래 "문제와 대처").
9. (실험 02 수정 지시) pairs-02-ko.md의 P9 hypothesis 교체, P10(제15조 제목+제1항 본문+제1호) 추가, 설계 원칙에 "판정 전에 가설을 고쳤다" 한 줄 추가 → extract-doc-text.py가 "제목"을 처리하게 고침 → 원문 세 개 확인 → citation-judge를 P7·P9·P10 각 3회(총 9회) 호출(앞선 결과·human·hypothesis는 넘기지 않음) → results-02.md 작성 → worklog 기록. commit·push는 하지 않음.
10. (findings) deep/05-citation/findings.md 작성: 지정한 파일에 적힌 것만 쓰고, 숫자는 파일에서 가져오며, 새 주장·해석을 보태지 않음. 지정한 절 구성(한 줄 결론 ~ 남은 질문, 끝에 상대 경로 링크). deep/README.md에 findings 링크 추가. worklog 기록. commit·push는 하지 않음.
11. (실험 03) 실험 02에서 조 제목이 판정을 뒤집은 이유를 좁힘: pairs-02-ko.md P9 hypothesis 아래에 correction 줄 추가(가설 원문은 그대로) → pairs-03-ko.md에 P11(제1항 본문+제1호+제2항), P12(…+제3항) 작성 → extract-doc-text.py로 원문 추출·가설 전제 확인, pairs-01·02 출력 불변 확인 → citation-judge P11·P12 각 3회(총 6회)를 한 건씩 순서대로 호출 → results-03.md 작성 → findings.md 갱신(발견 2, 한계 6·7, 설계 규칙 2, 남은 질문) → worklog 기록. commit·push는 하지 않음.
12. (07 계획서, 실제 작업 시각 2026-10-06 08:53 무렵부터) deep/07-graphrag/plan.md를 "MBB 공개 리포트로 산업 × 펌별 관점 비교 그래프" 계획으로 다시 씀(지정한 9개 절). 사람이 확인한 서지 정보는 그대로 쓰고 URL이 열리는지 확인해 확인 날짜를 붙임. arXiv:2506.05690은 열어서 제목·저자·날짜가 맞을 때만 넣음. 준 적 없는 논문·수치·인용은 만들지 않음. deep/README.md 07 항목에 plan.md 링크 확인·추가. worklog 2026-10-05 항목에 기록(지시대로). commit·push는 하지 않음.

### 읽은 파일

- .claude/settings.local.json (기존 설정 확인)
- deep/05-citation/data/sanan-law.md, deep/05-citation/experiments/pairs-01-ko.md (extract-doc-text.py가 입력으로 읽음)
- https://code.claude.com/docs/en/sub-agents (서브에이전트 정의 파일 형식과 로드 시점 확인, 확인일 2026-10-05)
- (세 번째 세션) AGENTS.md, README.md, worklog.md, .claude/agents/citation-judge.md, deep/05-citation/experiments/scripts/extract-doc-text.py, deep/05-citation/experiments/pairs-01-ko.md, deep/05-citation/experiments/results-01.md, deep/05-citation/experiments/results-01-layer1.md, deep/05-citation/data/sanan-law.md(extract-doc-text.py가 입력으로 읽음)
- (findings) deep/05-citation/experiments/design-01.md, results-01.md, results-01-layer1.md, results-01-layer2.md, pairs-01-ko.md, pairs-02-ko.md, results-02.md, deep/05-citation/tools.md, questions.md, data-plan.md, key-contexts.md, areas/02-document-parsing-chunking.md, areas/05-citation-grounding.md, areas/06-rag-evaluation.md, deep/README.md, field-map.md(링크 확인), deep/05-citation/data/sanan-law.md(제15조에서 "안전보건관리책임자" 위치 확인)
- (07 계획서) deep/07-graphrag/plan.md(고치기 전), papers.md, tools.md, areas/07-graphrag.md, deep/README.md, worklog.md
- (07 계획서, 웹, 확인 2026-10-06) https://arxiv.org/abs/2404.16130 , https://arxiv.org/abs/2410.05779 , https://arxiv.org/abs/2506.05690 , https://github.com/HKUDS/LightRAG , https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/ , https://github.com/neo4j-labs/llm-graph-builder , https://github.com/microsoft/graphrag
- (실험 03) deep/05-citation/experiments/pairs-02-ko.md, pairs-03-ko.md·pairs-01-ko.md(스크립트 입력), deep/05-citation/data/sanan-law.md(스크립트 입력), deep/05-citation/findings.md, worklog.md
- (실험 02) deep/05-citation/experiments/scripts/check-article-numbers.py(parse_ref 확인), deep/05-citation/data/sanan-law.md(제15조 확인, 스크립트 입력), deep/05-citation/experiments/pairs-02-ko.md·pairs-01-ko.md(스크립트 입력), worklog.md

### 만든·고친 파일

- deep/05-citation/experiments/scripts/run-minicheck.py: 수정 (2026-10-05, Claude Code) — 맨 위에 "[미사용 기록]" 주석 머리말 추가(지우지 않음). commit·push는 하지 않음
- deep/05-citation/experiments/pairs-01.md: 수정 (2026-10-05, Claude Code) — 제목 아래에 "[미사용 기록]" 인용 블록 추가(지우지 않음). commit·push는 하지 않음
- deep/05-citation/experiments/pairs-01-ko.md: 만듦 (2026-10-05, Claude Code) — 한국어 판정 쌍 P1~P8과 설계 원칙. 지정한 내용 그대로, 조문 원문은 적지 않음. commit·push는 하지 않음
- .claude/agents/citation-judge.md: 만듦 (2026-10-05, Claude Code) — 조문과 주장 한 쌍의 뒷받침 여부만 판정하는 서브에이전트. 지정한 name·description·규칙을 그대로 넣고, 프런트매터에 `disallowedTools: Read, Glob, Grep, Bash, Edit, Write, NotebookEdit`를 추가함(저장소 파일을 읽지 말라는 규칙을 도구 수준에서도 막으려는 추가이며, 지시에 없던 항목). commit·push는 하지 않음
- deep/05-citation/experiments/scripts/extract-doc-text.py: 만듦 (2026-10-05, Claude Code) — pairs-01-ko.md의 doc_ref에 해당하는 조문 원문을 sanan-law.md에서 뽑아 화면에 출력. check-article-numbers.py의 parse_law·parse_ref·judge를 재사용하고, 조문 자르기 결과가 parse_law와 같은지 실행 때마다 검사함. 표준 라이브러리만 사용. 실행 결과 8개 쌍의 원문이 모두 정상 추출됨. commit·push는 하지 않음
- (지움, 저장소 밖) ~/.venvs/minicheck, ~/.cache/minicheck-ckpts: 삭제 (2026-10-05, 에드워드 승인). 아래 "정리 기록" 참고
- (만들지 못한 파일, 앞선 두 세션) deep/05-citation/experiments/results-01-layer2.md, results-01.md의 "자동 판정" 칸: 판정이 실행되지 않아 만들지 않음·채우지 않음 → 세 번째 세션에서 아래 두 줄로 처리함
- deep/05-citation/experiments/results-01-layer2.md: 만듦 (2026-10-05, Claude Code) — citation-judge 8회 판정 결과. 일치 7, 불일치 1(P7). commit·push는 하지 않음
- deep/05-citation/experiments/results-01.md: 수정 (2026-10-05, Claude Code) — Q1~Q5 "자동 판정" 칸만 "층위 1: 값 / 층위 2: 값"으로 채움. "사람 판정" 칸과 pairs-01-ko.md의 human 값은 건드리지 않음. commit·push는 하지 않음
- worklog.md: 2026-10-05 항목에 판정 실행·반복 작업 자동화 기록 추가 (이 기록)
- deep/05-citation/experiments/pairs-02-ko.md: 만듦 (2026-10-05, Claude Code) — 실험 02 판정 쌍. P9를 지정한 내용대로 넣고, 뒤이은 지시로 P9 hypothesis 교체, P10 추가, 설계 원칙에 판정 전 가설 수정 한 줄 추가. commit·push는 하지 않음
- deep/05-citation/experiments/scripts/extract-doc-text.py: 수정 (2026-10-05, Claude Code) — (1) "제○항 본문"(항 표시부터 첫 호 줄 전까지, 조 제목 제외) 처리, (2) "제○조 제목"(조 첫 줄의 "제○조(제목)" 부분) 처리, (3) "+제1호"처럼 호만 적힌 뒤쪽 표기가 앞쪽의 조·항을 이어받게 함, (4) 첫 인자로 쌍 파일을 받게 함(기본값 pairs-01-ko.md). 맨 위 주석도 고침. 수정 뒤 pairs-01-ko.md 출력이 수정 전과 같은지 diff로 확인함(차이 없음). commit·push는 하지 않음
- deep/05-citation/experiments/results-02.md: 만듦 (2026-10-05, Claude Code) — 실험 02 결과(P7·P9·P10 각 3회 판정). commit·push는 하지 않음
- worklog.md: 2026-10-05 항목에 실험 02 기록 추가 (이 기록)
- deep/05-citation/findings.md: 만듦 (2026-10-05, Claude Code) — 05 심화 결론 문서. 발견 4개, 통제군, 빗나간 가설, 한계 7개, 출발 질문에 주는 답(설계 규칙 3개), 1차 과제와의 연결(확인한 것/못한 것), 남은 질문(실험 3개). commit·push는 하지 않음
- deep/README.md: 수정 (2026-10-05, Claude Code) — 05 절에 findings.md 링크 한 줄 추가. commit·push는 하지 않음
- worklog.md: 2026-10-05 항목에 findings 작성 기록 추가 (이 기록)
- deep/05-citation/experiments/pairs-02-ko.md: 수정 (2026-10-05, Claude Code) — P9 hypothesis 바로 아래에 지정한 correction 줄 추가. 가설 원문은 사전 등록 기록으로 그대로 둠. extract-doc-text.py는 KEYS에 없는 줄을 읽지 않으므로 출력에 영향 없음(확인함). commit·push는 하지 않음
- deep/05-citation/experiments/pairs-03-ko.md: 만듦 (2026-10-05, Claude Code) — 실험 03 판정 쌍 P11·P12. 지정한 내용 그대로. commit·push는 하지 않음
- deep/05-citation/experiments/results-03.md: 만듦 (2026-10-05, Claude Code) — 실험 03 결과(P11·P12 각 3회 순차 판정). commit·push는 하지 않음
- deep/05-citation/findings.md: 수정 (2026-10-05, Claude Code) — 발견 2에 P11·P12 반영, 한계 6을 실험 03 결과로 갱신(확인 필요 해소, 범위 제한은 남김), 한계 4·5·7 갱신, 설계 규칙 2 보강, 남은 질문 정리. 지시 범위 밖이지만 일관성을 위해 "무엇을 했나"에 실험 03 문단, "빗나간 가설"에 correction 줄 반영과 P11·P12 결과, "1차 과제와의 연결"에 P11, 맨 아래 링크에 실험 03 추가. commit·push는 하지 않음
- extract-doc-text.py: 고치지 않음. "제15조 제1항 본문+제1호+제2항"과 "…+제3항"은 실험 02에서 넣은 코드("+" 뒤 항 표기는 앞쪽 조를 이어받음)로 처리됐음
- worklog.md: 2026-10-05 항목에 실험 03 기록 추가 (이 기록)
- deep/07-graphrag/plan.md: 다시 씀 (2026-10-06, Claude Code) — 기존 내용(주제·참고 자료·활용처·수집·개체 관계·질문 3개)을 지정한 9개 절로 바꿈. 기존에 있던 펌별 연구 조직 링크 3개와 papers.md 링크는 새 구성에 없어 넣지 않음. commit·push는 하지 않음
- deep/README.md: 수정 (2026-10-06, Claude Code) — 07 항목에 plan.md 링크가 없어 한 줄 추가. commit·push는 하지 않음
- worklog.md: 2026-10-05 항목에 07 계획서 작성 기록 추가 (이 기록)
- worklog.md: 2026-10-05 항목 추가 (이 기록)
- .gitignore: 수정 (2026-10-05, Claude Code) — `.claude/settings.local.json`, `.venv/` 두 줄 추가. 개인 권한 설정 파일을 gitignore에 넣어 공개 대상에서 제외했다. commit·push는 하지 않음

### 정리 기록 (용량)

- 지우기 전 용량: ~/.venvs/minicheck 1.1GB, ~/.cache/minicheck-ckpts 12KB
- ~/.cache/pip: 이 경로는 없음. macOS의 pip 캐시는 ~/Library/Caches/pip이고 728MB(다른 파이썬 작업과 공유되므로 지우지 않음)
- df -h / : 사용 가능 5.5Gi(사용률 68%) → 삭제 후 6.7Gi(64%). 데이터 볼륨(df -h ~)은 5.5Gi(98%) → 6.7Gi(97%). 확보된 여유는 약 1.2GiB
- 참고: 10/4 설치 직후에는 7.2GiB였는데 오늘 삭제 전에 5.5GiB로 줄어 있었음(그 사이 MiniCheck와 무관한 다른 사용분)
- 모델 가중치는 내려받기 전에 중단했다. 실제로 용량을 쓴 것은 torch·transformers가 들어간 가상환경(1.1GB)이었고, 가중치 폴더는 12KB뿐이었다.

### 내가 검토한 것

- 삭제 승인(에드워드): 위 두 경로의 삭제를 승인함. 저장소 안 파일은 지우지 않기로 함
- run-minicheck.py와 pairs-01.md를 지우지 않고 머리말만 붙여 남기기로 판단. 근거는 AGENTS.md "## 실험 코드"의 규칙(설치가 필요한 도구는 설치 명령, 성공·실패 여부, 실패 시 오류 문구를 .md에 남긴다)이며, 실패한 경로도 시도 기록으로 남겨야 한다고 봄

### 커밋

-

### Pages URL

- 변경 없음

### 문제와 대처

- 서브에이전트 호출 실패: `Agent type 'citation-judge' not found. Available agents: claude, claude-code-guide, Explore, general-purpose, Plan, statusline-setup`. 원인은 .claude/agents/ 폴더가 이번 세션 시작 때 없었기 때문임. 공식 문서(확인 2026-10-05)에 새 agents 폴더의 첫 파일은 재시작해야 로드된다고 적혀 있음. → [D-2]의 판정 호출 8회를 한 번도 실행하지 못했고(0/8), 임의로 general-purpose 등 다른 에이전트로 바꿔 돌리지 않고 멈춰서 보고함. [D-3] 중단 조건(P8, P5)에 해당한 것은 아님
- ~/.cache/pip 경로가 없어 지시한 용량 측정 대상이 비어 있음 → 실제 pip 캐시 위치(~/Library/Caches/pip)를 찾아 용량만 보고하고 지우지 않음
- 재시도(2026-10-05 09:50): [D-2]를 이어서 하려고 extract-doc-text.py를 다시 실행해 8개 쌍의 조문 원문을 얻었으나(정상), citation-judge 호출은 같은 오류(`Agent type 'citation-judge' not found. Available agents: claude, claude-code-guide, Explore, general-purpose, Plan, statusline-setup`)로 실패함. 판정 호출 0/8. 진단: 프런트매터는 name·description·disallowedTools 세 줄로 형식이 맞고, 설치된 Claude Code 2.1.274 실행 파일에 disallowedTools 필드명이 들어 있으며 공식 문서에도 지원 필드로 적혀 있어 disallowedTools가 원인일 가능성은 낮다고 봄(파일이 실제로 파싱되는지는 직접 확인하지 못함). 에이전트 목록이 앞선 시도와 같은 것으로 보아, .claude/agents/가 만들어진(09:40:54) 뒤에 세션이 새로 시작되지 않은 것으로 판단함. 프런트매터는 바꾸지 않았고 결과 파일도 쓰지 않음 → 사람에게 보고
- 세 번째 세션(2026-10-05 10:01 무렵): Claude Code를 새로 시작한 세션에서 citation-judge가 에이전트 목록에 나타났고 8회 호출이 모두 성공함(8/8, 서브에이전트 도구 사용 0회). 프런트매터는 고치지 않았으므로, 앞선 실패는 .claude/agents/ 폴더를 새로 만든 뒤 재시작하지 않았기 때문이라는 진단과 맞음. 공식 문서 문구: "New agents directories require a restart"(https://code.claude.com/docs/en/sub-agents , 확인 2026-10-05). 기존 대화를 이어가는 것은 재시작에 해당하지 않음
- P9 가설이 원문과 다름(실험 02, 판정 전에 바로잡음): 처음 P9 hypothesis는 "제1항 본문에 주체(안전보건관리책임자)와 의무(총괄하여 관리)가 있다"고 적었음. 이 가설을 쓴 쪽은 사람(Claude Cowork)임. Claude Code가 extract-doc-text.py로 원문을 뽑아 확인하니, 제1항 본문에는 의무("총괄하여 관리하도록 하여야 한다")는 있으나 "안전보건관리책임자"라는 명칭은 없고 조 제목 "제15조(안전보건관리책임자)"에만 있었음. Claude Code는 판정 호출을 하지 않고 멈춰서 어긋남을 보고함. 사람이 P9 hypothesis를 고치고 조 제목을 넣은 P10을 추가한 뒤 판정을 실행함. 가설은 판정 결과를 보기 전에 고쳤음(이 시점까지 P9 판정 호출 0회)
- 에이전트 오류(Claude Code, findings 작성 중 발견): 위 P9 어긋남을 보고할 때 Claude Code는 제1항만 확인하고 "명칭은 조 제목에만 있다"고 보고했고, 이 기록에도 같은 내용("조 제목 … 에만 있었음")을 적었음. findings 작성 중 sanan-law.md 제15조 전체를 확인하니 "안전보건관리책임자"는 조 제목 외에 제2항("이하 "안전보건관리책임자"라 한다", 정의 문장)과 제3항에도 있었음. 이 보고를 바탕으로 고친 pairs-02-ko.md의 P9 hypothesis에도 "명칭은 조 제목에만 있다"가 들어감. 실험 02에 건넨 조각들(제1호, 제1항 본문, 조 제목) 안에서는 맞는 말이라 판정 입력·결과에는 영향이 없음. 대처: findings.md에 정확한 위치를 적고 "빗나간 가설"에 기록함. pairs-02-ko.md의 hypothesis와 이 worklog의 앞선 문장은 기록 보존을 위해 고치지 않고 사람에게 보고함
- findings 지시와 원문이 다른 점: 지시는 발견 2에 "제15조에서 '안전보건관리책임자'가 나오는 곳이 조 제목뿐"이라고 쓰라고 했으나 원문과 달라(위 항목) 그대로 쓰지 않음. 대신 "건넨 조각 안에서는 조 제목에만 있고, 제15조 전체로는 제2항·제3항에도 있다"로 씀. 지시의 출발 질문 규칙 예시("조 제목을 떼면 그 조각으로는 답변을 검증할 수 없다")도 제2항으로 이어 주는 경우를 시험하지 않았으므로 쓰지 않고, 실험 결과로 뒷받침되는 규칙만 씀

### 층위 2 판정 실행 기록

- 실행 시각: 2026-10-05 10:01~10:02 +0900 (extract-doc-text.py 10:01:21 실행, 종료 코드 0)
- 판정자: citation-judge 서브에이전트, 호출 8회(쌍마다 1회, 재실행 없음)
- 넘긴 것: 조문 원문, claim_ko / 넘기지 않은 것: human, hypothesis, P 번호(claim_id, doc_ref도 넘기지 않음)
- 중단 조건: P8 뒷받침 안 됨, P5 뒷받침됨 → 해당 없음
- human과 비교(8개 판정이 끝난 뒤): 일치 7, 불일치 1(P7, 자동 뒷받침 안 됨 / 사람 맞음). P1·P2는 둘 다 뒷받침 안 됨으로 갈리지 않음
- 비교할 때 human "맞음"을 "뒷받침됨"과 같은 쪽으로 봄(pairs-01-ko.md의 human 표기가 두 가지라 정한 대응). results-01-layer2.md에 적어 둠

### 실험 02 실행 기록

- 목적: 실험 01 P7의 불일치(자동 뒷받침 안 됨 / 사람 맞음)가 근거를 자른 범위 때문인지 확인. 같은 주장에 근거를 제1호(P7) → 제1항 본문+제1호(P9) → 조 제목+제1항 본문+제1호(P10)로 넓힘
- 원문 추출: 2026-10-05 10:13:10 +0900, extract-doc-text.py(pairs-01-ko.md, pairs-02-ko.md) 모두 종료 코드 0
- 판정: citation-judge 9회(P7·P9·P10 각 3회), 병렬 호출, 10:13:36 확인 시점에 모두 끝남. 서브에이전트 도구 사용 0회. 넘긴 것은 조문 원문과 claim_ko뿐
- 결과: P7 뒷받침 안 됨 ×3, P9 뒷받침 안 됨 ×3, P10 뒷받침됨 ×3. 쌍마다 3회가 모두 같았음
- 판정이 바뀐 지점: 조 제목을 더한 P9 → P10. 제1항 본문을 더한 P7 → P9에서는 바뀌지 않음

### 실험 03 실행 기록

- 목적: 실험 02에서 조 제목이 판정을 뒤집은 이유가 "명칭이 글자로 들어와서"인지 "명칭과 의무를 잇는 정의가 들어와서"인지 구분. 제목을 빼고 제2항 정의문(P11) 또는 제3항 명칭(P12)을 제1항 본문+제1호에 더함
- 원문 추출: 2026-10-05 10:24:38 +0900, extract-doc-text.py(pairs-03-ko.md) 종료 코드 0. pairs-01-ko.md 출력은 실험 02 때 저장본과 diff 차이 없음, pairs-02-ko.md 출력은 results-02.md의 원문과 같음
- 가설 전제 확인(판정 전): P11 제2항에 정의문 있음, P12 제3항에 명칭만 있고 제1항과 잇는 정의 없음. 둘 다 원문과 맞음
- 판정: citation-judge 6회(P11 3회 → P12 3회), 한 건씩 순서대로 호출(앞 결과가 돌아온 뒤 다음 호출), 10:25:38 확인 시점에 모두 끝남. 서브에이전트 도구 사용 0회. 넘긴 것은 조문 원문과 claim_ko뿐
- 결과: P11 뒷받침됨 ×3, P12 뒷받침 안 됨 ×3. 쌍마다 3회가 모두 같았음. P11·P12 가설은 빗나가지 않음
- 관찰: P11-3과 P12-2의 근거가 한 줄이 아니라 여러 문장이었음(citation-judge 규칙은 한 줄). 판정 값은 두 값 중 하나로 규칙대로였음. results-03.md에 적어 둠

### 07 계획서 확인 기록 (2026-10-06 작업)

- 날짜: 지시는 이 2026-10-05 항목에 기록하고 확인 날짜를 2026-10-05로 붙이라고 했으나, 실제 확인은 2026-10-06 08:53 +0900 이후에 했음. 확인 날짜는 실제 날짜(2026-10-06)로 적음
- URL 확인(7개 모두 열림): arXiv 2404.16130·2410.05779 서지(제목·저자 순서·v1/v2/v3 날짜)는 사람이 준 값과 같음. LightRAG 저장소 제목에 "[EMNLP2025]" 표기 있음. Edge et al. 초록에서 전역 질문·커뮤니티 요약·"1 million token range"·포괄성과 다양성 개선 문구 확인
- arXiv:2506.05690: 제목이 사람이 준 후보와 같음. 저자 Zhishang Xiang, Chuanjie Wu, Qinggang Zhang, Shengyuan Chen, Zijin Hong, Xiao Huang, Jinsong Su, v1 2025-06-06, v3 2026-02-22 → 넣음. 본문은 읽지 않았고 초록 내용만 씀
- 사람이 준 사실과 원문이 다른 점:
  - Neo4j LLM Graph Builder: 지시는 "LLM API 키가 필요하다"였으나, labs 페이지에는 API 키 필요 여부가 명시돼 있지 않음. 저장소 README에는 OpenAI 모델용 키와 함께 Ollama 로컬 모델 설정이 있음 → plan.md에 그대로 적고 "확인 필요"로 둠
  - LightRAG: 지시는 "기본 저장이 파일 기반"이었으나, README는 기본 저장소 4개가 메모리 기반이고 로컬 파일은 저장(persistence)용이라고 적음. 그래프 DB 없이 쓸 수 있다는 점은 같음 → README 표현대로 적음
  - MS GraphRAG: "유료 API 키가 전제"를 직접 적은 문장은 README에서 찾지 못함. README에는 "indexing can be an expensive operation"만 있음 → 사람이 정리한 내용으로 표시하고 지원 모델·로컬 모델은 확인 필요로 둠
- 디스크 여유: 지시의 약 6.7GiB는 2026-10-05 MiniCheck 삭제 직후 값. 2026-10-06 확인 시 `df -h ~` 사용 가능 3.9Gi(99%) → 두 값을 시점과 함께 적음
- 저장소 안의 deep/07-graphrag/papers.md·tools.md는 고치지 않음. tools.md의 LightRAG "필요한 것: LLM API 키"는 README의 로컬 모델 경로와 맞지 않을 수 있음(사람이 판단)

### 설계 기록

- citation-judge로 쌍 8개 판정을 자동화하기로 한 것은 반복 작업 자동화 기록이다. 다만 서브에이전트가 이번 세션에서 로드되지 않아 자동화 자체는 아직 실행하지 못했다.
- 반복 작업 자동화 (세 번째 세션에서 실행): 같은 규칙으로 (조문, 주장) 쌍을 판정하는 일을 citation-judge 서브에이전트 하나로 정의해 두고, 쌍 8개를 같은 정의로 8회 호출해 처리했다. 판정 규칙·출력 형식·도구 제한이 정의 파일 한 곳에 있으므로, 쌍이 늘어나도 호출만 반복하면 되고 판정 조건이 호출마다 달라지지 않는다.
- 판정자에게 사람 판정(human)과 기대 답(hypothesis 등)을 넘기지 않는다. 판정자에게 넘기는 것은 조문 원문과 claim_ko 두 개뿐이고, P 번호도 넘기지 않으며, 비교는 8개 판정이 모두 끝난 뒤에 한다. 서브에이전트 규칙에도 results-01.md, design-01.md, pairs-01-ko.md를 읽지 말라고 적었다. 이렇게 판정자가 정답 쪽 정보를 보지 못하게 해 판정이 오염되는 것을 막는 설계다.

### 다음 작업

- (완료, 세 번째 세션) citation-judge 로드 확인 → 8회 호출 → human과 비교 → results-01-layer2.md 작성, results-01.md "자동 판정" 칸 기록
- 사람이 results-01-layer2.md를 검토(특히 P7 불일치, P3를 "뒷받침됨"으로 본 것, human "맞음"↔"뒷받침됨" 대응)
- 같은 쌍을 여러 번 돌려 판정이 매번 같은지 확인할지 결정(이번에는 쌍마다 1회) → 실험 02에서 P7·P9·P10을 각 3회 돌림(쌍마다 3회 모두 같았음). 실험 01의 나머지 쌍은 아직 1회
- 사람이 results-02.md 검토
- 사람이 findings.md 검토. pairs-02-ko.md P9 hypothesis의 "명칭은 조 제목에만 있다"를 고칠지 결정
- (findings 남은 질문 1) 같은 주장에 제1항 본문+제1호+제2항을 건네 정의 문장으로 이어 줘도 판정이 바뀌는지 확인 → 실험 03에서 완료(P11 뒷받침됨 ×3)
- 사람이 results-03.md와 갱신된 findings.md 검토
- 사람이 07 plan.md 검토. Neo4j·LightRAG·MS GraphRAG 서술 차이(위 "07 계획서 확인 기록") 확인, papers.md·tools.md를 plan.md에 맞춰 고칠지 결정
- 07 1차 범위 산업·주제 정하기 → deep/07-graphrag/data/reports.md 만들기(아직 없음)
- deep/05-citation 실험 재료로 EU AI Act 발췌 추가
- 자동 판정과 사람 판정이 갈리는 질문 정리 → findings 작성

## 2026-10-06

### 목표

실험 04: 개인정보 보호법을 새 입력으로 삼아 05의 절차(원문 추출 → 답변 생성 → 층위 1·2 판정 → 사람 판정과 비교 → 기록)를 그대로 적용하고, 어디까지 재사용되고 어디서 깨지는지 확인

### 시작·종료 시각

- 시작:
- 종료:

### 환경

- macOS, Claude Code 데스크톱, Python 3.13.3

### Claude Code에 준 지시

1. 실험 04 계획만 먼저 제시하고 승인 전에는 파일을 만들지 않음(계획 제시, 파일 만들지 않음).
2. 계획 승인과 결정: (1) 발췌 범위 제2조, 제15조~제18조, 제28조의2~제28조의3 (2) 통제군은 Claude Code가 답변 생성 전에 법령 원문에서 거짓 주장 후보 2~3개를 뽑고 에드워드가 하나 고름 (3) 층위 2는 기본 1회, "뒷받침 안 됨"이 나온 쌍과 통제군만 3회. 이 규칙을 pairs-04-ko.md에 돌리기 전에 적어 둠 (4) 스크립트를 고치기 전 상태를 먼저 보고 (5) settings.local.json은 바꾸지 않고, 메인 세션은 규칙으로만 막혀 있다는 점을 결과 파일 한계에 적음. 추가: [A] Q6 층위 2에서 "뒷받침 안 됨"이 다수 나올 것이라는 예측을 판정 전에 pairs-04-ko.md에 적음 [B] Q6 호 인용 2건만 doc_ref를 "제15조 제1항 본문+해당 호"로 바꾼 짝 비교 쌍 추가. 1단계(원문 수집)부터 하고 구조를 보고한 뒤 멈춤.
3. 1단계 승인. 판(시행일) 건을 privacy-law.md 머리말과 worklog에 기록(Cowork 교차 확인 결과와 출처, 핵심 맥락 2번과의 관계, 시행일이 세 갈래라는 점). 2단계: questions-04.md(기대 답 없이), answer-key-04.md(빈 틀), .claude/agents/answer-writer.md(disallowedTools, 본문 규칙은 design-01.md 인용 강제 프롬프트 그대로) 만들고 에이전트 목록에 뜨는지 확인. 거짓 주장 후보 2~3개 제시. 다 되면 멈추고 보고.
4. (새 세션, 11:02 +0900) 3단계부터 이어서 함. [0] answer-writer 로드 확인, 안 되면 멈추고 다른 에이전트로 대체하지 않음 [1] 로드 건을 관찰한 사실만 기록, 원인은 "확인 필요" [2] 결정 사항 기록(층위 2 human 칸 (b), 통제군 C3, 부분 오류 쌍 C1, C2 안 씀, answer-writer.md 역할 설명 한 줄 유지) [3] 답변 생성은 시작하지 않고 [0]~[2]만 하고 보고. commit·push 하지 않음.
5. (새 세션, 13:17 +0900 시작) 3단계(답변 생성)와 4단계(층위 1). answer-key-04.md는 읽지 않음. [1] answer-writer 실제 호출 확인, 안 되면 멈춤 [2] Q6·Q7 각 1회(총 2회), 넘기는 것은 발췌 원문과 질문 하나, 답변과 답변 끝 조항 목록을 글자 그대로 results-04.md에 옮김 [3] check-article-numbers.py를 고치지 않고 새 입력에 돌려 깨지는 모습과 오류 문구를 기록, 돌린 뒤 멈춤 [4] results-04.md와 worklog 기록. 스크립트 고치기, commit·push 하지 않음.
6. (같은 세션, 13:30경) 층위 1 스크립트를 새 입력에서도 돌아가게 고침. 방법은 Claude Code가 정함. 완료 기준 7개(인용 항목 판정, 제28조의2·의3 독립, 가지번호·목 파싱, 조용한 실패 방지와 사실과 다른 사유 고침, 경로 인자, 실험 01~03 회귀 검사 — 다르면 보고하고 멈춤, 고친 항목별 기록). 고치기 전 기록은 지우지 않음. answer-key-04.md 읽지 않음, commit·push 하지 않음.
7. (같은 세션, 13:41경) 회귀 차이는 1번 채택(목 표 추가를 받아들임). [1] results-01-layer1.md를 새 스크립트 출력으로 교체하고 머리말에 교체 기록 단락 추가 [2] results-04.md에 "도구를 고치면서 옛 결과가 바뀐 건" 절 [3] 실험 02·03은 층위 1 입력이 아니었고 회귀 대상은 실험 01뿐이었다는 기록 [4] privacy-law.md·results-04.md로 돌려 완료 기준 1~5 확인, 예상과 다르면 고치기 전에 보고. answer-key-04.md 읽지 않음, commit·push 하지 않음.
8. (같은 세션, 13:45경) [1] `제1의2호` 표기를 `제1호의2`로 고치고 privacy-law 입력으로 다시 돌려 확인, results-04.md에 기록 [2] 경고 경계를 "절반 초과"에서 "절반 이상"으로, 혼합 시험 입력으로 다시 확인 [3] (a) fdb2e94·faa5067 커밋 내용을 한 줄씩 기록, 히스토리는 고치지 않음 (b) Claude Cowork 추정이 틀렸던 건 기록. answer-key-04.md 읽지 않음, commit·push 하지 않음.
9. (같은 세션, 13:55경) 실험 04 층위 2. 완료 기준 6개(extract-doc-text.py가 목·가지번호를 뽑게 하고 회귀 검사, pairs-04-ko.md 기계적 분할, C3·C1·짝 비교 2건·예측 [A] 사전 기록, answer-key-04-pairs.md human 칸 비움, citation-judge 기본 1회·뒷받침 안 됨/C3/C1은 3회·한 건씩, results-04-layer2.md). 중단 조건: C3가 뒷받침됨이면 결과 파일을 쓰지 않고 보고. answer-key-04.md 읽지 않음, commit·push 하지 않음.
10. (같은 세션, 14:05경) 2번(3칸 사다리) 채택. [1] 예측 [A]를 원문 그대로 적고 바로 아래 전제가 맞지 않았다는 사실과 관찰(인용 단위는 답변하는 쪽이 고르고 그 선택이 층위 2 입력 범위를 정한다)을 판정 전에 기록 [2] Q6 호 서술 2개로 3칸 사다리(항 전체 / 본문+호 / 호만), 사람이 설계했음을 표시 [3] 기계적 분할 전부 유지, Q7 메타 문장도 쌍으로 만들고 사실 주장이 아니라는 점 기록 [4] 사람 판정 표본 규칙을 판정 전에 기록 [5] extract-doc-text.py를 깨뜨린 건 기록(이미 있으면 그대로). 나머지는 지시 9대로. answer-key-04.md 읽지 않음, commit·push 하지 않음.

### 읽은 파일

- deep/05-citation/experiments/scripts/check-article-numbers.py, deep/05-citation/data/sanan-law.md(머리말 형식), .claude/settings.local.json(읽기만), .gitignore, worklog.md (계획 단계)
- 국가법령정보센터 개인정보 보호법 페이지(Claude 내장 브라우저): https://www.law.go.kr/법령/개인정보보호법 → 본문 프레임 https://www.law.go.kr/LSW//lsInfoP.do?lsiSeq=283839&chrClsCd=010202&urlMode=lsInfoP&efYd=20260911&ancYnChk=0 (확인 2026-10-06)
- (2단계) deep/05-citation/experiments/design-01.md(인용 강제 프롬프트 대조), .claude/agents/ 목록, https://code.claude.com/docs/en/sub-agents.md (로드 시점 문구 재확인, 확인 2026-10-06)
- (새 세션, 11:02) AGENTS.md, README.md, worklog.md, .claude/agents/answer-writer.md, deep/05-citation/experiments/questions-04.md, deep/05-citation/experiments/answer-key-04.md(읽으면 안 되는 파일을 읽음. 아래 "문제와 대처" 참고)
- (새 세션, 13:17) AGENTS.md, README.md, worklog.md(640행부터), deep/05-citation/experiments/questions-04.md, deep/05-citation/data/privacy-law.md, deep/05-citation/experiments/scripts/check-article-numbers.py, .claude/agents/answer-writer.md, deep/05-citation/experiments/results-01.md(형식 참고). answer-key-04.md는 읽지 않음(폴더 목록에 이름만 보임)

### 만든·고친 파일

- deep/05-citation/data/privacy-law.md: 만듦 (2026-10-06, Claude Code) — 개인정보 보호법(시행 2026. 9. 11., 법률 제21445호) 제2조, 제15조~제18조, 제28조의2~제28조의3 발췌. 머리말에 출처·시행일·법률 번호·URL·수집일·범위 기록. commit·push는 하지 않음
- worklog.md: 2026-10-06 항목 추가 (이 기록)
- deep/05-citation/data/privacy-law.md: 수정 (2026-10-06, Claude Code) — 머리말에 판(시행일) 교차 확인 기록 추가(Cowork 확인 결과·출처, 시행일 세 갈래). 본문은 고치지 않음. commit·push는 하지 않음
- deep/05-citation/experiments/questions-04.md: 만듦 (2026-10-06, Claude Code) — Q6·Q7과 입력 자료 지정만. 기대 답 없음. commit·push는 하지 않음
- deep/05-citation/experiments/answer-key-04.md: 만듦 (2026-10-06, Claude Code) — 빈 틀(질문별 기대 답·기대 근거 조항·사람 판정, 층위 2 쌍 human 표). 값은 비움. commit·push는 하지 않음
- .claude/agents/answer-writer.md: 만듦 (2026-10-06 10:52, Claude Code) — name·description·disallowedTools(Read, Glob, Grep, Bash, Edit, Write, NotebookEdit). 본문은 역할 안내 한 줄("너는 질문에 답하는 에이전트다. 호출할 때 법령 발췌 원문과 질문 하나를 받는다. 아래 규칙을 따른다.")과 design-01.md 인용 강제 프롬프트. 프롬프트 블록은 design-01.md와 diff로 글자 단위 일치 확인(5줄). 역할 안내 한 줄은 지시에 없던 추가임. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06 11:02 이후, Claude Code, 새 세션) — 지시 4, 읽은 파일, answer-writer 로드 경위, 결정 기록, 다음 작업 갱신. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06 11:28, Claude Code) — "문제와 대처"에 기대 답이 메인 세션에 노출된 일을 기록. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06, Claude Code) — 노출 기록에 에드워드가 준 네 항목(격리 경로, 발견·보고, 대처, 서브에이전트 영향 없음)을 덧붙이고 다음 작업 갱신. 기대 답 내용은 옮기지 않음. commit·push는 하지 않음
- deep/05-citation/experiments/results-04.md: 만듦 (2026-10-06 13:20~13:23, Claude Code) — 답변 생성 기록, Q6·Q7 답변 원문(코드 블록), 실제 인용 조항(답변 끝 목록 그대로), 층위 1 첫 실행 결과(고치기 전). 기대 답·사람 판정 칸 없음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06 13:22~, Claude Code) — 지시 5, 읽은 파일, 답변 생성·층위 1 첫 실행 기록, 계획 변경 기록, 다음 작업. commit·push는 하지 않음
- deep/05-citation/experiments/scripts/check-article-numbers.py: 수정 (2026-10-06 13:35, Claude Code, 지시 6) — 경로 인자, 조·호 가지번호, 목, 코드 블록, 여러 줄 인용 목록, 생략 표기 이어받기, 실패 사유 구분, 조용한 실패 시 종료 코드 2, 자기 법률 이름을 발췌본에서 읽기, 출력 제목·링크 계산. 항목별 이유는 results-04.md "층위 1 스크립트 수정" 절. commit·push는 하지 않음
- deep/05-citation/experiments/results-04.md: 수정 (2026-10-06 13:40경, Claude Code, 지시 6) — "층위 1 스크립트 수정" 절 추가(고친 항목, 회귀 검사 결과). 첫 실행 절은 고치지 않음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06, Claude Code, 지시 6) — 지시 6, 수정·회귀 기록. commit·push는 하지 않음
- 저장소 밖(세션 스크래치 폴더)에만 만든 것: 회귀 검사용 폴더 reg-old·reg-new·reg-old-02·reg-old-03(저장소와 같은 구조, sanan-law.md·results-01~03.md 사본). 저장소의 results-01-layer1.md는 이번에도 바뀌지 않음
- deep/05-citation/experiments/results-01-layer1.md: 교체 (2026-10-06 13:42:04, Claude Code, 지시 7) — 고친 스크립트(SHA-256 6610e234…)를 저장소 루트에서 인자 없이 실행해 덮어씀. 교체 전후 diff는 실행 시각 1줄과 목 표 6줄. 이어서 머리말에 교체 기록 단락을 손으로 덧붙임(스크립트 출력 아님을 단락에 적음). 교체 전 사본은 세션 스크래치 폴더에 둠. commit·push는 하지 않음
- deep/05-citation/experiments/results-04-layer1.md: 만듦 (2026-10-06 13:42:40, check-article-numbers.py 출력, 지시 7). commit·push는 하지 않음
- deep/05-citation/experiments/results-04.md: 수정 (2026-10-06 13:42~13:44, Claude Code, 지시 7) — "결정과 교체", "도구를 고치면서 옛 결과가 바뀐 건", "실험 02·03과 회귀 검사의 범위", "층위 1 실행 (고친 스크립트)" 절 추가. 수정 절 제목의 "진행 중 — 회귀 검사에서 멈춤"을 뺌. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06, Claude Code, 지시 7). commit·push는 하지 않음
- deep/05-citation/experiments/scripts/check-article-numbers.py: 수정 (2026-10-06 13:46, Claude Code, 지시 8) — 호 가지번호 표기 `제1호의2`, 경고 경계 "절반 이상". SHA-256 03d8e702…. commit·push는 하지 않음
- deep/05-citation/experiments/results-04-layer1.md: 다시 씀 (2026-10-06 13:47:11, 스크립트 출력, 지시 8). commit·push는 하지 않음
- deep/05-citation/experiments/results-04.md: 수정 (2026-10-06 13:48, Claude Code, 지시 8) — "표기 오류와 경계 조건 수정" 절 추가. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06, Claude Code, 지시 8) — 지시 8, 커밋 내용, Cowork 추정 건. commit·push는 하지 않음
- deep/05-citation/experiments/scripts/extract-doc-text.py: 수정 (2026-10-06 13:58, Claude Code, 지시 9) — check-article-numbers.py 지시 6 수정 뒤 바뀐 함수 형식(조 키 튜플, parse_ref 4항목)에 맞춤, 조·호 가지번호와 목 뽑기, 목 목록 일치 검사, --law 인자. SHA-256은 아래 기록. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06, Claude Code, 지시 9). commit·push는 하지 않음
- deep/05-citation/experiments/scripts/split-answer-sentences.py: 만듦 (2026-10-06 14:10경, Claude Code, 지시 10) — 결과 파일 답변 원문을 문장 단위로 나눠 P 절을 만드는 스크립트(기계적 분할 규칙을 코드로 고정). commit·push는 하지 않음
- deep/05-citation/experiments/pairs-04-ko.md: 만듦 (2026-10-06 14:15경, Claude Code, 지시 10, 판정 전) — 설계 원칙, 분할 규칙, 사다리 고르기 규칙, 예측 [A]와 전제 불일치·관찰, 판정 규칙, 표본 규칙, P13~P46. 14:25에 사다리 (a)칸 번호 정정(아래 문제와 대처). commit·push는 하지 않음
- deep/05-citation/experiments/answer-key-04-pairs.md: 만듦 (2026-10-06 14:16경, Claude Code, 지시 10, 판정 전) — 쌍 번호·claim_id·주장·표본 칸, human 칸 비움. 14:25 사다리 번호 정정, 14:40 자동 뒷받침 안 됨 쌍(P17·P28·P29) 표본 추가. commit·push는 하지 않음
- deep/05-citation/experiments/results-04-layer2.md: 만듦 (2026-10-06 14:40경, Claude Code, 지시 10) — 판정 방식, 판정 표, 3회 일치, 예측 [A], 사다리, Q7 메타 문장, 뒷받침 안 됨 쌍 관찰, 출력 원문, 조문 원문, 한계. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-06, Claude Code, 지시 10). commit·push는 하지 않음
- 저장소 밖(세션 스크래치 폴더)에만 만든 것: 넘긴 본문 확인용 사본, Q6 답변 사본, 층위 1 실행용 임시 폴더(run1, 스크립트 복사본과 이름을 바꾼 입력 사본, 출력 results-01-layer1.md). 저장소의 check-article-numbers.py와 results-01-layer1.md는 바뀌지 않음(SHA-256 실행 전후 같음)

### 원문 수집 기록

- 방법: 내장 브라우저로 페이지를 열고, 본문 프레임의 innerText에서 세 구간(제2조, 제15조~제18조, 제28조의2~제28조의3)을 잘라 냄. 줄 앞 공백만 지우고 3줄 이상 빈 줄을 2줄로 줄였으며 글자는 바꾸지 않음
- 검증: 브라우저에서 세 구간의 SHA-256을 계산하고, 저장한 파일에서 같은 구간을 잘라 SHA-256을 비교함 → 세 구간 모두 일치(길이 1355 / 3510 / 533자)
- curl로 같은 URL을 받으면 본문이 들어 있지 않음(본문은 페이지가 따로 불러옴). 그래서 브라우저 경로를 씀
- 현행 판 선택: 같은 페이지에 "[시행일: 2027. 3. 9.] 제2조"(제9호 "인공지능기술" 추가, <개정 … 2026. 9. 8.>)가 함께 실려 있었음. 현행(시행 2026. 9. 11.) 제2조를 옮기고 머리말에 적음

### 판(시행일) 기록

- 발견: Claude Code가 수집 중 law.go.kr 같은 페이지에서 시행 예정 제2조를 발견해 보고함
- 교차 확인(확인자: Claude Cowork, 확인일 2026-10-06, law.go.kr 밖의 자료). Claude Code의 보고와 일치함
  - 현행: 법률 제21445호, 2026. 3. 10. 공포, 2026. 9. 11. 시행
  - 미시행: 법률 제21910호, 2026. 9. 8. 공포, 2027. 3. 9. 시행. 제2조제9호를 신설해 "인공지능기술"을 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」에 따른 인공지능기술로 정의
  - 현행 개정법 부칙상 제32조의2 제1항 단서와 제75조 제2항 제15호는 2027. 7. 1. 시행으로 따로 늦춰져 있음(이번 발췌 범위 밖)
  - 출처: https://www.lawtimes.co.kr/news/articleView.html?idxno=226510 (법률신문), https://datalaw.kr/posts/pipa-2026-amendment-comparison/ (신구조문 대조표). Claude Code는 이 두 출처를 직접 열어 보지 않았음
- (1) 1차 과제 핵심 맥락 2번("최신 버전만 근거로 남기기")이 실제 자료에서 나타난 사례다. 다만 이번에는 구버전이 섞인 것이 아니라, 아직 시행되지 않은 미래판이 섞인 반대 방향의 경우다
- (2) 같은 법 안에 시행일이 서로 다른 조항이 최소 세 갈래(2026. 9. 11. / 2027. 3. 9. / 2027. 7. 1.) 있다. 문서 식별자(법률 이름·번호)만으로는 "어느 판에서 왔는가"가 정해지지 않고, 조항 단위의 시행일까지 따라가야 한다

### 커밋

- faa5067 (2026-10-06 13:24:45, 에드워드): results-04.md 처음 작성분(답변 생성 기록, Q6·Q7 답변 원문과 실제 인용 조항, 층위 1 첫 실행 기록), worklog.md 지시 5 기록, deep/05-citation/.DS_Store. 스크립트는 들어 있지 않음. 메시지 "Record experiment 04 answers and the unmodified layer-1 run"과 내용이 맞음
- fdb2e94 (2026-10-06 13:38:24, 에드워드, 부모 faa5067): check-article-numbers.py 수정본(지시 6, SHA-256 6610e234…), results-04.md "층위 1 스크립트 수정" 절(고친 항목, 회귀 검사에서 멈춤), worklog.md 지시 6 기록. 메시지는 faa5067과 똑같은 "Record experiment 04 answers and the unmodified layer-1 run"이라 스크립트 수정을 담은 것이 드러나지 않음. 히스토리는 고치지 않음(지시 8)

### Pages URL

- 변경 없음

### 문제와 대처

- 계획 단계의 위험 2(새 에이전트 파일이 재시작 없이 로드되는지)는 에드워드가 공식 문서를 확인해 해소함: .claude/agents/ 폴더 안 파일 변경은 자동 반영되고 재시작은 폴더를 새로 만든 경우만 필요(https://code.claude.com/docs/en/sub-agents.md, 확인 2026-10-05, 에드워드). answer-writer를 만든 뒤 실제로 로드되는지는 아직 확인하지 않음
- answer-writer 로드 실패(2026-10-06 10:52~10:53): 파일을 만든 직후와 약 1분 뒤 두 번 로드 확인용 호출(실험 답변이 아닌 "로드 확인" 요청)을 보냈으나 둘 다 `Agent type 'answer-writer' not found. Available agents: citation-judge, claude, claude-code-guide, Explore, general-purpose, Plan, statusline-setup`. .claude/agents/는 이 세션 시작 전부터 있던 폴더이고(citation-judge는 로드돼 있음), 파일 형식은 citation-judge와 같음. 공식 문서(재확인 2026-10-06)는 기존 agents 폴더의 파일 변경을 몇 초 안에 감지한다고 적고, 예외로 새 agents 폴더, --add-dir 폴더, --disable-slash-commands로 시작한 세션 세 가지를 든다. 이 세션이 어느 예외에 해당하는지, 데스크톱 앱 환경에서 감시가 동작하지 않는지는 확인하지 못함(확인 필요). 다른 에이전트로 바꿔 돌리지 않고 멈춰서 보고함. 답변 생성은 아직 시작 전이라(기대 답 미기입) 실험 진행에는 아직 영향 없음

#### 서브에이전트 로드 기록 (관찰 사실만, 원인은 확인 필요)

| 날짜 | 에이전트 | 폴더 상태 | 관찰 |
|------|----------|-----------|------|
| 2026-10-05 | citation-judge | .claude/agents/ 폴더를 새로 만들면서 추가 | 같은 세션에서 두 번 실패. 새 세션에서 로드됨 |
| 2026-10-06 10:52~ | answer-writer | 폴더가 이미 있음(citation-judge 로드된 상태) | 같은 대화 안에서 두 번 실패(`Agent type 'answer-writer' not found`). 그 뒤 한 번 더 시도했으나 같은 대화를 이어 쓴 것이라 새 세션이 아니었고 결과도 같았음 |
| 2026-10-06 11:02 | answer-writer | 같음 | 사이드바에서 시작한 새 세션. 세션 시작 시 주어진 에이전트 유형 목록에 answer-writer가 있음(설명 "주어진 법령 발췌 원문과 질문 하나에 대해, 원문만 근거로 인용을 달아 답한다", 도구 "Read, Glob, Grep, Bash, Edit, Write, NotebookEdit 제외"). 답변 생성을 시작하지 말라는 지시에 따라 실제 호출은 하지 않음. 즉 "목록에 뜸"까지 확인했고 "호출 성공"은 아직 확인하지 않음 |

- 공식 문서(https://code.claude.com/docs/en/sub-agents.md, 확인 2026-10-06): 기존 agents 폴더 안의 변경은 몇 초 안에 반영된다고 하며, 재시작이 필요한 경우로 새 agents 폴더, --add-dir로 추가한 폴더, --disable-slash-commands 세 가지만 든다. 10-06 answer-writer 건은 셋 중 어디에도 해당하지 않는데 같은 세션에서 로드되지 않았다. 문서와 관찰이 다른 이유(데스크톱 앱 환경 차이, 감시 동작 여부 등)는 확인 필요
- 운영상 배운 사실: 새 에이전트를 만들면 그 대화에서는 쓸 수 없고, 사이드바에서 새 대화를 시작해야 한다. 기존 대화를 이어 쓰는 것은 재시작이 아니다(이 저장소, 데스크톱 앱에서 관찰한 범위)
- 에이전트 오류(2026-10-06 11:02 세션, Claude Code): 이어서 할 일을 파악하려고 experiments 폴더 파일을 읽다가 answer-key-04.md를 읽음. 이 파일 머리말은 "메인 세션은 모든 판정이 끝나기 전까지 이 파일을 읽지 않는다"고 정함. 읽은 시점의 내용은 빈 틀(기대 답·기대 근거 조항·사람 판정·쌍 표 모두 빈 칸)이라 정답 쪽 정보는 보지 않음. 이후 이 파일은 다시 읽지 않고 고치지도 않음. 에드워드가 기대 답을 채운 뒤에는 판정이 끝날 때까지 읽지 않는다
- 기대 답 노출(2026-10-06 11:28, 같은 세션): 에드워드가 Q6·Q7 기대 답, 기대 근거 조항, Q6 제4호 메모, 층위 2 절 문구를 대화창에 붙여 넣음(지시 문장 없이 내용만). 이로써 이 메인 세션은 기대 답 내용을 알게 됨. answer-writer와 citation-judge는 호출마다 받은 입력만 보므로 영향이 없다. 다만 이 세션이 3단계를 맡으면 쌍 고르기, doc_ref 자르기, pairs-04-ko.md 예측 쓰기에 기대 답이 영향을 줄 수 있다. Claude Code는 answer-key-04.md에 쓰지 않았고(머리말상 에드워드가 직접 채우는 파일), 어떻게 할지 에드워드에게 물음
  - 정답표를 파일로 분리하는 것만으로는 격리가 되지 않았다. 사람이 대화창에 붙여 넣는 경로가 남아 있었고, 실제로 그 경로로 메인 세션에 노출됐다
  - 노출을 발견한 쪽은 Claude Code이고, 파일에 쓰기 전에 멈춰서 보고했다. 기대 답 내용은 저장소에 들어가지 않았다
  - 대처(에드워드 결정, 2026-10-06): 이 대화를 버리고 새 세션에서 3단계를 시작한다. 정답표는 에드워드가 편집기로 직접 채운다
  - 두 서브에이전트(answer-writer, citation-judge)는 호출 입력만 보고 파일 읽기가 도구 수준에서 막혀 있어 영향받지 않았다
- Claude Cowork 추정이 틀렸던 건(2026-10-06 지시 7): 지시 [2]에 "실험 01의 파싱 실패 0은 파서가 목을 볼 줄 몰라서 나온 값"이라는 문장이 있었음(Claude Cowork의 추정, 에드워드 전언). 사실과 달랐음. Claude Code가 고치기 전 파서 사본에 `제2조 제11호 가목`을 직접 넣어 보니 `해석하지 못한 남은 글자: '가목'`으로 파싱 실패가 남. 파싱 실패 0은 당시 인용에 목이 없었기 때문이고, 목을 몰라서 조용히 빠진 곳은 구조 표였음. 그대로 쓰지 않고 바로잡아 results-04.md에 적고 보고함
  - 에드워드는 이번이 같은 유형의 세 번째라고 함(앞의 두 건: 9월 존재하지 않는 폴더를 가정한 것, 10-05 P9 가설). worklog 기록과 대조한 결과는 아래와 같음(Claude Code, 2026-10-06)
  - 9월 건: 2026-09-28 항목에 "지시문은 deep/README.md와 deep/04-versioning 폴더가 이미 있다고 전제했으나, 이 저장소에는 deep/ 폴더 자체가 없었음(git log·작업 폴더 모두 확인)"이라고 있음. Claude Code가 저장소를 직접 확인해 잡은 것은 기록과 맞음. 다만 그 지시문을 Cowork가 썼다는 것은 worklog에 적혀 있지 않음(에드워드 전언으로만 확인)
  - 10-05 건: 기록상 두 단계임. (1) 처음 P9 hypothesis "제1항 본문에 주체(안전보건관리책임자)와 의무가 있다"는 Claude Cowork가 씀 → Claude Code가 extract-doc-text.py로 원문을 뽑아 잡음. 이것이 Cowork 추정 건에 해당함 (2) "명칭은 조 제목에만 있다"는 그 보고를 하면서 Claude Code가 제1항만 보고 쓴 문장이고, 기록에 "에이전트 오류(Claude Code)"로 남아 있음. findings 작성 중 Claude Code가 제15조 전체를 확인해 제2항·제3항에도 명칭이 있음을 스스로 찾음. 따라서 "명칭은 조 제목에만 있다"는 Cowork의 추정이 아니라 Claude Code의 오류임
  - 정리: 세 건 모두 원문이나 코드를 직접 확인해 잡은 것은 맞음. Cowork의 미확인 추정이었던 것은 9월 건(지시문 작성자는 전언), 10-05의 처음 P9 가설, 이번 건. "명칭은 조 제목에만 있다"는 그 셋에 들지 않음
- 에이전트 오류(2026-10-06 14:25, Claude Code, 지시 10): pairs-04-ko.md와 answer-key-04-pairs.md에 사다리 (a)칸을 "P16·P17"로 적었으나 실제 Q6-s04·s05의 쌍 번호는 P15·P16이었음(P17은 Q6-s06). 스크립트 출력의 번호를 확인하지 않고 claim_id 순서를 짐작해 적은 것이 원인. 판정 10여 건 뒤, 판정 기록에 붙이던 P 번호도 P15부터 하나씩 밀려 있는 것을 발견함. 판정자에게는 P 번호를 넘기지 않고 주장 문장을 넘기므로 판정 입력과 값에는 영향 없음. 두 파일의 번호를 고치고 pairs-04-ko.md에 정정 줄을 남김. 판정 기록은 주장 문장으로 대조해 번호를 다시 붙임

### 통제군 거짓 주장 후보 (답변 생성 전, 2026-10-06 제시)

- C1 (제15조 제1항): "개인정보처리자는 제15조제1항 각 호에 따라 수집한 개인정보를 수집 목적과 관계없이 이용할 수 있다." — 원문은 "그 수집 목적의 범위에서 이용할 수 있다"
- C2 (제2조 제1호의2): "“가명처리”란 개인정보의 전부를 삭제하여 추가 정보가 있어도 특정 개인을 알아볼 수 없도록 처리하는 것을 말한다." — 원문은 "일부를 삭제하거나 일부 또는 전부를 대체하는 등의 방법으로 추가 정보가 없이는" 알아볼 수 없도록 처리
- C3 (제28조의2 제1항): "개인정보처리자는 통계작성, 과학적 연구, 공익적 기록보존 등을 위하여 가명정보를 처리하려면 정보주체의 동의를 받아야 한다." — 원문은 "정보주체의 동의 없이 가명정보를 처리할 수 있다"
- 에드워드가 하나를 고른다 → 2026-10-06 11:02 세션에서 결정(아래 "결정 기록")

### 결정 기록 (2026-10-06 11:02 세션, 에드워드)

- 층위 2 human 칸: (b)로 감. 쌍 human 값은 answer-key-04.md가 아니라 별도 파일 answer-key-04-pairs.md에 둔다. 쌍 번호와 주장만 넣고 human 칸은 비워 둔다. 쌍이 정해진 뒤에(pairs-04-ko.md를 만든 뒤에) 만든다 → 아직 만들지 않음
- 통제군(거짓 주장): C3(제28조의2 제1항, "동의를 받아야 한다")
- 부분 오류 쌍: C1(제15조 제1항, "수집 목적과 관계없이 이용할 수 있다")을 통제군과 따로 넣는다. 대부분 맞고 한 구절만 틀린 주장으로, 실험 01 Q5와 같은 오류 유형을 보는 쌍이다. pairs-04-ko.md에서 통제군과 구분해 표시한다
- C2는 쓰지 않는다
- answer-writer.md에 추가한 역할 설명 한 줄은 그대로 둔다
- answer-key-04.md "층위 2 쌍의 사람 판정" 절은 "이 표에 옮긴다"로 되어 있어 위 (b) 결정과 맞지 않음. 메인 세션은 이 파일을 고치지 않으므로 에드워드가 고칠지 판단

### 답변 생성 기록 (3단계, 2026-10-06 13:17~13:20 세션)

- answer-writer 호출 성공. 이번 세션 첫 호출(Q6)에서 `not found` 오류 없이 답이 돌아옴 → 위 "서브에이전트 로드 기록" 표의 "호출 성공은 아직 확인하지 않음"이 이번에 확인됨(사이드바에서 시작한 새 세션)
- 호출 2회(Q6 → Q7, 순서대로). 서브에이전트 도구 사용 0회씩. 넘긴 것은 privacy-law.md 18~160행과 질문 문장뿐(`[문서]`·`[질문]` 머리표 두 줄 추가). 넘긴 본문은 원본과 diff 차이 없음
- 관찰(판정 아님): Q7 답변은 제2조가 항이 아니라 호·목으로 되어 있어 [제○조 제○항] 형식을 쓸 수 없다고 스스로 밝히고 [제2조 제1호 다목]처럼 표시함. Q6 답변은 `## ` 제목과 `---`가 있는 마크다운 문서 형태로 돌아옴. 두 답변 모두 답변 끝 조항 목록이 여러 줄 목록임
- 답변과 조항 목록은 results-04.md에 글자 그대로 옮김(Q6은 사본과 diff로 확인)

### 층위 1 첫 실행 기록 (4단계, 스크립트를 고치기 전)

- 2026-10-06 13:21:25 +0900, 파이썬 3.13.3, 종료 코드 0. 파이썬 예외·`오류:` 문구 없음
- 결과: Q6 `('실제 인용 조항:' 줄 없음)` → 파싱 실패 1, Q7 `(인용 항목 없음)`(출력 파일에만, 터미널에는 Q7 줄 자체가 없음). 대조 단계에 간 인용 항목 0건
- 발췌본 파싱: 제28조의2·제28조의3이 조로 잡히지 않고 그 항이 제18조에 붙음(제18조 항 10개 ①②③④⑤①②①②③), 제2조 제1호의2·제7호의2와 목(가·나·다)이 빠짐
- 자세한 내용과 원인 표는 results-04.md "층위 1 첫 실행" 절. 스크립트는 고치지 않음

### 층위 2 판정 기록 (지시 10)

- 분할: `split-answer-sentences.py --start 13`(종료 코드 0) → 기계적 분할 쌍 28건(Q6 22, Q7 6), 인용 없는 문장 6개는 쌍으로 만들지 않음. 사람이 설계한 쌍 6건(C3, C1, 사다리 (b)·(c) 4건). 합계 34건(P13~P46)
- 원문 추출: extract-doc-text.py(--law privacy-law.md) 14:17, 종료 코드 0, 일치 검사 통과(조 7개), 쌍 34개
- 판정: citation-judge 46회(C3·C1 각 3, 기계적 28 + 뒷받침 안 됨 4쌍 × 추가 2, 사다리 4), 한 건씩 순서대로, 14:19~14:37. 도구 사용 모두 0회. 넘긴 것은 조문 원문과 claim_ko뿐
- 중단 조건: C3 뒷받침 안 됨 ×3 → 해당 없음
- 결과: 기계적 28건 중 뒷받침됨 24, 뒷받침 안 됨 4(P17·P28·P29·P40). C1 뒷받침 안 됨 ×3. 사다리 6칸 모두 뒷받침됨 → 예측 [A] 맞지 않음
- 예상과 다른 것: P29가 3회 중 갈림(안 됨·안 됨·됨). 실험 02·03에서 3회 돌린 쌍은 모두 같았음. 절차를 바꿀 일은 아니어서 멈추지 않고 그대로 기록하고 끝까지 진행함(보고에 적음)
- 출력 형식: P17-1이 코드 블록으로 감싸져 나옴, 근거가 두 문장 이상인 출력 5건. 판정 값은 모두 규칙대로

### extract-doc-text.py 수정 기록 (지시 9)

- 발견: 지시 9 시작 시 extract-doc-text.py를 기존 입력(pairs-01·02·03-ko.md)에 돌리니 셋 다 `오류: 조 목록이 parse_law 결과와 다릅니다.`, 종료 코드 1. 이 스크립트는 check-article-numbers.py의 parse_law·parse_ref·judge를 불러 쓰는데, 지시 6에서 그 함수들의 형식(조 키를 정수에서 (조, 가지번호) 튜플로, parse_ref 결과를 3항목에서 4항목으로)을 바꿨기 때문
- 고친 것(항목마다 한 줄)
  - 조 나누기: `제<숫자>조의<숫자>(`도 조 시작으로 읽고, 조 키를 parse_law와 같은 튜플로 맞춤. 위 오류와 제28조의2·의3 때문
  - 호: `1의2.` 같은 가지번호 호 줄을 찾고 뽑음. Q7이 "제2조 제1호의2"를 인용하기 때문
  - 목: doc_ref "제2조 제1호 다목"이면 그 목 줄 하나를 뽑음. Q7이 목을 인용하기 때문
  - 일치 검사: 항·호에 더해 목 목록도 parse_law 결과와 같은지 검사함. 목을 새로 읽게 되었으므로
  - doc_ref 해석: "제28조의2 제1항"처럼 가지번호 조를 "+" 이어받기에서도 다룸. 예전 규칙은 `제\d+조`만 보고 "의2"를 잃었음
  - 입력: `--law` 인자를 추가함(기본 sanan-law.md). 예전에는 발췌본 경로가 코드에 고정
- 고친 판: extract-doc-text.py SHA-256 c932cccc38f1905726c90df081d2edc2038c2837aa18937a3aa2bbdf490a2232 (check-article-numbers.py는 03d8e702…)
- 회귀 검사: 고치기 전 판(f9c90ab의 두 스크립트, SHA-256 check c3d75403…)을 임시 폴더에서 돌린 출력과, 고친 판을 저장소에서 돌린 출력이 pairs-01·02·03 모두 바이트 단위로 같음(종료 코드 0)
- 새 표기 시험(시험 쌍 파일, 세션 스크래치 폴더, privacy-law.md): 제2조 제1호 다목, 제2조 제1호의2, 제2조 제7호의2, 제28조의2 제1항, 제28조의2(조 전체), 제15조 제1항 본문+제2호, 제28조의3 제목 → 모두 원문 줄을 뽑음, 일치 검사 통과(조 7개). "제2조 제1호 본문"은 기존 규칙(본문은 항 뒤에만)대로 오류
- 에이전트 오류(Claude Code, 지시 6): check-article-numbers.py를 고칠 때 이 스크립트가 그 함수를 불러 쓴다는 것(두 스크립트 머리 주석에 적혀 있음)을 확인하지 않았고, 회귀 검사도 check-article-numbers.py 출력만 봤음. 그래서 extract-doc-text.py가 깨진 채 지시 6~8을 마침. 층위 2를 시작하기 전에 발견해 판정 입력에는 영향 없음. 도구가 다른 도구의 함수를 불러 쓰면, 고친 쪽뿐 아니라 불러 쓰는 쪽도 회귀 검사 대상이다
- 멈춘 지점: 기준 1까지 마치고, pairs-04-ko.md를 만들기 전에 멈춤. Q6 답변의 호 설명 문장들이 모두 [제15조 제1항](항 단위)을 인용하고 호 단위 인용([제15조 제1항 제2호] 같은 것)이 하나도 없음. 예측 [A]와 짝 비교는 "Q6의 호 인용"을 전제로 하므로 에드워드에게 보고함

### 층위 1 스크립트 수정 기록 (지시 6)

- 기준선: 고치기 전 스크립트를 저장소와 같은 구조의 임시 폴더에서 돌리면 results-01-layer1.md와 실행 시각만 다름(13:33:06) → 저장소 파일이 지금 스크립트의 출력임을 확인
- 회귀 검사(13:35:46): 실험 01에서 실행 시각 말고 한 군데 다름. 1절 표 아래에 "목이 있는 호" 표(제2조 조 직속 제11호 가나다라마)가 새로 생김. 2절 판정 표·3절 요약은 같음. 원인은 sanan-law.md 제2조 제11호 아래 가~마목을 새로 읽게 된 것(완료 기준 3). 기준 3과 6이 이 입력에서 함께 지켜지지 않음
- 실험 02·03: 결과 파일에 "## Q" 절이 없어 고치기 전·후 모두 같은 오류(`'## Q' 절을 하나도 찾지 못했습니다`, 종료 코드 1). 비교할 층위 1 출력이 원래 없음
- 지시대로 회귀 차이에서 멈춤. privacy-law.md·results-04.md로는 아직 돌리지 않음
- (지시 7) 에드워드가 1번 채택 → results-01-layer1.md 교체(13:42:04)
- 고친 스크립트로 실험 04 실행(13:42:40, 종료 코드 0): 인용 16건 모두 실재함. 완료 기준 1~5 충족(Claude Code 확인). 기준 4는 시험 입력 두 개로 따로 확인(종료 코드 2 경고, Q 절 밖 인용 줄·닫히지 않은 코드 블록 경고)
- 예상과 다른 것: Q7 `제2조 제1호의2`가 출력에 `제2조 제1의2호`로 찍힘(판정은 맞음, 표기만 다름). 지시대로 고치지 않고 보고함
- 지시 [2]의 "파싱 실패 0은 파서가 목을 볼 줄 몰라서 나온 값" 문장은 그대로 적지 않음. 고치기 전 파서에 `제2조 제11호 가목`을 넣으면 파싱 실패로 나오므로, 0은 당시 목 인용이 없었기 때문이다. 목을 몰라서 조용히 빠진 곳은 구조 표였다. 이렇게 고쳐 적고 에드워드에게 보고함

### 계획 변경 기록

- 층위 2 쌍 human 값을 answer-key-04.md 안의 표 대신 별도 파일 answer-key-04-pairs.md에 둠(위 결정 기록)
- 거짓 주장 쌍을 통제군 1개(C3)에서 통제군 C3 + 부분 오류 쌍 C1로 늘림
- (13:17 세션, Claude Code 판단) answer-writer 호출 확인용 호출을 따로 하지 않고 Q6 답변 생성 호출을 첫 호출 겸 확인으로 씀. 지시의 "총 2회"를 지키기 위함. 다음 작업 목록의 "실제 호출은 답변 생성 때 첫 호출로 확인"과 같은 방식
- (13:17 세션, Claude Code 판단) 층위 1을 저장소에서 바로 돌리지 않음. 스크립트 경로가 고정돼 있어 그대로 돌리면 새 입력을 못 읽고 results-01-layer1.md를 덮어쓰기 때문. 스크립트를 바이트 그대로 저장소 밖 임시 폴더에 복사하고 입력 파일 이름만 바꿔 돌림. 코드는 한 글자도 바꾸지 않았지만, "고치지 않은 스크립트를 새 입력에 돌린다"를 이렇게 해석했다는 점은 에드워드가 확인할 것
- (13:17 세션, Claude Code 판단) results-04.md에 답변 원문을 코드 블록으로 감쌈. 글자는 그대로지만 Q6 답변의 `## ` 줄 때문에 파일 구조가 깨지지 않게 하려는 것. 스크립트는 코드 블록을 모르므로 이 선택이 층위 1 결과(Q6 줄 없음)에 영향을 줌. 코드 블록 없이 넣었어도 `## ` 줄에서 Q6 절이 끝나는 것은 같음
- 실험 01과 달리 "실제 인용 조항"을 한 줄 범위 표기로 정리하지 않고 답변 끝 목록을 그대로 씀(지시대로). 이 차이가 층위 1에서 Q7 항목 0건의 원인

### 다음 작업

- (완료) 2단계 파일 만들기, 거짓 주장 후보 제시
- (완료) 에드워드: 통제군 후보 고르기 → C3, 부분 오류 쌍 C1
- 에드워드: answer-key-04.md에 기대 답을 편집기로 직접 채우기 (다음 차례)
- 3단계는 사이드바에서 시작한 새 대화에서 한다(11:02 세션은 기대 답이 노출돼 버림)
- (완료) answer-writer 로드: 13:17 세션 첫 호출에서 호출 성공 확인
- (완료) 답변 생성(3단계): Q6·Q7 각 1회, results-04.md에 원문 기록
- (완료) 층위 1 첫 실행(고치기 전): 결과와 깨진 곳 기록. 스크립트는 고치지 않음
- 에드워드: results-04.md 층위 1 첫 실행 결과 검토, 임시 폴더 실행 방식을 인정할지 판단
- (완료, 지시 7에서 1번 채택) check-article-numbers.py 고치기. 에드워드: 실험 01 출력에 "목이 있는 호" 표가 새로 생기는 것을 받아들일지(기준 6을 "판정 결과가 같음"으로 볼지), 아니면 목 표를 다른 방식으로 낼지 결정
- (완료) privacy-law.md·results-04.md로 실행 → results-04-layer1.md, 완료 기준 1~5 확인
- (완료, 지시 8) `제1의2호` 표기 고침, 경고 경계 "절반 이상"
- 에드워드: results-04.md "도구를 고치면서 옛 결과가 바뀐 건"의 파싱 실패 0 설명, worklog "Claude Cowork 추정이 틀렸던 건"의 10-05 건 정리 검토
- (완료, 지시 10) pairs-04-ko.md 만들기(C3 통제군, C1 부분 오류 쌍 구분) → answer-key-04-pairs.md 만들기(human 칸 비움) → 층위 2 판정
- (완료) 층위 2 쌍 human 값 넣는 방식 결정 → (b) 별도 파일

## 2026-10-07

### 목표

실험 04 마지막 단계: 층위 2 사람 판정(17건)과 자동 판정을 비교하고, Q6·Q7 답변을 기대 답과 대조

### 환경

- macOS, Claude Code 데스크톱, Python 3.13.3

### Claude Code에 준 지시

1. answer-key-04.md와 answer-key-04-pairs.md를 읽어도 됨(모든 판정 끝). results-04.md에 "사람 판정과 자동 판정 비교" 절(표본 17건 표, "부분 뒷받침" 처리 규칙을 표 앞에), 갈린 쌍마다 양쪽 근거 인용 단락, "판정 기준에 대한 관찰"을 P17·P29 자동 근거와 나란히, Q6·Q7 기대 답 대조 절(근거 조항, 더하거나 빠뜨린 것, Q6 제4호 각주), 한계 3가지. 판정 값은 고치지 않음, commit·push 하지 않음.
2. deep/05-citation/findings.md를 실험 04까지 반영해 갱신. 기존 내용은 지우지 않음, 지정한 실험 파일과 worklog 10-06·10-07에 적힌 것만 씀. 한 줄 결론 재판단, "무엇을 했나"에 실험 04, 새 발견 9개(각 근거 파일 명시), 한계 3개 추가, 설계 규칙 재검토, 빗나간 가설에 [A]와 그 전제, 남은 질문 5개 이내, 링크 갱신. commit·push 하지 않음.
3. findings.md "1차 과제와의 연결"에 핵심 맥락 2번(최신 버전만 근거로 남기기) 항목을 더함. 실험 04 자료 수집 단계에서 나타난 판(시행일) 건을 확인된 것으로 적고 근거를 붙임. 판정 실험의 결과가 아니라 자료 수집 중 관찰이라는 점을 구분. commit·push 하지 않음.
4. deep/07-graphrag/plan.md 다시 쓰기(MBB 공개 리포트 "산업 × 펌별 관점 비교" 그래프). Cowork가 확인한 서지 정보를 쓰되 각 URL이 열리는지 확인하고 확인 날짜 2026-10-07을 붙임, 열리지 않으면 확인 필요로 표시·보고. arXiv:2506.05690은 열어서 맞을 때만 넣음. 1~9절 구성(주제, 레퍼런스, B2B, 수집, 노드·엣지 표, 질문 3개, 도구 비교 표와 조건부 2단계, 05 연결 최소 4가지, 남은 질문 3개 이내). deep/README.md 07 항목 링크 확인. commit·push 하지 않음.
5. plan.md 7절 결론을 고친 사실에 맞춰 다시 봄. 결론이 성립하는지 확인하고, 실제 제약을 환경 쪽 사실(디스크 3.6GiB, 유료 API 키 없음)로 쓰고, 도구마다 "API 키 때문"인지 "필요한 모델을 올릴 하드웨어가 없어서"인지 구분. 결론이 바뀌면 바꾸고 이유 한 줄. worklog에 Cowork 설명 네 가지가 원문과 달랐던 건 기록. commit·push 하지 않음.

### 읽은 파일

- deep/05-citation/experiments/answer-key-04.md (메인 세션이 처음 읽음, 모든 판정이 끝난 뒤)
- deep/05-citation/experiments/answer-key-04-pairs.md (에드워드가 채운 사람 판정·메모·관찰)
- deep/05-citation/experiments/results-04.md (절 구조), worklog.md (끝부분)
- 자동 판정 근거는 이 세션이 2026-10-06에 쓴 results-04-layer2.md 출력 원문과 판정 기록에서 옮김
- (지시 2) deep/05-citation/findings.md, experiments/design-01.md, results-01-layer2.md, results-03.md (이 세션에서 처음 끝까지 읽음). results-01.md, results-01-layer1.md, results-02.md, questions-04.md, results-04.md, results-04-layer1.md, results-04-layer2.md, pairs-04-ko.md, answer-key-04.md, answer-key-04-pairs.md, worklog.md 10-06·10-07은 이 세션에서 앞서 읽었거나 썼고, 숫자는 파일에서 다시 확인함(층위 1 16건, 호출 46회, 표본 17건, 일치 14/같은 쪽 1/불일치 2)
- (지시 3) key-contexts.md(2번 문구 인용용), findings.md "1차 과제와의 연결" 절. privacy-law.md 머리말과 worklog 2026-10-06 "원문 수집 기록"·"판(시행일) 기록"은 이 세션에서 앞서 읽은 내용으로 대조
- (지시 4) deep/07-graphrag/plan.md(다시 쓰기 전), deep/README.md(07 항목), deep/07-graphrag/ 목록, worklog.md 2026-10-06 "07 계획서 확인 기록", findings.md(8절 연결용, 이 세션에서 갱신한 내용)
- (지시 4) 웹, 모두 2026-10-07 확인(WebFetch): https://arxiv.org/abs/2404.16130 , https://arxiv.org/abs/2410.05779 , https://arxiv.org/abs/2506.05690 , https://github.com/HKUDS/LightRAG , https://neo4j.com/labs/genai-ecosystem/llm-graph-builder/ , https://github.com/neo4j-labs/llm-graph-builder , https://github.com/microsoft/graphrag
- (지시 5) 로컬: `sysctl -n machdep.cpu.brand_string hw.memsize`(Apple M1, 8589934592바이트=8GB), `df -h ~`(3.7GiB, 17:41). 웹(2026-10-07): https://microsoft.github.io/graphrag/config/models/ , https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507

### 만든·고친 파일

- deep/05-citation/experiments/results-04.md: 수정 (2026-10-07, Claude Code) — "사람 판정과 자동 판정 비교 (층위 2)", "기대 답과 대조 (Q6·Q7)", "한계 (실험 04)" 절 추가. Q6·Q7 절 끝에 사람 판정 빈칸(에드워드가 채울 자리) 둠. 기존 절은 고치지 않음. 추가 뒤 check-article-numbers.py로 이 파일을 다시 읽어 Q6·Q7 인용 줄 해석이 깨지지 않는 것 확인(종료 코드 0, 출력은 세션 스크래치 폴더). commit·push는 하지 않음
- worklog.md: 수정 (2026-10-07, Claude Code) — 2026-10-06 다음 작업 한 줄 완료 표시, 이 항목 추가. commit·push는 하지 않음
- deep/05-citation/findings.md: 수정 (2026-10-07, Claude Code, 지시 2) — 기존 내용은 지우지 않음. 머리말 범위를 실험 01~04로, 한 줄 결론을 좁히고 바꾼 이유와 이전 문장을 남김, "무엇을 했나"에 실험 04, 발견 5~13과 "실험 04의 통제군과 부분 오류 쌍" 추가(기존 "통제군" 절 제목은 "통제군 (실험 01)"로), 빗나간 가설에 [A]·전제, 한계 8~12와 한계 5 갱신 줄, 설계 규칙 2에 좁힘 줄·규칙 3 보강·규칙 4~6 추가, 남은 질문 갱신(5개), 링크에 실험 04 파일과 worklog 추가. "1차 과제와의 연결" 절은 지시 범위 밖이라 고치지 않음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-07, Claude Code, 지시 2). commit·push는 하지 않음
- deep/05-citation/findings.md: 수정 (2026-10-07 17:21, Claude Code, 지시 3) — "1차 과제와의 연결"에 key-contexts.md 2번 항목 추가(확인한 것: 자료 수집 중 관찰, 판정 실험 결과 아님 / 확인하지 못한 것: 파이프라인의 판 거르기, 구버전이 섞인 경우). 1번의 "문서 식별자·개정판 추적", 4번의 "구버전 문서·개정 이력 평가" 줄은 지우지 않고 새 항목을 가리키는 괄호를 붙임. 2027. 7. 1. 시행 조항은 Cowork 교차 확인에서 나온 것이고 Claude Code는 법률신문·datalaw.kr 두 출처를 직접 열지 않았다는 점도 적음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-07, Claude Code, 지시 3). commit·push는 하지 않음
- deep/07-graphrag/plan.md: 다시 씀 (2026-10-07 17:27, Claude Code, 지시 4) — 1~9절. 레퍼런스 표에 확인 열(열림, 2026-10-07), 7절에 "받은 설명과 원문이 다른 점", 8절에 05 연결 7가지(통제군, 근거 범위, 도구의 판, 조용한 실패, 재현성, 단위·잘린 주장, 척도·사람 판정 독립성). deep/README.md 07 항목에는 이미 plan.md 링크가 있어 고치지 않음. papers.md·tools.md는 고치지 않음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-07, Claude Code, 지시 4). commit·push는 하지 않음
- deep/07-graphrag/plan.md: 수정 (2026-10-07 17:42, Claude Code, 지시 5) — 7절 도구 표의 "실행 가능한가" 칸을 API 경로·로컬 경로로 나눠 다시 씀, 근거에 GraphRAG 모델 설정 문서·Qwen3-30B-A3B 모델 페이지 추가, 환경에 하드웨어(M1, 8GB) 추가, 결론 절에 도구별 제약 표와 "바뀐 점" 한 줄, 2단계 조건 넓힘, 남은 질문 3 갱신. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-07, Claude Code, 지시 5). commit·push는 하지 않음
- worklog.md: 수정 (2026-10-08, Claude Code, 에드워드 지시) — 2026-10-07 항목 끝에 "판단 기록 — AI 제안 / 내 선택 / 이유 (멘토 피드백 ③)" 절을 에드워드가 준 문구 그대로 추가(다듬지 않음). 추가 전 대조: 절이 근거로 든 기록(worklog 2026-10-04·10-05, plan.md)에서 7.2GiB(10-04 설치 후), 1.1GB, 3.6GiB(10-07)는 확인됨. "사용률 97%"는 10-05 삭제 후 값(6.7GiB, 97%)으로 기록돼 있고 10-04 시점 사용률은 기록에 없음. "flan-t5-large 3.13GB / roberta-large 1.42GB"는 그 기록들에 없음(10-04 기록은 "모델 가중치 약 3GB 예정"). 문구는 고치지 않고 에드워드에게 보고함. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-08, Claude Code, 에드워드 지시) — "판단 기록" 절의 "그 뒤 기록으로 확인된 것" 문단만 에드워드가 준 문구로 교체(앞 세 문단은 고치지 않음), 2026-10-07 "문제와 대처"의 "없음"을 세 줄로 바꿈. 교체 전 대조: 두 HuggingFace URL이 열리고 pytorch_model.bin이 각각 3.13 GB, 1.42 GB인 것을 Claude Code가 확인함(2026-10-08). commit·push는 하지 않음

### 비교 결과 요약

- 층위 2 표본 17건: 일치 14, 같은 쪽(정확히 일치는 아님) 1(P28, 사람 "부분 뒷받침"), 불일치 2(P29 사람 뒷받침됨 / 자동 안 됨·안 됨·됨, P35 사람 뒷받침 안 됨 / 자동 뒷받침됨)
- 통제군 C3·부분 오류 C1: 사람·자동 모두 뒷받침 안 됨
- Q6: 기대 근거 조항 중 제15조 제3항은 같고, 제15조 제1항 제2호~제7호는 답변이 항 단위로 인용. 답변은 기대 답에 없는 제16조·제18조·제28조의2·제28조의3·제2조 정의를 더함. 제4호는 둘 다 포함했으나, 기대 답 각주는 애매함과 제15조 제2항을 들었고 답변은 제1호에만 "동의"가 있다는 것을 근거로 듦
- Q7: 기대 근거 조항 네 개 모두 인용, 제28조의2 제1항을 더함. 빠뜨린 요소는 찾지 못함
- answer-key-04.md의 Q6·Q7 "사람 판정" 칸은 비어 있어 비워 둠(에드워드가 채울 자리)

### findings 갱신 판단 기록 (지시 2)

- 한 줄 결론: 실험 04 사다리(발견 9)에서 범위를 바꿔도 판정이 같았으므로 "근거를 어디서 자르느냐에 따라 뒤집힌다"를 "주장이 건넨 조각 밖의 요소를 담고 있을 때"로 좁힘. 바꾼 이유와 이전 문장을 findings에 남김
- 발견 9의 좁힌 결론은 지시에 따라 적었고, results-04-layer2.md가 이 차이를 Claude Code의 관찰·"확인 필요"로 둔 점과 근거가 주장 세 개(실험 02·03 하나, 실험 04 둘)뿐이라는 점을 같은 절에 적음
- 발견 6의 실험 01 대비: 실험 01 "파싱 실패 0"은 진짜 0이었음(목 인용이 없었음, 발견 7). 그래서 "두 실행이 종료 코드와 오류 문구만으로는 구별되지 않았다"까지만 적음
- 설계 규칙: 규칙 1은 그대로. 규칙 2는 문장을 지우지 않고 좁힘 줄을 붙임. 규칙 3에 C3·C1 결과를 더함. 규칙 4(도구 판 기록, 발견 7), 5(조용한 실패 방지, 발견 6), 6(여러 번 돌려 일치 여부 기록, 발견 12)을 더함. "조각에 조 번호를 붙여 건네라"는 실험으로 시험하지 않아 규칙으로 넣지 않고 남은 질문 3에 둠

### 07 계획서 다시 쓰기 기록 (지시 4)

- URL 7개 모두 열림(2026-10-07). "확인 필요"로 표시한 URL 없음
- arXiv 세 편: 제목·저자 순서·버전 날짜가 받은 값과 같음. 받은 값에 없던 LightRAG v2(2024-11-07), Xiang et al. v2(2025-10-07)를 arXiv 페이지에서 확인해 더함. arXiv:2506.05690은 열어서 맞는 것을 확인한 뒤 넣음
- 받은 설명과 원문이 다른 점(2026-10-06 확인 때와 같음, plan.md 7절에 적음)
  - MS GraphRAG "유료 API 키가 전제": README에 없음. README는 "indexing can be an expensive operation"만 적음. 필요한 API 키·제공자, 그래프 저장 방식도 README에서 찾지 못함
  - LightRAG "기본 저장이 파일 기반": README는 기본 저장소 네 개가 메모리 기반이고 WORKING_DIR 아래 로컬 파일로 저장한다고 적음. 이번에 README에 소규모 시험·평가·디버깅용이고 운영용이 아니라는 문장도 있음을 확인
  - LightRAG 임베딩 "권한다": README 표현은 "a solid choice"(로컬 배포 기준). 표에 원문 표현을 씀
  - Neo4j "LLM API 키 필요": labs 페이지에 없음. README는 OpenAI 모델에 OpenAI 키 필요, Ollama 로컬 설정 있음. 로컬 모델만으로 키 없이 되는지는 명시 없음
  - 디스크 "약 6.7GiB": 2026-10-05 값. 2026-10-07 17:25 `df -h ~` 3.6GiB
- 8절 통제군: 지시는 "05에서 C3·C1이 모두 걸러졌기 때문에"였으나 findings상 C1은 통제군이 아니라 부분 오류 쌍이다. 통제군(P8, C3)과 부분 오류 쌍(C1)을 나눠 적음
- 8절 근거 범위: findings 발견 9의 좁힌 결론(주장이 조각 밖 요소를 담을 때 범위가 판정을 바꿈)을 함께 적음
- 8절에 지시의 네 가지 말고 findings에서 재현성(발견 12), 단위·잘린 주장(발견 8·10), 척도·사람 판정 독립성(발견 13, 한계 8)을 더함. 리포트 그래프에서 같은 결과가 나오는지는 시험하지 않았다는 점을 8절 머리에 적음

### 07 계획서 7절 결론 재검토 기록 (지시 5)

- 결론("세 도구 모두 지금 조건에서 실행 불가, 1단계는 수동")은 그대로 성립. 근거를 도구별로 고침
  - MS GraphRAG: API 경로는 유료 API 키 없음. 로컬 경로가 있음(모델 설정 문서: OpenAI가 기본, LiteLLM으로 다른 모델 가능, 모델이 JSON 구조화 출력을 내야 함, Ollama 같은 프록시에서 JSON 오류가 잦다고 적음). 로컬 경로를 막는 것은 확인 부족(8GB 메모리·디스크 3.7GiB에 올릴 모델이 그 출력을 안정적으로 내는지 모름)
  - LightRAG: 로컬 경로를 막는 것은 하드웨어 부족. README의 "reasonable minimum" Qwen3-30B-A3B-Instruct는 30.5B 파라미터·BF16(Hugging Face 페이지)이라 원본 가중치 약 61GB(30.5B × 2바이트로 Claude Code가 계산). 양자화판 크기는 확인하지 않음. README의 모델 이름과 Hugging Face의 2507판이 같은 것인지는 확인 필요
  - Neo4j LLM Graph Builder: 로컬 경로(Ollama)를 막는 이유는 API 키가 아님. 필요한 모델 크기가 명시돼 있지 않아 지금 하드웨어로 되는지 확인 부족. 실행되더라도 슬라이드형 자료에 덜 적합
- 바뀐 것: 2단계 조건을 "API 키가 생기면"에서 "API 키가 생기거나, 로컬 모델을 올릴 하드웨어가 생기거나, 작은 로컬 모델로 추출이 되는지 확인되면"으로 넓힘. 세 도구 모두 로컬 경로가 있어 API 키만이 막는 이유가 아니었기 때문
- 새로 확인한 사실: MS GraphRAG도 로컬 모델 경로가 있다. 지시 4 때는 README만 봐서 확인하지 못했던 것

### Cowork 설명이 원문과 달랐던 건 (지시 4·5, 에드워드 지시로 기록)

- 지시 4로 받은 설명 네 가지가 원문과 달랐고, Claude Code가 원문을 열어 잡았다
  1. MS GraphRAG "유료 API 키가 전제": README에 없음. 모델 설정 문서는 로컬 모델 경로도 적음
  2. LightRAG "기본 저장이 파일 기반": README는 기본 저장소 네 개가 메모리 기반, 로컬 파일은 저장용
  3. Neo4j LLM Graph Builder "LLM API 키가 필요": labs 페이지에 없음. 저장소 README에는 OpenAI 모델용 키와 Ollama 로컬 설정이 함께 있음
  4. 디스크 "약 6.7GiB": 2026-10-05 값. 2026-10-06에 이미 3.9GiB, 2026-10-07에 3.6~3.7GiB였음. 이틀 전 값을 갱신하지 않고 쓴 것
- 1~3은 2026-10-06 "07 계획서 확인 기록"에서 Claude Code가 이미 원문과 다르다고 적은 내용이다. 지시 4가 같은 설명을 다시 담고 있었다
- Neo4j 건은 Cowork가 웹 페이지 요약 모델의 추론을 문서에 적힌 사실처럼 옮긴 것이다(에드워드 전언. Cowork가 어떤 경로로 이 설명을 만들었는지 Claude Code는 확인할 수 없음)
- 에드워드는 이번이 Cowork의 미확인 추정을 Claude Code가 잡은 네 번째 사례라고 함. 앞의 세 건으로 든 것은 9월 존재하지 않는 폴더 가정, 10-05 P9 가설의 "명칭은 조 제목에만 있다", 10-06 실험 01 "파싱 실패 0"의 원인 설명
- 기록과 대조(Claude Code): 위 2026-10-06 "문제와 대처"에 적은 대로, 10-05 건에서 Cowork가 쓴 것은 처음 P9 가설("제1항 본문에 주체와 의무가 있다")이고, "명칭은 조 제목에만 있다"는 Claude Code가 보고하면서 쓴 문장(기록상 "에이전트 오류(Claude Code)")이다. 그래서 기록 기준으로는 네 건이 9월 폴더 가정(지시문 작성자는 전언), 10-05 처음 P9 가설, 10-06 "파싱 실패 0" 원인 설명, 이번 도구·환경 설명 네 가지다. 건수(네 번째)는 같고, 10-05 건의 내용이 다르다

### 커밋

-

### Pages URL

- 변경 없음

### 문제와 대처

- Cowork가 준 판단 기록 문단에서 모델 가중치 수치(3.13GB / 1.42GB)를 "기록으로 확인된 것"으로 적었으나 worklog에는 없는 값이었다. Cowork가 10-05에 외부에서 확인한 값인데 저장소에 남기지 않은 것이다. Claude Code가 대조해 잡았고, 출처를 붙여 정정했다.
- 디스크 사용률 97%는 10-05 값인데 10-04에 붙여 쓴 것도 함께 정정했다.
- 이번이 Cowork의 미확인·출처 없는 서술을 Claude Code가 잡아낸 다섯 번째 사례다.

### 다음 작업

- 에드워드: answer-key-04.md Q6·Q7 사람 판정 채우기, results-04.md 비교 절 검토(특히 P29·P35 단락이 양쪽 근거만 옮기고 해석을 더하지 않았는지)
- findings.md에 실험 04 결과 반영 여부 결정

### 판단 기록 — AI 제안 / 내 선택 / 이유 (멘토 피드백 ③)

작성: 에드워드, 2026-10-08. 대상 장면은 2026-10-04 MiniCheck를 접고 서브에이전트로 바꾼 결정이다.

AI가 제안한 것: Cowork가 네 가지를 제시했다. (1) Claude Code를 판정기로 쓰기
(2) Claude Code 먼저 하고 MiniCheck 나중에 (3) MiniCheck를 더 작은 모델(roberta-large, 1.42GB)로 계속
(4) 거기서 멈추고 findings 정리.

내가 채택하거나 고친 것: (1)을 골랐다. 그리고 Cowork가 제안하지 않은 것을 추가로 물었다 —
이미 설치한 MiniCheck 가상환경을 지우라는 지시도 있어야 하지 않느냐.

그렇게 판단한 이유: 저장용량이 부족했다. roberta-large로 줄여도 결국 용량을 쓰는 건 같아서,
아예 설치가 필요 없는 쪽으로 갔다.

그 뒤 확인된 것: 2026-10-04 MiniCheck 설치 후 디스크 여유 7.2GiB, 가상환경만으로 1.1GB 사용
(worklog 2026-10-04·10-05). 2026-10-07 기준 여유 3.6GiB(deep/07-graphrag/plan.md).
모델 가중치는 flan-t5-large 3.13GB, roberta-large 1.42GB로, Claude Cowork가 2026-10-05에
HuggingFace 파일 목록에서 확인했다.
- https://huggingface.co/lytang/MiniCheck-Flan-T5-Large/tree/main
- https://huggingface.co/lytang/MiniCheck-RoBERTa-Large/tree/main
10-04 시점의 디스크 사용률은 worklog에 기록돼 있지 않다.

## 2026-10-08

### 목표

멘토 피드백에 대한 답을 07 계획서에 넣음

### Claude Code에 준 지시

1. deep/07-graphrag/plan.md 1절 바로 뒤에 "왜 이 주제와 개체·관계를 골랐나" 절을 에드워드가 쓴 문구 그대로 추가(멘토 피드백 "주제와 개체·관계를 왜 그렇게 골랐는지 짧게 설명해 달라"에 대한 답). 5절 "근거 유형을 왜 넣는지" 단락이 어긋나면 위 절을 가리키는 한 줄을 붙임. 위 절 문구는 고치지 않음. commit·push 하지 않음.
2. README.md "문서 목록" 바로 위에 "## 2026-10-11 발표 요약"과 같은 페이지 앵커 목차(8개) 추가. 별도 파일 만들지 않음, 기존 내용 지우지 않음. findings.md·results-01~04·plan.md에 있는 것만 옮기고 숫자는 파일에서 확인. 각 절 끝에 출처 링크와 "목차로" 링크. 배포된 페이지에서 목차 링크 여덟 개 동작 확인. commit·push 하지 않음.
3. README.md 발표 요약의 발견 1·2·3 절에 "어떤 경험에서 나온 발견인지" 설명 보강. [1] 발견 1 맨 앞에 Q5 질문·기대 답·답변 단락 [2] 발견 2 표 앞에 P7의 출처·갈린 판정·건넨 조각 단락 [3] 발견 3 불릿 뒤에 "원인" 소절(0건 원인 / 구조를 틀리게 읽은 원인). 원본과 다르면 고치지 말고 보고. commit·push 하지 않음.
4. (2026-10-10 지시) README.md 발표 요약에 "### 멘토 피드백에 무엇을 했나" 절을 "### 무엇을 했나" 뒤, "### 발견 1" 앞에 추가하고 목차에도 넣음(목차 9개). ①은 worklog 10-06·10-07 "Claude Code에 준 지시"에서 확인되는 것만(완료 기준 개수, 방법을 정한 주체, 중단 조건, 1번 채택), ②는 findings 한계 10과 worklog 10-06에서 확인되는 것만(파일 분리, 서브에이전트 도구 차단, 대화창 붙여 넣기로 노출, 세션 버림, 날짜·시각), ③은 "판단 기록" 절 링크와 세 줄 요지를 고쳐 쓰지 않고 인용. 기존 절은 고치지 않음, answer-key-04.md 읽지 않음, commit·push 하지 않음.

### 읽은 파일

- deep/07-graphrag/plan.md (절 구성, 5절 "근거 유형"을 넣는 이유)
- (지시 2) README.md, deep/05-citation/findings.md, experiments/results-03.md(비교 표), scripts/ 네 개의 머리 주석, 배포 페이지 https://chihun-an.github.io/rag-field-scan/ 와 https://chihun-an.github.io/rag-field-scan/deep/05-citation/findings.html (Claude 내장 브라우저, 제목 id 규칙 확인, 2026-10-08)
- (지시 3) results-01.md Q2·Q5, pairs-01-ko.md P7, data/sanan-law.md 제15조, results-04.md "층위 1 첫 실행" 터미널 출력과 원인 표
- (지시 4, 2026-10-10) README.md, worklog.md 2026-10-06·10-07 "Claude Code에 준 지시", 2026-10-06 "문제와 대처"(11:02·11:28 기록), "판단 기록" 절, deep/05-citation/findings.md 한계 10, 배포 페이지 https://chihun-an.github.io/rag-field-scan/worklog.html (내장 브라우저, "판단 기록" 제목 id 확인). 멘토 피드백 ①②의 원래 문구는 저장소에서 찾지 못함(grep "멘토")

### 만든·고친 파일

- deep/07-graphrag/plan.md: 수정 (2026-10-08, Claude Code, 지시 1) — 1절 뒤, 2절 앞에 "## 왜 이 주제와 개체·관계를 골랐나" 절 추가. 이 절은 에드워드가 쓴 설명이고(절 안에 "작성: 에드워드, 2026-10-08"), Claude Code는 문구를 다듬거나 바꾸지 않고 옮겼다. 5절 "근거 유형"을 넣는 이유 단락 끝에 위 절을 가리키는 한 줄을 붙였다. 판단: 5절 단락은 "세 펌이 서로 다른 종류의 근거를 쓰는지 비교"를 이유로 들고, 에드워드의 절은 "다섯 유형마다 원출처로 되짚을 수 있는 정도가 다르다"를 핵심 이유로 든다. 서로 모순되지는 않지만 드는 이유가 달라 한 줄을 붙임. 5절 단락 본문은 고치지 않음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-08, Claude Code, 지시 1) — 이 항목 추가. commit·push는 하지 않음
- README.md: 수정 (2026-10-08, Claude Code, 지시 2) — "## 2026-10-11 발표 요약" 절(목차 8개, 하위 절 8개: 무엇을 했나 / 발견 1~3 / 빗나간 예측 / 07 GraphRAG / 한계 / 만든 에이전트와 스크립트) 추가. 기존 절(결론, 배포 URL, 출발 질문, 문서 목록)은 고치지 않음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-08, Claude Code, 지시 2). commit·push는 하지 않음
- README.md: 수정 (2026-10-08, Claude Code, 지시 3) — 발견 1 맨 앞 단락, 발견 2 표 앞 단락, 발견 3 "#### 원인" 소절 추가. 출처 줄·"목차로" 링크는 그대로. 받은 사실은 원본과 모두 맞음. 다만 제18조 터미널 줄은 지시에 앞부분만 있었고, 원본 줄 전체(뒤에 "/ 호 15개 ②: 1~10 / ③: 1~5")를 그대로 옮김. 추가 뒤 목차 앵커 재확인(어긋남 0, 중복 id 0). commit·push는 하지 않음
- worklog.md: 수정 (2026-10-08, Claude Code, 지시 3). commit·push는 하지 않음
- README.md: 수정 (2026-10-10, Claude Code, 지시 4) — 목차에 "멘토 피드백에 무엇을 했나" 링크 추가(9개), 같은 이름의 절 추가(① 지시 방식 / ② 정답표 격리 / ③ AI 제안·내 선택·이유, 출처 줄과 "목차로" 링크). 기존 절은 고치지 않음. 확인: 목차 링크 9개 모두 제목 id와 맞음, 중복 id 0, worklog "판단 기록" 앵커 1곳과 맞음. commit·push는 하지 않음
- worklog.md: 수정 (2026-10-10, Claude Code, 지시 4). commit·push는 하지 않음

### 멘토 피드백 절 기록 (지시 4, 2026-10-10)

- ① 근거: 2026-10-06 지시 6(완료 기준 7개, 방법은 Claude Code가 정함, 회귀 검사 다르면 보고하고 멈춤), 지시 9(완료 기준 6개, C3 중단 조건), 지시 7(회귀 차이는 1번 채택). 10-06·10-07의 다른 지시는 worklog에 완료 기준 개수나 방법을 정한 주체가 적혀 있지 않아 쓰지 않음. 지시 9의 방법을 누가 정했는지도 worklog 요약에 없어 쓰지 않음
- ② 근거: findings 한계 10, worklog 2026-10-06 "문제와 대처"(11:02 세션에서 Claude Code가 빈 틀 answer-key-04.md를 읽은 에이전트 오류, 11:28 기대 답 노출, 대처: 세션 버리고 새 세션), 지시 2의 (5)(메인 세션은 규칙으로만 막힘), 지시 5(새 세션 13:17 시작). 지시에 없던 11:02 읽기 오류도 같은 기록에 있어 함께 적음(실패를 줄여 쓰지 않으려고)
- ③: "판단 기록" 절의 원문 문장을 그대로 인용. 원문의 줄바꿈만 공백으로 이었고 낱말은 바꾸지 않음
- 지시와 기록이 다른 점: 지시는 "판단 기록" 절을 "worklog.md 2026-10-08"이라고 했으나, 이 절은 2026-10-07 항목 끝에 있다(2026-10-08 지시로 그 자리에 넣었고, 절 안에 "작성: 에드워드, 2026-10-08"). 배포 페이지에서도 "## 2026-10-07" 아래에 있음. README에서는 날짜 항목을 쓰지 않고 절로 링크함
- 앵커: 배포 페이지의 실제 id가 `판단-기록--ai-제안--내-선택--이유-멘토-피드백-`(③이 빠지고 끝이 하이픈)임을 확인함. 지시 2 때 쓴 앵커 계산은 ③을 남겼을 것이라, 배포 페이지 id로 계산 규칙을 고쳐(글자·결합 문자·10진 숫자·밑줄만 남김) 다시 확인함
- 멘토 피드백 ①②의 원래 문구는 저장소에 없고, AGENTS.md "공개 금지"에 멘토링 평가서가 있어 인용하지 않음. 절 안의 "지시 방식", "정답표 격리"는 한 일을 가리키는 이름이다

### README 발표 요약 기록 (지시 2)

- 앵커 규칙 확인: 배포 페이지의 기존 제목 id를 내장 브라우저로 읽음. findings.html에서 "발견 1 — 번호가 …" → `발견-1--번호가-…`, "발견 9 — 예측 [A]는 빗나갔다: …" → `발견-9--예측-a는-빗나갔다-…`, "1차 과제와의 연결" → `1차-과제와의-연결`. 즉 소문자화, 글자·숫자·하이픈·공백 외 문자(—, [], :, (), 따옴표) 제거, 공백 → 하이픈, 앞자리 숫자 유지. github.com 규칙과 같음
- 이 규칙으로 README 제목 id를 계산해 목차 링크 8개와 "목차로" 링크(#2026-10-11-발표-요약)가 모두 제목 id와 맞는 것을 스크립트로 확인함(어긋남 0)
- 배포 페이지 확인은 아직 못 함: 배포 페이지는 main에 push된 내용만 반영하는데, 이 수정은 commit·push 전이다. push 뒤 https://chihun-an.github.io/rag-field-scan/ 에서 목차 링크 8개를 눌러 확인해야 한다
- 숫자 출처: 실험 01 층위 1 29건·층위 2 8쌍(findings 발견 1, results-01-layer2.md), 실험 02 9회·03 6회(results-02.md, results-03.md), 실험 04 층위 1 16건(results-04-layer1.md), 쌍 34·호출 46(results-04-layer2.md), 표본 17·일치 14/같은 쪽 1/불일치 2(results-04.md). citation-judge 69회는 8+9+6+46을 더한 값
- "만든 에이전트와 스크립트" 표의 스크립트 칸은 실행 횟수가 아니라 어떤 결과를 냈는지 적음. 스크립트 실행 횟수는 회귀 검사·시험 실행이 섞여 있어 한 숫자로 세지 않음

## 2026-10-10 (Claude Cowork가 저장소 파일을 직접 고침)

### 경위

Claude Code가 주간 사용 한도에 걸려(한도 재설정 2026-10-10 15:00) 아래 두 가지는 Claude Cowork가 저장소 파일을 직접 고쳤다. 에드워드가 지시하고 확인했고, commit·push는 에드워드가 했다. 지금까지의 파일 수정은 모두 Claude Code가 했으므로, 수정 주체가 다른 것을 여기에 적는다.

### 고친 파일

- README.md, deep/05-citation/experiments/results-04-layer2.md: `예측 [A](판정 전)`을 `예측 A(판정 전)`으로 고침. 마크다운이 `[A](판정 전)`을 링크로 해석해, 배포 페이지에서 "판정 전"이라는 글자가 보이지 않고 `판정 전`으로 가는 죽은 링크가 생겨 있었다. 내장 브라우저로 배포 페이지 DOM을 읽어 확인한 뒤 고침(링크 href가 "판정 전", 보이는 글자는 "예측 A:"뿐이었다)
- README.md: 발표 요약의 "### 멘토 피드백에 무엇을 했나" 제목을 "### 작업 방식"으로 바꾸고 목차 링크도 같이 바꿈. 절 첫 줄에 "지시 설계, 정답표 격리, 판단 기록 세 가지다. 멘토 피드백 ①②③에 대한 답이기도 하다."를 추가. 절 본문(①②③)과 출처 줄은 고치지 않음. 제목을 바꾼 이유는 에드워드 판단으로, 멘토링이 끝난 뒤에도 남는 저장소에 "시킨 것을 했다"는 제목이 맞지 않는다고 봤기 때문이다

### 확인

- 배포 페이지(2026-10-10 푸시분, 커밋 e1759aa) 전수 조사: 페이지 안 링크 33개 중 어긋난 것 0. URL 형태가 아닌 href는 `판정 전` 하나뿐이었고 그것을 고침
- 제목을 바꾼 뒤 목차 링크 9개와 제목 id를 다시 대조(어긋남 0, 중복 id 0)
- 위 수정은 아직 commit·push 전이다. push 뒤 배포 페이지에서 "작업 방식" 목차 링크와 "판정 전" 표시를 다시 확인해야 한다

## 2026-10-12

### 목표

저장소에 올라간 macOS·R 임시 파일을 git에서 빼고, 다시 올라가지 않게 막음

### Claude Code에 준 지시

1. git이 추적 중인 임시 파일 네 개(.DS_Store, deep/.DS_Store, deep/05-citation/.DS_Store, deep/05-citation/experiments/.Rhistory(빈 파일))를 git 추적에서 빼고 디스크에서도 지움
2. .gitignore에 .DS_Store와 .Rhistory를 추가해 어느 폴더에 생겨도 무시되게 함. 기존 .gitignore 내용과 주석은 그대로 둠
3. git ls-files 결과에 .DS_Store와 .Rhistory가 하나도 없는지 확인
4. 위 네 파일과 .gitignore, worklog.md 말고는 아무 파일도 바꾸지 않음
5. worklog.md에 2026-10-12 항목을 만들고 이 지시, 지운 파일 경로, .gitignore에 추가한 줄, 3번 확인 결과를 기록
6. commit·push 하지 않음

### 읽은 파일

- AGENTS.md, README.md(앞부분), worklog.md(처음과 마지막 항목), .gitignore
- `git ls-files`, `git status` 출력

### 만든·고친 파일

- 지움 (2026-10-12 13:32경, Claude Code, `git rm`으로 추적 해제와 디스크 삭제를 함께 함. 파일 삭제는 에드워드가 이 지시로 승인함):
  - .DS_Store
  - deep/.DS_Store
  - deep/05-citation/.DS_Store
  - deep/05-citation/experiments/.Rhistory
- .gitignore: 수정 (2026-10-12, Claude Code) — 기존 두 묶음과 주석은 그대로 두고 맨 끝에 아래 세 줄을 추가함. 슬래시 없는 패턴이라 어느 폴더에서든 맞는다

  ```
  # macOS·R이 자동으로 만드는 임시 파일은 어느 폴더에서든 올리지 않는다
  .DS_Store
  .Rhistory
  ```

- worklog.md: 수정 (2026-10-12, Claude Code) — 이 항목 추가

### 확인

- `git ls-files | grep -cE '(^|/)\.(DS_Store|Rhistory)$'` → 0. 추적 중인 .DS_Store·.Rhistory 없음
- 위 네 경로가 디스크에 남아 있지 않음(`ls -a`로 확인)
- `git check-ignore -v --no-index deep/07-graphrag/.DS_Store areas/x/.Rhistory` → 둘 다 .gitignore 10·11번 줄에 걸림. 하위 폴더에서도 무시됨
- `git status --short`: 네 파일 삭제(D, 스테이징됨), .gitignore 수정(M). 그 밖에 바뀐 파일 없음(이 worklog.md 수정 제외)
- commit·push는 하지 않음. 네 파일의 삭제는 `git rm`으로 스테이징만 된 상태이고, commit은 에드워드가 한다

### 3주 챌린지 작업 공간 (2026-10-12 17:44경, Claude Code)

#### 2번 도메인 변경

2번 도메인 변경 승인을 요청했고, 답이 오기 전에 진행하며, 거절되면 defense/ 폴더를 새로 만들어 전환한다.

- 두 도메인: 1번 AI 컨설팅, 2번 무역 & 기름(지금 다루는 제품 UMO, ULO, PPO)
- 2번은 원래 방산으로 받았고, 2026-10-12에 에드워드가 무역 & 기름으로 바꾸는 승인을 요청함

#### Claude Code에 준 지시

목표: 3주 챌린지(두 도메인 GraphRAG)를 시작하기 위해 deep/07-graphrag/ 안에 도메인별 작업 공간을 만들고, 2번 도메인을 바꾸기로 한 사실을 기록한다.

1. deep/07-graphrag/ 아래에 ai-consulting/, oil-trade/, shared/ 세 폴더를 만들고 각 폴더에 README.md(폴더가 무엇을 담는지 두세 줄)를 둠. shared/는 골든 룰 검사 스크립트처럼 도메인과 상관없는 도구를 두는 곳
2. deep/07-graphrag/README.md를 새로 만들어 폴더 구조, 두 도메인 이름, 2번 도메인이 승인 대기 중이라는 사실, 기존 plan.md·papers.md·tools.md가 이전 과제(MBB 리포트) 계획이라는 것을 적음. 기존 세 파일은 고치지 않음
3. AGENTS.md "공개 금지"에 "무역 & 기름 도메인의 실무 정보(거래처, 가격, 계약 조건, 받은 서류)는 저장소에 올리지 않는다"를 한 줄 추가. 다른 줄은 고치지 않음
4. worklog.md의 2026-10-12 항목에 이어서 이 지시와 2번 도메인 변경 사실을 기록
5. 위 파일 말고는 바꾸지 않음. commit·push 하지 않음

#### 읽은 파일

- AGENTS.md "공개 금지" 절
- deep/07-graphrag/plan.md·papers.md·tools.md 앞부분(이전 과제 계획인지 확인. 고치지 않음)
- 저장소 전체에서 "골든"·"golden"을 찾았으나 나오지 않음. 골든 룰이 무엇인지는 저장소에 정의가 없어, shared/README.md에는 지시 문구("골든 룰 검사 스크립트처럼")만 옮기고 내용은 풀어 쓰지 않음

#### 만든·고친 파일

- deep/07-graphrag/README.md: 새로 만듦 — 두 도메인 표(2번 "승인 대기 중"), 변경 경위와 거절 시 defense/ 전환, 폴더 구조, 기존 세 파일이 이전 과제 계획이라는 설명
- deep/07-graphrag/ai-consulting/README.md: 새로 만듦
- deep/07-graphrag/oil-trade/README.md: 새로 만듦 — 승인 대기 중이라는 사실과 실무 정보를 두지 않는다는 줄 포함
- deep/07-graphrag/shared/README.md: 새로 만듦
- AGENTS.md: 수정 — "공개 금지" 끝에 위 한 줄 추가. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 방침 변경 (2026-10-12 17:53경, Claude Code)

2번 도메인(무역 & 기름)의 진행 방침을 바꿨다. 위 절의 기록과 지시 원문은 그때 방침 그대로 두고 고치지 않았다.

- 이전 방침: 2번 도메인 변경 승인을 요청했고, 답이 오기 전에 진행하며, 거절되면 defense/ 폴더를 새로 만들어 전환한다
- 새 방침: 멘토 답이 오기 전까지 2번 도메인 작업은 하지 않고 대기한다. 승인되면 무역 & 기름으로 진행하고, 기존의 방산 도메인을 유지하라는 지침이 있으면 방산으로 다시 바꾼 뒤 진행한다. 1번 AI 컨설팅은 그대로 진행한다
- 바꾼 이유: 멘토 승인 없이 진행하면 의견을 무시하는 것으로 보일 수 있어서(에드워드 판단)

#### Claude Code에 준 지시

1. deep/07-graphrag/README.md에서 "답이 오기 전에 진행한다"와 거절 시 전환 문장을 새 방침으로 바꿈. 표의 상태 "승인 대기 중"은 그대로 둠
2. deep/07-graphrag/oil-trade/README.md도 새 방침과 어긋나는 문장이 있으면 맞춤
3. worklog.md에 이미 적힌 기록(지시 원문 포함)은 고치지 않고, 2026-10-12 항목 끝에 이 절을 덧붙임
4. 위 파일 말고는 바꾸지 않음. commit·push 하지 않음

#### 읽은 파일

- deep/07-graphrag/README.md, deep/07-graphrag/oil-trade/README.md

#### 만든·고친 파일

- deep/07-graphrag/README.md: 수정 — 두 도메인 표 아래 문단의 "답이 오기 전에 진행한다. 거절되면 defense/ 폴더를 새로 만들어 방산으로 전환한다."를 새 방침 문장으로 바꿈. 표의 상태 "승인 대기 중"과 폴더 구조는 그대로 둠
- deep/07-graphrag/oil-trade/README.md: 고치지 않음 — "승인 대기 중이다(2026-10-12 요청)"만 있고 진행·전환을 말하는 문장이 없어 새 방침과 어긋나지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

## 2026-10-13

### 목표

E1(두 도메인 범위 + 분류 축 결정)을 deep/07-graphrag/e1-decisions.md에 기록

### Claude Code에 준 지시

1. deep/07-graphrag/e1-decisions.md를 새로 만들고 다음을 적음
   - 1번 AI 컨설팅 범위: 컨설팅 펌이 공개한 AI 도입 사례. 대상 펌은 McKinsey, BCG, Bain, Deloitte, PwC, EY, KPMG 일곱 곳
   - 2번 무역 & 기름: 멘토 승인 대기 중. 범위는 승인 뒤에 정함(07 README 링크)
   - 분류 축: 업무 유형(잠정). 2번 도메인 답이 오면 확정
   - 판단 기록: 세 항목(AI가 제안한 것 / 내가 채택하거나 고친 것 / 그렇게 판단한 이유)을 글자 그대로 옮기고, 맨 위에 "작성: 에드워드, 2026-10-13. 1항은 Cowork가 사실을 정리했고, 2·3항은 에드워드가 쓰고 Cowork가 문장만 다듬음"을 적음
2. deep/07-graphrag/README.md에 e1-decisions.md로 가는 링크를 한 줄 추가. 다른 문장은 고치지 않음
3. worklog.md에 2026-10-13 항목을 만들고 이 지시와 만든·고친 파일을 기록
4. 위 파일 말고는 바꾸지 않음. commit·push 하지 않음

첫 지시에는 판단 기록 세 항목이 "(위 완성본 1항 그대로)" 같은 자리표시로만 있고 원문이 없었다. Claude Code가 내용을 채우지 않고 원문을 요청했고, 에드워드가 세 항목 원문을 따로 보내 줌(2026-10-13).

### 읽은 파일

- deep/07-graphrag/README.md
- worklog.md 끝부분(2026-10-12 항목)

### 만든·고친 파일

- deep/07-graphrag/e1-decisions.md: 새로 만듦 (2026-10-13 15:02경, Claude Code) — 1번 범위와 대상 펌 일곱 곳, 2번 승인 대기(07 README 링크), 분류 축 업무 유형(잠정), 판단 기록. 판단 기록 세 항목은 에드워드가 보낸 원문을 글자 그대로 옮기고 고치지 않음
- deep/07-graphrag/README.md: 수정 — 두 도메인 문단 뒤에 "E1 결정(두 도메인 범위와 분류 축): [e1-decisions.md](e1-decisions.md)" 한 줄 추가. 다른 문장과 폴더 구조 블록은 고치지 않음(그래서 폴더 구조 블록에는 e1-decisions.md가 아직 없다)
- worklog.md: 수정 — 이 항목 추가
- commit·push는 하지 않음

### 1번 도메인 원천 원장 (2026-10-13 15:20경~16:50경, Claude Code)

#### Claude Code에 준 지시

목표: 1번 도메인(AI 컨설팅)의 원천 원장을 만든다. 원장은 나중에 그래프를 만들 자료의 목록이다. 검색 방법과 파일 형식은 Claude Code가 정한다. 범위는 E1 결정(컨설팅 펌이 공개한 AI 도입 사례, McKinsey·BCG·Bain·Deloitte·PwC·EY·KPMG).

- 넣는 기준: 펌 공식 사이트의 고객 사례 페이지, AI(머신러닝, 생성형 AI 등)가 해결책의 중심, 고객이 겪던 문제와 펌이 한 일이 본문에 있음
- 빼는 것: 리포트·서베이·의견 기사, 펌 자체 제품 광고, 언론 보도만 있는 사례

1. deep/07-graphrag/ai-consulting/에 원장 파일. 스크립트로 읽을 수 있고 깃허브에서 표로 보이는 형식
2. 총 15~20건, 펌마다 2건 이상
3. 원장 칸은 서지 정보만(번호, 펌, 제목, URL, 발행일(없으면 "확인 불가"), 확인한 날짜, 원문 저장 경로, 원문 해시(SHA-256)). 업무 유형·병목·해결책·고객 산업은 적지 않음(사람 그래프를 에이전트 결과를 보지 않고 먼저 만들어야 하므로)
4. 찾았지만 기준에 안 맞거나 읽지 못한 자료도 따로 표로(URL, 이유)
5. 각 사례 본문을 ai-consulting/raw/에 저장하고 이 폴더는 .gitignore에 넣음(저작권). 해시는 이 파일 기준
6. 15건이 안 되면 원장을 쓰지 말고 멈춰서 펌별 건수 보고
7. worklog 2026-10-13 항목에 이 지시, 검색 방법, 펌별 건수, 만든·고친 파일 기록
8. 위 파일 말고는 바꾸지 않음. commit·push 하지 않음

#### 검색·수집 방법

- 후보 찾기: 펌마다 WebSearch(대상 도메인으로 제한)로 "client story / case study / client results + AI" 검색. 펌 사이트의 사례 목록 페이지(McKinsey Tech and AI case studies, PwC 사례 라이브러리, EY AI case studies)에서 링크를 더 찾음. 검색 결과 요약이 아니라 페이지 본문을 직접 읽고 넣는 기준을 판정함
- 본문 저장: curl로 직접 받으려 했으나 McKinsey(응답 없음), BCG·Bain·PwC(403)가 막아서, 모든 페이지를 Claude 내장 브라우저로 열어 읽음. 저장 텍스트 규칙: 페이지의 본문 요소(main이 있으면 main, 없으면 사례 첫 문장과 마지막 문장을 함께 담는 가장 안쪽 요소, 그것이 페이지 전체이면 제목 줄부터 마지막 본문 문장까지)의 innerText. 줄 끝 공백 제거, 줄바꿈 3개 이상은 2개로, 끝에 줄바꿈 하나. 이 규칙이라 관련 사례 목록·담당자 이름 같은 주변 글이 일부 섞인 파일이 있음
- 해시 검증: 브라우저 안에서 같은 텍스트의 SHA-256을 계산하고, 파일로 쓴 뒤 shasum -a 256 값과 대조함. 브라우저에서 읽은 15건 모두 일치
- Bain: 내장 브라우저에서 Cloudflare 사람 확인(체크박스)이 떠서 Claude Code는 누르지 않음. 에드워드가 눌러도 내장 브라우저가 봇으로 인식해 통과되지 않았고, 에드워드가 구글 크롬에서 페이지를 PDF로 저장해 줌(InsuranceCo 1개 2026-10-13 16:32, 이어서 검색 결과 10개 묶음 Desktop/Bain 16:37~16:38). Claude Code가 macOS 기본 PDFKit(JXA, `osascript -l JavaScript`)로 텍스트를 추출해 raw/에 저장. 설치한 도구 없음(pdftotext·pypdf·PyMuPDF는 없었음). 이 두 파일은 브라우저 텍스트가 아니라 PDF 추출 텍스트라 인쇄 머리글·바닥글(날짜, URL, 쪽 번호)이 섞여 있고, InsuranceCo의 "five-part plan" 목록 내용은 PDF에서 "."만 남아 빠져 있음
- 발행일 규칙: 페이지에 보이는 날짜 → 없으면 메타·JSON-LD의 발행일 → 메타 값끼리 서로 다르면 "확인 불가". 관련 사례 목록에 붙은 다른 글의 날짜는 쓰지 않음
  - 페이지 표시: 2(2024-11-13), 10(2026-01-07)
  - 메타: 3(JSON-LD datePublished 2026-02-04, itemdate 같음), 11(pwcReleaseDate 2026-08-31), 12(firstpublishdate와 dateuser 모두 2024-09-16)
  - 메타 값이 서로 달라 확인 불가: 13(firstpublishdate 2023-02-02 / dateuser 2023-01-17), 14(2026-10-12 / 2024-10-15), 15(publishDate 2025-01-21 / displayDate 2025-04-14), 16(2022-06-15 / 2024-02-09), 17(2021-01-01 / 2023-08-30)
  - 날짜 정보 없음: 1, 4, 5, 6, 7, 8, 9. 7의 PDF에 있는 "November 22, 2024"는 페이지 안 보도자료 묶음의 날짜라 쓰지 않음
- 형식: CSV. GitHub에서 표로 보이고 csv 모듈로 바로 읽힌다. AGENTS.md "모든 문서는 Markdown"과 다르지만, 원장은 문서가 아니라 데이터 파일로 보고 CSV로 함(확인 필요: 에드워드가 다르게 보면 바꿈)

#### 펌별 건수 (원장 17건)

| 펌 | 원장 | 제외 표 |
|----|------|---------|
| McKinsey | 3 | 4 |
| BCG | 2 | 2 |
| Bain | 2 | 9 |
| Deloitte | 2 | 0 |
| PwC | 2 | 1 |
| EY | 3 | 3 |
| KPMG | 3 | 0 |
| 합계 | 17 | 19 |

- 펌마다 2건을 먼저 채운 뒤(14건) 15건 기준을 넘기려고 EY·KPMG·McKinsey에서 1건씩 더 넣음. 세 펌을 고른 이유는 사례 목록에서 기준에 맞는 후보가 바로 보였기 때문이고, 다른 기준은 없음
- 판정이 얇은 것: 7(Banca Investis)은 고객 문제가 "서비스 모델의 혁신이 필요했다" 정도로만 적혀 있음. 펌이 한 일은 본문에 있어 넣음. 11(Seattle Mariners)은 고객 인터뷰 형식이지만 펌 사례 라이브러리 페이지이고 문제와 PwC가 한 일이 본문에 있어 넣음
- 제외 표에는 실제로 열어 보았거나 제목·URL로 판단한 것만 적음. 검색 결과에 나왔지만 판단하지 않은 후보(예: BCG Reckitt·KLM, Deloitte Zora 송장 사례, Bain Athena Pathway)는 적지 않음

#### 문제와 대처

- 내장 브라우저에서 로컬 수신 서버(127.0.0.1)로 본문을 보내 저장하려 했으나 브라우저에서 연결되지 않음(Failed to fetch). 임시 수신기(스크래치 폴더의 receiver.py, 저장소 밖)를 멈추고, 본문을 읽어 파일로 쓰고 해시를 대조하는 방식으로 바꿈. 시험할 때 만든 test-probe.txt는 Claude Code가 만든 것이라 바로 지움
- 저장소에 코드 파일은 만들지 않음. 쓴 코드는 브라우저에서 실행한 JavaScript, PDF 추출용 osascript 한 줄, 검증용 python 한 줄뿐이고 모두 이 기록의 방법 설명으로 남김
- McKinsey Aviva 페이지는 THE SOLUTION 절이 로드되지 않아(새로고침 뒤에도 같음) 제외함
- 작업 중 한 번 자동 모드 판정기가 일시적으로 쓸 수 없어 브라우저 실행이 막혔고, 그사이 Bain PDF 작업을 먼저 하고 돌아와 다시 실행함

#### 읽은 파일

- deep/07-graphrag/e1-decisions.md(범위), .gitignore
- 에드워드가 준 PDF: Desktop의 InsuranceCo PDF, Desktop/Bain 폴더의 PDF 중 Banca Investis·NatWest 두 개(나머지 8개는 파일 이름만 확인). Desktop의 다른 파일은 열지 않음
- 웹 페이지 원문은 raw/ 파일과 sources.csv의 URL 참고

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/sources.csv: 새로 만듦 — 원장 17건
- deep/07-graphrag/ai-consulting/excluded.csv: 새로 만듦 — 제외·읽지 못한 자료 19건(펌, URL, 이유)
- deep/07-graphrag/ai-consulting/raw/*.txt: 새로 만듦 — 사례 본문 17개. .gitignore로 저장소에 올라가지 않음
- .gitignore: 수정 — 맨 끝에 `# 사례 원문은 저작권 때문에 저장소에 올리지 않는다 (해시는 원장에 남긴다)`와 `deep/07-graphrag/ai-consulting/raw/` 두 줄 추가. 기존 줄은 그대로
- worklog.md: 수정 — 이 절 추가
- 확인: python csv 모듈로 sources.csv 17행·8열, excluded.csv 19행·3열을 읽음. 원장 해시와 raw 파일 해시 불일치 0. `git check-ignore`로 raw/ 무시 확인. `git status`에는 .gitignore, sources.csv, excluded.csv, worklog.md만 나옴
- commit·push는 하지 않음

### 원장 수정 (2026-10-13, Claude Code)

#### Claude Code에 준 지시

1. raw/ 파일 이름에 고객명·업무·해결책 같은 정보가 들어가 있어, 원장 "원문 저장 경로" 칸을 통해 원장에 그래프 내용을 적지 않기로 한 기준 3과 어긋남. raw/ 파일 이름을 원장 번호만 담은 이름(ac-01.txt ~ ac-17.txt)으로 바꾸고 sources.csv 경로 칸을 맞춤. 바꾼 뒤 해시 17개가 다시 일치하는지 확인. worklog에는 옛 이름과 새 이름의 대응표를 적지 않음
2. AGENTS.md "모든 문서는 Markdown(.md)으로 쓴다." 바로 아래에 "원장·그래프 데이터 같은 데이터 파일은 CSV나 JSON으로 둘 수 있다."를 한 줄 추가. 다른 줄은 고치지 않음
3. worklog 2026-10-13 항목에 기록. commit·push 하지 않음

#### 한 일

- raw/ 파일 17개: 파일 이름에 그래프에 들어갈 정보가 있어 번호로 바꿈. 파일 내용은 바꾸지 않음
- deep/07-graphrag/ai-consulting/sources.csv: 수정 — "원문 저장 경로" 칸을 raw/ac-01.txt ~ raw/ac-17.txt로 바꿈. python csv 모듈로 다시 써서, 쉼표가 없는 제목 칸의 따옴표가 빠짐(읽은 값은 같음)
- AGENTS.md: 수정 — "작업 방식"에 위 한 줄 추가. 다른 줄은 고치지 않음. 이 줄로 앞 절 "형식" 항목의 "확인 필요"가 풀림
- worklog.md: 수정 — 이 절 추가

#### 확인

- sources.csv 17행·8열, 경로 17개가 raw/ac-01.txt ~ raw/ac-17.txt와 정확히 일치, 원장 해시와 파일 해시 불일치 0
- 첫 확인 스크립트가 쓰기 파일을 닫기 전에 다시 읽어 "0행"으로 나왔다(Claude Code 스크립트 오류). 스크립트가 끝난 뒤 다시 읽어 17행·불일치 0을 확인함
- commit·push는 하지 않음

### 인수인계 문서와 Codex 역할 (2026-10-13 17:40경, Claude Code)

#### Claude Code에 준 지시

목표: 두 가지를 한다. (1) Claude 쪽 AI(새 Claude Code 대화, 새 Cowork 세션)가
새 대화를 시작해 이 파일 하나만 읽으면 과제를 이어받을 수 있는 인수인계 문서를
저장소 맨 위에 handoff.md로 만든다. (2) Codex의 역할을 정한 판단 기록을 남긴다.

handoff.md에 들어갈 내용(1쪽 분량 목표, 자세한 건 다른 파일 링크로):
1. 이 저장소가 무엇인가: 출발 질문, 멘토 프로그램 원칙
2. 지금까지의 흐름: 1차 과제, 2차 과제(05 실험의 방법·규모·주요 발견·정답 격리
   사고·한계, 07 계획), 3주 챌린지
3. 3주 챌린지: 핵심 질문, 단계 E0~E7과 마감, 필수선, 지켜야 할 규칙
4. 현재 상태: 단계별 완료·진행·대기 표. 2번 도메인 승인 대기 포함
5. 다음 할 일
6. 역할과 규칙:
   - 에드워드: 지휘, 결정, 사람 그래프, 정답 확인, commit·push
   - Cowork: 단계 설계, 지시문 작성, 결과 검토
   - Claude Code: 주 실행
   - Codex: 판정과 감사만(E5 다른 계열 판정, E4 그래프 맞춰보기 판정, 필요할 때
     골든 룰 검사 스크립트 감사). 조언·설계·계획 검토·생성은 맡기지 않는다.
     백업으로 쓰지 않는다. 결과는 통과/실패와 근거로만 받는다.
   - Codex를 합류시킨 이유: 멘토님이 웹 AI끼리 토론시키는 것보다 데스크톱 AI끼리
     일을 시키는 게 낫다고 조언해서 이를 연습하기 위함(아래 판단 기록 참고)
   - Codex 판정 격리: 판정 대화에는 프로젝트 폴더를 연결하지 않는다. 판정 규칙을
     매 지시문 맨 위에 붙인다. Codex 메모리는 꺼져 있다(2026-10-13 에드워드 확인).
     Codex 맞춤 지시는 비워 둔다. 판정이 끝나면 Codex 화면에 파일·명령 사용
     기록이 없는지 확인한다.
   - 규칙: 정답을 본 대화는 다른 작업에 다시 쓰지 않는다. 동시 편집 금지.
     worklog에 누가 했는지 적는다. handoff.md는 Codex 판정 대화에 주지 않는다.
7. 더 볼 곳: 핵심 파일 링크

완료 기준:
1. handoff.md의 모든 문장은 저장소 파일에서 확인한 것만 쓴다. 확인 못 한 것은
   "확인 필요"로 적고, 숫자는 파일에서 직접 확인한다. 6번의 역할·이유·격리
   방법은 이 지시문을 근거로 쓴다.
2. 정답(기대 답) 파일이 어디 있는지는 적지 않는다.
3. AGENTS.md에 세 줄 추가: "새 대화를 시작하면 handoff.md를 먼저 읽는다",
   "작업을 마치면 handoff.md의 현재 상태와 다음 할 일을 갱신한다",
   "Codex는 판정과 감사만 맡고, 조언·설계·생성은 맡기지 않는다".
   다른 줄은 고치지 않는다.
4. README.md "문서 목록"에 handoff.md 링크 한 줄 추가.
5. worklog.md 2026-10-13 항목에 이 지시와 아래 판단 기록을 글자 그대로 옮긴다.
   판단 기록 맨 위에 "작성: 에드워드, 2026-10-13. 1항은 Cowork가 사실을
   정리했고, 2·3항은 에드워드의 말을 Cowork가 정리함"을 적는다.
6. commit·push 하지 않는다.

#### 판단 기록 — Codex의 역할

작성: 에드워드, 2026-10-13. 1항은 Cowork가 사실을 정리했고, 2·3항은 에드워드의 말을 Cowork가 정리함

AI가 제안한 것: Cowork는 처음에 Codex를 다른 모델 계열이 필요한 자리(E3 기대 답 초안, E5 판정, 스크립트 교차 검토)에 쓰자고 했다. 백업 용도를 듣고는 인수인계 문서를 두고 Codex를 백업 겸 검토자로 쓰자고 했다. 판정자 전용안에 대해서는, 백업과 판정자를 함께 맡기면 Codex가 만든 결과를 Codex가 판정하게 돼 객관성이 깨진다고 했고, E4 그래프 맞춰보기 판정과 골든 룰 검사 스크립트 감사를 판정자 자리로 추가하자고 했다.

내가 채택하거나 고친 것: Codex는 조언자로는 절대 쓰지 않고 판정과 감사만 맡긴다(E5 다른 계열 판정, E4 그래프 맞춰보기 판정, 필요할 때 골든 룰 검사 스크립트 감사). 백업 용도는 포기했다.

그렇게 판단한 이유: Codex는 앞선 과제의 맥락 없이 답을 줄 수 있고, 그 조언이 Cowork의 판단에도 안 좋은 영향을 줄 수 있다고 봤다. 판정자는 오히려 맥락이 없을수록 객관적이다. 그리고 10/11 발표 때 멘토님께 웹 브라우저에서 ChatGPT와 Gemini를 토론시켜 일한다고 말씀드렸더니, 웹 AI보다 데스크톱 AI끼리 일을 시키는 게 낫다고 하셔서, 그 조언을 이번 과제에서 실제로 연습해보려고 Codex를 합류시켰다.

#### 읽은 파일

- AGENTS.md, README.md, worklog.md(처음 365줄과 2026-10-08 이후 전부. 그 사이는 절 제목과 검색으로 필요한 줄만)
- scope.md, process.md, deep/README.md, deep/05-citation/findings.md(앞부분, 절 제목, 한계 10), deep/05-citation/experiments/results-04.md(일치 14·같은 쪽 1·불일치 2 줄), deep/07-graphrag/README.md, e1-decisions.md, ai-consulting/·oil-trade/·shared/ README.md, deep/07-graphrag/plan.md(절 제목)
- `git log`, `git show --stat 0d9f7e2`
- 기대 답 파일은 읽지 않음

#### 만든·고친 파일

- handoff.md: 새로 만듦 — 지시의 1~7절. 저장소에서 찾지 못한 것은 "확인 필요"로 적음: 멘토 프로그램 원칙 문서, 3주 챌린지 핵심 질문, 단계 E0~E7의 정의·마감, 필수선. E3·E4·E5 이름은 이 지시문에만 나와 "지시문에는 … 나온다"로 적음. 숫자는 findings.md·results-04.md에서 확인. 정답 격리 사고는 기대 답 파일 이름·경로 없이 적음. 6절은 지시문을 근거로 씀
- AGENTS.md: 수정 — "작업 방식"의 "작업 전에 … 먼저 읽는다." 아래에 handoff.md 두 줄, "적용 범위" 끝에 Codex 한 줄 추가. 다른 줄은 고치지 않음
- README.md: 수정 — "문서 목록"의 AGENTS.md 줄 아래에 handoff.md 링크 한 줄 추가
- worklog.md: 수정 — 이 절 추가. 지시와 판단 기록은 받은 문구를 줄바꿈까지 그대로 옮김
- commit·push는 하지 않음

### 과제 정의 파일과 handoff 수정 (2026-10-13 17:45경, Claude Code)

#### Claude Code에 준 지시

1. deep/07-graphrag/challenge.md를 새로 만들고 Cowork가 정리한 3주 챌린지 과제 정의를 글자 그대로 옮김
2. handoff.md 수정: 1절 멘토 프로그램 원칙을 네 줄(출처 괄호 + "원문은 저장소에 없음")로 바꿈. 2절 2차 과제 맨 앞에 05·07·공통 목표 세 줄(출처: 2차 과제 안내 요약, 원문은 저장소에 없음). 3절 핵심 질문·단계 E0~E7과 마감·필수선을 challenge.md로 채우고 링크, "지시문에는 E3 기대 답 초안, E4 그래프 맞춰보기, E5 판정이라는 이름이 나온다" 문장은 사실과 달라 지움. 4절 표 E3~E7을 단계 이름이 보이게. 5절 다음 할 일을 "1번 E3 골든 세트: 스키마 → 질문·통제 항목 → 기대 답 → 골든 룰과 검사 스크립트 → 예측"으로. 6절 규칙에 정답 위치 규칙의 적용 범위 한 줄 추가. 그 밖의 확인된 문장과 6절 역할·격리 내용은 고치지 않음
3. deep/07-graphrag/README.md에 challenge.md 링크 한 줄 추가, worklog 기록. commit·push 하지 않음

#### 만든·고친 파일

- deep/07-graphrag/challenge.md: 새로 만듦 — 받은 내용을 글자 그대로 옮김
- handoff.md: 수정 — 위 지시 2대로. 3절 단계와 마감은 challenge.md의 주차별 단계·점검 시각을 표로 옮김. 필수선의 "방산"에는 "(2번)"을 붙임. 4절 표의 "E3~E7" 한 행을 E3~E7 다섯 행(단계 이름, 상태 대기)으로 나눔. 1번 다음 할 일에 있던 "사람 그래프는 에이전트 결과보다 먼저 만든다"는 바꾸라는 줄 안에 있어 함께 빠졌고, 같은 내용은 3절 규칙에 남아 있음
- deep/07-graphrag/README.md: 수정 — E1 결정 줄 아래에 challenge.md 링크 한 줄 추가. 폴더 구조 블록은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 2번 도메인 변경 승인 반영 (2026-10-13 17:57경, Claude Code)

#### 사실

2026-10-13 멘토가 2번 도메인을 방산에서 무역 & 기름으로 바꾸는 것을 승인했다(에드워드가 전함).

#### Claude Code에 준 지시

1. deep/07-graphrag/README.md: 두 도메인 표의 2번 상태를 "진행(2026-10-13 멘토 승인)"으로, 표 아래 방침 문단을 승인·확정과 1주차 마감(10/18)까지 2번 E1·E2·E3 진행 문장으로, 폴더 구조 블록의 "(승인 대기 중)"은 지움
2. deep/07-graphrag/oil-trade/README.md: 승인 대기 문장을 승인 사실로. 실무 정보를 두지 않는다는 줄은 그대로
3. deep/07-graphrag/e1-decisions.md: "2번 무역 & 기름" 절의 "멘토 승인 대기 중이다"를 "2026-10-13 멘토 승인. 범위와 분류 축 확정은 이어서 기록한다."로. 판단 기록은 고치지 않음
4. deep/07-graphrag/challenge.md: 본문은 고치지 않고 맨 아래 "## 변경 기록" 절 추가
5. handoff.md: 승인 대기라고 적힌 곳을 모두 승인으로. 4절·5절에 2번 E1 → E2 → E3 순서, 3절 규칙에 방산 범위 제한이 2번에 해당하지 않고 무역 & 기름 실무 정보 금지가 적용된다는 줄
6. worklog 기록. commit·push 하지 않음

#### 읽은 파일

- AGENTS.md(대화 첫머리에 주어짐), handoff.md, worklog.md(2026-10-13 17:40 이후 절)
- deep/07-graphrag/README.md, oil-trade/README.md, e1-decisions.md, challenge.md

#### 만든·고친 파일

- deep/07-graphrag/README.md: 수정 — 2번 상태를 "진행(2026-10-13 멘토 승인)"으로. 표 아래 방침 문단 전체를 지시 문장으로 바꿈. 폴더 구조 블록 oil-trade/ 줄의 "(승인 대기 중)" 지움. 폴더 구조에 e1-decisions.md·challenge.md가 없는 것은 이번 지시 범위 밖이라 그대로 둠
- deep/07-graphrag/oil-trade/README.md: 수정 — "승인 대기 중이다(2026-10-12 요청)"를 "2026-10-13 멘토가 승인했다(2026-10-12 요청)"로. 실무 정보 줄은 그대로
- deep/07-graphrag/e1-decisions.md: 수정 — 지시한 문장만 바꿈. 같은 줄의 "범위는 승인 뒤에 정한다. 방침은 … 있다."와 "분류 축" 절의 "2번 도메인 답이 오면 확정한다."는 지시 범위 밖이라 그대로 둠. 판단 기록은 고치지 않음
- deep/07-graphrag/challenge.md: 수정 — 맨 아래 "## 변경 기록" 절과 지시 문장 한 줄 추가. 본문(13행 "승인을 요청한 상태다" 포함)은 고치지 않음
- handoff.md: 수정 — 3절 두 도메인 줄의 "변경 승인 대기"를 "2026-10-13 멘토 승인으로 변경"으로. 3절 규칙의 "2번 도메인은 멘토 답이 오기 전까지 작업하지 않는다"를 승인 사실로 바꾸고, 방산 범위 제한 줄 추가. 4절 표 E1 2번 칸을 "진행 예정(2026-10-13 멘토 승인)"과 E1 → E2 → E3 순서로. 5절 첫 줄을 2번 E1 → E2 → E3(1주차 마감 10/18까지)로. E2·E3 행의 2번 "대기"는 아직 시작 전이라 그대로 둠
- worklog.md: 수정 — 이 절 추가. 지난 기록은 고치지 않음
- commit·push는 하지 않음

## 2026-10-14

### 2번 도메인 E1과 분류 축 확정 (2026-10-14 11:10경, Claude Code)

#### Claude Code에 준 지시

1. deep/07-graphrag/e1-decisions.md "## 2번 무역 & 기름" 절을 멘토 승인, 제품(UMO·ULO·PPO), 기준(한국 법령과 바젤협약·HS 코드), 설계 범위, 측정 범위(품목 분류·규제·수출입 절차, 무역 일반은 측정에서 뺌), 공개 자료만 쓴다는 줄로 바꾸고, 남아 있던 "범위는 승인 뒤에 정한다" 문장을 지움
2. "## 분류 축" 절을 업무 유형 확정(2026-10-14) 문장으로 바꿈. 1번은 AI를 적용한 업무·과제의 종류, 2번은 무역 업무 단계, 2번 단계 목록은 E3 스키마에서 원문 자료를 근거로 정함
3. 맨 아래 "## 판단 기록 — 2번 도메인" 절을 새로 만들고, 작성자 줄 뒤에 판단 기록 세 항목을 글자 그대로 옮김. 기존 판단 기록(1번 도메인)은 고치지 않음
4. handoff.md 현재 상태 표 E1을 "1번 완료(분류 축 확정) / 2번 완료"로, 다음 할 일을 "2번 E2(원장 10건 이상, 찾았지만 못 쓴 자료도 셈) → 두 도메인 E3 골든 세트"로
5. worklog 2026-10-14 항목 기록. commit·push 하지 않음

#### 판단 기록 — 2번 도메인

작성: 에드워드, 2026-10-14. 1항은 Cowork가 사실을 정리했고, 2·3항은 에드워드의 말을 Cowork가 정리함

AI가 제안한 것: Cowork는 방산을 유지할 때와 무역 & 기름으로 바꿀 때를 비교해, 바꾸면 비교 축이 "자료 양"에서 "믿을 자료의 양"으로 바뀐다고 했다. 무역 일반(용어, 서류, 거래 흐름)은 자료가 많아 "자료가 적은 도메인" 역할이 흐려지니, 숫자로 재는 범위는 기름 무역의 품목 분류·규제·수출입 절차로 좁히자고 했다. 특화 에이전트는 처음엔 과제 뒤로 미루자고 했다. 제품은 UMO·ULO·PPO만, 기준은 한국 법령과 국제 규칙(바젤협약, HS 코드), 분류 축은 업무 유형을 추천했다.

내가 채택하거나 고친 것: 2번 도메인을 방산 대신 무역 & 기름으로 바꾸자고 내가 제안했고, 2026-10-13 멘토 승인을 받았다. 제품은 UMO·ULO·PPO, 기준은 한국 법령과 국제 규칙, 측정 범위는 품목 분류·규제·수출입 절차로 정했고, 분류 축은 업무 유형으로 확정했다. Cowork가 특화 에이전트를 과제 뒤로 미루자고 했을 때, 두 도메인 모두 완전히 특화되게 만들고 싶다고 해서 "설계는 넓게, 측정만 좁게"로 바꿨다.

그렇게 판단한 이유: 기름 무역은 이제 막 시작한 일인데 처음 접하는 분야라 용어도 제품도 아예 모른다. AI의 도움을 받아 배운 내용과 앞으로 배울 내용을 정리해 RAG를 만들고, 기름으로 무역을 하려면 어떤 과정을 거쳐야 하는지 알려주는 특화 에이전트를 만들고 싶었다. 분류 축을 업무 유형으로 확정한 것도 그 에이전트가 무역 과정을 단계별로 알려줘야 하기 때문이다. AI 컨설팅과 함께 앞으로 일하게 될 가능성이 높은 두 업종의 데이터를 과제가 끝난 뒤에도 차곡차곡 쌓아가려고 방산에서 방향을 틀었다.

#### 읽은 파일

- deep/07-graphrag/e1-decisions.md, handoff.md(4·5절), worklog.md(끝부분)
- `git status`

#### 만든·고친 파일

- deep/07-graphrag/e1-decisions.md: 수정 — "## 2번 무역 & 기름" 절을 지시한 여섯 줄 목록으로 바꿈(전날 남은 "범위와 분류 축 확정은 이어서 기록한다. 범위는 승인 뒤에 정한다. 방침은 … 있다." 문장도 함께 지움). "## 분류 축" 절을 지시 문장으로 바꿈. 맨 아래 "## 판단 기록 — 2번 도메인" 절 추가(세 항목은 받은 문구 그대로). 1번 판단 기록과 3행 "2026-10-13에 적었다."는 고치지 않음. 바젤협약·HS 코드의 출처 URL은 아직 없음(E2 원장에서 확인 필요)
- handoff.md: 수정 — 4절 표 E1 행을 1번 "완료(분류 축 확정)", 2번 "완료"로. 5절 첫 줄을 "2번 E2(…) → 두 도메인 E3 골든 세트"로. 5절의 "1번 E3 골든 세트: 스키마 → …" 줄과 07 README 폴더 구조 줄은 그대로 둠. 4절 제목 날짜와 맨 위 "마지막 갱신"을 2026-10-14로
- worklog.md: 수정 — 2026-10-14 항목 새로 만들고 이 절 추가. 지난 기록은 고치지 않음
- commit·push는 하지 않음

### 2번 도메인 원천 원장 (2026-10-14, 11:35경 마침, Claude Code)

#### Claude Code에 준 지시

목표: 2번 도메인(무역 & 기름)의 원천 원장을 만든다. 1번 도메인 원장(deep/07-graphrag/ai-consulting/)과 같은 방식으로 하되 아래 기준을 따른다. 검색 방법과 세부 형식은 Claude Code가 정한다.

- 범위(E1 결정): 제품 UMO(폐엔진오일)·ULO(폐윤활유)·PPO(폐플라스틱 열분해유), 기준은 한국 법령과 국제 규칙(바젤협약, HS 코드). 측정 범위(품목 분류·규제·수출입 절차)와 세 제품의 정의를 다루는 자료를 모으고, 무역 일반(용어, 결제 등)은 넣지 않음
- 넣는 기준: 공개 자료(법령·시행령·시행규칙·고시, 국제협약 원문과 공식 지침, 정부·공공기관의 공식 안내·보도자료, 공식 품목분류 자료) 중 세 제품의 분류·규제·수출입 절차 중 하나 이상을 직접 다루는 것
- 빼는 것(제외 표로): 판매 광고나 거래 제안, 출처를 확인할 수 없는 글, 유료라 원문을 볼 수 없는 자료, 범위 밖(무역 일반, 다른 제품). 찾았지만 못 쓴 자료도 빠짐없이

1. deep/07-graphrag/oil-trade/에 sources.csv와 excluded.csv. 1번 도메인과 같은 칸을 쓰되 "펌" 대신 "발행 기관". 법령은 법률 번호와 시행일을 함께 적음
2. 쓰는 자료 10건 이상
3. 원장에는 서지 정보만. 품목 분류 결과, 규제 내용, 절차 단계처럼 그래프에 들어갈 내용은 적지 않음
4. 원문은 oil-trade/raw/ot-01.txt처럼 번호만 담은 이름으로 저장하고 이 폴더는 .gitignore에. 해시는 이 파일 기준
5. 실무 정보(거래처, 가격, 계약, 받은 서류)는 쓰지 않음. 에드워드가 따로 건네준 파일 말고는 저장소 밖 파일을 열지 않음
6. 10건이 안 되면 원장을 쓰지 말고 멈춰서 보고
7. worklog 2026-10-14 항목에 기록, handoff.md 현재 상태와 다음 할 일 갱신
8. commit·push 하지 않음

#### 검색·수집 방법

- 후보 찾기: WebSearch(한국어·영어)로 바젤협약 원문·폐유 기술지침, WCO HS 2710·27류 주, 폐기물국가간이동법과 수출입 품목 고시, 열분해유 관련 환경부 보도자료, 관세청 품목분류 사례, 한국석유관리원 기준을 찾음. 법령은 국가법령정보센터에서 제품 관련 낱말(폐유, 윤활유, 열분해, 폐플라스틱)이 본문에 나오는지 세어 보고, 나온 곳의 앞뒤 문장을 읽어 "직접 다루는지"를 판정함
- 국제 자료(1~3번): basel.int, wcoomd.org PDF를 curl로 받아 macOS PDFKit(JXA, `osascript -l JavaScript`)으로 텍스트 추출
- 법령 본문(4·5·8·10·15번): 내장 브라우저로 국가법령정보센터 법령 페이지가 본문을 `lsInfoR.do?lsiSeq=…&efYd=…`로 불러오는 것을 확인한 뒤, 같은 주소를 curl로 받아 id="contentBody" 요소의 텍스트를 python 표준 라이브러리(html.parser)로 뽑음. 블록 요소 경계는 줄바꿈. 원장 URL 칸에는 사람이 열 수 있는 `lsInfoP.do?lsiSeq=…&efYd=…`를 적음. 이 규칙이라 법령 본문 파일에는 페이지의 "판례·연혁" 같은 메뉴 글자와 소관 부서 대표 전화번호가 섞여 있음
- 별표·별지(6·7·9·11~14번): 국가법령정보센터의 별표는 본문에 없고 별도 PDF라, 내장 브라우저로 별표 페이지의 PDF 파일 번호(pdfFlSeq)를 읽고 `flDownload.do?flSeq=…`를 curl로 받아 PDFKit으로 추출. 원장 URL 칸에는 이 PDF 주소를 적음
- 보도자료(16번): 정책브리핑 페이지 본문이 첨부 파일뿐이라 첨부 hwpx를 받아 zip 안 Contents/section*.xml의 문단 글자를 이어 붙임(python 표준 라이브러리). 원문에 담당 공무원 이름·전화번호가 들어 있으나 raw/는 올리지 않음
- 모든 raw 파일 공통: 줄 끝 공백 제거, 빈 줄 3개 이상은 2개로, 끝에 줄바꿈 하나. 해시는 이렇게 쓴 raw/ot-NN.txt의 SHA-256
- 쓴 코드: 스크래치 폴더(저장소 밖)의 pdf2txt.js(PDFKit 추출), law2txt.py(HTML 요소 텍스트 추출), hwpx2txt.py(hwpx 텍스트 추출), build-raw.py(정규화·저장), build-csv.py(원장·제외 표 쓰기). 실험 코드가 아니라 수집 도구라 저장소에 두지 않음(1번 도메인과 같음). 설치한 도구 없음
- 발행일 규칙: 법령은 공포일, 시행일은 국가법령정보센터 머리줄 "[시행 …]" 값. 별표는 그 별표를 보여 준 법령 판의 번호·공포일·시행일을 적음. 별표 PDF 첫 줄의 개정일은 법령 판과 다름(시행령 별표 1 "<개정 2025. 10. 1.>", 시행규칙 별표 4·4의2·4의3·5의3 "<개정 2025. 12. 30.>"). 국제 자료는 문서에 보이는 값: 1번 "2025"(연도만), 2번 "1997 (2002-11 재인쇄)", 3번 문서 안 날짜 없음 → "확인 불가"
- "법령 번호" 칸: 지시는 "법률 번호"였으나 시행령·시행규칙·고시도 있어 "법령 번호"로 이름 붙이고 법률·대통령령·부령·고시 번호를 그대로 적음. 국제 자료와 보도자료는 "해당 없음"
- 발행 기관: 법령·고시는 국가법령정보센터에 표시된 소관 부처(기후에너지환경부). 2026-10-14 현재 표시가 "기후에너지환경부"로 바뀌어 있음. 16번 보도자료는 당시 발행 기관(환경부)

#### 건수 (원장 16건, 제외 23건)

| 묶음 | 원장 | 제외 표 |
|------|------|---------|
| 국제 규칙(바젤협약·WCO) | 3 | 2 |
| 폐기물국가간이동법과 품목 고시 | 4 | 2 |
| 폐기물관리법·시행령·시행규칙과 별표 | 7 | 1 |
| 자원재활용법 시행령 | 1 | 0 |
| 석유사업법·관세법 | 0 | 3 |
| 정부 보도자료·정책 기사 | 1 | 6 |
| 비공식(위키문헌·민간 HS 사이트·유료 보고서·언론) | 0 | 9 |
| 합계 | 16 | 23 |

- 판정이 얇은 것: 4·5번(폐기물국가간이동법과 시행령)은 본문에 제품 이름이 없고 "수출입규제폐기물"의 절차를 정함. 그 품목표(6번 고시 별지)에 폐유가 들어 있어 세 제품의 수출입 절차를 직접 다루는 것으로 보고 넣음. 15번(자원재활용법 시행령)은 재활용의무 대상 제품에 윤활유를 정한 조문(제18조) 때문에 넣음(폐윤활유 재활용 의무의 근거로 판단). 제외 표의 석유사업법 시행령과 2022-02-03 보도자료도 판정이 얇다고 이유 칸에 적음
- 쓰지 못한 것: 관세법 별표 관세율표(한국 10단위 세번)는 PDF가 안내문 1쪽뿐이고 한글 파일은 열 도구가 없어 읽지 못함. 관세청 품목분류 결정 사례와 한국석유관리원 기준은 검색에서 공식 원문을 찾지 못함(제외 표에는 실제로 판단한 URL만 적어 이 둘은 없음). 바젤 Y8 지침은 서지 정보를 확인할 수 없어 제외
- 제외 표에는 열어 보았거나 제목·URL로 판단한 것만 적음. 검색 결과에 나왔지만 판단하지 않은 후보는 적지 않음

#### 문제와 대처

- 시행규칙 별표 PDF 4개를 받을 때 zsh에서 `set -- $p`가 낱말로 나뉘지 않아 파일 번호 없이 요청했고, 오류 페이지(5,786바이트)가 이름에 공백이 든 .pdf 4개로 저장됨(Claude Code 스크립트 오류). Claude Code가 이번에 스크래치 폴더에 만든 파일이라 바로 지우고 bash로 다시 받음. 이어서 같은 방식의 쉘 반복문은 bash로 돌림
- zsh에서 `echo ====`가 명령 경로 확장으로 실패해 반복문이 첫 파일 뒤 멈춤(Claude Code 오류). 남은 파일을 따로 추출함
- grep(ugrep)이 한글 앞뒤 글자 수 정규식을 "복잡도 한계 초과"로 거부해 python으로 바꿈

#### 읽은 파일

- AGENTS.md(대화 첫머리에 주어짐), handoff.md, README.md, worklog.md(2026-10-13 1번 원장 절과 끝부분), .gitignore
- deep/07-graphrag/e1-decisions.md, ai-consulting/sources.csv·excluded.csv·README.md, oil-trade/README.md
- 웹 원문은 raw/ 파일과 sources.csv·excluded.csv의 URL 참고. 저장소 밖 파일은 스크래치 폴더의 내려받은 파일만 열었고, 에드워드에게서 받은 파일은 없음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/sources.csv: 새로 만듦 — 원장 16건, 10칸(번호, 발행 기관, 제목, URL, 발행일, 법령 번호, 시행일, 확인한 날짜, 원문 저장 경로, 원문 해시(SHA-256))
- deep/07-graphrag/oil-trade/excluded.csv: 새로 만듦 — 제외·읽지 못한 자료 23건(발행 기관, URL, 이유)
- deep/07-graphrag/oil-trade/raw/ot-01.txt ~ ot-16.txt: 새로 만듦 — 원문 텍스트. .gitignore로 저장소에 올라가지 않음
- .gitignore: 수정 — 맨 끝에 주석 한 줄과 `deep/07-graphrag/oil-trade/raw/` 추가. 기존 줄은 그대로
- worklog.md: 수정 — 이 절 추가
- handoff.md: 수정 — 4절 표 E2 행, 5절 다음 할 일
- 확인: python csv 모듈로 sources.csv 16행·10열, excluded.csv 23행·3열을 읽음. 원장 해시와 raw 파일 해시 불일치 0. `git check-ignore`로 oil-trade/raw/ 무시 확인
- commit·push는 하지 않음

- handoff.md에 Cowork 대화에만 있던 내용(주간 기록 파일, E3 계획 안, Codex 판정 규칙 초안, Cowork 작업 방식)을 옮겼다. 내용 정리는 Cowork, 파일 작업은 Claude Code가 했다.

### handoff 상태 갱신 (2026-10-14, 11:45경 마침, Claude Code)

받은 지시(Cowork가 쓰고 에드워드가 전달): handoff.md 4절 표 E2 행의 2번 칸 "완료(커밋 전). 원장 16건, 제외 23건"을 "완료. 원장 16건, 제외 23건(커밋 5e4c595)"으로, 5절 첫 줄("- 2번 E2 원장 검토와 commit(에드워드). …")을 2번 E2 후속 문장(관세율표 읽을 방법, 원장 9·11~14번 별표 자체 개정일, 원장 6·7·9번 법령 번호 사람 확인)으로 바꾼다. 다른 줄은 건드리지 않는다. commit·push 하지 않음

#### 읽은 파일

- handoff.md, worklog.md(2026-10-14 항목 끝부분)

#### 만든·고친 파일

- handoff.md: 수정 — 4절 표 E2 행 2번 칸, 5절 첫 줄. 다른 줄은 고치지 않음; 5절 첫 줄 끝에 판정이 얇은 자료의 확인 상태 두 문장을 덧붙임(Cowork 지시문에서 빠졌던 항목을 되살림)
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 2번 원장에 관세율표 추가 (2026-10-14, 13:58경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 관세법 [별표] 관세율표를 읽어 2번 도메인 원장에 넣을지 판정하고, 넣으면 원장에 추가한다.

1. 에드워드가 국가법령정보센터에서 내려받은 한글 파일 ~/Downloads/law0015562022123119186KC_000000E.hwp의 SHA-256이 3b14a5f9b99e29279cc6990e26a618bd422098a40912e585889f66ef5ff54eb3인지 확인하고, 다르면 멈춘다. 이 파일 말고 저장소 밖 파일은 열지 않고, 웹에서 다시 받지 않는다
2. 도구를 설치하지 않고 python 표준 라이브러리로 텍스트를 뽑는다(OLE 복합 문서, BodyText/Section 스트림을 raw deflate로 풂, 레코드 태그 67 PARA_TEXT의 UTF-16LE 글자를 문단마다 한 줄, 글자 코드 1~9·11~12·14~23은 16바이트 컨트롤로 건너뜀). 첫 줄 "■ 관세법 [별표] <개정 2022. 12. 31.>"과 "제27류" 제목 줄을 확인하고, 아니면 멈춘다
3. ot-01~16과 같은 정규화로 raw/ot-17.txt에 저장하고, 해시는 이 파일의 SHA-256
4. 넣는 기준은 원장 때와 같다(세 제품의 품목 분류·규제·수출입 절차 중 하나 이상을 직접 다루는가). 넣지 않으면 원장·제외 표·handoff는 고치지 않고 멈춘다
5. 넣으면 sources.csv 끝에 지시한 17번 행을 추가(해시 칸은 3번 값). excluded.csv의 flSeq=169662461 행은 이유 칸만 지시 문장으로 바꾼다
6. handoff.md 4절 표 E2 행 2번 칸과 5절 첫 줄을 지시 문장으로 바꾼다
7. worklog 2026-10-14 항목 끝에 이 절. 판정 이유에 세번 번호, 품목 이름, 세율, 분류 결과를 쓰지 않는다
8. commit·push 하지 않음

#### 입력 파일과 해시 확인

- ~/Downloads/law0015562022123119186KC_000000E.hwp, 1,325,568바이트. `shasum -a 256` 결과 3b14a5f9b99e29279cc6990e26a618bd422098a40912e585889f66ef5ff54eb3로 지시한 값과 일치

#### 추출 방법

- 스크래치 폴더(저장소 밖)에 hwp2txt.py를 써서 돌림. python 표준 라이브러리(struct, zlib)만 씀. 설치한 도구 없음
- olefile 같은 OLE 라이브러리가 표준에 없어, 복합 문서 구조(머리글, DIFAT, FAT, 미니 FAT, 디렉터리)를 직접 읽는 짧은 코드를 함께 씀
- FileHeader: 서명 "HWP Document File", 버전 5.1.0.1, 압축 플래그 켜짐, 암호 플래그 꺼짐. 본문 스트림은 BodyText/Section0 하나
- Section0을 `zlib.decompress(data, -15)`로 풀고, 레코드 머리(태그 10비트, 크기 12비트, 크기 0xFFF면 다음 4바이트)를 따라 태그 67만 읽음. 16바이트 컨트롤(1~9, 11~12, 14~23)은 건너뛰고, 나머지 32 미만 글자(문단 끝 13 등)는 버림
- 정규화: ot-01~16과 같이 줄 끝 공백 제거, 빈 줄 3개 이상은 2개로, 끝에 줄바꿈 하나. 줄 끝 공백 제거는 python `str.rstrip()`이라 전각 공백(U+3000)도 지워짐. 지난번 build-raw.py는 지난 세션 스크래치 폴더에 있어 열어 보지 않았으므로, 전각 공백 처리가 ot-01~16과 같은지는 확인 필요
- 확인: 추출한 텍스트의 맨 앞 두 줄은 빈 줄(글자 없이 컨트롤만 있는 문단)이고, 글자가 있는 첫 줄이 "■ 관세법 [별표] <개정 2022. 12. 31.>"임. 지시의 "첫 줄"을 글자가 있는 첫 줄로 보고 진행함. 앞의 빈 두 줄은 정규화 규칙에 없어 그대로 둠. "제27류" 제목 줄은 1개 있음
- raw/ot-17.txt: 41,364줄, SHA-256 f84816d24ab1d3066458514088ba28b5f19b95fb5137a4da09f2afe2c2f59293. `git check-ignore`로 무시되는 것 확인

#### 판정 결과와 이유

- 판정: 넣음(원장 17번)
- 이유: 세 제품 중 하나 이상에 해당하는 물품의 정의와 분류 대상을 정한 주(註)가 있어, 품목 분류를 직접 다룬다고 봄. 넣는 기준(세 제품의 품목 분류·규제·수출입 절차 중 하나 이상을 직접 다룸)에 맞음
- handoff 5절에 넣은 "제27류에는 10단위 세번이 없고 호·소호와 번호 매긴 세분 항목만 있다"는 ot-17.txt의 제27류 범위(제27류 제목 줄부터 제28류 제목 줄 전까지)에서 숫자만 있는 줄의 자릿수를 세어 확인함(4자리·2자리·1자리만 있고, 점이나 줄표로 이은 10자리 번호 0건). "관세법 본문은 … 고시한다고 정한다"는 Claude Code가 이번에 확인하지 않음(관세법 본문 ot 파일 없음)

#### 읽은 파일

- AGENTS.md(대화 첫머리에 주어짐), handoff.md, worklog.md(2026-10-14 "2번 도메인 원천 원장" 절과 끝부분)
- deep/07-graphrag/oil-trade/sources.csv, excluded.csv, raw/ot-04.txt(첫 30바이트만, 정규화 형태 확인)
- 저장소 밖: ~/Downloads/law0015562022123119186KC_000000E.hwp(지시한 파일), 스크래치 폴더의 추출 결과

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/raw/ot-17.txt: 새로 만듦 — 관세율표 텍스트. .gitignore로 저장소에 올라가지 않음
- deep/07-graphrag/oil-trade/sources.csv: 수정 — 끝에 17번 행 추가(지시한 행 그대로, 해시 칸은 위 값)
- deep/07-graphrag/oil-trade/excluded.csv: 수정 — URL이 flSeq=169662461인 행의 이유 칸만 지시 문장으로 바꿈. 다른 행은 고치지 않음
- handoff.md: 수정 — 4절 표 E2 행 2번 칸, 5절 첫 줄. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- 확인: python csv 모듈로 sources.csv 17행·10열, excluded.csv 23행·3열을 읽음
- commit·push는 하지 않음

### 2번 제외 표 결정 반영 (2026-10-14, 14:00경 마침, Claude Code)

#### 에드워드의 결정

- 석유사업법 시행령: 제외 확정. 다루는 UMO·ULO는 재생 처리 전 폐유이고, 신품 석유제품을 다루는 석유사업법과는 개념이 다르다고 판단함
- 2022-02-03 보도자료: 제외 확정. 제품이 아니라 시설 입지 이야기라고 판단함
- 관세법 본문: 에드워드가 2026-10-14 국가법령정보센터에서 내려받은 한글 파일(HWPML)을 Cowork가 열어, 수출입 통관 일반 조문이고 세 제품 낱말이 없음을 확인함. 제외 표에 범위 밖으로 추가
- AI가 제안한 것: Cowork가 석유사업법과 폐유의 법적 틀이 다르다고 설명하고 두 자료 모두 기준상 제외 쪽이라고 했으며, 관세법 본문은 제외 표에 남기자고 제안함. 결정은 에드워드가 함

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 도메인 제외 표에 에드워드의 결정 세 가지를 반영한다. 관세율표 작업에 이어서 하며, 아직 커밋하지 않은 변경 위에 그대로 덧붙인다.

1. excluded.csv를 python csv 모듈로 읽고 써서 세 곳만 바꾼다: 석유사업법 시행령 행(lsiSeq=290545)과 2022-02-03 보도자료 행(boardId=1506160)의 이유 칸 끝에 한 칸 띄우고 지시 문장을 덧붙이고, 맨 끝에 관세법 본문 행(lsiSeq=290673, 범위 밖)을 추가한다. git diff로 다른 행이 바뀌지 않았는지 확인한다
2. handoff.md 세 곳만 고친다: 4절 표 E2 행 2번 칸(제외 24건과 추가 내역), 5절 첫 줄 안의 석유사업법 시행령·보도자료 문장(제외 확정), 5절 첫 줄 안의 "(10단위 세번이 그 고시에 있는지는 확인 필요)"(Cowork가 관세법 본문에서 확인한 사실 덧붙임)
3. worklog 2026-10-14 항목 끝에 이 절. "에드워드의 결정" 네 줄은 그대로
4. 관세법 본문 파일과 그 밖의 저장소 밖 파일은 열지 않고, 웹에서 받지 않는다. commit·push 하지 않음

#### 읽은 파일

- handoff.md, worklog.md(끝부분), deep/07-graphrag/oil-trade/excluded.csv
- 저장소 밖 파일은 열지 않음. 관세법 본문의 내용(낱말 없음, 고시 조문)은 Cowork가 확인한 것이고 Claude Code는 확인하지 않음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/excluded.csv: 수정 — 석유사업법 시행령 행과 2022-02-03 보도자료 행의 이유 칸 끝에 지시 문장 덧붙임, 맨 끝에 관세법 본문 행 추가. python csv 모듈로 읽고 씀(따옴표 규칙은 기존 행과 같게 나옴). git diff로 이 세 곳과 지난 절의 flSeq=169662461 행 말고는 바뀐 행이 없음을 확인. csv 모듈로 다시 읽어 24행·3열 확인
- handoff.md: 수정 — 4절 표 E2 행 2번 칸, 5절 첫 줄 안의 두 곳. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 2번 원장 별표 개정일 칸 추가 (2026-10-14, 14:04경 마침, Claude Code)

#### 에드워드의 결정

- 별표 자체 개정일: 원장에 칸을 더해 적는다
- 원장 4·5·15번: 그대로 둔다
- AI가 제안한 것: 에드워드가 먼저 이렇게 하자고 했고, Cowork도 같은 의견이었다. Cowork가 든 이유는 발행일·시행일 칸이 별표를 보여 준 법령 판 값이라 칸이 없으면 별표가 최근에 바뀐 것처럼 읽힐 수 있다는 것, 개정 이력이 출발 질문과 IATF 과제의 문제 유형(개정 이력)에 이어진다는 것, 4·5번은 수출입 절차를 정한 법이라 빼면 측정 범위의 절차 쪽이 빈다는 것, 15번은 가장 얇지만 E4·E5에서 쓰이지 않으면 그것도 발견으로 적을 수 있다는 것이다

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 원장에 "별표 자체 개정일" 칸을 더하고, 원장 4·5·15번을 그대로 두기로 한 결정을 기록한다.

1. sources.csv를 python csv 모듈로 읽고 써서 "시행일" 칸 바로 뒤에 "별표 자체 개정일" 칸을 더한다(9번 2025-10-01, 11~14번 2025-12-30, 17번 2022-12-31, 6·7번 표시 없음, 나머지 해당 없음). 다른 칸은 바꾸지 않는다. 각 값을 raw 파일 별표 제목 줄의 "<개정 …>" 표시와 맞춰 보고, 다르면 멈춘다. 끝나면 17행·11열, 해시 칸 그대로, 줄바꿈 LF 그대로인지 확인한다
2. handoff.md 5절 첫 줄 안의 두 문장(별표 자체 개정일, 원장 4·5·15번)만 지시 문장으로 바꾼다
3. worklog 2026-10-14 항목 끝에 이 절. "에드워드의 결정" 세 줄은 그대로
4. 저장소 밖 파일은 열지 않는다. commit·push 하지 않음

#### 값 확인

- raw 파일 별표 제목 줄의 개정 표시: ot-09 1행 "■ 폐기물관리법 시행령 [별표 1] <개정 2025. 10. 1.>", ot-11·12·13·14 1행 시행규칙 [별표 4]·[별표 4의2]·[별표 4의3]·[별표 5의3] 모두 "<개정 2025. 12. 30.>", ot-17 3행 "■ 관세법 [별표] <개정 2022. 12. 31.>"(1·2행은 빈 줄). 지시 값과 모두 일치
- ot-06(1행 "[별지]")과 ot-07(1행 "[별표 2]")은 파일 전체에 "개정" 낱말이 없어 "표시 없음"과 맞음

#### 읽은 파일

- handoff.md, worklog.md(끝부분), deep/07-graphrag/oil-trade/sources.csv
- deep/07-graphrag/oil-trade/raw/ot-06·07·09·11·12·13·14·17.txt(별표 제목 줄과 "개정" 낱말 검색)
- 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/sources.csv: 수정 — "시행일"(7번째 칸) 뒤에 "별표 자체 개정일" 칸 추가. 확인: csv 모듈로 다시 읽어 17행·11열, 해시 칸 17개 모두 고치기 전과 같음, CR 없음(LF 그대로). 새 칸을 뺀 나머지가 고치기 전 18줄(머리줄 포함)과 같음을 git diff로 비교함
- handoff.md: 수정 — 5절 첫 줄 안의 두 문장. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 1번 E3 스키마 (2026-10-14, 14:24경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 1번 도메인(AI 컨설팅) 그래프 스키마를 deep/07-graphrag/ai-consulting/schema.md로 만든다. 사람 그래프와 에이전트 그래프가 같은 틀을 쓰게 하는 파일이다.

- 지킬 것: ai-consulting/raw/ 안의 사례 본문은 열지 않는다(사람 그래프를 에이전트 결과보다 먼저 만들기 위한 규칙). 저장소 밖 파일은 열지 않고, 웹을 쓰지 않는다. commit·push 하지 않는다

1. schema.md를 새로 만든다. 지시문의 "=== schema.md 시작 ==="과 "=== schema.md 끝 ===" 사이 내용을 한 글자도 바꾸지 않고 쓴다(1~10절: 원칙, 노드 8종, 산업 GICS 11개 섹터, 업무 유형 10개와 판정 규칙, AI 기술 6개, 관계 7종, 기록 형식, E4 비교 방법, 사람 그래프 대상 7건, 판단 기록)
2. ai-consulting/README.md 끝에 "그래프 스키마(E3): [schema.md](schema.md)" 한 줄을 더한다
3. handoff.md 4절 표 E3 행의 1번 칸을 "진행. 스키마 확정(…)"으로, 5절 "1번 E3 골든 세트" 줄의 "스키마"를 "스키마(완료, …)"로 바꾼다
4. worklog 2026-10-14 항목 끝에 이 절

#### 읽은 파일

- handoff.md, worklog.md(끝부분)
- deep/07-graphrag/ai-consulting/README.md, sources.csv(번호·펌 두 칸만. schema.md 9절의 펌별 가장 작은 원장 번호 1·4·6·8·10·12·15가 원장과 맞는지 확인, 일치)
- ai-consulting/raw/는 열지 않음(폴더 이름이 `ls` 결과에 나온 것뿐). 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/schema.md: 새로 만듦 — 받은 내용 그대로(116줄). 고치지 않음
- deep/07-graphrag/ai-consulting/README.md: 수정 — 끝에 지시한 한 줄 추가. 바로 앞 줄과 빈 줄 없이 붙어 있어 Markdown에서는 앞 문단에 이어져 보임
- handoff.md: 수정 — 4절 표 E3 행 1번 칸, 5절 "1번 E3 골든 세트" 줄. 2번 칸과 근거 칸, 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 1번 E3 질문·통제 항목 (2026-10-14, 14:31경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 1번 도메인 골든 세트의 질문 10개와 통제 항목 5개를 deep/07-graphrag/ai-consulting/questions.md로 만든다.

- 지킬 것: ai-consulting/raw/ 안의 사례 본문은 열지 않는다. 저장소 밖 파일은 열지 않고, 웹을 쓰지 않는다. commit·push 하지 않는다. 기대 답(정답)은 쓰지 않고 질문만 쓴다

1. questions.md를 새로 만든다. 지시문의 "=== questions.md 시작 ==="과 "=== questions.md 끝 ===" 사이 내용을 한 글자도 바꾸지 않고 쓴다(1~6절: 설계 원칙, 질문 종류 A~E, 질문 10개와 고른 방법, 통제 항목 5개, 기대 답을 쓸 때 확인할 것, 판단 기록)
2. ai-consulting/README.md 끝에 "골든 세트 질문(E3): [questions.md](questions.md)" 한 줄을 더한다
3. handoff.md 4절 표 E3 행의 1번 칸을 "진행. 스키마(…)·질문(…) 확정"으로, 5절 "1번 E3 골든 세트" 줄의 "질문·통제 항목"을 "질문·통제 항목(완료, …)"으로 바꾼다
4. worklog 2026-10-14 항목 끝에 이 절

#### 읽은 파일

- handoff.md, worklog.md(끝부분), deep/07-graphrag/ai-consulting/README.md
- deep/07-graphrag/ai-consulting/sources.csv(번호·펌·제목 칸만). questions.md 3절 "고른 방법"이 원장과 맞는지 확인함: 사람 그래프 대상이 아닌 사례 중 펌이 서로 다른 두 건을 번호가 작은 것부터 고르면 2번(McKinsey)·5번(BCG)으로 Q1·Q2와 일치(3번은 2번과 같은 McKinsey). 제목에 은행·보험이 보이는 원장은 1·6·10·13번
- ai-consulting/raw/는 열지 않음. 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/questions.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음. 기대 답(정답)은 쓰지 않음
- deep/07-graphrag/ai-consulting/README.md: 수정 — 끝에 지시한 한 줄 추가(앞 줄과 빈 줄 없이 붙음)
- handoff.md: 수정 — 4절 표 E3 행 1번 칸, 5절 "1번 E3 골든 세트" 줄. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### E3 정답 격리 규칙 확정 (2026-10-14, 14:37경 마침, Claude Code)

#### 에드워드의 결정

- 기대 답은 암호를 건 디스크 이미지에 둔다. 에드워드가 "Codex와 Cowork 모두 맥에 접근 권한이 있어 저장소 밖이어도 위험하다"고 짚었다
- AI가 제안한 것: Cowork가 handoff의 "검토" 안이던 암호화 디스크 이미지를 기본 방안으로 올리고 운영 규칙을 붙였다. 승인 화면으로 정답이 보이는 문제와 정답 확인 시점, settings.local.json의 python3 허용도 Cowork가 짚었다. 결정은 에드워드가 함

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: handoff.md 5절의 "E3 계획 안"을 2026-10-14에 확정한 정답 격리 규칙으로 바꾼다.

1. handoff.md 5절의 "- E3 계획 안(…)" 줄과 그 아래 들여쓴 세 줄을 지우고, 그 자리에 지시한 아홉 줄("- E3 정답 격리 규칙(2026-10-14 확정. …):"과 들여쓴 여덟 줄: 암호 디스크 이미지 위치와 이유, 열고 잠그는 때, 암호 관리, 기대 답 초안을 쓰는 대화, 그 대화의 자동 승인 예외, 에드워드의 확인 시점과 새 판, settings.local.json 주의, 예측 커밋 시점)을 그대로 넣는다. 다른 줄은 건드리지 않는다
2. worklog 2026-10-14 항목 끝에 이 절. "에드워드의 결정" 두 줄은 그대로
3. 저장소 밖 파일과 ai-consulting/raw/는 열지 않는다. .claude/settings.local.json은 읽기만 하고 고치지 않는다. commit·push 하지 않음

#### 읽은 파일

- handoff.md, worklog.md(끝부분)
- .claude/settings.local.json(읽기만, 고치지 않음). allow 목록에 "Bash(python3 -)"가 있는 것을 확인함. 이 규칙이 `python3 - <<'EOF'`처럼 뒤에 입력이 붙은 명령까지 승인 없이 통과시키는지는 Claude Code가 확인하지 않음(확인 필요). 이 대화는 자동 모드로 돌고 있어 승인 화면이 뜨지 않은 것으로는 판단할 수 없음
- 저장소 밖 파일과 ai-consulting/raw/는 열지 않음. 디스크 이미지(~/Documents/rag-answer-keys.dmg)도 열거나 확인하지 않음

#### 만든·고친 파일

- handoff.md: 수정 — 5절 "E3 계획 안" 네 줄을 지시한 아홉 줄로 바꿈. 다른 줄은 고치지 않음; 이어서 Cowork 정정에 따라 5절 "주의" 줄을 고침(자동 모드 위험을 적고, python3 허용이 입력 붙은 명령까지 통과시키는지는 확인 필요로 바꿈. 처음 문장은 Cowork가 확인 없이 단정한 것이었음)
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 1번 E3 기대 답 (2026-10-14, 16:30경 마침, 정답 격리 Claude Code 대화)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 1번 도메인 골든 세트의 기대 답(정답)을 쓴다. 이 대화는 정답 격리 전용이고 끝나면 다시 쓰지 않는다.

- 지킬 것: handoff.md 5절 정답 격리 규칙에 따라 저장소 밖에는 /Volumes/rag-answer-keys에만 쓴다(AGENTS.md "저장소 폴더 안에서만" 규칙의 예외). 다른 저장소 밖 파일은 열지 않고 웹을 쓰지 않는다. schema.md 원칙대로 원문에 적힌 것만 쓴다. 디스크 안 파일은 Write/Edit 도구로만 쓰고 Bash에는 정답 내용을 넣지 않는다. 저장소 안에는 정답 내용을 쓰지 않고 raw/를 복사하지 않는다. commit·push 하지 않는다
1. 디스크 안 ai-consulting/ 폴더에 기준 그래프, Q1~Q10·T1~T4 기대 답, T5 진술과 기대 답(사람 그래프 대상 7건이 아닌 사례로) 세 파일을 쓴다
2. 저장소에 세 파일의 SHA-256 해시 파일을 만들고, handoff.md 4절 표 E3 행 1번 칸과 5절 "1번 E3 골든 세트" 줄에 해시 파일 링크를 넣는다
3. worklog 2026-10-14 항목 끝에 이 절
4. 마지막 보고는 정답 내용 없이 한다

#### 읽은 파일

- AGENTS.md, handoff.md, worklog.md(끝부분)
- deep/07-graphrag/ai-consulting/schema.md, questions.md, sources.csv
- deep/07-graphrag/ai-consulting/raw/ac-01.txt ~ ac-17.txt(17건 전부)
- 저장소 밖: /Volumes/rag-answer-keys(폴더 목록, 이 대화가 쓴 파일만). 다른 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음
- 근거 문장이 원문에 그대로 있는지 확인하는 스크립트를 이 대화의 임시 폴더(저장소 밖, Claude Code scratchpad)에 두고 돌림. 스크립트에는 정답 내용이 없고, 출력은 행 번호만 냄

#### 만든·고친 파일

- 디스크 안(/Volumes/rag-answer-keys/ai-consulting/, 저장소 밖): reference-triples.csv(177줄), answer-key.md(422줄), t5-statement.md(26줄). 내용은 여기 적지 않음
- deep/07-graphrag/ai-consulting/answer-key.sha256: 새로 만듦 — 디스크 안 폴더에서 `shasum -a 256 answer-key.md reference-triples.csv t5-statement.md`를 돌린 출력 그대로
- handoff.md: 수정 — 4절 표 E3 행 1번 칸, 5절 "1번 E3 골든 세트" 줄. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- 정답 내용은 저장소에 쓰지 않음. raw/ 파일은 다른 곳으로 복사하지 않음
- commit·push는 하지 않음. 디스크 잠그기는 에드워드가 함

### 정답 격리 후속 (2026-10-14, 에드워드)

- 기대 답을 쓴 Claude Code 세션을 에드워드가 삭제했다. 대화 기록에 정답이 남아 디스크 밖 사본이 되는 것을 막기 위해서다. 디스크는 잠갔다.

### 1번 E3 골든 룰과 검사 스크립트 (2026-10-14, 16:47경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 1번 도메인 골든 룰(답이 채점 전에 지켜야 할 규칙)과 검사 스크립트를 만들고 시험한다.

- 지킬 것: 정답(기대 답)은 보지 않는다. /Volumes/rag-answer-keys는 열지 않고, 열려 있으면 멈춘다. 저장소 밖 파일은 열지 않고, 웹을 쓰지 않고, 설치하지 않는다(python 표준 라이브러리만). commit·push 하지 않는다. 시험 파일에는 원장 제목, sources.csv의 펌(수행), 일부러 틀린 값, "테스트" 같은 문자열만 쓰고 사례를 분류한 실제 값은 쓰지 않는다

1. ai-consulting/golden-rules.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다(1~5절: 하는 일과 하지 않는 일, 답의 모양, 골든 룰 G1~G9, 검사 스크립트, 판단 기록)
2. experiments/scripts/check-golden-rules.py: 맨 위 한국어 주석(하는 일, 입력, 출력), G1~G9 구현, 출력과 종료 코드는 4절대로 한국어로. 스키마 목록 상수를 시작할 때 schema.md 본문과 대조해 없으면 종료 코드 2. 원장 번호·펌은 sources.csv, G4는 ai-consulting/raw/를 읽고 없으면 종료 코드 2. 한 주장에 걸린 규칙은 모두 보고
3. experiments/fixtures/에 golden-rules-pass.json(모두 통과), golden-rules-fail.json(G1~G9 하나씩), golden-rules-empty.json(빈 목록) — 항목은 지시대로
4. 세 파일로 돌려 experiments/golden-rules-test.md에 실행 명령, 종료 코드, 출력 그대로, 판정 표(코드 판정과 사람 판정 열을 나눔, 사람 판정은 "에드워드 확인 전")를 남긴다. 기대와 다르면 고치고 고친 내용과 다시 돌린 결과를 남긴다
5. ai-consulting/README.md 끝에 "골든 룰(E3): [golden-rules.md](golden-rules.md)" 한 줄
6. handoff.md 4절 표 E3 행 1번 칸의 " 확정" 앞에 골든 룰 링크, 5절 "1번 E3 골든 세트" 줄의 "골든 룰과 검사 스크립트"에 "(완료, …)"
7. worklog 2026-10-14 항목 끝에 "정답 격리 후속"(에드워드) 절과 이 절

#### 한 일과 결과

- 시작 전에 `ls /Volumes`로 rag-answer-keys가 마운트되어 있지 않음을 확인함(Macintosh HD만 있음). 디스크 안은 열지 않음
- 시험 결과: 통과 시험 종료 코드 0(위반 없음), 위반 시험 종료 코드 1(G1~G9가 항목마다 하나씩 걸림, T1만 G8이 두 조건으로 두 번), 입력 오류 시험 종료 코드 2. 기대와 다르게 나온 것이 없어 시험 뒤 스크립트를 고치지 않음. 자세한 출력은 deep/07-graphrag/experiments/golden-rules-test.md
- G4 정규화 시험이 실제로 되었는지 따로 확인함: 원장 7번 제목은 원문에 그대로는 없고 공백 정규화 뒤에는 있음(원문 내용은 출력하지 않음)
- 규칙끼리 어긋난 곳(확인 필요): 스키마 5절 목록 이름은 "생성형 AI(LLM 포함)"인데 골든 룰 G9는 Q3 값을 "생성형 AI"로 정함. 스크립트는 목록 이름을 "생성형 AI"로 보고 괄호는 설명으로 뺐다. 에드워드가 정할 일
- 입력 오류 기준을 글자대로 구현해 파일 전체 주장이 0개여도 종료 코드 2가 됨(T1·T3·T4 답만 든 파일은 입력 오류). G4는 하이픈을 붙인 정규화로 못 찾으면 하이픈을 남긴 정규화로도 한 번 더 봄(낱말 안 하이픈 대비). 둘 다 golden-rules-test.md 3절에 적음
- 설치한 도구 없음(python 표준 라이브러리 csv, json, re, pathlib)

#### 읽은 파일

- handoff.md, worklog.md(끝부분), deep/07-graphrag/ai-consulting/README.md, schema.md(스크립트가 읽음), sources.csv(번호·펌·제목)
- ai-consulting/raw/ac-*.txt: 스크립트(G4)와 7번 정규화 확인 코드가 읽음. Claude Code가 원문 내용을 화면에 출력하거나 읽지는 않았고, 시험에 쓴 근거 문장은 원장 제목과 테스트 문장뿐
- 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음. /Volumes/rag-answer-keys와 ai-consulting/answer-key.sha256은 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/golden-rules.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음
- deep/07-graphrag/experiments/scripts/check-golden-rules.py: 새로 만듦 — 골든 룰 검사 스크립트
- deep/07-graphrag/experiments/fixtures/golden-rules-pass.json, golden-rules-fail.json, golden-rules-empty.json: 새로 만듦 — 시험 파일(원장 제목, 수행 펌, 일부러 틀린 값만)
- deep/07-graphrag/experiments/golden-rules-test.md: 새로 만듦 — 시험 결과
- deep/07-graphrag/ai-consulting/README.md: 수정 — 끝에 지시한 한 줄 추가
- handoff.md: 수정 — 4절 표 E3 행 1번 칸, 5절 "1번 E3 골든 세트" 줄. 다른 줄은 고치지 않음. 4절 칸은 지시문을 쓴 뒤 커밋 b847eaf에서 "·기대 답 해시(…)"가 들어가 있어, 처음 고치기 코드가 지시문의 옛 문구를 찾지 못해 멈춤(handoff는 그때 바뀌지 않음, README와 worklog는 이미 써짐). 지시대로 " 확정" 바로 앞, 곧 기대 답 해시 링크 뒤에 골든 룰 링크를 넣음
- worklog.md: 수정 — "정답 격리 후속" 절(에드워드가 준 문장 그대로)과 이 절 추가
- commit·push는 하지 않음

### 1번 E3 골든 룰 정정 (2026-10-14, 16:57경 마침, Claude Code)

- 경위: Claude Code가 스키마 5절 "생성형 AI(LLM 포함)"와 G9 "생성형 AI"의 불일치를 찾았다. Cowork가 지시문을 쓰며 낸 실수다. 스키마는 기대 답보다 먼저 커밋됐으므로 스키마 이름을 기준으로 G9와 스크립트를 고쳤다. 같은 때 입력 오류 기준(주장 0개만으로는 오류가 아님), G4 하이픈 처리 문서화, __pycache__ 무시를 함께 정리했다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

커밋 전에 골든 룰을 고친다. 정답(디스크)은 보지 않는다. 저장소 밖 파일은 열지 않는다. 설치하지 않는다. commit·push 하지 않는다.

1. golden-rules.md 세 곳만: G9의 Q3 값을 "생성형 AI(LLM 포함)"로, G4 행에 하이픈을 남긴 채 한 번 더 보는 문장 추가, 4절 입력 오류 문장을 "질문을 하나도 읽지 못하면 2로 끝낸다. 주장이 0개인 답은 G1·G2·G8로 본다."로
2. check-golden-rules.py: AI 기술 목록과 G9 Q3 값을 "생성형 AI(LLM 포함)"로 하고 괄호를 빼던 주석과 처리를 없앤다. 종료 코드 2는 질문 0개(와 기존 파일·JSON·스키마·원장·raw 오류)에만
3. fixtures/golden-rules-controls-only.json(T1·T3·T4, 자료에 없음, 주장 빈 목록, 요약 "테스트")을 만들고 종료 코드 0이 나와야 함
4. 시험 파일 네 개로 다시 돌려 golden-rules-test.md 끝에 "## 4. 정정 뒤 다시 돌린 결과 (2026-10-14)" 절(고친 내용, 실행 명령, 종료 코드, 출력 그대로, 판정 표, 사람 판정은 "에드워드 확인 전"). 앞 절은 고치지 않음
5. .gitignore 맨 끝에 "# 파이썬 실행 캐시"와 "__pycache__/" 두 줄. git status에 __pycache__가 안 나오는지 확인
6. worklog "1번 E3 골든 룰과 검사 스크립트" 절 뒤에 이 절. 경위 줄은 그대로

#### 결과

- 시작 전에 `ls /Volumes`로 rag-answer-keys가 마운트되어 있지 않음을 확인함
- 다시 돌린 결과: pass 0(위반 없음), fail 1(G1~G9 하나씩, 정정 전과 같은 출력), empty 2(질문 0개), controls-only 0(위반 없음). 모두 기대대로
- __pycache__: deep/07-graphrag/experiments/scripts/__pycache__가 있었음. 앞 절 작업에서 Claude Code가 7번 정규화를 확인하려고 스크립트를 모듈로 불러올 때 생긴 것으로 보임. .gitignore에 두 줄을 더한 뒤 `git status --short --untracked-files=all`에 __pycache__가 나오지 않음을 확인함. 폴더는 지우지 않음

#### 읽은 파일

- worklog.md(절 제목 목록과 끝부분), .gitignore, golden-rules.md, check-golden-rules.py, golden-rules-test.md(모두 이 대화에서 만든 파일)
- ai-consulting/raw/는 스크립트(G4)만 읽음. 저장소 밖 파일과 디스크는 열지 않음. worklog의 "1번 E3 기대 답" 절과 answer-key.sha256은 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/golden-rules.md: 수정 — G9 Q3 값, G4 행 문장 추가, 4절 입력 오류 문장. 다른 곳은 고치지 않음
- deep/07-graphrag/experiments/scripts/check-golden-rules.py: 수정 — AI 기술 목록과 G9 Q3 값을 "생성형 AI(LLM 포함)"로, 괄호 주석 지움, 입력 오류 조건을 질문 0개로(맨 위 주석의 종료 코드 설명도 맞춤)
- deep/07-graphrag/experiments/fixtures/golden-rules-controls-only.json: 새로 만듦
- deep/07-graphrag/experiments/golden-rules-test.md: 수정 — 끝에 4절 추가. 앞 절은 고치지 않음
- .gitignore: 수정 — 맨 끝에 두 줄 추가. 기존 줄은 그대로
- worklog.md: 수정 — 이 절 추가
- 설치한 도구 없음. commit·push는 하지 않음

### 1번 E3 예측 (2026-10-14, 17:27경 마침, Claude Code)

- 예측 문장은 에드워드가 AI 의견 없이 썼고, Cowork는 양식과 판정 기준만 제안했다. 판정 기준은 결과를 보기 전에 정했다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 1번 도메인 예측을 deep/07-graphrag/ai-consulting/predictions.md로 만든다. 그래프를 만들기 전에 커밋할 파일이다.

- 지킬 것: 정답(디스크)과 ai-consulting/raw/는 열지 않는다. 저장소 밖 파일은 열지 않는다. commit·push 하지 않는다

1. predictions.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다(1~4절: 질문 종류별 예측, 통제 항목 예측, E4 일치율 예측, 판정 기준)
2. ai-consulting/README.md 끝에 "예측(E3): [predictions.md](predictions.md)" 한 줄
3. handoff.md 4절 표 E3 행 1번 칸의 " 확정" 바로 앞에 예측 링크, 5절 "1번 E3 골든 세트" 줄 끝 " → 예측"을 " → 예측(완료, …)"으로
4. worklog 2026-10-14 항목 끝에 이 절. 첫 줄은 그대로

#### 읽은 파일

- handoff.md(4절 E3 행과 5절 줄), deep/07-graphrag/ai-consulting/README.md, worklog.md(끝부분)
- 디스크(/Volumes/rag-answer-keys), ai-consulting/raw/, 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/predictions.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음
- deep/07-graphrag/ai-consulting/README.md: 수정 — 끝에 지시한 한 줄 추가
- handoff.md: 수정 — 4절 표 E3 행 1번 칸, 5절 "1번 E3 골든 세트" 줄 끝. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 1번 E3 판단 기록 이유 채움 (2026-10-14, 17:33경 마침, Claude Code)

- 이유 문장은 Cowork가 E1 기록과 에드워드의 말을 바탕으로 낸 보기 가운데 에드워드가 고른 것(schema 1번 가·나와 2번 가, questions 가·가, golden-rules 가+나)을 Cowork가 문장으로 이었다. 스키마·질문·골든 룰의 내용은 바꾸지 않았다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 1번 도메인 세 파일의 판단 기록 이유 칸을 채운다. 다른 줄은 건드리지 않는다. 정답(디스크)과 ai-consulting/raw/, 저장소 밖 파일은 열지 않는다. commit·push 하지 않는다.

1. ai-consulting/schema.md, questions.md, golden-rules.md의 판단 기록 머리줄 "작성: 에드워드, 2026-10-14. 1·2항은 Cowork가 사실을 정리함"에 ". 3항은 Cowork가 낸 보기 가운데 에드워드가 고른 것을 Cowork가 문장으로 이음"을 붙인 줄로 바꾼다
2. 세 파일의 "그렇게 판단한 이유: 아직 적지 않음(에드워드가 채운다)." 줄을 파일마다 지시한 문장으로 바꾼다(schema: 펌이 맡는 과제가 궁금했고 5·7번은 펌이 한 일로 나눔 / questions: 종류별 비교와 MBB·Big4 비교 / golden-rules: 05 실험 경험과 사람 검토의 한계로 기계로 먼저 거름)
3. worklog 2026-10-14 항목 끝에 이 절. 첫 줄은 그대로

#### 읽은 파일

- deep/07-graphrag/ai-consulting/schema.md, questions.md, golden-rules.md(고칠 두 줄을 찾는 데만), worklog.md(끝부분)
- 디스크, ai-consulting/raw/, 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/ai-consulting/schema.md, questions.md, golden-rules.md: 수정 — 파일마다 판단 기록 머리줄과 이유 줄 두 줄만 바꿈(git diff로 파일마다 2줄 바뀐 것 확인). 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 2번 E3 스키마 (2026-10-14, 17:40경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 도메인(무역 & 기름) 그래프 스키마를 deep/07-graphrag/oil-trade/schema.md로 만들고, 1번 E3를 완료로 표시한다.

- 지킬 것: 정답(디스크)은 열지 않는다. 저장소 밖 파일은 열지 않는다. 웹을 쓰지 않는다. commit·push 하지 않는다

1. oil-trade/schema.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다(1~7절: 원칙, 한 줄의 모양(관계 3종), 닫힌 목록(제품·분류 체계·주체), 업무 단계 9개와 판정 규칙, 기록 형식, 비교 방법, 판단 기록)
2. oil-trade/README.md 끝에 "그래프 스키마(E3): [schema.md](schema.md)" 한 줄
3. handoff.md 4절 표 E3 행 1번 칸 맨 앞 "진행."을 "완료."로, 2번 칸 "대기"를 "진행. 스키마 확정(…)"으로. 5절 "- 두 도메인 E3 골든 세트" 줄을 2번 E3 골든 세트 순서 줄로
4. worklog 2026-10-14 항목 끝에 이 절

#### 확인한 것

- schema.md 4절 근거 조문이 원장에 실제로 있는지 확인함: 법 제5조의2·6·7·8·10·11·12·14·15·16·17·18·18조의2·18조의3·18조의4·18조의5·19·20·21조의2·21조의3(raw/ot-04.txt), 시행령 제10조·제17조의6(raw/ot-05.txt) 22개 모두 조문 머리줄이 있음. 조문 제목도 각 단계의 "하는 일"과 맞음(예: 법 제5조의2 폐기물 수출입자의 자격, 시행령 제17조의6 보증금 예탁기관의 지정 등, 시행령 제10조 수출입규제폐기물 수입동의요청의 간주). 조문 본문은 읽지 않음

#### 읽은 파일

- handoff.md(4절 E3 행과 5절), worklog.md(끝부분), deep/07-graphrag/oil-trade/README.md
- deep/07-graphrag/oil-trade/raw/ot-04.txt, ot-05.txt(조문 머리줄만 검색)
- 디스크와 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/schema.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음
- deep/07-graphrag/oil-trade/README.md: 수정 — 끝에 지시한 한 줄 추가(앞 줄과 빈 줄 없이 붙음)
- handoff.md: 수정 — 4절 표 E3 행 1번 칸 "진행."→"완료.", 2번 칸 "대기"→"진행. 스키마 확정(…)". 5절 "- 두 도메인 E3 골든 세트" 줄을 2번 E3 골든 세트 줄로. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 2번 E3 질문·통제 항목 (2026-10-14, 17:51경 마침, Claude Code)

- 2번 schema.md 판단 기록 이유는 Cowork가 낸 보기 가운데 에드워드가 고른 것(단계 근거 가·나, 통관 가)에 "통관은 나중에 추가할 예정"이라는 에드워드의 말을 더해 Cowork가 문장으로 이었다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 도메인 골든 세트 질문을 deep/07-graphrag/oil-trade/questions.md로 만들고, 2번 schema.md의 판단 기록 이유를 채운다.

- 지킬 것: 정답(디스크), 저장소 밖 파일은 열지 않는다. 웹을 쓰지 않는다. 기대 답은 쓰지 않는다. commit·push 하지 않는다

1. oil-trade/questions.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다(1~6절: 설계 원칙, 질문 종류 A~E, 질문 10개와 고른 방법, 통제 항목 5개, 기대 답을 쓸 때 확인할 것, 판단 기록)
2. oil-trade/schema.md 7절 두 줄만: 판단 기록 머리줄에 "3항은 …" 문장을 붙이고, 이유 줄을 지시 문장으로
3. oil-trade/README.md 끝에 "골든 세트 질문(E3): [questions.md](questions.md)" 한 줄
4. handoff.md 4절 표 E3 행 2번 칸을 "진행. 스키마(…)·질문(…) 확정"으로, 5절 "2번 E3 골든 세트" 줄의 "질문·통제 항목"에 "(완료, …)"
5. worklog 2026-10-14 항목 끝에 이 절. 첫 줄은 그대로

#### 확인한 것

- questions.md "고른 방법"과 T2 기대 행동이 원장 4번 조문 제목과 맞는지 확인함(앞 절 "2번 E3 스키마"에서 뽑은 조문 머리줄): 제7조 "수출이동서류의 작성 등", 제6조 "수출입규제폐기물의 수출허가"로 T2가 바로잡을 내용과 같음

#### 읽은 파일

- handoff.md(4절 E3 행과 5절), worklog.md(끝부분), deep/07-graphrag/oil-trade/schema.md(7절), README.md
- 디스크와 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음. 이번에 raw 파일은 새로 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/questions.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음. 기대 답은 쓰지 않음
- deep/07-graphrag/oil-trade/schema.md: 수정 — 7절 판단 기록 머리줄과 이유 줄 두 줄만 바꿈
- deep/07-graphrag/oil-trade/README.md: 수정 — 끝에 지시한 한 줄 추가
- handoff.md: 수정 — 4절 표 E3 행 2번 칸, 5절 "2번 E3 골든 세트" 줄. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

## 2026-10-15

### 2번 E3 기대 답 (2026-10-15, 09:07경 마침, 정답 격리 Claude Code 대화)

- 지시는 "2026-10-14, HH:MM" 형식이었으나 실제로 마친 날짜가 2026-10-15라 그 날짜를 적었다. 처음에는 2026-10-14 항목 끝에 붙였고, 뒤에 Cowork 지시로 2026-10-15 항목을 새로 열었다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 도메인(무역 & 기름) 골든 세트의 기대 답(정답)을 쓴다. 이 대화는 정답 격리 전용이고 끝나면 다시 쓰지 않는다.

- 지킬 것: handoff.md 5절 정답 격리 규칙에 따라 저장소 밖에는 /Volumes/rag-answer-keys에만 쓴다(AGENTS.md "저장소 폴더 안에서만" 규칙의 예외). 다른 저장소 밖 파일은 열지 않고 웹을 쓰지 않는다. schema.md 원칙대로 원문에 적힌 것만 쓴다. 디스크 안 파일은 Write/Edit 도구로만 쓰고 Bash에는 정답 내용을 넣지 않는다. 저장소 안에는 정답 내용을 쓰지 않고 raw/를 복사하지 않는다. 실무 정보는 어디에도 쓰지 않는다. commit·push 하지 않는다
1. 디스크 안 oil-trade/ 폴더에 기준 그래프(schema.md 5절 칸), Q1~Q10·T1~T4 기대 답, T5 진술과 기대 답 세 파일을 쓴다
2. 저장소에 세 파일의 SHA-256 해시 파일을 만들고, handoff.md 4절 표 E3 행 2번 칸과 5절 "2번 E3 골든 세트" 줄에 해시 파일 링크를 넣는다
3. worklog 2026-10-14 항목 끝에 이 절
4. 마지막 보고는 정답 내용 없이 한다(질문별 답 있음/없음, T1~T3 질문 수정 필요 여부, 파일 줄 수, 해시 파일 경로)

#### 읽은 파일

- AGENTS.md, handoff.md, worklog.md(끝부분, 1번 E3 기대 답 절과 2번 E3 스키마·질문 절)
- deep/07-graphrag/oil-trade/schema.md, questions.md, sources.csv
- raw/ 전체를 읽은 것: ot-02, ot-03, ot-04, ot-05, ot-06, ot-07, ot-09, ot-11, ot-12, ot-16
- raw/ 일부를 읽은 것: ot-01, ot-08, ot-10, ot-13, ot-14, ot-15, ot-17. 읽은 줄 범위와 그 부분의 내용 설명은 정답 위치를 알려 줄 수 있어 저장소에 남기지 않았다(2026-10-15 Cowork 지시로 지움).
- 저장소 밖: /Volumes/rag-answer-keys(폴더 목록, 이 대화가 쓴 파일만). 다른 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음
- 근거 문장이 원문에 그대로 있는지 확인하고 업무 단계·주체 칸을 세는 스크립트를 이 대화의 임시 폴더(저장소 밖, Claude Code scratchpad)에 두고 돌림. 스크립트에는 정답 내용이 없고, 출력은 행 번호와 칸 값 집계만 냄. 결과: 근거 문장 139줄 모두 원문에 있음

#### 만든·고친 파일

- 디스크 안(/Volumes/rag-answer-keys/oil-trade/, 저장소 밖): reference-triples.csv(140줄, 머리줄 포함), answer-key.md(415줄), t5-statement.md(24줄). 내용은 여기 적지 않음
- deep/07-graphrag/oil-trade/answer-key.sha256: 새로 만듦 — 디스크 안 폴더에서 `shasum -a 256 answer-key.md reference-triples.csv t5-statement.md`를 돌린 출력 그대로. `shasum -a 256 -c`로 세 파일 모두 OK 확인
- handoff.md: 수정 — 4절 표 E3 행 2번 칸, 5절 "2번 E3 골든 세트" 줄. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- 정답 내용은 저장소에 쓰지 않음. raw/ 파일은 다른 곳으로 복사하지 않음
- commit·push는 하지 않음. 디스크 잠그기와 세션 삭제는 에드워드가 함

### 2번 E3 기대 답 후속 (2026-10-15, 09:26경 마침, Claude Code)

- 격리 대화의 마지막 보고에 정답 일부(Q9의 결과 건수, T1·T3의 근거 설명)가 들어갔다. 지시는 "보고에 정답 내용을 쓰지 않는다"였다. 이 보고를 에드워드와 Cowork가 읽었다. 2번은 사람 그래프가 필수가 아니고 에드워드와 Cowork는 답하는 쪽이 아니어서, 다시 시작하지 않고 기록만 남긴다.
- 같은 대화가 worklog에 원문을 읽은 줄 범위와 그 부분의 내용 설명을 적었다. 그래프를 만들거나 답하는 대화가 worklog를 읽으면 정답 위치의 힌트가 될 수 있어 커밋 전에 지웠다. Cowork는 확인하면서 그 줄을 읽었다.
- Q9는 격리 대화가 질문을 바꾸자고 했으나 그대로 둔다(에드워드 결정). 답을 안 뒤에 질문을 고치면 정답에 맞춰 질문을 다듬는 셈이 되기 때문이다. Q9는 결과적으로 통제 항목에 가까운 성격을 띤다.
- 격리 대화는 제품과 분류를 원문 문장 두 개(원문 용어 근거, 분류 근거)로 이었다고 보고했다. 이 방식을 허용할지는 2번 골든 룰에서 정한다.
- 정답을 쓴 세션은 에드워드가 삭제했고, 디스크는 잠갔다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 커밋 전에 worklog.md를 정리한다. 정답(디스크)과 저장소 밖 파일은 열지 않는다. commit·push 하지 않는다.

1. "### 2번 E3 기대 답 (2026-10-15, 09:07경 마침, 정답 격리 Claude Code 대화)" 절의 "#### 읽은 파일" 아래 "- raw/ 일부를 읽은 것" 줄과 그 아래 들여쓴 줄들("- 저장소 밖:" 줄 앞까지)을 지우고, 읽은 raw 파일 번호만 적은 한 줄(지시 문장)로 바꾼다. 지울 줄의 내용은 화면에 출력하거나 읽지 않고, 줄 머리 글자로 위치를 찾는 스크립트로 지우며, 확인은 `git diff --stat`과 지운 줄 수로만 한다
2. 같은 절 맨 앞의 "- 지시는 "2026-10-14, HH:MM" 형식이었으나 …" 줄을 지시 문장(2026-10-15 항목을 새로 연 경위)으로 바꾼다
3. 그 절 제목 바로 앞에 "## 2026-10-15" 줄을 넣는다(앞뒤 빈 줄 하나씩)
4. worklog 맨 끝(2026-10-15 항목 안)에 이 절. 맨 앞 다섯 줄은 그대로

#### 한 일과 확인

- 시작 전에 `ls /Volumes`로 디스크가 마운트되어 있지 않음을 확인함
- 스크립트가 출력한 것은 줄 번호, 줄 수, 참·거짓뿐. 대상 절에서 "- raw/ 일부를 읽은 것" 줄 1줄과 "- 저장소 밖:" 줄 사이의 6줄이 모두 들여쓴 줄이고 빈 줄이 없음을 확인한 뒤, 이 7줄을 지시한 1줄로 바꿈(worklog 2,048줄 → 2,044줄. "## 2026-10-15"와 빈 줄 2줄 추가 포함)
- `git diff --stat`: 대상 절이 아직 커밋 전이라 HEAD 대비 추가만 잡힘(34줄 추가, 삭제 0). 그래서 지운 줄 수는 스크립트로 센 값(7줄)으로 확인함
- 1번 대상 줄을 지우기 전에 Claude Code가 그 줄의 내용을 읽거나 출력하지 않음

#### 읽은 파일

- worklog.md: 대상 절의 위치(제목, 소제목, 줄 머리 글자)만 스크립트로 찾음. 대상 절의 본문 내용은 읽지 않음
- 디스크와 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- worklog.md: 수정 — "2번 E3 기대 답" 절의 "읽은 파일" 7줄을 1줄로 바꿈, 같은 절 첫 줄 바꿈, 절 앞에 "## 2026-10-15" 항목 머리 추가, 끝에 이 절 추가
- commit·push는 하지 않음

### 2번 E3 골든 룰과 검사 스크립트 (2026-10-15, 09:33경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 도메인 골든 룰과 검사 스크립트를 만들고 시험한다.

- 지킬 것: 정답(디스크)과 저장소 밖 파일은 열지 않는다. 웹을 쓰지 않는다. 설치하지 않는다(python 표준 라이브러리만). commit·push 하지 않는다. 1번 스크립트(check-golden-rules.py)와 1번 시험 파일은 고치지 않는다. 시험 파일에는 원장 제목, 원문 머리줄, 일부러 틀린 값, "테스트" 같은 문자열만 쓰고 실제 분류·요건·업무 단계 값을 원문에서 찾아 쓰지 않는다

1. oil-trade/golden-rules.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다(1~5절: 하는 일과 하지 않는 일, 답의 모양(주장 일곱 칸, 근거 세 칸, 근거 두 개 허용), 골든 룰 G1~G9, 검사 스크립트, 판단 기록)
2. experiments/scripts/check-golden-rules-oil-trade.py: 맨 위 한국어 주석, G1~G9 구현, 출력·종료 코드는 4절대로 한국어로, 정규화·하이픈 처리는 1번과 같게. 스키마 목록 상수를 oil-trade/schema.md 본문과 대조해 없으면 종료 코드 2. 원장 번호는 oil-trade/sources.csv, G4는 oil-trade/raw/(없으면 종료 코드 2). 한 주장·근거에 걸린 규칙은 모두 보고
3. experiments/fixtures/에 oil-trade-golden-rules-pass.json, -fail.json(G1~G9 하나씩), -empty.json, -controls-only.json — 항목은 지시대로, 실제 값이 필요한 자리는 "기타: 테스트"
4. 네 파일로 돌려 experiments/golden-rules-oil-trade-test.md에 실행 명령, 종료 코드, 출력 그대로, 판정 표(사람 판정은 "에드워드 확인 전"). 기대: pass 0, fail 1, empty 2, controls-only 0. 다르면 고치고 기록
5. oil-trade/README.md 끝에 "골든 룰(E3): [golden-rules.md](golden-rules.md)" 한 줄
6. handoff.md 4절 표 E3 행 2번 칸의 " 확정" 앞에 골든 룰 링크, 5절 "2번 E3 골든 세트" 줄의 "골든 룰과 검사 스크립트"에 "(완료, …)"
7. worklog 2026-10-15 항목 끝에 이 절

#### 한 일과 결과

- 시작 전에 `ls /Volumes`로 디스크가 마운트되어 있지 않음을 확인함
- 시험 결과: pass 종료 코드 0(위반 없음), fail 1(G1~G9가 항목마다 하나씩, G7·G8만 한 항목에서 두 조건이 함께 걸림), empty 2(질문 0개), controls-only 0(위반 없음). 처음 돌린 결과가 기대와 같아 스크립트를 고치지 않음
- 시험 파일에 쓴 값: sources.csv 4·5·8번 제목, ot-17.txt에서 글자가 있는 첫 줄(머리줄), 일부러 틀린 값, "테스트"·"기타: 테스트"·"테스트 분류 값". 실제 분류·요건·업무 단계 값은 찾아 쓰지 않음
- 분류 체계 상수는 스키마 3절 표기 그대로 "HS(관세율표·WCO)"로 둠(1번 "생성형 AI(LLM 포함)" 정정과 같은 기준)
- handoff: 지시문을 쓴 뒤 커밋 11e0a4c에서 4절 2번 칸에 "·기대 답 해시(…)"가 들어가 있어, 처음 고치기 코드가 옛 문구를 찾지 못해 멈춤(handoff는 그때 바뀌지 않음, README 줄은 이미 써짐). 지시대로 " 확정" 바로 앞, 곧 기대 답 해시 링크 뒤에 골든 룰 링크를 넣음
- 1번 스크립트와 1번 시험 파일은 고치지 않음(git status에 나오지 않음)
- 설치한 도구 없음(python 표준 라이브러리 csv, json, re, pathlib)

#### 읽은 파일

- handoff.md(4절 E3 행과 5절), worklog.md(끝부분), deep/07-graphrag/oil-trade/README.md, schema.md(3절 목록 줄, 스크립트가 본문 대조), sources.csv(4·5·8번 제목, 스크립트가 번호)
- deep/07-graphrag/oil-trade/raw/ot-17.txt: 글자가 있는 첫 줄만 뽑음. raw 전체는 스크립트(G4)가 읽음. Claude Code가 원문 본문을 화면에 출력하거나 읽지는 않음
- 디스크, oil-trade/answer-key.sha256, 저장소 밖 파일은 열지 않았고 웹도 쓰지 않음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/golden-rules.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음
- deep/07-graphrag/experiments/scripts/check-golden-rules-oil-trade.py: 새로 만듦
- deep/07-graphrag/experiments/fixtures/oil-trade-golden-rules-pass.json, -fail.json, -empty.json, -controls-only.json: 새로 만듦
- deep/07-graphrag/experiments/golden-rules-oil-trade-test.md: 새로 만듦 — 시험 결과
- deep/07-graphrag/oil-trade/README.md: 수정 — 끝에 지시한 한 줄 추가
- handoff.md: 수정 — 4절 표 E3 행 2번 칸, 5절 "2번 E3 골든 세트" 줄. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 2번 E3 예측 (2026-10-15, 09:39경 마침, Claude Code)

- 예측 문장은 에드워드가 AI 의견 없이 썼고, Cowork는 양식과 판정 기준만 제안했다. 판정 기준은 결과를 보기 전에 정했다. 에드워드는 Q9 결과 일부를 본 뒤에 이 예측을 썼다.

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 2번 도메인 예측을 deep/07-graphrag/oil-trade/predictions.md로 만들고, 2번 E3를 완료로 표시한다. 그래프를 만들기 전에 커밋할 파일이다.

- 지킬 것: 정답(디스크), 저장소 밖 파일은 열지 않는다. commit·push 하지 않는다

1. oil-trade/predictions.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다(1~5절: 질문 종류별 예측, 통제 항목 예측, E4 일치율 예측, 두 도메인 비교 예측, 판정 기준)
2. oil-trade/README.md 끝에 "예측(E3): [predictions.md](predictions.md)" 한 줄
3. handoff.md 4절 표 E3 행 2번 칸 맨 앞 "진행."을 "완료."로, 그 칸의 " 확정" 바로 앞에 예측 링크. 5절 "2번 E3 골든 세트" 줄 끝 " → 예측"을 " → 예측(완료, …)"으로
4. worklog 2026-10-15 항목 끝에 이 절. 첫 줄은 그대로

#### 읽은 파일

- handoff.md(4절 E3 행과 5절), deep/07-graphrag/oil-trade/README.md, worklog.md(끝부분)
- 디스크와 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- deep/07-graphrag/oil-trade/predictions.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음
- deep/07-graphrag/oil-trade/README.md: 수정 — 끝에 지시한 한 줄 추가
- handoff.md: 수정 — 4절 표 E3 행 2번 칸("진행."→"완료.", " 확정" 앞에 예측 링크. 기대 답 해시·골든 룰 링크 뒤에 들어감), 5절 "2번 E3 골든 세트" 줄 끝. 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### handoff 인수인계 보강 (2026-10-15, 09:45경 마침, Cowork)

- 에드워드 요청("다른 AI한테 넘길 수 있게 인수인계 같은 거 적어주는 건 어때?")으로 Cowork가 handoff.md를 직접 고쳤다. 6절의 "에드워드 허락을 받은 경우"에 해당한다. Claude Code를 거치지 않은 이유는 크레딧 절약이다.

#### 만든·고친 파일

- handoff.md: 수정 — 머리줄(다른 AI 포함, 8절 안내, 마지막 갱신), 4절 날짜와 "E2·E3 경위" 묶음(5절에 있던 2번 E2 후속, 1번·2번 E3 골든 세트 줄을 옮김, 2번 기대 답 노출 기록 추가), 5절(1주차 남은 일, 2주차 E4·E5, 남은 작은 일), 8절 "다른 AI로 넘길 때" 새로 만듦
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### challenge.md 승인 문구 고침 (2026-10-15, Cowork)

- 에드워드 요청("이거부터 하자")으로 Cowork가 직접 고쳤다. challenge.md 12행의 "승인을 요청한 상태다"가 07 README(2026-10-13 멘토 승인)와 어긋나 있었다.
- deep/07-graphrag/challenge.md: 수정 — 12행을 "2026-10-13 멘토 승인으로 방산에서 무역 & 기름으로 바뀌었다. 아래 원문의 "방산"은 무역 & 기름으로 읽는다"로. 멘토 원문을 옮긴 다른 줄은 고치지 않음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

### 1주차 진행 기록 (2026-10-15, Cowork)

- progress/week-1.md: 새로 만듦 — Cowork가 이번 주 실제 일로 보기를 내고, 에드워드가 고른 것(발견 나·다·라, 막힌 점 가·다·라, 한 일·다음 주 계획은 제안 그대로)을 Cowork가 문장으로 이음
- worklog.md: 수정 — 이 절 추가
- commit·push는 하지 않음

## 2026-10-16

### 리즈 저장소 상호 검토 (2026-10-16, 14:20경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: 리즈 저장소 상호 검토를 progress/review-liz-week-1.md로 만든다.

- 지킬 것: 저장소 밖 파일은 열지 않는다. commit·push 하지 않는다

1. progress/review-liz-week-1.md를 지시문의 시작·끝 표시 사이 내용 그대로 새로 만든다. 고치지 않는다(검토 대상과 범위, 잘된 점 3개, 궁금한 점 3개, 출처를 1차 자료로 바꾸자는 제안, 작성 경위)
2. worklog 2026-10-15 항목 뒤에 "## 2026-10-16" 항목을 새로 만들고 이 절을 남긴다
3. 만든·고친 파일 목록과 새 파일 줄 수를 보고한다

#### 읽은 파일

- worklog.md(날짜 항목 머리와 끝부분), progress/ 폴더 목록(week-1.md가 있음, 열지 않음)
- 리즈 저장소와 검토 문서에 적힌 URL은 열지 않음(검토 내용은 받은 문장 그대로). 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- progress/review-liz-week-1.md: 새로 만듦 — 받은 내용 그대로. 고치지 않음
- worklog.md: 수정 — "## 2026-10-16" 항목과 이 절 추가
- commit·push는 하지 않음

## 2026-10-19

### 리즈 저장소 추가 검토 (2026-10-19, 10:52경 마침, Claude Code)

#### 받은 지시(Cowork가 쓰고 에드워드가 전달)

목표: progress/review-liz-week-1.md 끝에 추가 검토 절을 덧붙인다.

- 지킬 것: 이미 있는 줄은 고치지 않는다. 저장소 밖 파일과 검토 문서의 URL은 열지 않는다. commit·push 하지 않는다

1. review-liz-week-1.md 맨 끝("작성 경위:" 줄 뒤)에 빈 줄 하나를 두고, 지시문의 시작·끝 표시 사이 내용을 그대로 덧붙인다("## 추가 검토 (2026-10-19)": 받은 주소와 받은 시각, 달라진 점, 잘된 점 3개, 궁금한 점 2개, 제안 2개, 작성 경위)
2. worklog 끝에 "## 2026-10-19" 항목을 새로 만들고 이 절을 남긴다
3. 고친 파일 목록과 review-liz-week-1.md 전체 줄 수를 보고한다

#### 읽은 파일

- progress/review-liz-week-1.md(끝 부분 줄바꿈만 확인), worklog.md(날짜 항목 머리와 끝부분)
- 리즈 저장소와 검토 문서의 URL은 열지 않음(검토 내용은 받은 문장 그대로). 저장소 밖 파일은 열지 않음

#### 만든·고친 파일

- progress/review-liz-week-1.md: 수정 — 맨 끝에 빈 줄 하나와 추가 검토 절을 덧붙임. 이미 있던 26줄은 고치지 않음(git diff 삭제 0줄)
- worklog.md: 수정 — "## 2026-10-19" 항목과 이 절 추가
- commit·push는 하지 않음
