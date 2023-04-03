import jsonl


def stream_json_lines_from_file(file_path: str) -> None:
    for line in jsonl.load(file_path):
        print(line)


def load_json_lines_from_file(file_path: str) -> list[dict]:
    lines = [line for line in jsonl.load(file_path)]
    return lines


def dump_json_lines_to_file(file_path: str, lines: list[dict]) -> None:
    jsonl.dump(file_path, lines, file_mode="w")


def append_json_lines_to_file(file_path: str, lines: list[dict]) -> None:
    jsonl.dump(file_path, lines, file_mode="a")


def load_json_lines_from_string(string: str) -> list[dict]:
    lines = jsonl.loads(string)
    return lines


def dump_json_lines_to_string(lines: list[dict]) -> str:
    string = jsonl.dumps(lines)
    return string
