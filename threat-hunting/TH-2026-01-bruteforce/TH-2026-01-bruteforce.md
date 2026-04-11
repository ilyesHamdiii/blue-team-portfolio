# Threat Hunting Report: Windows Authentication Brute Force Activity

**Hunt ID:** TH-2026-01

**Date Conducted:** 2026-02-20

**Analyst:** Ilyes HAMDI

**Status:** Completed

## 1. Objective

The purpose of this hunt is to identify potential brute force authentication attempts against Windows systems that may not have triggered existing detection rules.

Previous investigations involved authentication-related events, but detection coverage focused primarily on alert-driven brute-force rules. This hunt aims to proactively determine whether repeated failed login attempts occurred without generating alerts.

## 2. Hypothesis

If an attacker attempts password brute forcing against Windows accounts, a pattern of repeated failed authentication events (Event ID 4625) will be observed from a single source host or against a single user account within a short time window, potentially without triggering an alert.

## 3. Data Sources

- Windows Security Event Logs
- Windows Event ID 4625 (Failed Logon)
- Windows Event ID 4624 (Successful Logon)
- Wazuh alerts index (wazuh-alerts-\*)
- Wazuh archives/raw logs index
- Time range analyzed: Last 7 days

## 4. Methodology

Step 1 — Identify Failed Logon Events

Query executed in Wazuh Discover:

```
event.code:4625
```

Fields examined:

- TargetUserName
- IpAddress / WorkstationName
- LogonType
- FailureReason

Step 2 — Identify High-Frequency Failures

Filtered for:

- Same TargetUserName with repeated failures
- Same source IP generating multiple failures
- Failures within short time windows

Query refinement example:

```
event.code:4625 AND TargetUserName:*
```

Then aggregated by:

- TargetUserName
- source.ip

Step 3 — Check for Successful Logons After Failures

To detect possible password spraying success:

```
event.code:4624 AND TargetUserName:"<suspected_user>"
```

Compared timestamps to see if a successful login followed multiple failures.

Step 4 — Compare Against Alerts

Searched for existing brute-force related alerts:

```
rule.description:*brute*
```

Checked whether repeated failures corresponded to triggered alert rules.

Noise Reduction

- Excluded known lab mis-typed credentials.
- Excluded machine accounts ending with $.
- Focused on LogonType 2 (Interactive) and 10 (RemoteInteractive).
- Ignored isolated single failure events.

## 5. Observations

- 132 total Event ID 4625 entries observed within the selected timeframe.
- Most failures were isolated (1–2 attempts per user).
- One user account showed 9 failed login attempts within a 6-minute window from a single internal IP.
- No corresponding successful Event ID 4624 was observed immediately after those failures.
- Wazuh did not trigger a brute-force alert for this pattern.
- No evidence of password spraying across multiple accounts was observed.

## 6. Analysis

The cluster of 9 failed login attempts within a short timeframe suggests potential brute force behavior; however:

- The source IP was internal.
- No follow-up successful authentication occurred.
- Activity may be attributed to user credential misconfiguration or repeated manual login attempts.
- Because no alert rule was triggered, this suggests that the existing brute-force detection threshold may be higher than the observed activity.

The evidence partially supports the hypothesis that suspicious repeated authentication attempts may occur without triggering alerts. However, the activity does not conclusively indicate malicious intent.

## 7. Conclusion

The hypothesis is partially supported.

Repeated authentication failures consistent with brute force patterns were identified. However, no successful compromise or clear malicious attribution was observed.

Detection coverage may not flag lower-volume brute-force attempts.

## 8. Recommendations

- Review brute-force alert thresholds in Wazuh rules.
- Consider implementing a rule for: ≥5 failed logons within 5 minutes from a single source IP.
- Monitor repeated failures on privileged or service accounts.
- Enable correlation between 4625 clusters followed by 4624 success events.

## 9. Limitations

- Lab environment does not represent enterprise-scale baseline behavior.
- No external network telemetry available.
- Limited 7-day timeframe.
- Possible incomplete logging configuration.
- No account lockout policy analysis included.
