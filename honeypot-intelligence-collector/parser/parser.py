import json

input_file = "./sample_logs/cowrie.log"
output_file = "./output/parsed.json"

parsed = []

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()

        try:
            log = json.loads(line)
        except:
            continue

        parsed.append({
            "timestamp": log.get("timestamp"),
            "src_ip": log.get("src_ip"),
            "username": log.get("username"),
            "password": log.get("password"),
            "event": log.get("eventid"),
            "input": log.get("input")
        })

with open(output_file, "w") as f:
    json.dump(parsed, f, indent=4)