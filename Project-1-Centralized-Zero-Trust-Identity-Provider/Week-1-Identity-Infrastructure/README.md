# 🔐 Project 1 – Centralized Zero Trust Identity Provider  
## Week 1 – Infrastructure Deployment

Part of the **Infotact CDOC – Cyber Defense Operations Center**

This phase establishes the foundational Identity Infrastructure required for a Zero Trust architecture.

---

# 🎯 Objective

Deploy a production-structured Identity Provider using:

- Keycloak (Identity & Access Management)
- PostgreSQL (Relational Database Backend)
- Docker (Containerization Platform)

The goal of Week 1 was to build a secure, containerized IAM foundation ready for application integration in Week 2.

---

# 🏗️ Infrastructure Architecture

## Identity Layer Components

- Keycloak Server (Dockerized)
- PostgreSQL 15 Backend
- Dedicated Docker Network (`keycloak-net`)
- Persistent Docker Volume (`pgdata`)

### Logical Flow

User → Keycloak (Authentication & Authorization) → PostgreSQL (Data Persistence)

---

# ⚙️ Environment Preparation

Operating System: Kali Linux

### Docker Installation

```bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
```

### Docker Compose Installation

```bash
sudo apt install docker-compose -y
```

### Docker Permission Configuration

```bash
sudo usermod -aG docker $USER
newgrp docker
```

---

# 🐳 Docker Compose Configuration

Services Deployed:

- postgres:15
- quay.io/keycloak/keycloak:24.0.1

Keycloak launched in development mode:

```yaml
command: start-dev
```

Port Mapping:

```yaml
8080 → 8080
```

---

# 🚀 Deployment Execution

```bash
docker-compose up -d
```

Verification:

```bash
docker ps
docker logs keycloak
```

Admin Console:

```
http://localhost:8080/admin
```

---

# 🔑 Identity Configuration

## Realm Created
Infotact

## Roles Defined
- Admin
- Developer
- Viewer

## Groups Created
- Admin_Group
- Dev_Group
- Viewer_Group

Role-to-group mappings enforced for structured access control.

---

# 👤 Test User Validation

User Created:
- Username: devuser
- Group: /Dev_Group
- Email verification enabled
- Permanent password configured

Login URL:

```
http://localhost:8080/realms/Infotact/account
```

Authentication and profile update flow validated successfully.

---

# 🛡️ Security Considerations (Week 1 Scope)

- Container isolation via Docker network
- Database credentials configured via environment variables
- Persistent volume for data durability
- Development mode clearly identified (not production-ready)

---

# 📊 Outcome

✔ Functional Identity Provider deployed  
✔ Role-Based Access Control structure implemented  
✔ User onboarding validated  
✔ Infrastructure prepared for OIDC application integration  

Week 1 establishes the Identity foundation for:

- Single Sign-On (SSO)
- Conditional Access Policies
- Multi-Factor Authentication (MFA)
- Advanced Policy Engineering (Week 3)
- Auditing & Hardening (Week 4)

---

# 🚀 Next Phase

➡ Week 2 – Application Integration  
OIDC Client registration and protected application integration.
