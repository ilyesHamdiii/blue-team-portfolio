# Honeypot Intelligence Collector

## Overview

The **Honeypot Intelligence Collector** is a lightweight security data pipeline that transforms raw honeypot logs into structured and actionable threat intelligence.

Instead of only deploying a honeypot, this project focuses on **post-collection processing**, converting unstructured attacker activity into analyzable security telemetry.

---

## Objective

To demonstrate how raw attacker interactions can be:

* Ingested from honeypot logs
* Parsed into structured data
* Normalized into a consistent schema
* Analyzed to extract meaningful intelligence

---

## Architecture

```
Honeypot (Cowrie)
        ↓
Raw Logs (JSON / text)
        ↓
Parser (Python)
        ↓
Normalized Data (JSON)
        ↓
Analysis Engine
        ↓
Threat Intelligence Output
```

---

## Features

* Log ingestion from honeypot output
* JSON parsing and normalization
* Extraction of key attacker attributes:

  * Source IP
  * Username attempts
  * Password attempts
  * Commands executed
* Aggregated intelligence generation:

  * Top attacking IPs
  * Most targeted usernames
  * Most used passwords
  * Event frequency

---

## Project Structure

```
honeypot-intelligence-collector/
│── README.md
│── requirements.txt
│
├── sample_logs/
│   └── cowrie.log
│
├── parser/
│   └── parser.py
│
├── analysis/
│   └── summarize.py
│
├── output/
│   ├── parsed.json
│   └── summary.txt
│
└── screenshots/
```

---

## Data Schema

Example normalized event:

```json
{
  "timestamp": "2024-01-01T12:00:00",
  "source_ip": "192.168.1.10",
  "username": "root",
  "password": "123456",
  "event_type": "cowrie.login.failed",
  "command": null
}
```

---

## Usage

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 2. Run parser

```bash
python parser/parser.py
```

---

### 3. Run analysis

```bash
python analysis/summarize.py
```

---

## Example Output

```
Top IPs:
[('192.168.1.10', 25), ('10.0.0.5', 18)]

Top Usernames:
[('root', 40), ('admin', 22)]

Top Passwords:
[('123456', 35), ('password', 20)]
```

---

## Skills Demonstrated

* Log parsing and data ingestion
* Data normalization and schema design
* Security telemetry handling
* Basic threat intelligence analysis
* Python scripting for security automation

---

## Limitations

* Uses offline sample logs (no live ingestion pipeline)
* No enrichment (e.g., GeoIP, ASN)
* Limited to basic statistical analysis

---

## Future Improvements

* Real-time log streaming pipeline
* GeoIP enrichment of attacker IPs
* Session-based attack reconstruction
* Integration with SIEM platforms
* Visualization dashboard

---

## Conclusion

This project demonstrates how raw honeypot data can be transformed into structured intelligence, simulating a simplified detection engineering workflow commonly used in SOC environments.

---
