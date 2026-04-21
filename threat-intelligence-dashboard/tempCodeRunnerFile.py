from pathlib import Path
from ingestion.loader import load_json
from ingestion.parser import normalize_batch

file_path = Path(__file__).resolve().parent / "raw_logs.json"
logs = load_json(str(file_path))
clean = normalize_batch(logs)

print(clean)