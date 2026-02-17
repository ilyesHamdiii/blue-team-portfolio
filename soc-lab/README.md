# SOC Home Lab — Foundation Project

## Project Objective

The goal of this lab is to build a functional Security Operations Center (SOC) environment capable of ingesting logs from Windows and Linux endpoints, generating alerts, and demonstrating endpoint monitoring. This project simulates a mini-SOC workflow, allowing for log collection, detection, and alert validation using Wazuh and Sysmon.

---

## Architecture Diagram

+----------------+ +------------+ +---------------------------+ +------------------+
| Windows VM | -----> | Wazuh Agent| -----> | Ubuntu Server (Wazuh | -----> | Wazuh Dashboard |
| (Sysmon logs) | | | | Manager + Elasticsearch) | | |
+----------------+ +------------+ +---------------------------+ +------------------+

## Environment Setup

- **Ubuntu Server:** 22.04 LTS
- **Windows VM:** Windows 10/11
- **Network Configuration:**
  - Adapter 1: Internal Network (`SOC-LAB`) for VM-to-VM communication
  - Adapter 2: NAT for internet access
- **Static IPs:**
  - Ubuntu Server: `192.168.100.10`
  - Windows VM: `192.168.100.20`

---

## Tools and Versions

- **Wazuh Manager:** 4.7.5
- **Wazuh Agent:** 4.7.5 (Windows)
- **Sysmon:** 14.50 (Microsoft Sysinternals)
- **Elasticsearch / Kibana:** 8.9.0

---

## Configuration Files

All configuration files are located in the `config/` folder:

- `sysmonconfig-export.xml` — Windows Sysmon configuration
- `local_rules.xml` — Custom Wazuh detection rules
- ossec.conf` snippet showing log collection configuration

Note: The provided `sysmonconfig-export.xml` is based on the community Sysmon configuration "SwiftonSecurity" (SwiftOnSecurity) and may be tuned further for your environment.

---

## Detection Scenarios

The lab demonstrates the following detection cases:

1. **PowerShell spawning cmd.exe**
   - Event monitored: Sysmon Event ID 1 (Process Creation)
   - Detection: Wazuh custom rule triggers an alert when `powershell.exe` spawns `cmd.exe`.
   - Purpose: Demonstrates detection of potentially suspicious activity and rule logic implementation.

2. **Network activity / suspicious connections**
   - Event monitored: Sysmon Event ID 3 (Network Connection)
   - Detection: Captures and alerts on abnormal outbound connections from endpoints.

---

## Screenshots

Include the following screenshots in the `screenshots/` folder:

1. `network_config.png` — VirtualBox adapter settings for Ubuntu and Windows
2. `wazuh_services.png` — Ubuntu showing Wazuh services running (`systemctl status`)
3. `agent_active.png` — Wazuh dashboard showing Windows agent active
4. `raw_sysmon_event.png` — Raw Sysmon event (Event ID 1) in dashboard Discover
5. `custom_alert.png` — Alert triggered by custom rule
6. `architecture-diagram.png` — Lab architecture / log flow diagram

---

## Lessons Learned / Next Steps

- Proper network configuration is critical for log ingestion.
- Understanding Sysmon event fields (`Image`, `ParentImage`, `CommandLine`) is essential for rule creation.
- Next steps for lab improvement:
  - Tune alert noise and severity levels
  - Add Linux endpoints for broader log coverage
  - Map alerts to MITRE ATT&CK framework for portfolio demonstration
  - Create additional custom detection rules for real-world scenarios
