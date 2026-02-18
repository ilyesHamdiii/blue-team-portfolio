Detection Rule: Windows Brute-Force Authentication Attempt

Detection ID: DET-2026-01

Date Created: 2026-02-18

Author: Ilyes HAMDI

Status: Active

## 1. Objective

Detect repeated failed Windows authentication attempts within a short time window that may indicate brute-force password guessing activity.

The rule focuses on identifying rapid authentication failures targeting a single user account.

## 2. Threat Context

Relevant MITRE ATT&CK Technique: T1110 – Brute Force

Threat scenario: An attacker attempts multiple password guesses against a user account to gain unauthorized access.

Why this detection matters: Brute-force attempts are a common initial access vector. Early detection reduces the likelihood of account compromise and lateral movement.

This rule addresses password guessing rather than credential stuffing or distributed password spraying (unless extended).

## 3. Data Sources

Log types used:

- Windows Security Log

Required fields:

- Event ID
- TargetUserName
- LogonType
- Timestamp
- Hostname

SIEM source:

Wazuh agent → Wazuh manager → SIEM dashboard

Relevant Event IDs:

- 4625 – Failed logon
- 4624 – Successful logon (contextual correlation)

## 4. Detection Logic

Core Logic

Trigger alert when:

- Event ID = 4625
- ≥ 5 occurrences
- Same TargetUserName
- Within 300 seconds (5 minutes)

Example Wazuh Rule

```xml
<group name="windows,authentication,bruteforce">
	<rule id="100101" level="10">
		<if_sid>18107</if_sid>
		<frequency>5</frequency>
		<timeframe>300</timeframe>
		<description>Multiple failed login attempts detected (possible brute force)</description>
		<mitre>
			<id>T1110</id>
		</mitre>
	</rule>
</group>
```

Threshold Rationale

5 attempts is sufficient to indicate abnormal behavior in a short window.

5-minute window captures rapid brute-force activity while limiting noise from occasional user error.

Thresholds are adjustable depending on environment size and password policy.

## 5. Testing Procedure

Simulation Method

Created test account: `ANGRY-BOB`

Generated 5 consecutive failed login attempts.

Performed 1 successful login immediately after.

Logs Generated

Multiple Event ID 4625 entries.

One Event ID 4624 entry.

Expected Behavior

Alert triggered after fifth failed attempt.

Alert visible in SIEM dashboard.

Actual Behavior

Alert triggered as configured.

Events correctly correlated within defined timeframe.

No unexpected alert noise observed during testing.

## 6. False Positive Analysis

Potential Legitimate Triggers

User mistyping password multiple times.

Service account with outdated credentials.

Automated script attempting authentication with wrong password.

Likelihood of Benign Triggers

In small environments, user typing errors are the most common benign cause. However, 5 failures within 5 minutes remains relatively uncommon for normal behavior.

Mitigation Strategies

Exclude known service accounts if necessary.

Increase threshold to 7–10 attempts in high-noise environments.

Correlate with successful login to raise severity rather than generate standalone alerts.

## 7. Tuning Adjustments

After testing:

Confirmed 5 attempts produced minimal noise in lab.

No exclusions required in current environment.

Severity left at Medium by default.

Future production tuning may include:

Filtering specific LogonType values.

Increasing threshold for high-volume environments.

Escalating severity if 4624 follows repeated 4625 events.

## 8. Limitations

Does not detect slow brute-force attempts spread over long periods.

Cannot detect distributed password spraying across multiple hosts without correlation logic.

Depends entirely on Windows Security logging being enabled.

Does not evaluate password complexity or account lockout policy.

This rule detects pattern frequency, not intent.

## 9. Related Incidents or Hunts

Related Incident Report: IR-2026-01 – Brute-Force Authentication Attempt (Lab Simulation)

This detection was derived directly from controlled simulation and validated through documented incident response workflow.
