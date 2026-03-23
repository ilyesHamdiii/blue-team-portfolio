Detection Rule: Suspicious PowerShell Execution

Detection ID: DET-2026-02

Date Created: 2026-02-18

Author: Ilyes HAMDI

Status: Active

## 1. Objective

Detect encoded or suspicious PowerShell executions indicative of potential malware or unauthorized system access attempts.

## 2. Threat Context

MITRE ATT&CK: T1059.001 – PowerShell

Scenario: An attacker runs encoded PowerShell commands to evade detection

Importance: Early detection prevents unauthorized command execution and potential lateral movement

## 3. Data Sources

- Windows PowerShell Operational log (Microsoft-Windows-PowerShell/Operational)
- Event IDs: 4104 (Script Block Logging), 4688 (Process Creation)
- Wazuh agent → SIEM dashboard

## 4. Detection Logic

Alert when:

- Event ID 4104 OR 4688
- powershell.exe is executed with -EncodedCommand or other suspicious parameters
- Threshold: single execution triggers alert in lab scenario
- Severity: Medium

Rationale: Encoded commands are rarely used by normal users; single-event detection is sufficient in lab/testing context.

## 5. Testing Procedure

- Controlled execution of encoded PowerShell commands
- Verified ingestion in Wazuh logs
- Confirmed alert triggers in SIEM

## 6. False Positive Analysis

Potential triggers: legitimate admin scripts using encoded commands

Mitigation:

- Exclude known admin accounts or service scripts
- Review alert before escalation

## 7. Tuning Adjustments

- No tuning needed for lab scenario
- In production: consider excluding safe modules, increasing threshold for repeated executions

```powreshell
<group name="windows,powershell,suspicious">
  <rule id="100201" level="10">
    <if_sid>18109</if_sid> <!-- Script Block Logging -->
    <description>Suspicious PowerShell command execution detected</description>
    <mitre>
      <id>T1059.001</id>
    </mitre>
  </rule>
</group>
```

## 8. Limitations

- Only captures PowerShell executed on the monitored host
- Cannot detect obfuscated attacks outside of logging scope
- Windows Home has limited GPO control; relies on registry logging

## 9. Related Incidents or Hunts

Incident Report: IR-2026-02 – Suspicious PowerShell Execution (lab simulation)
