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
- README.md, worklog.md: 수정 3 (2026-09-20 00:22, Claude Cowork) — 사용자 요청으로 사용자 수면 중 대신 작성. README에 배포 URL 기록, worklog에 커밋·Pages URL·문제와 대처·에이전트 오류 후보 기록, 남은 자리표시자를 "확인 필요"로 표시. commit·push는 하지 않음
- worklog.md: 수정 4 (2026-09-21, Claude Code) — Codex 시도 결과의 이유 칸과 아래 문장을 "선호도 이유"로 교체. commit·push는 하지 않음
- worklog.md: 수정 5 (2026-09-21, Claude Code) — 시작 시각을 "2026-09-19 23:40경"으로, Codex 시도 결과의 이유 칸과 아래 문장을 실제 이유 문장으로 교체, "내가 검토한 것"에 두 줄 추가. commit·push는 하지 않음
- worklog.md: 수정 6 (2026-09-21, Claude Code) — "다음 작업"을 9/21~9/25 일정으로 교체, "문제와 대처"의 자리표시자 항목 끝에 "→ 9/21에 실제 값으로 채움" 추가. commit·push는 하지 않음

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
