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

- 없음

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

그 뒤 기록으로 확인된 것: 당시 디스크 여유 7.2GiB(사용률 97%), 가상환경만으로 1.1GB 사용,
모델 가중치는 flan-t5-large 3.13GB / roberta-large 1.42GB였다. 2026-10-07 기준 여유는 3.6GiB다.
(worklog 2026-10-04·10-05, deep/07-graphrag/plan.md)
