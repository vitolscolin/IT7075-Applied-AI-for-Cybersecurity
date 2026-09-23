# LLM Hosting walkthrough

Open `MiniProject_LLMHosting_Walkthrough.ipynb` in VS Code. Choose **Select Kernel → Python Environments → .venv-llmhosting/bin/python** from the repository root. If it is not listed, choose the interpreter by its path.

The dedicated environment contains CPU PyTorch, Transformers, Gradio, Jupyter's kernel, and the measurement/chart dependencies. It does not modify the course's existing `.venv`. Ollama already had `llama3.2:1b`; setup added `qwen2.5:0.5b`. The notebook downloads `HuggingFaceTB/SmolLM2-135M-Instruct` into the repository's ignored `.cache/huggingface` directory.

Run the notebook in order, starting with your prompt plan. Most experiment cells run real inference and may take minutes on CPU. Gradio starts only when its cell is run and closes in the final cell. Ollama must be running; use `ollama serve` in a separate terminal if needed.

Your measurements are saved under `llmhosting_results/<environment>/`, with CSV, chart, and ZIP export cells. These generated files and the local environment are ignored by Git. Setup verification outputs live separately under `/tmp/llmhosting-smoke` and are not your assignment measurements.

For Colab and Jetstream2, follow the environment setup section inside the notebook. Those environments require your Google account and class VM access and have not been provisioned by local setup. Complete your own screenshots, interpretation, report, and live video after running the experiments.

To rebuild locally on Linux from the repository root:

```bash
python3 -m venv .venv-llmhosting
.venv-llmhosting/bin/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv-llmhosting/bin/python -m pip install -r 03_LLMs_Local_and_Cloud/assignments/project/requirements-llmhosting.txt
.venv-llmhosting/bin/python -m ipykernel install --prefix .venv-llmhosting --name llmhosting --display-name 'Python (LLM Hosting)'
```

For GPU machines, install a compatible CUDA PyTorch build instead of the CPU build. The notebook records actual GPU availability and model placement.
