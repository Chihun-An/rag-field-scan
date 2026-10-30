# 07 GraphRAG

3주 챌린지(두 도메인 GraphRAG)의 작업 공간이다. 2026-10-12에 만들었다.

## 두 도메인

| 번호 | 도메인 | 폴더 | 상태 |
|------|--------|------|------|
| 1 | AI 컨설팅 | [ai-consulting/](ai-consulting/README.md) | 완료(E0~E7) |
| 2 | 무역 & 기름 (지금 다루는 제품: UMO, ULO, PPO) | [oil-trade/](oil-trade/README.md) | 완료(E0~E7) |

2026-10-13 멘토가 승인해 2번 도메인을 방산에서 무역 & 기름으로 바꿨다. 두 도메인 모두 E0~E7을 마쳤다(2026-10-27).

E1 결정(두 도메인 범위와 분류 축): [e1-decisions.md](e1-decisions.md)

3주 챌린지 과제 정의(핵심 질문, 단계 E0~E7과 마감, 필수선): [challenge.md](challenge.md)

실험 방법과 결과(E4·E5): [experiments/](experiments/)

E6 그래프 뷰어: [viewer/](viewer/index.html) (배포: https://chihun-an.github.io/rag-field-scan/deep/07-graphrag/viewer/)

E7 발견 정리(예측 대 실제, 2번 보완): [findings.md](findings.md)

## 폴더 구조

```
deep/07-graphrag/
├── README.md          이 파일
├── challenge.md       3주 챌린지 과제 정의
├── e1-decisions.md    E1 결정(범위와 분류 축)
├── ai-consulting/     1번 도메인 — AI 컨설팅
├── oil-trade/         2번 도메인 — 무역 & 기름
├── experiments/       E4·E5 방법, 지시문, 결과, 스크립트(scripts/)
├── shared/            두 도메인 공통 규칙(Codex 판정 규칙)
├── viewer/            E6 그래프 뷰어 (정적 HTML)
├── findings.md        E7 발견 정리
├── plan.md            이전 과제 계획
├── papers.md          이전 과제 계획
└── tools.md           이전 과제 계획
```

## 이전 과제 계획

[plan.md](plan.md), [papers.md](papers.md), [tools.md](tools.md)는 이전 과제의 계획(MBB 공개 리포트로 만드는 "산업 × 펌별 관점 비교" 그래프)이다. 3주 챌린지 계획이 아니며, 고치지 않고 그대로 둔다.
