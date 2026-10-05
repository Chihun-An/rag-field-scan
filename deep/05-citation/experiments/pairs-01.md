# 층위 2 판정 쌍 (pairs-01)

> [미사용 기록] 이 파일의 영어 번역 쌍은 실제 판정에 쓰이지 않았다. 영어로 학습된 MiniCheck에
> 넣으려고 만들었으나 설치·용량·체크포인트 형식 문제로 경로를 바꿨다. 실제 판정에는 한국어 원문을
> 그대로 쓰는 pairs-01-ko.md를 썼고, 그래서 번역이 판정을 바꿀 위험이 없다. 이 파일은 시도한
> 경로의 기록으로 남긴다.

MiniCheck에 넣을 (문서, 주장) 쌍 목록. 층위 2는 인용한 조항의 내용이 답변 문장을 실제로 뒷받침하는지를 본다.

## 번역 원칙

- 문서(doc_en)는 data/sanan-law.md 원문을 사람이 영어로 옮긴 것이다.
- 주장(claim_en)은 results-01.md의 실제 답변 문장을 사람이 영어로 옮긴 것이다.
- 답변이 원문을 잘못 서술한 경우, 번역에서 고치지 않고 틀린 그대로 옮긴다. 고치면 판정 대상이 사라진다.
- MiniCheck는 영어 데이터로 학습된 모델이므로 한국어 원문을 그대로 넣지 않고 번역 쌍을 쓴다. 번역이 판정을 바꿀 수 있다는 점은 한계로 기록한다.
- P8은 에이전트 출력이 아니라 사람이 판정기 교정용으로 쓴 문장이다. 에이전트 오류로 기록하지 않는다.

## P1

doc_id: 제42조 제2항
doc_en: An employer who intends to commence a construction project under subparagraph 3 of paragraph (1) shall, when preparing the hazard prevention plan, hear the opinion of a person holding a qualification prescribed by Ordinance of the Ministry of Employment and Labor, such as a qualification in the field of construction safety.
claim_id: Q5-A
claim_en: Paragraph (2) of Article 42 provides for the preparation, submission and review of the hazard prevention plan.
human: 뒷받침 안 됨
hypothesis: 사람 판정과 같으면 자동 판정이 내용 오류를 잡아낸 것이다.

## P2

doc_id: 제42조 제1항+제2항
doc_en: (1) Where an employer falls under any of the following cases, the employer shall prepare a plan stating the matters concerning the prevention of hazards and dangers prescribed by this Act or by any order issued under this Act (hereinafter referred to as the "hazard prevention plan"), submit it to the Minister of Employment and Labor as prescribed by Ordinance of the Ministry of Employment and Labor, and undergo a review. (2) An employer who intends to commence a construction project under subparagraph 3 of paragraph (1) shall, when preparing the hazard prevention plan, hear the opinion of a person holding a qualification prescribed by Ordinance of the Ministry of Employment and Labor, such as a qualification in the field of construction safety.
claim_id: Q5-A
claim_en: Paragraph (2) of Article 42 provides for the preparation, submission and review of the hazard prevention plan.
human: 뒷받침 안 됨
hypothesis: 같은 조의 제1항에 "작성·제출·심사"가 있으므로, 조 전체를 주면 판정기가 항을 구분하지 못하고 뒷받침됨으로 볼 수 있다. P1과 결과가 갈리는지가 핵심이다.

## P3

doc_id: 제42조 제1항+제2항
doc_en: (same as P2)
claim_id: Q5-B
claim_en: This document does not state the amount of any administrative fine for failure to submit the hazard prevention plan.
human: 맞음
hypothesis: "문서에 없음"이라는 부정 주장은 문서가 뒷받침할 대상이 아니다. 판정기가 뒷받침 안 됨으로 내도 그것이 답변이 틀렸다는 뜻은 아니다.

## P4

doc_id: 제36조 제6항
doc_en: The methods, procedures and timing of risk assessment and other necessary matters shall be prescribed by Ordinance of the Ministry of Employment and Labor.
claim_id: Q1
claim_en: The methods, procedures and timing of risk assessment and other necessary matters are prescribed by Ordinance of the Ministry of Employment and Labor.
human: 맞음
hypothesis: 뒷받침됨으로 나와야 한다.

## P5

doc_id: 제40조
doc_en: Workers shall observe the measures prescribed by Ordinance of the Ministry of Employment and Labor among the measures taken by the employer pursuant to Articles 38 and 39.
claim_id: Q3
claim_en: Workers shall observe the measures prescribed by Ordinance of the Ministry of Employment and Labor among the measures taken by the employer pursuant to Articles 38 and 39.
human: 맞음
hypothesis: 문서와 주장이 거의 같다. 뒷받침됨으로 나오지 않으면 판정기나 설정에 문제가 있다는 신호다.

## P6

doc_id: 제2조 제3호
doc_en: The term "worker" means a worker as defined in subparagraph 1 of Article 2 (1) of the Labor Standards Act.
claim_id: Q4
claim_en: Under this Act, "worker" means a worker under subparagraph 1 of Article 2 (1) of the Labor Standards Act.
human: 맞음
hypothesis: 뒷받침됨으로 나와야 한다. 다른 법률을 가리키기만 한다는 점은 판정 대상이 아니다.

## P7

doc_id: 제15조 제1항 제1호
doc_en: Matters concerning the formulation of plans for the prevention of industrial accidents at the workplace.
claim_id: Q2
claim_en: The safety and health manager shall manage, in an integrated manner, matters concerning the formulation of plans for the prevention of industrial accidents at the workplace.
human: 맞음
hypothesis: 의무를 지우는 문구("총괄하여 관리한다")는 제15조 제1항 본문에 있고 제1호에는 없다. 호만 떼어 주면 주장의 일부만 뒷받침된다. 청크 경계가 근거를 끊는 경우에 해당한다.

## P8

doc_id: 제42조 제1항+제2항
doc_en: (same as P2)
claim_id: 통제군
claim_en: An employer shall submit the hazard prevention plan within 30 days from the commencement of construction.
human: 뒷받침 안 됨
hypothesis: 사람이 실험용으로 쓴 거짓 주장이다. 판정기가 이것도 뒷받침됨으로 내면, 판정값 전체를 신뢰할 수 없다는 뜻이다.
