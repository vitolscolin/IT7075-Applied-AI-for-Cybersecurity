# LLM Hosting walkthrough

Open `MiniProject_LLMHosting_Walkthrough.ipynb` in VS Code. Choose **Select Kernel → Python Environments → .venv-llmhosting/bin/python** from the repository root. If it is not listed, choose the interpreter by its path.

The dedicated environment contains CPU PyTorch, Transformers, Gradio, Jupyter's kernel, and the measurement/chart dependencies. It does not modify the course's existing `.venv`. Ollama already had `llama3.2:1b`; setup added `qwen2.5:0.5b`. The notebook downloads `HuggingFaceTB/SmolLM2-135M-Instruct` into the repository's ignored `.cache/huggingface` directory.

Run the notebook in order, starting with your prompt plan. Most experiment cells run real inference and may take minutes on CPU. Gradio starts only when its cell is run and closes in the final cell. Ollama must be running; use `ollama serve` in a separate terminal if needed.

Your measurements are saved under `llmhosting_results/<environment>/`, with CSV, chart, and ZIP export cells. These generated files and the local environment are ignored by Git. Setup verification outputs live separately under `/tmp/llmhosting-smoke` and are not your assignment measurements.

For Colab and Jetstream2, follow the environment setup section inside the notebook. Jetstream is now provisioned as described below; Colab still requires setup in each new runtime. Complete your own screenshots, interpretation, report, and live video after running the experiments.

To rebuild locally on Linux from the repository root:

```bash
python3 -m venv .venv-llmhosting
.venv-llmhosting/bin/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv-llmhosting/bin/python -m pip install -r 03_LLMs_Local_and_Cloud/assignments/project/requirements-llmhosting.txt
.venv-llmhosting/bin/python -m ipykernel install --prefix .venv-llmhosting --name llmhosting --display-name 'Python (LLM Hosting)'
```

For GPU machines, install a compatible CUDA PyTorch build instead of the CPU build. The notebook records actual GPU availability and model placement.

## Everyday local use (without running the assignment)

For a terminal conversation, open a terminal and run:

```bash
ollama run llama3.2:1b
# Or use the smaller Qwen model:
ollama run qwen2.5:0.5b
```

Type a prompt and press Enter. Type `/bye` to leave the conversation. If Ollama cannot connect, run `ollama serve` in another terminal and leave it open. If port 11434 is already occupied, the service may already be running; try `ollama list`. You do not need to activate the Python environment for these commands.

For a one-off request from your own script or terminal, use the local API:

```bash
curl --noproxy '*' http://127.0.0.1:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d '{"model":"llama3.2:1b","prompt":"Explain what a firewall does in three sentences.","stream":false}'
```

Read the `response` field in the returned JSON. This example sends a single independent prompt; it does not retain chat history. API reference: <https://docs.ollama.com/api/generate>.

## Run the notebook in VS Code

1. Open this repository folder in VS Code, then open `MiniProject_LLMHosting_Walkthrough.ipynb` alongside this guide.
2. Select the interpreter at `.venv-llmhosting/bin/python` using the notebook's kernel picker. The Python and Jupyter VS Code extensions are needed for notebook execution.
3. Run the shared configuration cell with `ACTIVE_ENVIRONMENT = "local"`, then use **1. Local workstation** with `DEVICE = "cpu"`. Leave `INSTALL_PACKAGES`, `START_OLLAMA`, and `COLAB_PUBLIC_LINK` false when the existing Ollama service is running.
4. Run the cells in order. Model setup can use the internet even when the model files are already cached. The notebook reuses installed Ollama models and checks the Hugging Face snapshot; enable `OFFLINE_MODE` to require cached files.
5. At your selected environment's **Graphical interface** step, open <http://127.0.0.1:7860> to use the browser interface. It runs **SmolLM2**, not the Ollama models. Each submission is independent; it is not a conversation with retained history.
6. Pause before the final cleanup cell if you want to keep using the interface. **Run All closes Gradio at the end.** Keep VS Code and its notebook kernel running while using the page.
7. Run your selected environment's **Export this environment and compare matching runs** cells for CSV, chart, and ZIP exports. Increment `TRIAL` before another benchmark run; earlier rows are appended, not replaced.

For only the browser interface, run shared configuration, then the selected environment's configuration, dependency/import/health checks, hardware check, measurement helpers, Hugging Face Transformers, and Graphical interface cells. Skip the Ollama experiment cells. The Transformers step still runs the five baseline prompts before the interface starts.

For longer personal-use answers, increase `BASE_SETTINGS["max_tokens"]`, for example to 256, before starting the interface. Keep assignment baseline settings unchanged across environments. SmolLM2 is a tiny demonstration model, so inspect its answers carefully.

## Offline use after downloads

The `ollama run` commands work with models already shown by `ollama list`. To run the notebook offline, set `OFFLINE_MODE = True` in your chosen environment's configuration cell. The download cells then require cached Ollama models and pass `local_files_only=True` for the Hugging Face snapshot. A complete Hugging Face snapshot must already exist in the configured cache. No cloud API key is required for these local inference paths.

## Stop local work

Run the notebook's final cleanup cell (or `demo.close()`) to stop Gradio. Stop the notebook kernel to release the Transformers model's RAM. Unload Ollama models if you have been using them interactively:

```bash
ollama stop llama3.2:1b
ollama stop qwen2.5:0.5b
```

If you manually started `ollama serve`, Ctrl+C in that terminal stops that server. An existing system service can stay running for your next session.

## Private Jetstream connection from this workstation

The connection is configured outside this repository in `~/.ssh/config`, using a
dedicated key in `~/.ssh/`. Host details and authentication material must stay
outside source control. The aliases below refer to that private local configuration;
they will not automatically exist on another workstation.

Open a remote shell:

```bash
ssh jetstream-lab
```

For browser access, keep a separate local terminal running:

```bash
ssh -N jetstream-lab-tunnel
```

This forwards local loopback ports **8888** (Jupyter) and **7860** (Gradio) to the VM.
Once the corresponding remote services are running, use `http://127.0.0.1:8888`
and `http://127.0.0.1:7860`. Use Jupyter's token when prompted. If a local service
already occupies either port, stop it or adjust the private SSH configuration.
Ctrl+C closes the tunnel; it does not stop the VM or remote services.

In VS Code, use **Remote-SSH: Connect to Host... → jetstream-lab**, then open your
remote lab folder. Select the Python environment installed on the VM for remote
notebooks. Remote Python/Jupyter extensions may need installation in that window.
The prepared remote lab is in `~/mini_project_LLMHosting`; its Python interpreter is
`.venv-llmhosting/bin/python` inside that folder.

When running the notebook on the VM, set `ACTIVE_ENVIRONMENT = "jetstream2"` in shared configuration and use
`DEVICE = "cuda"` only after the remote Python environment confirms CUDA is available.
Keep prompts and baseline generation settings consistent with your other runs.
If the VM address changes, update `HostName` in your private `~/.ssh/config`.
Never put passwords, private keys, Jupyter tokens, or credential-bearing connection
URLs in notebooks, repository settings, or committed documentation.

## Prepared Jetstream lab

Connect with `ssh jetstream-lab`, then:

```bash
cd ~/mini_project_LLMHosting
source .venv-llmhosting/bin/activate
./start-jupyter.sh
```

Keep that terminal open. In another **local** terminal, run
`ssh -N jetstream-lab-tunnel`, then open the local Jupyter URL shown by the launcher.
Jupyter requires its generated token; keep that URL private. Open
`MiniProject_LLMHosting_Walkthrough.ipynb` and select **Python (LLM Hosting GPU)**.
Alternatively, connect through VS Code Remote SSH, open `~/mini_project_LLMHosting`,
and choose `.venv-llmhosting/bin/python` as the notebook interpreter.

The remote copy selects `ACTIVE_ENVIRONMENT = "jetstream2"`; its Jetstream section uses `DEVICE = "cuda"`.
The repository's original notebook keeps its local defaults. Edit your hypothesis
and prompt plan before collecting assignment measurements. Setup verification
outputs are stored separately in `~/mini_project_LLMHosting/setup-verification/`;
they are not assignment results. Ollama runs as a system service on VM loopback.
Gradio becomes available on local port 7860 after its selected section's notebook cell runs; pause
before the final cleanup cell to keep using it.

To retrieve your actual results, run from the repository root on your workstation:

```bash
scp -r jetstream-lab:mini_project_LLMHosting/llmhosting_results/ \
  03_LLMs_Local_and_Cloud/assignments/project/
```

These results are ignored by Git. Remote notebook edits are not automatically
synchronized back to this repository. Save your results before stopping the VM
through the class dashboard when finished.

On this VM image, NVIDIA device files belong to the `vglusers` group. The Ollama
service account was added to that group and the service restarted so it can use
the GPU. When rebuilding, check actual placement with `ollama ps` or the notebook's
saved placement records; `DEVICE = "cuda"` alone does not prove GPU offload.
Installation follows the [official Ollama Linux instructions](https://docs.ollama.com/linux)
and the [PyTorch CUDA installation guidance](https://pytorch.org/get-started/locally/).

Updated walkthrough exports are written under `llmhosting_results/llmhosting-<environment>.zip`. Comparison charts filter by the current prompt plan and exact baseline settings, with actual placement shown separately from the requested device. Legacy rows without placement metadata are labelled `unverified`.

## Three-section walkthrough

The notebook has a shared prompt plan and selector followed by **1. Local workstation**,
**2. Google Colab**, and **3. Jetstream2**. Each section includes its complete lab workflow.
Run shared configuration first, then the section for the machine actually executing the
kernel. Code in unselected sections is skipped, so Run All operates only on the selected
environment. Restart the kernel before changing environments. The final cross-environment
analysis checklist follows the Jetstream workflow and applies to all three runs.
