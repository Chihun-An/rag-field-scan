# E5 사람 판정과 자동 판정 비교

2026-10-26. 사람 판정 40개([e5-human-judge.md](e5-human-judge.md))를 citation-judge([e5-judge-claude.json](e5-judge-claude.json))와 Codex([e5-codex-output.md](e5-codex-output.md))의 같은 단위 판정과 비교했다. 조건은 [e5-method.md](e5-method.md) 끝 "추가(2026-10-26, 사람 판정)"에 있다. 사람과 Codex의 "정보 부족"은 "뒷받침 안 됨"으로 보았다.

```bash
python3 deep/07-graphrag/experiments/scripts/compare-e5-human-judge.py
```

```
## 사람 판정 40개와 자동 판정 비교
읽은 번호: 40개
사람 "정보 부족": 4개 ("뒷받침 안 됨"으로 봄)
Codex "정보 부족": 14개 ("뒷받침 안 됨"으로 봄)
citation-judge "형식 오류": 0개

### 사람 대 citation-judge
일치: 27/40 (67.5%)

사람 \ citation-judge	뒷받침됨	뒷받침 안 됨	합계
뒷받침됨	21	8	29
뒷받침 안 됨	5	6	11
합계	26	14	40

### 사람 대 Codex
일치: 27/40 (67.5%)

사람 \ Codex	뒷받침됨	뒷받침 안 됨	합계
뒷받침됨	21	8	29
뒷받침 안 됨	5	6	11
합계	26	14	40

### 세 판정이 모두 같은 수: 23/40 (57.5%)

### 사람 원래 판정별 citation-judge 판정과 Codex 원래 판정
사람 원래 판정	개수	citation-judge 뒷받침됨	citation-judge 뒷받침 안 됨	Codex 뒷받침됨	Codex 뒷받침 안 됨	Codex 정보 부족
뒷받침됨	29	21	8	21	0	8
뒷받침 안 됨	7	5	2	5	0	2
정보 부족	4	0	4	0	0	4

### 도메인별 일치율
도메인	개수	사람 대 citation-judge	사람 대 Codex
1번	21	13/21 (61.9%)	15/21 (71.4%)
2번	19	14/19 (73.7%)	12/19 (63.2%)
```
