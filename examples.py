import jsonl

def load_json_lines_from_file(file_path: str) -> list[dict]:
    lines = jsonl.load(file_path)
    return lines

def dump_json_lines_to_file(file_path: str, lines: list[dict]) -> None:
    jsonl.dump(file_path, lines)

def load_json_lines_from_string(string: str) -> list[dict]:
    lines = jsonl.loads(string)
    return lines

def dump_json_lines_to_string(lines: list[dict]) -> str:
    string = jsonl.dumps(lines)
    return string