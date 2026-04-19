from ingestion.loader import load_json
from ingestion.parser import normalize_batch

logs = load_json("/data/raw_logs.json")
clean = normalize_batch(logs)

print(clean)