# RAG submission review

Reviewed against MiniProject_RAG.pdf on October 26, 2026.

- Executed all ten code cells top to bottom with saved outputs and no execution errors.
- Practice checks pass: 22 chunks, 6/6 evidence matches, 2/2 refusals.
- Custom corpus: five documents, 10,209 characters, source declarations present.
- Gold set: six answerable questions with exact source evidence and two unanswerable questions.
- Corrected chunk-size experiments to keep overlap fixed at 80 characters. The 350-character result is now 5/6, with 2/2 refusals.
- Default: 26 chunks, 6/6 evidence matches, 2/2 refusals.
- Added full Q3 rank comparison to Part 10 for concrete error analysis.
- Regenerated results.csv and figure.png.
- Report: five pages; all rendered pages visually inspected.

## Remaining submission work

The supplied video link is included on report page one: https://youtu.be/xpWqbe0acow?si=Svsk99xHfkICu-Jh. The video content was not reviewed.
1. At the review time, the GitHub repository was public. The assignment requires private visibility until grading.
2. At the review time, the GitHub collaborator listing returned only vitolscolin. Add the instructor and TA using their correct GitHub accounts.
Repository visibility and collaborator access were not changed during this review.

## Interpretation boundary

The response function returns a first-chunk excerpt or refusal; no language model consumes the assembled prompt. Scores evaluate evidence anywhere in retained chunks, not complete generated answers. Q3 with k=1 is an exact-phrase miss despite a semantically relevant first chunk. The report explains these limitations.

## Rebuild the PDF

From the repository root, run `python3 rag_project/report/build_report.py` in an environment with ReportLab installed. The builder reads the current CSV, gold set, and chart. Render and inspect the PDF again after changes.
