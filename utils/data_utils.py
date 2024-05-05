import json

def read_json(fp: str) -> dict:
    with open(fp, 'r', encoding='utf-8') as f:
        return json.load(f)