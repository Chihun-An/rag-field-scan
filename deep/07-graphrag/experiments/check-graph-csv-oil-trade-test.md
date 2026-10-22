# 2번 그래프 CSV 형식 검사 스크립트 시험 (E4)

[check-graph-csv-oil-trade.py](scripts/check-graph-csv-oil-trade.py)가 위반 규칙 9개와 경고 규칙 2개를 기대대로 잡는지 지어낸 시험 파일 세 개로 확인했다. 2026-10-22, Claude Code가 돌렸다. 에이전트 그래프 1회차 전이다.

- 시험 파일: [oil-trade-graph-csv-pass.csv](fixtures/oil-trade-graph-csv-pass.csv), [oil-trade-graph-csv-fail.csv](fixtures/oil-trade-graph-csv-fail.csv), [oil-trade-graph-csv-warn.csv](fixtures/oil-trade-graph-csv-warn.csv)
- 시험 파일에 쓴 문자열의 출처: ot-17.txt에서 글자가 있는 첫 줄 "■ 관세법 [별표] <개정 2022. 12. 31.>"(2번 골든 룰 시험 파일과 같은 줄), "테스트"·"테스트 용어"·"테스트 분류 값"·"테스트 요건"·"기타: 테스트" 같은 문자열, 스키마 목록 이름, 일부러 틀린 값(관계 "협력", 업무 단계 "통관", 원장 번호 18, 원문에 없는 테스트 문장 등)만 썼다. 원문에서 실제 분류·요건 값을 찾아 쓰지 않았다.
- 머리줄이 틀린 파일(머리줄 "주어,관계,값")은 저장소 밖 임시 폴더(Claude Code 스크래치 폴더)에 만들어 돌렸고 저장소에는 두지 않았다. 출력 "줄 1: header", 종료 코드 2
- 설치한 도구 없음(python 표준 라이브러리 csv, re, collections, pathlib만 씀)
- 처음 돌린 결과가 모두 기대와 같아 스크립트를 고친 일은 없다.

## 1. 실행과 출력

모두 저장소 맨 위에서 돌렸다.

### 통과 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-graph-csv-pass.csv
```

종료 코드: 0

```
관계별 줄 수: 원문 용어 1, 품목 분류 1, 요건 2
주어별 줄 수: UMO 0, ULO 1, PPO 1, 그 밖의 주어 2
줄 4개, 위반 0건, 경고 0건
```

### 위반 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-graph-csv-fail.csv
```

종료 코드: 1

```
줄 2: columns
줄 3: relation
줄 4: subject
줄 5: empty
줄 6: extra-field
줄 7: closed-list
줄 8: ledger
줄 9: not-in-raw
줄 10: duplicate
줄 11: duplicate
관계별 줄 수: 원문 용어 5, 품목 분류 2, 요건 1
주어별 줄 수: UMO 0, ULO 2, PPO 5, 그 밖의 주어 2
줄 10개, 위반 10건, 경고 0건
```

### 경고 시험

```bash
python3 deep/07-graphrag/experiments/scripts/check-graph-csv-oil-trade.py deep/07-graphrag/experiments/fixtures/oil-trade-graph-csv-warn.csv
```

종료 코드: 0

```
줄 2: 경고: multi-value
줄 3: 경고: stage-number
줄 4: 경고: stage-number
관계별 줄 수: 원문 용어 0, 품목 분류 0, 요건 3
주어별 줄 수: UMO 0, ULO 0, PPO 0, 그 밖의 주어 3
줄 3개, 위반 0건, 경고 3건
```

## 2. 판정 표

| 시험 파일 | 넣은 것 | 기대 | 스크립트 결과 | 사람 확인 |
|-----------|---------|------|---------------|-----------|
| pass | 원문 용어 1줄, 품목 분류 1줄(HS(관세율표·WCO)), 요건 1줄(허가·신고, 수출자), 요건 1줄(처리·재활용, 주체 "기타: 테스트"). 모두 원장 17번, 근거 문장은 ot-17.txt 머리줄 | 위반 0, 경고 0, 종료 코드 0 | 위반 0, 경고 0, 종료 코드 0 | 에드워드 확인 전 |
| fail | 줄 2 칸 3개 / 줄 3 관계 "협력" / 줄 4 원문 용어인데 주어 "테스트 분류 값" / 줄 5 위치 빈 칸 / 줄 6 원문 용어에 분류 체계 "기타: 테스트" / 줄 7 업무 단계 "통관" / 줄 8 원장 번호 18 / 줄 9 원문에 없는 근거 문장 / 줄 10·11 같은 줄 두 번 | 줄마다 columns, relation, subject, empty, extra-field, closed-list, ledger, not-in-raw, duplicate(10·11)만, 종료 코드 1 | 기대와 같음(위반 10건), 종료 코드 1 | 에드워드 확인 전 |
| warn | 주체 "수출자, 수입자" 1줄, 업무 단계 "3" 1줄, 업무 단계 "3. 허가·신고" 1줄 | 위반 0, 경고 3(multi-value 1, stage-number 2), 종료 코드 0 | 위반 0, 경고 3(줄 2 multi-value, 줄 3·4 stage-number), 종료 코드 0 | 에드워드 확인 전 |

## 3. 구현에서 정한 것

- 한 줄에 같은 규칙이 여러 번 걸려도(예: 빈 칸이 둘) 그 줄에는 규칙 이름을 한 번만 낸다
- subject는 주어 칸이 비어 있지 않을 때만 본다(비어 있으면 empty). ledger는 원장 번호 칸이 비어 있지 않을 때만 본다(비어 있으면 empty)
- extra-field는 지시 문구대로 관계가 스키마에 없는 줄에도 적용한다(그런 줄에서 분류 체계·업무 단계·주체가 채워져 있으면 relation과 함께 걸린다)
- 경고 모양(multi-value, stage-number)에 맞으면 closed-list로 세지 않는다. stage-number는 업무 단계 칸에만 본다
- "주어별 줄 수"의 "그 밖의 주어"에는 빈 주어도 들어간다. 칸이 9개가 아닌 줄은 관계별·주어별 줄 수에 넣지 않는다
