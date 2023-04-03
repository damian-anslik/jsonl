import os
import json
import typing
from jsonl import constants


def load(file_path: os.PathLike) -> typing.Generator[dict, None, None]:
    """  
    Load a JSONL file and return a generator of objects. Each object is a line.
    """
    FILE_MODE = 'r'
    with open(file_path, FILE_MODE, encoding=constants.FILE_ENCODING) as f:
        while True:
            line = f.readline()
            if not line:
                break
            yield json.loads(line)


def dump(file_path: os.PathLike, lines: list[dict], file_mode: str = "w") -> None:
    """
    Dump a list of objects into a JSONL file. Each object is a line.
    """
    with open(file_path, file_mode, encoding=constants.FILE_ENCODING) as f:
        for line in lines:
            f.write(json.dumps(line) + constants.LINE_SEPARATOR)
