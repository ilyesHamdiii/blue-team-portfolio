# Detection Rule: Privilege Escalation Followed by Persistence Activity (Sysmon-Based)

**Detection ID:** DET-2026-04-STEP4-01  
**Date Created:** 2026-04-12  
**Author:** Ilyes Hamdi
**Status:** Testing

---

## 1. Objective

Detect suspicious sequences where a user session shows signs of elevated execution followed shortly by persistence mechanisms such as:

- Scheduled task creation
- Registry Run key modification
- New service installation

The goal is to identify post-compromise behavior chains, not isolated events.

---

## 2. Threat Context

**Relevant MITRE ATT&CK Techniques:**

- T1547.001 — Registry Run Keys / Startup Folder
- T1053.005 — Scheduled Task/Job
- T1543.003 — Windows Service Creation
- T1068 — Privilege Escalation

**Threat scenario:**

An attacker gains local execution context, elevates privileges, and establishes persistence to maintain access after reboot or session termination.

**Why this detection matters:**

Single persistence events are often benign. However, when combined with elevated process activity, they strongly indicate post-compromise behavior.

---

## 3. Data Sources

- Sysmon Event Log (Microsoft-Windows-Sysmon/Operational)
- Windows Security Event Log (if available)
- Wazuh agent event channel ingestion

**Required fields:**

- EventID
- User
- ProcessName
- CommandLine
- ParentImage
- TargetObject (registry)
- Image (service/process)

---

## 4. Detection Logic

**Correlation Logic (conceptual Wazuh rule)**

Trigger when a privilege indicator is detected (Sysmon Event ID 1 — process creation executed with elevated context such as admin tools: cmd.exe, powershell.exe, etc.) AND within 10 minutes one or more persistence actions occur:

- Sysmon Event ID 13 → Registry Run Key modification
- Event ID 1 → schtasks.exe execution (scheduled task creation)
- Event ID 1 or System log → service creation (sc.exe create or Event 7045)

**Logical Rule Structure (pseudo)**

IF:

    (Process Creation detected with admin context)

AND
(Registry Run Key modification OR Scheduled Task creation OR Service creation)
WITHIN 10 minutes
THEN:

    Alert = "Post-Exploitation Privilege + Persistence Chain Detected"

**Thresholds**

- Time window: 10 minutes
- Minimum events: 2 distinct event types
- Scope: single host, same user session

---

## 5. Testing Procedure

**Steps performed (simulation):**

1. Simulated elevated command prompt execution (e.g., `whoami /priv`).
2. Created scheduled task:
   - `schtasks /create /tn "UpdateCheckTask"`.
3. Modified registry Run key:
   - `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` (add `FakeApp`).
4. Created service:
   - `sc create FakeUpdaterService`.

**Expected behavior:**

- Sysmon Event ID 1 logs process execution
- Sysmon Event ID 13 logs registry modification
- Wazuh correlates events into a single alert

**Actual result:**

- Sysmon generated process and persistence logs as expected
- Wazuh ingested persistence events
- Correlation alert triggered in dashboard (assuming rule implemented)

---

## 6. False Positive Analysis

**Legitimate activities that may trigger this rule:**

- IT administrators deploying software
- System updates creating scheduled tasks
- Enterprise software installing services
- User customization of startup applications

**Noise level:**

- Medium in enterprise environments, low in controlled lab environments

**Mitigation strategies:**

- Exclude known admin accounts from hitting this rule
- Whitelist trusted service or installer paths (e.g., Windows Update, Defender)
- Filter signed Microsoft binaries where appropriate

---

## 7. Tuning Adjustments

After testing, recommended improvements:

- Increase time window from 10 → 15 minutes in noisy environments
- Add filter for: `Image != "msiexec.exe"` (optional tuning)
- Restrict rule to non-system users
- Add severity scaling:
  - 2 events = Medium
  - 3+ events = High confidence alert

---

## 8. Limitations

- Requires Sysmon deployment (native Windows logs alone are insufficient)
- Cannot reliably detect privilege escalation root cause by itself
- Time-based correlation may miss slow-moving attackers
- Potential for false positives in admin-heavy environments

---

## 9. Related Incidents or Hunts

- IR-2026-04-STEP4-01: Privilege Escalation + Persistence Simulation
- Threat hunt: Registry Run Key persistence patterns
- Threat hunt: Service creation anomalies post-process execution

---

_Prepared by SOC-Lab Analyst — testing and tuning in progress._
