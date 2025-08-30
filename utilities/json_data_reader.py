import json
import os

def load_json(file_name: str):
    data_dir = os.path.join(os.getcwd(), "data")
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

