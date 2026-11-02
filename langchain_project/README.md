# Incident-triage RAG with LangChain

This project rebuilds the earlier `rag_project` incident-triage retriever using LangChain loaders, a text splitter, local MiniLM embeddings, Chroma, a threshold retriever, and an LCEL prompt/model/parser chain. It reuses the exact same five documents and eight questions, compares one-setting-at-a-time experiments, and inspects a retrieval failure. The default answer stage quotes retrieved context in offline mode; it does not call a generative model.

## Setup and live execution

From the repository root, using Python 3.12:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r langchain_project/requirements.txt
python -m ipykernel install --user --name it7075-langchain --display-name "Python (IT7075 LangChain)"
```

Windows PowerShell: use `py -3.12 -m venv .venv` and `.\.venv\Scripts\Activate.ps1` instead of the first two commands. The remaining `python` commands are the same.

Open `langchain_project/langchain_notebook.ipynb` in VS Code/Jupyter, select **Python (IT7075 LangChain)**, and choose **Restart Kernel and Run All**. Run from the repository root or the notebook folder. Initial dependency installation and the first MiniLM download require internet; cached-model execution needs no API key, GPU, or network. To download the model before recording:

```bash
python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2', device='cpu')"
```

For a terminal execution with saved outputs (also works in PowerShell):

```bash
python langchain_project/run_notebook.py
```

This runs the actual notebook top to bottom and saves it only after successful execution. It does not synthesize outputs. The notebook independently checks data identity, reruns the earlier manual experiments, validates score conversion, and checks retrieval parity on identical chunks. Run it twice if demonstrating rerun isolation: each vector store uses a unique collection name.

## Recording proof

Use `VIDEO_WALKTHROUGH.md` for a 5–10 minute live-screen outline. During recording, restart the kernel and run all cells, then show the generated transcript, results, and assertions. Saved outputs alone are not proof of a live run. The two lecture notebooks in `05_LangChain/code/` were also run through their no-key practice paths; those paths preview model calls rather than executing them. The completed project notebook executes the actual local retrieval and chain.

## Results and comparison

- `results_langchain.csv`: eight custom configurations. Labels retain the earlier manual distance labels; `score_threshold` explicitly gives the LangChain relevance cutoff.
- `results_manual_rerun.csv`: current rerun of the original notebook's functions.
- `comparison.csv`: manual and LangChain measurements side by side.
- `results_practice.csv`: separate course-knowledge-base sweep, not the custom experiment.
- `evaluation_details.json`, `error_analysis.json`, `transcript.txt`: per-question evidence and the Q3 ranking failure.
- `data_manifest.json`: SHA-256 hashes of unchanged inputs, checked against `../rag_project` every run.
- `run_environment.json`: package versions from the executed kernel.

Custom retrieval uses normalized embeddings and cosine distance. For positive thresholds, `relevance = max(0, min(1, 1 - distance))`; the earlier `max_distance=0.50` corresponds to `score_threshold=0.50`, while distance 0.35 corresponds to score 0.65. Practice retains the starter's L2 metric, so do not use practice scores as cosine scores. LangChain fixed-character splitting can omit redundant final overlapping tails; the notebook reports this and validates both matched settings and identical-chunk retrieval.

“Found” means a gold evidence phrase appeared within a retrieved chunk. “Refused” means zero chunks for an unanswerable question. Neither is a generative-answer quality metric, and eight authored questions do not establish production accuracy.

## Report and remaining submission steps

The report is in `report/LangChain_RAG_Report.pdf`; its first-page **Video URL** field is editable in a PDF form reader. Paste your uploaded recording link there and save a copy. `report/report.md` is editable source text as well.

1. Record and upload your own 5–10 minute narrated live run, then complete the report's video field.
2. Submit the completed PDF and confirm the instructor can open both links.

The original assignment starters are unchanged. All implementation lives in this student project folder; the previous RAG project is preserved.
