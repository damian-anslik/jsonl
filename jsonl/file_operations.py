import os
import json
from jsonl import constants


def load(file_path: os.PathLike) -> list[dict]:
    """
    Load a JSONL file into a list of objects, and return a list of objects.
    """
    with open(file_path, 'r', encoding=constants.FILE_ENCODING) as f:
        lines = f.readlines()
    return [json.loads(line) for line in lines]


def dump(file_path: os.PathLike, lines: list[dict]) -> None:
    """
    Dump a list of objects into a JSONL file. Each object is a line.
    """
    with open(file_path, 'w', encoding=constants.FILE_ENCODING) as f:
        for line in lines:
            f.write(json.dumps(line) + constants.LINE_SEPARATOR)
