# E5 답 보고 (oil-trade, search)

2026-10-22, ~/Documents/rag-e5-oil-trade-search에서 새 Claude Code 대화로 만든 답의 마지막 보고를 에드워드가 옮겼다. 보고 앞의 진행 메시지를 빼고, 결과 파일 링크를 글자로 바꾸고, 임시 폴더 전체 경로를 줄인 것 말고는 고치지 않았다. 답 파일은 [oil-trade/e5-answers-search.json](../oil-trade/e5-answers-search.json)다.

I've answered all 15 questions and saved them as answers.json in the shape set by answer-shape.md, in UTF-8. Every evidence sentence (근거 문장) was matched word-for-word against its file in raw/. The 17 raw files still match their hashes in sources.csv, and I didn't edit schema.md, answer-shape.md, questions.md or sources.csv. I opened nothing outside the folder and didn't use the internet.

**Model:** Claude Opus 5.5 (`claude-opus-5-5`)

**Status and claim count (상태 · 주장 수) per question**

| 질문 | 상태 | 주장 수 |
|---|---|---|
| Q1 | 답함 | 2 |
| Q2 | 답함 | 4 |
| Q3 | 답함 | 29 |
| Q4 | 답함 | 15 |
| Q5 | 답함 | 98 |
| Q6 | 답함 | 17 |
| Q7 | 답함 | 42 |
| Q8 | 답함 | 23 |
| Q9 | 답함 | 8 |
| Q10 | 답함 | 12 |
| T1 | 자료에 없음 | 0 |
| T2 | 전제가 틀림 | 2 |
| T3 | 자료에 없음 | 0 |
| T4 | 전제가 틀림 | 0 |
| T5 | 전제가 틀림 | 3 |

**How much of each file I read**
- **Read in full:** 03, 04, 06, 07, 09, 12, 16
- **Read in part:**
  - 01: Annex I, VIII and IX entries, plus Articles 4, 6 and 8
  - 02: Introduction, the used-oil definition, Table 21
  - 05: articles 1–25; the appendices (별표) appear only as file links, not their contents
  - 10: keyword search only
  - 11: the waste-oil (06) section
  - 13: the waste-oil table
  - 14: R-3-3, R-4-6, R-9-2, R-9-3
  - 15: Article 18 on lubricating oil
  - 17: Chapter 27 notes and heading 2710
  - 08: definitions only
- **Not opened:** none (every file was at least keyword-searched)

**Judgment calls**
- **Q6, Q7, Q8, Q10 (linking UMO/ULO to Basel and to 수출입규제폐기물):** No source sentence says this directly. I joined 원장 11번's "06-01 폐광물유 > 06-01-01 폐윤활유" with 원장 6번's A3020 "폐광물 유류", using the two-evidence pattern answer-shape.md allows. This is the main uncertain link in the answers.
- **UMO wording:** "엔진오일" doesn't appear anywhere. I linked UMO through "내연기관용 윤활유" (원장 11번), and "engine lubricating oil" / "used motor oil" (원장 2번).
- **Q6, Q9, PPO:** No classification system gives PPO a product classification. The pyrolysis oil only appears as the subject of recycling standards, so PPO counts as 0 systems and its export requirements can't be found.
- **Q3, Q5, stage rule:** Following the schema's "use the stage of the listed article" rule, 법 제6조③ and 제10조③④ went into 허가·신고 even though they are about consent. I counted requirements once per actor (주체). Basel only covers Articles 6 and 8, and 원장 14번 only covers oil-related items. Under that rule the counts are: 허가·신고 has the most (29); 수출입자 자격·보증 has the fewest of the non-zero stages (5); 품목 확인·분류 has 0.
- **Q8, foreign governments:** Only the Basel Convention (원장 1번) places duties on 상대국·경유국 정부; the Korean act and decree have none.
- **T4:** I marked it 전제가 틀림 because the schema says it left 통관 out as a stage. The other possible status would have been 자료에 없음.
