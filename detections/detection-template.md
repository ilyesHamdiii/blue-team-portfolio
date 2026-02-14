# Detection Rule: <Rule Name>

**Detection ID:** DET-YYYY-XX  
**Date Created:** YYYY-MM-DD  
**Author:** <Your Name>  
**Status:** Active / Testing / Tuned

---

## 1. Objective

Describe what behavior this rule aims to detect.

Example:
Detect repeated failed authentication attempts indicative of brute-force activity.

---

## 2. Threat Context

- Relevant MITRE ATT&CK Technique:
- Threat scenario:
- Why this detection matters:

Keep this concise and factual.

---

## 3. Data Sources

- Log types used
- Required fields
- SIEM index or source

---

## 4. Detection Logic

Describe:

- Query or rule logic
- Thresholds
- Time window
- Conditions

Explain why the thresholds were selected.

---

## 5. Testing Procedure

- How the behavior was simulated
- What logs were generated
- Expected vs actual alert behavior

---

## 6. False Positive Analysis

- Legitimate activities that may trigger this rule
- Frequency of benign triggers
- Mitigation strategies

This section is critical. SOC leads care about noise.

---

## 7. Tuning Adjustments

Document refinements made after testing:

- Threshold changes
- Field filters
- Host exclusions (if justified)

---

## 8. Limitations

- Evasion possibilities
- Log dependencies
- Blind spots

---

## 9. Related Incidents or Hunts

Reference:

- Incident reports
- Threat hunts that informed this detection
