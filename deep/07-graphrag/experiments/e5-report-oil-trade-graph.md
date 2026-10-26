# E5 답 보고 (oil-trade, graph)

2026-10-22, ~/Documents/rag-e5-oil-trade-graph에서 새 Claude Code 대화로 만든 답의 마지막 보고를 에드워드가 옮겼다. 보고 앞의 진행 메시지를 빼고, 결과 파일 링크를 글자로 바꾸고, 임시 폴더 전체 경로를 줄인 것 말고는 고치지 않았다. 답 파일은 [oil-trade/e5-answers-graph.json](../oil-trade/e5-answers-graph.json)다.

I've saved all 15 answers to answers.json in the answer-shape.md format, UTF-8. A script confirmed that every one of the 176 evidence quotes appears word for word in its source file.

**Model used:** Claude Opus 5.5 (claude-opus-5-5)

**Status, claim count and sources per question**

| 질문 | 상태 | 주장 수 | 쓴 자료 |
|---|---|---|---|
| Q1 | 답함 | 2 | 원문만 |
| Q2 | 답함 | 4 | 그래프+원문 |
| Q3 | 답함 | 48 | 원문만 |
| Q4 | 답함 | 24 | 그래프+원문 |
| Q5 | 답함 | 0 | 그래프+원문 |
| Q6 | 답함 | 20 | 그래프+원문 |
| Q7 | 답함 | 57 | 그래프+원문 |
| Q8 | 답함 | 34 | 그래프+원문 |
| Q9 | 답함 | 8 | 그래프+원문 |
| Q10 | 답함 | 14 | 그래프+원문 |
| T1 | 자료에 없음 | 0 | 원문만 |
| T2 | 전제가 틀림 | 2 | 원문만 |
| T3 | 자료에 없음 | 0 | 원문만 |
| T4 | 전제가 틀림 | 0 | 그래프만 (actually only schema.md; none of the three labels fits) |
| T5 | 답함 | 3 | 원문만 |

graph.csv has no requirement rows from the law (ot-04) or decree (ot-05). It only has terms, classifications and recycling standards, so most requirements came from reading the originals.

**Files**
- **Read in full:** 03, 04, 05, 06, 07, 09, 16. For 05, the addenda and annex/form titles were only skimmed.
- **Read in part:** 01 (Articles 4–9, Annex I Y8, Annex VIII A3020), 02 (paras 1–12), 11 (the 06 waste-oil section), 13 (a few lines by search), 17 (chapter 27 notes and the 2710 lines).
- **Not opened:** 08, 10, 12, 14, 15. The quote-check script did load every raw file to match graph quotes (some come from 14), but I didn't read these myself.

**Hard calls**
- **Q6–Q10, linking classifications (the biggest caveat):** No source says in one place that waste lubricating oil is Basel A3020/Y8 or a regulated export/import waste. None says UMO is HS 2710 either. I linked them with two pieces of evidence each:
  - ot-11's "06-01 폐광물유" matches ot-06/ot-01's "waste mineral oils unfit for their originally intended use".
  - ot-11's "06 폐유" matches the "폐유(廢油)" in the HS note.

  Without these links, the Q6 counts become UMO 1 and ULO 2 (instead of 4 and 4). The basis for Q7 and Q8 would then disappear.
- **Q3, Q7, stage rule:** The schema rule puts law Article 6③ (importing and transit country consent) and Article 10③④ under "허가·신고", not "상대국·경유국 동의".
- **Basel stage:** The schema table lists the whole Basel Convention under stage 4. I classified Basel requirements by what they do instead.
- **Q5 counts:** The result depends on which requirements are counted. I included discretionary provisions ("할 수 있다"), counted a provision once per actor, and left out Article 5 general duties and Article 22 onward. That gives 135 requirements: most in 허가·신고 (48), fewest non-zero in 수출입자 자격·보증 (6). There are no claims because the counts have no evidence sentence.
- **Q4 coverage:** I only read Basel Articles 4–9, so "모두" may be missing disposer duties elsewhere in the Convention.
- **Two versions of articles:** Article 18조의2 and others have a current text and one effective 2027-03-16. I used the current text.
- **T5 status:** I marked it 답함 because the question asks for a judgment. The statement is wrong in one place: 24 months should be "12개월의 범위".
- **T4 status:** I weighed 전제가 틀림 against 자료에 없음 and chose 전제가 틀림, because the schema has no "통관" stage at all.
