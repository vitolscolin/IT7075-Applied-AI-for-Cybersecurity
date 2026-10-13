# Incident Triage RAG

This project builds an offline retrieval-augmented generation system over an original five-document cybersecurity incident-triage knowledge base. The notebook completes the course practice pipeline, validates an eight-question gold set, builds a Chroma vector store with local MiniLM embeddings, prints grounded answer and refusal transcripts, and compares chunk size, retrieval count, and cosine-distance threshold settings. Run `rag_notebook.ipynb` from this folder with the repository's RAG dependencies installed.

## Run on Jetstream2

Clone this branch and create a dedicated environment from the repository root:

```bash
git clone --branch rag-project --single-branch \
  https://github.com/vitolscolin/IT7075-Applied-AI-for-Cybersecurity.git
cd IT7075-Applied-AI-for-Cybersecurity
python3 -m venv .venv-rag
source .venv-rag/bin/activate
python -m pip install --upgrade pip
python -m pip install -r 04_RAG/requirements.txt ipykernel nbformat nbclient
python -m ipykernel install --user --name it7075-rag \
  --display-name "Python (IT7075 RAG)"
```

Open the cloned repository through VS Code Remote-SSH, open `rag_project/rag_notebook.ipynb`, select **Python (IT7075 RAG)**, and run all cells from the top. The assignment pipeline intentionally uses CPU because the embedding model is small and no GPU is required. A Jetstream2 run will replace the saved local outputs and regenerate `results.csv` and `figure.png` from that machine.
