from database.db import fetch_all,get_top_commands

rows = fetch_all()
cmd = get_top_commands()

print(rows)