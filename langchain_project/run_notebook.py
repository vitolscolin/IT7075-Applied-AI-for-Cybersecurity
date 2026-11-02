"""Execute and save the project notebook with a fresh Python kernel."""
import os
from pathlib import Path

import nbformat
from nbclient import NotebookClient


def main():
    project = Path(__file__).resolve().parent
    path = project / "langchain_notebook.ipynb"
    os.environ["CUDA_VISIBLE_DEVICES"] = ""
    os.environ["TOKENIZERS_PARALLELISM"] = "false"
    notebook = nbformat.read(path, as_version=4)
    client = NotebookClient(notebook, timeout=600, kernel_name="python3",
                            resources={"metadata": {"path": str(project)}})
    client.execute()
    nbformat.write(notebook, path)
    count = sum(cell.cell_type == "code" for cell in notebook.cells)
    print(f"PASS: executed {count} code cells and saved {path.name}")


if __name__ == "__main__":
    main()
