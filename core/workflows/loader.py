# core/workflows/loader.py

import yaml
from pathlib import Path


WORKFLOW_DEFINITION_DIR = Path(__file__).parent / "definitions"


def load_workflow_definitions() -> list[dict]:
    workflows = []

    for file in WORKFLOW_DEFINITION_DIR.glob("*.yaml"):
        with open(file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            data["_file"] = file.name
            workflows.append(data)

    return workflows
