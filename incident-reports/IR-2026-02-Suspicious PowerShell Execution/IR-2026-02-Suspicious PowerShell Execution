Incident Report: Suspicious PowerShell Execution

Report ID: IR-2026-02

Date of Detection: 2026-02-18

Analyst: ilyes HAMDI

Severity Level: Medium

Status: Closed

## 1. Executive Summary

A controlled PowerShell script execution was detected on a Windows 10 Home lab endpoint. The execution was encoded, simulating potentially malicious behavior.

Detected: Encoded PowerShell command execution (powershell.exe -EncodedCommand)

Suspicious because: unusual encoded command execution is a common attack technique

Outcome: Controlled lab activity; logged and detected successfully

## 2. Detection Source

Detection name or alert rule: Suspicious PowerShell Execution

Data source(s): Wazuh agent → Microsoft-Windows-PowerShell/Operational logs

Trigger condition: Event ID 4104 / 4688 with powershell.exe and -EncodedCommand

MITRE ATT&CK mapping: T1059.001 – PowerShell

## 3. Environment Context

Affected host(s): WIN-CLIENT-01 (Windows 10 Home)

User account(s): ANGRY-BOB

Network segment: Lab NAT network

System role: Workstation

## 4. Timeline of Events

| Time (UTC) | Event Description                   | Log Source    |
| ---------- | ----------------------------------- | ------------- |
| 15:10:25   | Encoded PowerShell command executed | Event ID 4688 |
| 15:11:26   | Script block logged                 | Event ID 4104 |
| 15:12:05   | Wazuh alert triggered               | Wazuh SIEM    |

## 5. Investigation and Analysis

- Queried PowerShell Operational logs via Wazuh
- Expanded Event ID 4104 to inspect encoded command
- Verified process creation (4688) linked to encoded execution
- Pattern confirmed: single-user, lab-controlled activity
- Alternative explanations (legitimate admin scripts) ruled out due to lab context

## 6. Findings

- Confirmed malicious activity? No (controlled lab simulation)
- Scope of impact: Single workstation
- Persistence observed? No
- Lateral movement observed? No

## 7. Containment and Response Actions

- Verified no post-execution malicious behavior
- Monitored Wazuh for repeat occurrences

## 8. Root Cause

Controlled test activity to validate detection

Real-world equivalent: encoded PowerShell used by attackers to bypass defenses

## 9. Lessons Learned

- Script Block Logging effectively captures encoded commands
- Wazuh agent integration allows real-time alerting
- Highlighted need for detection tuning to differentiate benign admin scripts

## 10. Limitations

- Lab-only, single host
- Windows Home limits some GPO-based logging features
- No domain-wide correlation

## 11. Recommendations

- Apply detection logic in production with account exclusions for legitimate admin tasks
- Continue monitoring for unusual encoded PowerShell activity
- Expand detection to include file write operations triggered by PowerShell

### Encoded command used in simulation

To reproduce the test, the following PowerShell snippet was used to encode and execute a small command that writes processes to a file:

```powershell
$command = 'Get-Process | Out-File C:\Temp\process.txt'
$bytes = [System.Text.Encoding]::Unicode.GetBytes($command)
$encoded = [Convert]::ToBase64String($bytes)
powershell.exe -EncodedCommand $encoded
```

Note: during process inspection the `whoami` command was also observed as part of the simulated activity (the process executed an additional/related `whoami` call).

## References

- Microsoft Script Block Logging and PowerShell Operational logs
- Wazuh PowerShell monitoring integration
