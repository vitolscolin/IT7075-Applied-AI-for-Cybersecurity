# Live notebook recording guide

Record 5–10 minutes with your own narration and live screens. These notes explain what to show; adapt the phrasing so you can explain the code yourself.

## Before recording

1. Follow README setup, select the kernel, and do one full rehearsal run. Download the embedding model beforehand so setup does not consume recording time.
2. Open the completed notebook and the earlier `rag_project/rag_notebook.ipynb` side by side. Have the results CSV ready. Increase editor/output text to a readable size.
3. Start screen recording with microphone audio. Keep the notebook and kernel activity visible. Do not substitute screenshots of old outputs.

## 0:00–0:45 — Purpose and live start

Show the branch and project folder. Explain that this is the same five incident-triage documents and eight questions used in the manual RAG lab. Choose **Restart Kernel and Run All** on `langchain_notebook.ipynb` while recording. Show the running indicator and fresh execution counts. If the run takes longer, explain the stages while it finishes; avoid pretending a saved output is a new run.

## 0:45–2:15 — The five practice stages

- Show `TextLoader` and `split_documents`: files become Documents with text and metadata. This replaces the manual file-loading and chunking functions.
- Show `HuggingFaceEmbeddings` and `Chroma.from_documents`: the local model produces vectors, and LangChain stores vectors, text, and metadata. This replaces `embed` and `build_collection`.
- Show `as_retriever`: `k` limits candidates and `score_threshold` rejects low-relevance matches. Higher scores are better; lower distances were better in the earlier lab.
- Show `ChatPromptTemplate`: the question and retrieved context fill named placeholders.
- Trace the LCEL dictionary and pipes left to right. The question goes both to retrieval and straight into the prompt; the offline model quotes evidence, and the parser returns text. Explain clearly that this is an offline excerpt stand-in, not a live LLM.

## 2:15–3:30 — Your data and one answer plus one refusal

Show the data-integrity assertion and the five custom Documents. Scroll to the freshly executed transcript. Explain Q1's retrieved account-triage evidence, then Q7's watering-schedule refusal. Show that Q7 retrieved no evidence. All eight questions run in the transcript cell.

For an additional live interaction, add a temporary cell and execute:

```python
print(my_chain.invoke(MY_GOLD[0]["question"]))
print(my_chain.invoke(MY_GOLD[6]["question"]))
```

Do not change the gold questions or knowledge base for this comparison.

## 3:30–5:00 — Results and fair comparison

Show the freshly generated results table and comparison. Explain the default 500-character chunks, 80-character overlap, k=3, and 0.50 relevance cutoff. Show a one-setting change, such as k=1 or threshold 0.65. The threshold labels in the CSV preserve the old distance labels; use the explicit score column when discussing LangChain.

Explain the equation `score = 1 - cosine distance` (negative scores clipped to zero). Distance 0.35 is stricter than 0.50, so its corresponding score is 0.65. Show that the earlier manual runs reproduce, and that both retrievers agree when given identical chunks. Explain any chunk-count difference shown by the tail check rather than attributing it to the embedding model.

## 5:00–6:30 — An actual failure

Show Part 9's Q3 rank-by-rank inspection. Read the question about preserving a suspected phishing email. Point to the top-ranked passage and whether it contains the required phrase, then the lower-ranked passage with the evidence. Explain why k=1 can retrieve a related passage yet miss the required action. The default can find the evidence because it allows more chunks.

Also show Q8 at a loose threshold if time permits: similarity to incident-policy text does not prove that the corpus specifies an exact SIEM retention period.

## 6:30–7:30 — Judgment and limits

Explain which manual functions disappeared and what remains visible through metadata, raw scores, and diagnostics. State when you would use LangChain and when the manual implementation is easier to debug. Explain that found/refused evaluates retrieval, not the quality of an LLM-generated answer, and that eight questions are a small smoke test.

End by showing the successful final validation output and saving the notebook. Upload the recording, check its sharing permissions, paste the URL into the report's first-page video field, and save the completed PDF.

## Optional lecture practice proof

If asked to show both lecture notebooks, open `05_LangChain/code/langchain_basics.ipynb` and `langchain_rag.ipynb` and run their cells with no API key. These guarded lecture paths demonstrate templates and preview calls; they do not run the full retrieval chain without a key. The completed project notebook above provides the real local execution proof.
