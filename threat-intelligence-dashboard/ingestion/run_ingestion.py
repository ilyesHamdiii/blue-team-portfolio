from pathlib import Path
import sys

# Add project root to sys.path so sibling packages (database, loader, parser) are importable
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from loader import load_json
from parser import normalize_batch
from database.db import init_db, insert_batch,fetch_all

init_db()

data_file = ROOT / "data" / "raw_logs.json"
logs = load_json(str(data_file))
clean_logs = normalize_batch(logs)

insert_batch(clean_logs)


print(f"Inserted {len(clean_logs)} events into database.")
print(clean_logs)
