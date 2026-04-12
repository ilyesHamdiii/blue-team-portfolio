# Incident Report: Local Privilege Escalation and Persistence Simulation

**Report ID:** IR-2026-04-STEP4-01  
**Date of Detection:** 2026-04-12  
**Analyst:** SOC-Lab Analyst  
**Severity Level:** Medium  
**Status:** Resolved (Lab Simulation)

---

## 1. Executive Summary

A simulated endpoint security incident was conducted to evaluate detection capabilities for privilege escalation and persistence behaviors on a Windows 10 workstation monitored by Wazuh with Sysmon telemetry enabled.

Key simulated activity:

- Execution of processes with elevated privileges
- Creation of persistence mechanisms via scheduled tasks, registry Run key modification, and service creation

The activity was flagged as suspicious due to patterns consistent with post-compromise behavior. The investigation confirmed this was a controlled laboratory simulation (no real compromise).

---

## 2. Detection Source

**Detection name / rule:** Sysmon Process + Persistence Monitoring

**Data sources**

- Sysmon event logs (Event ID 1 — Process Create; Event ID 13 — Registry Object Modified)
- Windows Service Control Manager logs (Event ID 7045)
- Wazuh agent / centralized ingestion

**Trigger conditions observed**

- Process creation from an administrative context
- Modification of Registry Run key(s)
- New service installation (7045)

**MITRE ATT&CK mapping**

- T1053.005 — Scheduled Task/Job
- T1547.001 — Registry Run Keys / Startup Folder
- T1543.003 — Windows Service Creation
- T1068 — Exploitation for Privilege Escalation (simulated)

---

## 3. Environment Context

- **Affected host(s):** Windows 10 lab machine
- **User account(s):** Local test user (administrator context used during simulation)
- **Network segment:** Isolated lab environment
- **System role:** Endpoint workstation (SOC monitoring target)

---

## 4. Timeline of Events (UTC)

|     Time | Event                                    | Log Source        |
| -------: | ---------------------------------------- | ----------------- |
| 15:12:15 | Elevated command prompt execution        | Sysmon            |
| 15:13:02 | Scheduled task `UpdateCheckTask` created | Sysmon            |
| 15:13:40 | Registry Run key modified (`FakeApp`)    | Sysmon            |
| 15:14:10 | Service `FakeUpdaterService` created     | System Log (7045) |

---

## 5. Investigation and Analysis

Investigation methods:

- Wazuh dashboard queries filtering on Sysmon Event ID 1 (Process Creation), Event ID 13 (Registry modification) and Windows System logs for Service Control Manager events.
- Correlation of event timestamps to identify sequence and timing between process execution and persistence creation.

Key observations:

- Elevated process execution originating from a session with administrative privileges.
- Multiple persistence mechanisms deployed within a short time window after elevation:
  - Scheduled Task creation
  - Registry Run key modification
  - Service installation
- Event sequencing presents a structured post-compromise simulation pattern.
- No evidence of lateral movement or external network activity was observed.

Alternative explanations (e.g., legitimate administrative changes) were considered but the combination and timing of actions are strongly indicative of intentional persistence deployment used in attacker scenarios.

---

## 6. Findings

| Item                          | Result                                                            |
| ----------------------------- | ----------------------------------------------------------------- |
| Confirmed malicious activity? | No — Controlled simulation                                        |
| Scope of impact               | Single host; local system changes only                            |
| Persistence observed          | Yes — Scheduled task, Registry Run key, Service-based persistence |
| Lateral movement observed?    | No                                                                |

---

## 7. Containment & Response Actions

This was a controlled laboratory simulation no containment actions were performed. Specifically:

- No host isolation
- No account locks or disables
- No production mitigation applied

Recommended actions for a production incident:

- Immediate host isolation (network & console)
- Investigate origin of the administrative session and credential usage
- Review and remediate privilege escalation vector(s)
- Collect volatile artifacts and preserve logs for forensic analysis

---

## 8. Root Cause

- Root cause: Not an actual security failure. This was a deliberate SOC training simulation of privilege escalation and persistence techniques.

---

## 9. Lessons Learned

- Native Windows auditing alone may be insufficient for full process-level telemetry.
- Sysmon provides improved detection fidelity for:
  - Process creation visibility
  - Registry persistence tracking
  - Correlation of behavior chains
- SOC analysis benefits from correlating sequences of related events instead of analyzing single events in isolation.

---

## 10. Limitations

- Windows 10 Home (if used) may restrict full Advanced Audit Policy enforcement.
- Some native Windows security events (e.g., 4672, 4688) were not consistently generated during the simulation.
- Telemetry completeness depends on Sysmon configuration quality.
- No network-based telemetry was included in this simulation; network indicators could provide additional context.

---

## 11. Recommendations

- Standardize Sysmon across lab endpoints and tune configuration for relevant telemetry (process, registry, network, PowerShell).
- Implement centralized Wazuh rule correlation to detect short chains of behavior (e.g., Process → Persistence modifications in short time window).
- Extend monitoring to include:
  - PowerShell logging (Script Block/4104)
  - Sysmon Event ID 3 (Network connections) for host-based network visibility
- Develop correlation rules that flag rapid Process → Persistence chains for analyst review.

---

_Report prepared for SOC lab training and documentation purposes._
