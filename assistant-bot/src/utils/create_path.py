import os
import sys
from pathlib import Path
from src.constants import COMMANDS


def get_run_path():
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = os.getcwd()

    if path != COMMANDS["HELP"]:
        Path(path).mkdir(parents=True, exist_ok=True)
    return path