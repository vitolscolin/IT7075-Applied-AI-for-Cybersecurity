# Alert triage with LangGraph

This project extends my earlier incident-triage coursework into a deterministic LangGraph workflow. It classifies 12 synthetic labelled alerts, measures missed incidents and unnecessary escalations separately, and compares keyword tuning with a context-review node that calls a simulated read-only asset/change lookup. It includes saved notebook outputs, actual node traces, thread-memory evidence, and a report. No model, API key, GPU, or network service is used during the project run.

## Run it

From the repository root with Python 3.12:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r langgraph_project/requirements.txt
python -m ipykernel install --user --name it7075-langgraph --display-name "Python (IT7075 LangGraph)"
python langgraph_project/run_notebook.py
```

On Windows, create the environment with `py -3.12 -m venv .venv` and activate with `.venv\Scripts\Activate.ps1`. Initial package installation needs internet; project execution is offline. `requirements-lock.txt` records the exact tested environment.

For a live notebook run, open `agent_notebook.ipynb`, select the environment above, and **Restart Kernel and Run All**. The working directory can be the project folder or repository root. The runner selects its own Python interpreter and saves the notebook only after success. It disables dotenv loading, hosted-model keys, and tracing in its child kernels. To repeat the two lectures as well:

```bash
python langgraph_project/run_notebook.py --lectures
```

The lecture URL verdict is a no-key stub, not a validated malicious-URL classifier. The project itself executes its full intended deterministic logic. Original assignment starters remain untouched.

## Experiments

| Setting | Change | Caught /6 | Missed /6 | Over-escalated /6 |
|---|---|---:|---:|---:|
| K0 | Lecture keywords | 3 | 3 | 2 |
| K1 | K0 + credential | 4 | 2 | 2 |
| K2 | K1 + outbound | 5 | 1 | 3 |
| K3 | K2 + failed | 5 | 1 | 4 |
| K4 | K3 + password | 5 | 1 | 5 |
| G1 | K2 + context-review node/tool | 6 | 0 | 1 |

G1 is compared with K2, not K4. Its two context policies are a single combined graph intervention. A06 has no tested keywords and stays missed by all keyword variants. A07/A08 stay false alarms until the graph verifies simulated change context. G1 still escalates A09's routine backup transfer. These are development-set results on authored examples, not production performance or held-out validation.

## Files and evidence

- `agent_notebook.ipynb`: completed practice, custom graph, experiments, traces, memory, checks, interpretation.
- `my_alerts.json`: six escalate/six close scenarios and individual label rationales. Labels/notes are withheld from graph inputs.
- `context_fixture.json`: simulated asset and change records with no alert IDs or labels.
- `results_mine.csv`, `evaluation_details.json`: summary and per-alert measurements.
- `results_practice.csv`: separate instructor-data practice results.
- `traces.json`, `graph.mmd`, `memory_evidence.json`: real execution paths and thread continuity/isolation.
- `validation.json`, `run_environment.json`: boundary checks, versions, and input hashes.
- `SOURCES.md`: references and scenario provenance.
- `report/Alert_Triage_Agent_Report.pdf`, `report/report.md`: report and editable text.
- `VIDEO_WALKTHROUGH.md`: 5-10 minute live demonstration outline.

## Submission status

The report's video link remains pending until a new recording is supplied. An older project's video is not evidence for this project. After recording, rebuild the report with:

```bash
python langgraph_project/build_report.py --video-url "https://your-recording-link"
```

The assignment requires a private repository and instructor/TA access. The repository was observed public during preparation; visibility was not changed and collaborator access was not verified. Resolve those requirements before submitting the PDF. The synthetic alert labels and first-person report should be reviewed before narration; the work was prepared with AI assistance.
