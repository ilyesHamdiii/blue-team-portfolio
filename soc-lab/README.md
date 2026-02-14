# SOC Lab Environment

This folder documents the lab infrastructure used throughout this portfolio.

The environment is intentionally minimal but functional, designed to simulate the core components of a small SOC setup.

---

## Objectives

- Collect endpoint and server logs
- Forward data to a SIEM platform
- Generate alerts for detection testing
- Support incident response and threat hunting exercises

---

## Environment Overview

The lab includes:

- A Windows endpoint with Sysmon enabled
- A Linux server
- A SIEM platform (Wazuh) for log ingestion and alerting

Configuration files and relevant setup notes are stored in the `configs/` directory.

---

## Limitations

This lab does not replicate enterprise-scale infrastructure.  
The purpose is to demonstrate understanding of log flow, alerting logic, and investigative workflows in a controlled environment.
