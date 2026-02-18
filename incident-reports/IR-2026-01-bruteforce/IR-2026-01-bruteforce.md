# Incident Report: Brute-Force Authentication Attempt (Lab Simulation)

Report ID: IR-2026-01

Date of Detection: 2026-02-18

Analyst: Ilyes HAMDI

Severity Level: Medium

Status: Closed

## Purpose

This README summarizes the incident report for a simulated brute-force authentication attempt conducted within the SOC lab environment. It provides an executive summary, detection details, timeline, investigation notes, findings, containment actions, root cause, lessons learned, limitations, and recommendations.

Use this document as a quick reference for the incident and as a starting point for follow-up improvements to detections and lab capabilities.

## Quick facts

- Affected host: `WIN10-VICTIM` (Windows 10 lab endpoint)
- Affected user account: `ANGRY-BOB`
- Data source: Windows Security Log (via Wazuh agent)
- Detection: Multiple Failed Logins Threshold Alert (triggered on ≥5 failed attempts within 5 minutes)
- MITRE ATT&CK: T1110 — Brute Force

## 1. Executive summary

A sequence of multiple failed authentication attempts followed by a successful login was detected on a Windows endpoint in the SOC lab. The pattern matched a brute-force authentication attempt against a local test account. The activity was intentionally simulated to validate detection capabilities and incident response procedures. The event was contained within the lab; no persistence, lateral movement, or post-authentication abuse was observed.

## 2. Detection source

- Detection name / rule: **Multiple Failed Logins Threshold Alert**
- Data source(s): Windows Security Log (Wazuh agent)
- Trigger condition: ≥5 failed login attempts (Event ID 4625) within 5 minutes for the same account
- Detection logic: Frequency-based correlation (not anomaly-based)

The SIEM correlated multiple Event ID 4625 entries and generated an alert. A subsequent Event ID 4624 showed a successful authentication for the same account.

## 3. Environment context

- Host: `WIN10-VICTIM` (Workstation)
- User: `ANGRY-BOB`
- Network: Internal lab NAT network
- Environment: Controlled SOC lab with a Windows endpoint and a Wazuh manager on Ubuntu

## 4. Timeline of events (UTC)

| Time     | Event                                | Source               |
| -------- | ------------------------------------ | -------------------- |
| 16:03:12 | Failed login attempt (Event ID 4625) | Windows Security Log |
| 16:06:20 | Failed login attempt                 | Windows Security Log |
| 16:06:29 | Failed login attempt                 | Windows Security Log |
| 16:06:37 | Failed login attempt                 | Windows Security Log |
| 16:06:45 | Failed login attempt                 | Windows Security Log |
| 16:07:46 | Threshold alert triggered            | Wazuh SIEM           |
| 16:08:10 | Successful login (Event ID 4624)     | Windows Security Log |

Only authentication-related events were seen. No suspicious activity followed the successful login.

## 5. Investigation and analysis

Investigation steps performed:

- Queried Windows Security logs for Event IDs 4625 and 4624
- Filtered by username `ANGRY-BOB`, host `WIN10-VICTIM`, and the alert time window
- Examined logon type and source fields

Observations:

- Multiple failed interactive logins clustered within seconds
- Source IP was localhost (simulated activity)
- Successful interactive login followed the failures

Alternative explanations (mistyped password, misconfigured service) were considered but ruled out based on controlled test conditions and the tight clustering of events.

No signs of lateral movement, privilege escalation, or persistence were found in follow-up log queries.

## 6. Findings

- Confirmed malicious activity? **Yes (simulated)**
- Scope: Single local account on one workstation
- Persistence observed? **No**
- Lateral movement observed? **No**

Activity was limited to authentication attempts and ended at initial access.

## 7. Containment and response actions

- Reset the password for `ANGRY-BOB` (simulated containment)
- Temporarily disabled the account to demonstrate the IR process
- Reviewed and documented the detection rule
- Continued SIEM monitoring; no additional suspicious events observed

Because the activity was simulated in a contained lab, no escalation was necessary.

## 8. Root cause

Root cause: Controlled test activity executed to validate detection logic. In production, similar behavior could be caused by weak password policies, missing account lockout, or exposed authentication services. No misconfiguration contributed in the lab.

## 9. Lessons learned

- Frequency-based correlation effectively detects brute-force patterns
- Proper threshold tuning reduces false positives (e.g., user typos)
- Post-authentication monitoring is critical to detect abuse after a successful login
- Additional enrichment (source reputation, geo) strengthens detections in real environments

## 10. Limitations

- Single-host lab (no distributed attack simulation)
- No Active Directory domain controller logs collected
- No network-level telemetry (firewall logs)
- Source IP is always local in this lab

These limitations reduce realism for distributed/distant-source brute-force simulations.

## 11. Recommendations

- Implement account lockout policy after defined failed attempts
- Adjust detection to escalate when failed attempts are followed by a success
- Differentiate interactive vs. network logons in detection rules
- Expand lab to include DC logging and network telemetry ingestion to simulate more realistic attacks

## Reference

- Full incident write-up: `IR-2026-01-bruteforce.md` (same folder)

## Notes for reviewers

- This README is intended for quick consumption and can be embedded in a portfolio or used as a brief when discussing the lab exercise.
- For full forensic detail, review raw event logs and the long-form incident report `IR-2026-01-bruteforce.md`.
