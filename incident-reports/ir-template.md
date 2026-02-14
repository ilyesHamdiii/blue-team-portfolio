# Incident Report: <Short Incident Title>

**Report ID:** IR-YYYY-XX  
**Date of Detection:** YYYY-MM-DD  
**Analyst:** <Your Name>  
**Severity Level:** Low / Medium / High / Critical  
**Status:** Closed / Monitoring / Escalated

---

## 1. Executive Summary

Brief overview of the incident.

- What was detected?
- Why was it suspicious?
- What was the outcome?

This section should allow a SOC lead to understand the situation in under 30 seconds.

---

## 2. Detection Source

- Detection name or alert rule:
- Data source(s):
- Trigger condition:
- MITRE ATT&CK mapping (if applicable):

Describe how the alert was generated and why it fired.

---

## 3. Environment Context

- Affected host(s):
- User account(s) involved:
- Network segment (if relevant):
- System role (workstation, server, etc.):

Provide necessary operational context.

---

## 4. Timeline of Events

Chronological reconstruction of activity.

| Time (UTC) | Event Description                | Log Source           |
| ---------- | -------------------------------- | -------------------- |
| 10:03:12   | Failed login attempt             | Windows Security Log |
| 10:03:18   | Multiple login attempts detected | SIEM Alert           |
| 10:04:02   | Successful login                 | Windows Security Log |

Only include relevant events.

---

## 5. Investigation and Analysis

Describe:

- What logs were queried
- What patterns were examined
- What anomalies were identified
- What alternative explanations were considered

Document your reasoning clearly.  
Avoid speculation without supporting log evidence.

---

## 6. Findings

Summarize key confirmed facts:

- Confirmed malicious activity? (Yes / No / Inconclusive)
- Scope of impact
- Persistence observed?
- Lateral movement observed?

This section should be precise and evidence-based.

---

## 7. Containment and Response Actions

- Account locked or reset
- Host isolated (if simulated)
- Detection rule adjusted
- Monitoring continued

If no action was required, explain why.

---

## 8. Root Cause (If Determined)

- Weak password policy
- Misconfiguration
- User behavior
- Test activity in lab

If root cause cannot be confirmed, state that explicitly.

---

## 9. Lessons Learned

- Improvements to detection logic
- Logging gaps identified
- Potential monitoring enhancements
- Documentation improvements

This demonstrates growth and analytical maturity.

---

## 10. Limitations

- Missing logs
- Limited telemetry
- Lab constraints
- Inability to verify external activity

This shows professional awareness of investigative boundaries.

---

## 11. Recommendations

Optional but valuable:

- Improve password policy
- Enable additional logging
- Adjust alert thresholds
- Implement network segmentation

Keep recommendations realistic and proportionate.
