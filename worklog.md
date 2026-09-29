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
