# ELK Stack Based Security Information and Event Management (SIEM) Dashboard

## Project Overview

The ELK Stack Based SIEM Dashboard is a cybersecurity project that demonstrates how Security Information and Event Management (SIEM) systems collect, process, store, and visualize log data.

This project uses:

- Elasticsearch
- Logstash
- Kibana
- Docker Compose

Logstash collects and parses web server logs, Elasticsearch stores the processed data, and Kibana provides interactive dashboards for monitoring and analysis.

---

# Features

- Centralized log collection
- Log parsing using Grok filters
- Elasticsearch indexing
- Kibana dashboards
- Docker-based deployment
- HTTP Status Code Analysis
- Top Client IP Monitoring
- HTTP Method Analysis
- Most Requested URLs
- Requests Over Time Visualization

---

# Technologies Used

| Technology | Version |
|------------|----------|
| Docker Desktop | Latest |
| Docker Compose | Latest |
| Elasticsearch | 8.15 |
| Logstash | 8.15 |
| Kibana | 8.15 |
| Visual Studio Code | Latest |
| Windows | 11 |

---

# Project Structure

```
project/
│
├── docker-compose.yml
│
├── sample_logs/
│   ├── access.log
│   └── auth.log
│
├── logstash/
│   └── pipeline/
│       └── logstash.conf
│
└── README.md
```

---

# Architecture

```
               Sample Logs
                    │
                    ▼
              Logstash Pipeline
                    │
                    ▼
              Elasticsearch
                    │
                    ▼
                 Kibana
                    │
                    ▼
            SIEM Dashboard
```

---

# System Requirements

## Hardware

- Intel Core i5 or above
- Minimum 8 GB RAM
- 20 GB Free Storage

Recommended:

- Intel Core i7
- 16 GB RAM
- SSD Storage

---

## Software

- Windows 11
- Docker Desktop
- Visual Studio Code

---

# Installation

## Step 1

Clone the repository

```
git clone https://github.com/yourusername/elk-siem-dashboard.git
```

or download the ZIP.

---

## Step 2

Open the project in VS Code.

---

## Step 3

Start Docker Desktop.

Wait until Docker is running.

---

## Step 4

Open Terminal.

Run

```
docker compose up -d
```

---

## Step 5

Check containers

```
docker ps
```

Expected Containers

- elasticsearch
- logstash
- kibana

---

# Access Services

## Elasticsearch

```
http://localhost:9200
```

---

## Kibana

```
http://localhost:5601
```

---

# Logstash Pipeline

The Logstash configuration performs three stages.

## Input

Reads

```
sample_logs/access.log
```

---

## Filter

Uses Grok patterns to extract

- Client IP
- Timestamp
- HTTP Method
- URL
- Status Code
- Bytes

---

## Output

Stores parsed events into

```
web-logs
```

Elasticsearch index.

---

# Creating Kibana Data View

Open Kibana

Go to

```
Stack Management
```

↓

```
Data Views
```

↓

Create Data View

Name

```
web-logs
```

Time Field

```
@timestamp
```

---

# Dashboard Visualizations

The dashboard contains:

- Requests Over Time
- HTTP Status Codes
- Top Client IPs
- HTTP Methods
- Most Requested URLs

---

# Running the Project

Start

```
docker compose up -d
```

Stop

```
docker compose down
```

Restart Logstash

```
docker compose restart logstash
```

Restart Everything

```
docker compose down

docker compose up -d
```

---

# Useful Docker Commands

View Containers

```
docker ps
```

View Logs

```
docker logs logstash
```

Restart Elasticsearch

```
docker compose restart elasticsearch
```

Restart Kibana

```
docker compose restart kibana
```

Remove Containers

```
docker compose down
```

Remove Containers + Volumes

```
docker compose down -v
```

---

# Testing

| Test | Result |
|------|--------|
| Docker Containers Running | Passed |
| Elasticsearch Accessible | Passed |
| Kibana Accessible | Passed |
| Logstash Parsing Logs | Passed |
| Dashboard Working | Passed |
| Indexed Documents Available | Passed |

---

# Advantages

- Open-source SIEM
- Easy deployment
- Fast search engine
- Powerful dashboards
- Scalable architecture
- Beginner friendly
- Docker containerized

---

# Limitations

- Uses sample logs
- No real-time alerting
- No IDS integration
- No machine learning
- Educational project only

---

# Future Improvements

- Filebeat Integration
- Winlogbeat Integration
- Suricata IDS
- Snort IDS
- Email Alerts
- Elastic Security
- Threat Intelligence
- Machine Learning
- SOC Automation
- MITRE ATT&CK Mapping

---

# Learning Outcomes

This project demonstrates:

- Docker
- ELK Stack
- SIEM Fundamentals
- Log Management
- Security Monitoring
- Kibana Dashboard Creation
- Elasticsearch Indexing
- Logstash Pipelines

---

# Screenshots

Include screenshots of:

- Docker Containers
- Elasticsearch Homepage
- Kibana Homepage
- Discover Page
- SIEM Dashboard
- HTTP Status Visualization
- Top Client IP Visualization
- HTTP Methods
- Requests Over Time
- Most Requested URLs

---

# References

- Elasticsearch Documentation
- Logstash Documentation
- Kibana Documentation
- Docker Documentation
- Elastic Stack Documentation
- OWASP Logging Cheat Sheet
- NIST Cybersecurity Framework

---

# Author

**Gurpreet Singh**

Master of Computer Applications (Cyber Security)

CT University

Academic Session: 2025–2027

---

# License

This project is developed for educational and learning purposes only.

© 2026 Gurpreet Singh