# Three-environment organization — 2026-09-28

The walkthrough now has one shared prompt-plan/selector cell and three complete
sections: Local workstation, Google Colab, and Jetstream2. Each section includes
its own configuration, setup checks, model runs, GUI, settings experiment, exports,
and cleanup. Every environment-specific code cell is guarded by `ACTIVE_ENVIRONMENT`.
The larger-model experiment appears only in Jetstream. The final analysis checklist
follows that section and applies to all three environments.

Validation: notebook schema and all code compilation passed; inactive sections were
executed with no supporting variables to confirm they perform no work. AST comparisons
confirmed the existing model/measurement code was preserved in all three sections.
A full Jetstream run passed 21 rows, Gradio prediction, CSV/chart exports, and ZIP
integrity. Local inference was not repeated for this structural change; its unchanged
code passed the previous review. Colab remains unverified. The remote notebook's
shared selector defaults to Jetstream; the repository copy defaults to local.

# Walkthrough update — 2026-09-28

The review below is historical. The walkthrough now includes prepared Jetstream access,
a Colab runtime checklist, early Ollama/CUDA checks, cached-model reuse with an explicit
offline switch, and actual-device recording. Ollama placement mismatches produce error
rows rather than successful GPU results. Comparisons filter by both prompt plan and
canonical baseline settings; older rows without actual placement are grouped separately
as unverified. Exports share a configurable results root so verification data stays
separate from assignment measurements. The GUI instructions explain Run All cleanup.

Validation of the updated walkthrough: full local CPU and Jetstream GPU execution
passed with 21 successful rows each, real Gradio predictions, nonempty CSV/chart
exports, and valid ZIP archives. Targeted regression checks confirmed mixed settings,
other prompt plans, and failed rows do not enter matching summaries; legacy device
metadata stays separate, and requested GPU runs with CPU placement become error rows.
The refined Jetstream chart was visually inspected. Colab remains unverified.
Local verification artifacts: `/tmp/llmhosting-updated-local/` (temporary).
Remote verification artifacts: `~/mini_project_LLMHosting/setup-verification-updated/`.
The previous remote notebook was backed up before installing the clean updated copy.

# LLMHosting notebook review — 2026-09-23

The installed local CPU workflow passed real inference and integration checks. No blocking execution defect was found on this path. GPU, Colab, Jetstream2, fresh installation, and fresh model downloads were not verified.

## Findings

1. **Medium — comparison can mix different baseline configurations.** In section 10 (code cell 25), rows are filtered by prompt-plan hash, but the hash contains only prompts. The aggregation groups by environment, device, backend, and model, without filtering or grouping by `settings`. Running the same prompts again with a different token limit, temperature, top-p, or seed combines those runs in one chart bar. Keep baseline settings fixed for the assignment; a future code change should filter by the serialized baseline settings or group configurations separately. The test used only one baseline configuration, so its chart is unaffected.
2. **Low — cached models do not make the default notebook offline-ready.** Section 5 always calls `ollama pull`; section 6 calls `snapshot_download` without `local_files_only=True`. These setup steps can require network access despite local inference. The setup guide now explains how to reuse cached models offline.
3. **Usability — Run All closes the browser interface.** Section 11 calls `demo.close()`. This is appropriate cleanup, but for personal use pause after section 7 and leave the kernel running. The guide now explains this and identifies the interface's model (SmolLM2) and lack of conversation history.

The notebook code was left unchanged for this review. The adjacent setup guide was expanded with terminal, API, notebook, browser, offline, and cleanup instructions.

## Verified behavior

- Notebook structure passed `nbformat.validate`; code cells compiled and ran sequentially in the dedicated Python environment through a review harness.
- `pip check` reported no broken requirements.
- Both expected Ollama models were installed and the service responded on loopback.
- Three successful measured model loads, 15 successful baseline responses (five per model), and three successful settings responses: **21 successful measurement rows, zero error rows**.
- Gradio launched on loopback and answered a real HTTP prediction request through `gradio_client`.
- JSONL, prompt plan, hardware details, Ollama placement records, CSV summaries, PNG chart, and ZIP were created. The chart was visually inspected and ZIP integrity checked.
- Gradio closed successfully at cleanup.

| Model | Baseline responses | Mean response time |
|---|---:|---:|
| Llama 3.2 1B / Ollama | 5 | 5.77 s |
| Qwen 2.5 0.5B / Ollama | 5 | 1.95 s |
| SmolLM2 135M / Transformers | 5 | 3.43 s |

These are single-trial review measurements with differing output lengths, not a quality ranking or assignment evidence. The notebook correctly distinguishes Ollama decode throughput from Transformers full-generation throughput; compare client response times across backends. Ollama's duration fields are documented in nanoseconds in the [official generation API reference](https://docs.ollama.com/api/generate).

Successful execution does not establish response accuracy. In this test, SmolLM2 answered the logic question incorrectly, failed the requested JSON-only format, and invented a hash for a file it could not access. Several responses reached the 128-token limit and ended mid-answer. The model card also documents limitations in [SmolLM2's capabilities](https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct).

## Test scope and reproducibility

The harness redirected generated files to `/tmp/llmhosting-review-20260923/`, verified the installed Ollama models instead of pulling them again, and set `HF_HUB_OFFLINE=1` to use the cached Hugging Face snapshot. Optional installation, server startup, and larger-model cells remained disabled. Thus this was a test of the installed local execution path, not an unmodified online Run All or a clean-machine installation. The Gradio endpoint was tested programmatically; VS Code's interactive kernel picker and notebook rendering were not automated. Matplotlib used its noninteractive Agg renderer; PNG export succeeded.

Environment: Python 3.12 environment at `.venv-llmhosting`; Torch `2.14.0+cpu`, Transformers `4.57.6`, Gradio `5.50.0`, pandas `2.3.3`, psutil `7.2.2`. Torch reported CUDA unavailable; Ollama reported zero VRAM placement for both models.

Temporary evidence (may be removed by system cleanup):

- Harness: `/tmp/review_llmhosting.py`
- Execution log: `/tmp/llmhosting-review.log`
- Export archive: `/tmp/llmhosting-review-20260923/llmhosting-local.zip`

See [LLMHosting_Setup.md](LLMHosting_Setup.md) for local-use instructions.
