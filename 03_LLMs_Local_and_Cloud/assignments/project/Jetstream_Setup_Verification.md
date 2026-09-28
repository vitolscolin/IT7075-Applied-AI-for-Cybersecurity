# Jetstream lab setup verification — 2026-09-28

The remote lab is prepared in `~/mini_project_LLMHosting`. Connect through the
private local `jetstream-lab` SSH alias. No connection credentials belong in this
repository. See `LLMHosting_Setup.md` for opening the notebook.

Installed: Python 3.12.3, PyTorch 2.11.0+cu128, Transformers 4.57.6, Gradio 5.50.0,
JupyterLab 4.6.4, and Ollama 0.34.4. The remote `requirements-installed.txt` records
all installed Python dependency versions. The remote notebook selects
`ENVIRONMENT = "jetstream2"`, `DEVICE = "cuda"`, and the `llmhosting` kernel.

Verified on the allocated NVIDIA GRID A100X-20C (20 GiB VRAM):

- `pip check` passed; a real PyTorch CUDA tensor computation passed.
- Jupyter started on loopback, required a token, and exposed the lab kernel through
  its authenticated API. The verification server was stopped afterward.
- The full notebook executed through a separate smoke-test harness: 21 successful
  measurement rows and zero error rows, including the three baseline models.
- Saved Ollama placement records showed nonzero VRAM for both baseline models:
  Llama 3.2 1B and Qwen 2.5 0.5B. Transformers executed SmolLM2 on CUDA.
- Gradio served a real prediction through its client API and closed at cleanup.
- Notebook exports completed and the ZIP passed its integrity check.
- The optional `qwen2.5:7b` model was downloaded; its inference was not tested.

The VM's GPU device files use the `vglusers` group. Initially the Ollama service
could not access them and used CPU. Adding its service account to that existing
group and restarting the service corrected GPU access; the full smoke test was
then rerun. Earlier diagnostic outputs are preserved separately on the VM.

The clean remote notebook has no saved smoke outputs. Verification outputs and the
export archive are under `setup-verification/`; no assignment results folder was
created. These checks establish execution and integration, not answer quality or
completed assignment evidence. The VS Code remote interface was not visually
tested. Jupyter and Gradio are stopped; Ollama remains available on loopback and
models were unloaded by notebook cleanup. The VM remains running.

## Updated walkthrough verification

The revised walkthrough passed another 21-row GPU run, including actual-placement
recording, Gradio prediction, CSV/chart creation, and ZIP integrity. Its results live
in `setup-verification-updated/`. The export cell now uses the same configurable
results root as measurements. The updated clean remote notebook retains Jetstream
and CUDA defaults; the previous version is preserved in `backups/`. Colab execution
remains unverified. The 7B model is still downloaded but untested.
