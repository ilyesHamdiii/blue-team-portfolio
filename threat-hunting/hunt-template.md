# Threat Hunting Report: <Hunt Title>

**Hunt ID:** TH-YYYY-XX  
**Date Conducted:** YYYY-MM-DD  
**Analyst:** <Your Name>  
**Status:** Completed / Ongoing

---

## 1. Objective

Clearly define the purpose of the hunt.

Example:

- Identify potential misuse of PowerShell for lateral movement.
- Detect abnormal outbound network connections.
- Search for persistence mechanisms not covered by existing alerts.

This section must state _why_ the hunt is being performed.

---

## 2. Hypothesis

Formulate a clear, testable statement.

Example:
"If an attacker uses PowerShell for lateral movement, anomalous process creation events will appear in Sysmon logs with encoded command arguments."

The hypothesis should guide your query logic.

---

## 3. Data Sources

List all telemetry used:

- Windows Security Logs
- Sysmon
- Linux auth logs
- Network logs
- SIEM index names (if applicable)

---

## 4. Methodology

Describe:

- Queries executed
- Filters applied
- Time range analyzed
- Baseline comparison (if any)

Explain how you reduced noise and validated findings.

---

## 5. Observations

Document what was found.

- Suspicious patterns?
- Normal baseline behavior?
- Outliers?

If no suspicious activity was found, state that clearly.

---

## 6. Analysis

Interpret observations.

- Does the data support or refute the hypothesis?
- Could findings be benign?
- What alternative explanations exist?

Avoid assumptions without log support.

---

## 7. Conclusion

State outcome:

- Hypothesis supported
- Hypothesis partially supported
- Hypothesis not supported

Briefly summarize impact.

---

## 8. Recommendations

- Improve logging?
- Create new detection rule?
- Adjust thresholds?
- Continue monitoring?

---

## 9. Limitations

- Telemetry gaps
- Lab constraints
- Limited time window
- No external visibility

Documenting limitations increases credibility.
