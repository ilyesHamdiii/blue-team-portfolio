import json

def load_json(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data


if __name__ == "__main__":
    logs = load_json("./data/raw_logs.json")
    print(f"Loaded {len(logs)} events")
    print(logs[0])