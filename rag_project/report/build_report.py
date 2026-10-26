from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from pathlib import Path
import csv,json
from xml.sax.saxutils import escape
root=Path.cwd()/ 'rag_project'
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Body',fontName='Helvetica',fontSize=10.5,leading=15,spaceAfter=9))
styles.add(ParagraphStyle(name='SmallBody',fontName='Helvetica',fontSize=9,leading=12,spaceAfter=6))
for name in ['Title','Heading1','Heading2']: styles[name].textColor=colors.black
story=[]
source=[]
def p(t,style='Body'):
 story.append(Paragraph(t,styles[style]));source.append(t)
def h(t): p(t,'Heading1')
def page(): story.append(PageBreak());source.append('\n---\n')
def table(data,widths):
 t=Table([[Paragraph(escape(str(v)),styles['SmallBody']) for v in row] for row in data],colWidths=widths,repeatRows=1)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e2eaf2')),('GRID',(0,0),(-1,-1),.5,colors.HexColor('#d9d9d9')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5)]))
 story.append(t);story.append(Spacer(1,10));source.extend(' | '.join(map(str,row)) for row in data)
p('Incident Triage RAG Project Report','Title')
p('Colin Vitols | IT7075 Applied AI for Cybersecurity<br/>University of Cincinnati | October 26, 2026')
url='https://github.com/vitolscolin/IT7075-Applied-AI-for-Cybersecurity/tree/rag-project/rag_project'
p(f'<b>Project folder:</b> <link href="{url}" color="#17578a">GitHub incident triage RAG project</link><br/><font size="8">{url}</font>')
p('<b>Video:</b> <link href="https://youtu.be/xpWqbe0acow?si=Svsk99xHfkICu-Jh" color="#17578a">https://youtu.be/xpWqbe0acow?si=Svsk99xHfkICu-Jh</link>')
h('Project overview')
p('For this project, I built an offline RAG system around five documents on cybersecurity incident triage. I wanted it to find useful evidence for common analyst questions and recognize when the documents did not have an answer. With the default settings, it found the expected evidence for all six answerable questions and refused the other two. That is a good result for this small test, but eight questions are not enough to show that it would handle incident-response questions reliably in general.')
h('How the system works')
p('<b>Prepare and index.</b> I start by breaking the documents into smaller, overlapping pieces. The split_into_chunks function is in Part 1. Part 6 loads my documents and test questions, then checks that each expected evidence phrase actually appears in its source. In Part 7, I use 500-character chunks with 80 characters of overlap. This turns the 10,209 characters of source text into 26 chunks. The overlap helps keep useful information together when it falls near the edge of a chunk.')
p('Chunk size involves a tradeoff. If the chunks are too small, they can lose context or cut a useful phrase in half. If they are too large, several topics end up represented by one vector, which can make the search less precise. My chunker counts characters rather than following sentence boundaries, so some chunks begin or end in the middle of a sentence. This shows up in the saved responses.')
p('<b>Embed.</b> Part 1 loads all-MiniLM-L6-v2 on the CPU. An embedding turns text into a list of numbers that represents patterns in its meaning. Related pieces of text tend to have similar vectors, which lets the system search by meaning instead of requiring the question to use the exact words in the document. A close match is still only a clue, though. It does not guarantee that the text contains the answer.')
p('<b>Store.</b> In Part 2, build_collection puts each chunk into Chroma along with its normalized embedding, an ID, and the source filename. The collection stays in memory and is rebuilt when the notebook runs. I use cosine distance to compare vectors. A smaller distance means a closer match.')
page()
h('From a question to a response')
p('<b>Retrieve.</b> The retrieve function in Part 3 embeds the question with the same model used for the documents. Chroma then returns the nearest chunks, their distances, and their source information. My default settings request up to three chunks and keep only those with a distance of 0.50 or less. If none are close enough, the system has no context to use for an answer.')
p('<b>Augment.</b> In Part 4, build_context and ask arrange the retrieved chunks into numbered blocks with source filenames. Those blocks go into a prompt that tells the assistant to answer from the supplied text, cite its sources, and say when it does not have enough information.')
p('<b>Generate or refuse.</b> My notebook uses an offline fallback in grounded_answer, also in Part 4. It shows up to 360 characters from the first retrieved chunk and names the source. If no chunks pass the cutoff, it returns a refusal. The notebook builds the prompt, but it does not send it to a language model. This means I am testing retrieval and an evidence-based response, not how well an LLM writes an answer or follows instructions.')
p('Part 5 scores the practice pipeline, which produces the required 22 chunks, 6/6 evidence matches, and 2/2 refusals. Part 7 prints custom transcripts for Q1, Q3, Q6, Q7, and Q8. For example, Q1 retrieves the instruction to preserve failed and successful sign-ins as one timeline. Q8 returns no retained chunks and responds, “I don\'t know; the knowledge base does not contain relevant evidence.”')
h('Documents and question design')
p('I organized the knowledge base into five files: account_triage.md, endpoint_triage.md, email_triage.md, network_triage.md, and evidence_and_escalation.md. They cover account activity, process evidence, suspicious email, network correlation, and evidence handling. SOURCES.md records that these are original project procedures using made-up examples, not records from real incidents.')
p('I stored the eight test questions in goldset.json. For each answerable question, I included a short phrase copied exactly from the relevant document. Part 6 checks those phrases before the system is scored. I leave SOURCES.md out of the index because it describes where the documents came from rather than providing triage guidance.')
p('I used two different kinds of unanswerable questions. Q7 asks about watering tomato seedlings, which is clearly outside the topic. Q8 asks for the exact SIEM retention period required by the triage program. I chose that question because the documents mention retention rules but never give a specific period. The system needs to recognize that related wording is not enough to answer it. That makes Q8 a more useful challenge than a question that is obviously unrelated.')
page()
h('The eight evaluation questions')
gold=json.load(open(root/'goldset.json'))['questions']
for q in gold:
 p(f'<b>{q["qid"]}.</b> {escape(q["question"])}')
 if q['answerable']: p(f'<b>Expected evidence:</b> {escape(q["evidence"][0])}<br/><b>Source:</b> {q["source"]}','SmallBody')
 else: p('<b>Expected outcome:</b> Refuse because the documents do not answer this question.','SmallBody')
h('What the scores measure')
p('The found count tells me whether any retrieved chunk contains the expected evidence phrase, ignoring capitalization. The refused count tells me how many unanswerable questions returned no chunks. These checks do not tell me whether the displayed response is complete. The balanced_score column in results.csv adds the answer rate and refusal rate, giving each equal weight and producing a score from 0 to 2.')
page()
h('Experiment results')
p('In Part 8, I compare settings by changing one at a time and keeping overlap at 80 characters throughout. Part 9 creates the chart, while results.csv stores the scores and the IDs of missed questions. The table and chart below come from the full notebook run on October 26, 2026.')
rows=list(csv.DictReader(open(root/'results.csv')))
data=[['Configuration','Size','k','Cutoff','Chunks','Found','Refused']]
for r in rows:data.append([r['label'],r['chunk_size'],r['k'],r['max_distance'],r['chunks'],r['found']+'/6',r['refused']+'/2'])
table(data,[133,48,30,49,52,65,67])
im=Image(str(root/'figure.png')); im.drawHeight=im.imageHeight*480/im.imageWidth;im.drawWidth=480;story.append(im)
p('Figure 1. Evidence retrieval and refusal rates for each configuration.','SmallBody')
p('The distance cutoff made the biggest difference. Lowering it to 0.35 kept both refusals but found evidence for only 2/6 answerable questions. Raising it to 0.65 or 0.80 found all six, but the system stopped refusing Q8. It retrieved related triage text even though that text did not give the requested retention period. Getting more matches was not helpful when one of those matches should have been a refusal.')
p('Based on these results, I would keep 500-character chunks, 80-character overlap, k=3, and a cutoff of 0.50. The 350-character chunks found 5/6 answers, and the 700-character chunks found 4/6. Using k=1 missed Q3, while k=5 gave the same scores as the default. I would stay with k=3 because retrieving more chunks did not improve the results here. I would test these settings again if I added more documents or different questions.')
page()
h('A retrieval mistake')
p('In Part 10, I looked more closely at Q3: “What should an analyst preserve from a suspected phishing email?” With k=1, the system chose the first chunk from email_triage.md, with a cosine distance of about 0.404. It starts with “Suspicious Email Triage” and “Preserve the message.” It also says to preserve the original message or an approved export so headers, attachment hashes, URLs, and routing details remain available.')
p('The selected chunk is relevant, but it does not contain the exact phrase used for scoring: “preserve the original message with full headers and attachment hashes.” That phrase is in the second-ranked chunk, at a distance of about 0.407. With k=1, the system never gets that second chunk, so Q3 counts as a miss. With the default k=3, both chunks pass the 0.50 cutoff and the evidence check succeeds.')
p('What stood out to me is how close the two distances are. The model puts a useful introductory passage just ahead of the passage with the exact evidence. The first chunk also gives much of the right information in different words, so I would not call the response completely wrong. It fails the exact-phrase check. There is another limitation here: the offline response only displays the first chunk. Finding the gold phrase in a later chunk improves the retrieval score, but does not mean that phrase appears in the response the user sees.')
p('Q1 shows a different problem. Its correct account-triage chunk has a distance of about 0.410, so the stricter 0.35 cutoff removes it. The system then refuses a question that the documents can answer. Part 10 prints that chunk and the next two matches, making it clear that the evidence was available but filtered out.')
h('Limits and next steps')
p('The main limitation is the size of the test. With only six answerable questions, one missed question changes the answer rate by about 16.7 percentage points. With only two refusal questions, one mistake changes that rate by 50 points. I also used the same questions to compare settings, and the questions were designed around these documents. A perfect score here does not tell me how well the system will handle new questions.')
p('I have not tested reworded or ambiguous questions, conflicting procedures, larger document collections, prompt injection, or real incidents. The exact-phrase check can miss a valid answer that uses different wording, and chunk boundaries can split a phrase. It can also count a question as successful when the evidence is retrieved but left out of the displayed response. The distance cutoff helps reject weak matches, but Q8 shows that related text can still pass without answering the question.')
p('Next, I would add questions that were not used to choose the settings, including reworded questions and more questions that sound relevant but cannot be answered from the files. I would also try splitting text at sentence boundaries and score the completeness of the displayed responses separately. If I connect an LLM, I would need to check its answers for factual support, citations, and appropriate refusals. For now, this project shows how a small offline retrieval pipeline works and where it can make mistakes.')
p('<b>Project evidence:</b> rag_notebook.ipynb Parts 1-10; goldset.json; results.csv; figure.png; my_kb/SOURCES.md and the five procedure files.','SmallBody')
def footer(c,d):
 c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#555555'));c.drawRightString(558,30,f'{d.page}')
SimpleDocTemplate(str(root/'report/Incident_Triage_RAG_Report.pdf'),pagesize=(612,792),rightMargin=54,leftMargin=54,topMargin=45,bottomMargin=45,title='Incident Triage RAG Project Report',author='Colin Vitols').build(story,onFirstPage=footer,onLaterPages=footer)
(root/'report/Report_Text.txt').write_text('\n\n'.join(source))
