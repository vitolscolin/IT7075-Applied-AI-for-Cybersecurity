"""Execute real notebooks and save only successful runs; never synthesize outputs."""
import argparse
import os
from pathlib import Path
import sys

import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "langgraph_project"


def execute(path):
    notebook = nbformat.read(path, as_version=4)
    manager = KernelManager(kernel_name="python3")
    manager.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
    env = dict(os.environ)
    for key in ("OPENAI_API_KEY", "ANTHROPIC_API_KEY", "LANGSMITH_API_KEY", "LANGCHAIN_API_KEY"):
        env.pop(key, None)
    env.update(PYTHON_DOTENV_DISABLED="1", LANGSMITH_TRACING="false", LANGCHAIN_TRACING_V2="false")
    try:
        NotebookClient(notebook, km=manager, timeout=180, resources={"metadata": {"path": str(path.parent)}}).execute(env=env)
    finally:
        # A supplied manager belongs to this caller, so nbclient does not close it.
        if manager.has_kernel:
            manager.shutdown_kernel(now=True)
    nbformat.validate(notebook)
    nbformat.write(notebook, path)
    count = sum(c.cell_type == "code" for c in notebook.cells)
    print(f"Executed {path.relative_to(ROOT)}: {count} code cells, no cell errors")
    return notebook


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lectures", action="store_true", help="Also run the two course lectures through their guarded no-key paths")
    args = parser.parse_args()
    if args.lectures:
        for name in ("langgraph_state_nodes", "langgraph_branch_tools"):
            execute(ROOT / "06_LangGraph/code" / (name + ".ipynb"))
    execute(PROJECT / "agent_notebook.ipynb")
