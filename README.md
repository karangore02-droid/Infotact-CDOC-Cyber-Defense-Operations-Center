# 🛡️ Infotact CDOC – Cyber Defense Operations Center

This repository contains two enterprise-grade cybersecurity infrastructure projects developed as part of the Infotact CDOC program.

The objective is to design, deploy, and validate a secure, production-ready Cyber Defense Operations Center using industry-standard open-source tools.

---

# 📌 Projects Overview

## 🔐 Project 1: Centralized Zero Trust Identity Provider
**Technology:** Keycloak  
**Domain:** Identity & Access Management (IAM)

A production-ready Identity Provider implementing:
- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- Conditional Access Policies
- Role-Based Access Control (RBAC)
- OpenID Connect (OIDC)
- Federated Identity (Google Workspace)

📂 Folder: `/Project-1-IAM-Keycloak`

---

## 🛡️ Project 2: Enterprise EDR & Threat Hunting Grid
**Technology Stack:** Wazuh, Sysmon, MITRE ATT&CK, Atomic Red Team  
**Domain:** Endpoint Detection & Response (EDR)

A centralized detection and response system capable of:
- File Integrity Monitoring (FIM)
- Threat Detection & Custom Rule Engineering
- MITRE ATT&CK Mapping
- Automated Active Response (Firewall Drop)
- Threat Simulation & Kill Chain Visualization

📂 Folder: `/Project-2-EDR-Wazuh`

---

# 🏗️ Architecture Overview

The CDOC architecture is divided into two security layers:

## 1️⃣ Identity Layer (Access Control)
- Keycloak (Dockerized)
- PostgreSQL Backend
- OIDC Client Integration
- Conditional MFA Enforcement

## 2️⃣ Detection & Response Layer
- Wazuh Manager (Linux Server)
- Wazuh Agents (Windows + Linux)
- Sysmon (Deep Windows Telemetry)
- Suricata (Network IDS/IPS)
- Kibana / OpenSearch Dashboard

---

# 📆 Project Timeline Structure

Each project is executed over 4 structured weeks.

---

# 🔐 Project 1 – IAM (Keycloak)

## Week 1 – Infrastructure Deployment
- Deploy Keycloak (Docker)
- Configure PostgreSQL backend
- Create Realm
- Define Roles (Admin, Developer, Viewer)
- Secure Admin Console

## Week 2 – Application Integration
- Register OIDC Client
- Integrate Flask/Express Application
- Validate SSO Flow

## Week 3 – Advanced Policies
- Implement Conditional MFA
- Configure RBAC policies
- Inspect JWT tokens for claims validation

## Week 4 – Auditing & Hardening
- Enable Event Logging
- Customize Login Theme
- Perform Security Testing (Session Fixation / Redirect Checks)

---

# 🛡️ Project 2 – EDR & Threat Hunting Grid

## Week 1 – Infrastructure & Agent Deployment
- Deploy Wazuh Manager
- Deploy Agents (Windows & Linux)
- Install Sysmon
- Verify agent heartbeat & logs

## Week 2 – Detection Engineering
- Configure File Integrity Monitoring (FIM)
- Write Custom Rules & Decoders
- Enable Vulnerability Detection

## Week 3 – Active Response (IPS)
- Configure automated response scripts
- Simulate SSH brute force (Hydra)
- Auto-ban attacker IP via firewall-drop

## Week 4 – Threat Simulation
- Execute Atomic Red Team tests
- Map detections to MITRE ATT&CK
- Visualize Kill Chain in dashboard

---

# 🔍 Key Technologies Used

| Category | Tools |
|----------|--------|
| IAM | Keycloak, OIDC, OAuth2 |
| Backend | PostgreSQL |
| EDR | Wazuh |
| Telemetry | Sysmon |
| IDS/IPS | Suricata |
| Threat Simulation | Atomic Red Team |
| Framework | MITRE ATT&CK |
| Visualization | Kibana / OpenSearch |

---

# 🎯 Objectives Achieved

- Centralized Identity Control
- Elimination of Password Sprawl
- Zero Trust Access Enforcement
- Real-Time File Integrity Monitoring
- Automated Incident Response
- Threat Intelligence Mapping
- Blue Team Simulation & Validation

---

# 🚀 How to Use This Repository

Each project folder contains:
- Deployment guide
- Configuration files
- Screenshots
- Validation steps
- Gate check documentation

Refer to individual project folders for detailed setup instructions.

---

# 👨‍💻 Author
~artfield0
~JoshiNirmi-28
~nishita1127
~khandelwalakshita72-ai
~karangore02-droid

– Infotact Internship  
Specialization: Identity Security & Detection Engineering

---

# 📌 Status

✔ Project 1 – Completed  
✔ Project 2 – Completed  
🔄 Continuous Improvement & Hardening Ongoing
