import json
from jsonl import constants


def loads(string: str) -> list[dict]:
    """
    Load a JSONL string into a list of objects, and return a list of objects. Each object is a line. Lines are separated by the newline character.
    """
    return [json.loads(line) for line in string.split(constants.LINE_SEPARATOR)]


def dumps(lines: list[dict]) -> str:
    """
    Dump a list of objects into a JSONL string. Each object is a line. Lines are separated by the newline character.
    """
    return constants.LINE_SEPARATOR.join([json.dumps(line) for line in lines])
