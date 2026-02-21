"""
auth_failure_summary.py

Purpose:
    Automates analysis of Windows failed login events (Event ID 4625) from a CSV log file.
    Summarizes failed logins per user, per source IP, and per logon type.
    Detects potential brute-force attempts based on a configurable threshold and time window.

Usage:
    python auth_failure_summary.py <logfile.csv>
    - logfile.csv: CSV file with columns EventID, TargetUserName, IpAddress, LogonType, TimeCreated
    - Example:
        python auth_failure_summary.py SecurityEvents.csv

Assumptions:
    - Input log is in CSV format with appropriate column names.
    - Timestamps are in the format: YYYY-MM-DD HH:MM:SS
    - Only Event ID 4625 (failed logon) is analyzed.

Limitations:
    - Does not process other event IDs.
    - Brute-force detection uses a simple time-window threshold, may not capture sophisticated attacks.
    - Currently only prints output to console; no export to file.
    - Does not validate IP address formats.
"""

import csv
from collections import defaultdict
from datetime import datetime, timedelta

FAILED_EVENT_ID = "4625"
BRUTE_FORCE_THRESHOLD = 10        # number of failed attempts to flag
BRUTE_FORCE_WINDOW_MINUTES = 5    # time window for brute-force detection

def parse_timestamp(ts):
    """Parse timestamp string to datetime object."""
    return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")

def main(file_path):
    """Main function to summarize failed logins and detect potential brute-force attacks."""
    total_failed = 0
    users = defaultdict(int)       # failed logins per user
    source_ips = defaultdict(int)  # failed logins per IP
    logon_types = defaultdict(int) # count per logon type
    attempts = defaultdict(list)   # timestamps per (user, IP) for brute-force analysis

    # Read CSV log file
    with open(file_path, newline='', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row.get("EventID") != FAILED_EVENT_ID:
                continue

            total_failed += 1
            user = row.get("TargetUserName", "UNKNOWN")
            src_ip = row.get("IpAddress", "UNKNOWN")
            logon_type = row.get("LogonType", "UNKNOWN")
            timestamp = parse_timestamp(row.get("TimeCreated"))

            # Aggregate counts
            users[user] += 1
            source_ips[src_ip] += 1
            logon_types[logon_type] += 1
            attempts[(user, src_ip)].append(timestamp)

    # Print report
    print("\n=== Failed Login Summary ===")
    print(f"\nTotal failed logons: {total_failed}")

    print("\nTop Targeted Users:")
    for user, count in sorted(users.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {user}: {count}")

    print("\nTop Source IPs:")
    for ip, count in sorted(source_ips.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {ip}: {count}")

    print("\nLogon Types:")
    for lt, count in logon_types.items():
        print(f"  Type {lt}: {count}")

    print("\nPotential Brute Force Alerts:")
    for (user, ip), times in attempts.items():
        times.sort()
        for i in range(len(times)):
            window = times[i:i+BRUTE_FORCE_THRESHOLD]
            if len(window) == BRUTE_FORCE_THRESHOLD:
                if window[-1] - window[0] <= timedelta(minutes=BRUTE_FORCE_WINDOW_MINUTES):
                    print(f"  {user} from {ip} — "
                          f"{BRUTE_FORCE_THRESHOLD}+ attempts in "
                          f"{BRUTE_FORCE_WINDOW_MINUTES} minutes")
                    break

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python auth_failure_summary.py <logfile.csv>")
    else:
        main(sys.argv[1])