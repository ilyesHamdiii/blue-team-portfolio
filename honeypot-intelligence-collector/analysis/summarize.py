from collections import Counter
import json

with open("./output/parsed.json") as f:
    data = json.load(f)

ips = Counter()
users = Counter()
passwords = Counter()
events = Counter()

for d in data:
    if d["src_ip"]:
        ips[d["src_ip"]] += 1
    if d["username"]:
        users[d["username"]] += 1
    if d["password"]:
        passwords[d["password"]] += 1
    if d["event"]:
        events[d["event"]] += 1

print("Top IPs:", ips.most_common(10))
print("Top Usernames:", users.most_common(10))
print("Top Passwords:", passwords.most_common(10))
print("Top Events:", events.most_common(10))