# 🔐 Week 3 – Advanced Policies (RBAC + MFA)

![Keycloak](https://img.shields.io/badge/Keycloak-24-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![Security](https://img.shields.io/badge/Security-ZeroTrust-green)
![MFA](https://img.shields.io/badge/Auth-MFA-orange)
![JWT](https://img.shields.io/badge/Auth-JWT-yellow)

---

# 📌 Overview

Week 3 focuses on implementing **advanced authentication and authorization policies** within the Zero Trust Identity Provider architecture.

This phase builds upon the infrastructure from previous weeks and introduces:

• **Role-Based Access Control (RBAC)**  
• **Group-based Authorization**  
• **JWT Token Claim Inspection**  
• **Multi-Factor Authentication (MFA)**  

The goal is to ensure that **roles and groups are properly propagated inside access tokens** and verified by the protected application.

---

# 🏗 Architecture

```
User
  │
  ▼
Flask Application (Protected Resource)
  │
  ▼
Keycloak Identity Provider
  │
  ├── Realm: infotact
  │
  ├── Roles
  │     ├── admin
  │     ├── developer
  │     └── viewer
  │
  ├── Groups
  │     ├── engineering
  │
  ├── Authentication Flow
  │     ├── Username / Password
  │     └── OTP (MFA)
  │
  ▼
PostgreSQL Identity Database
```

---

# 🔑 Features Implemented

## 1️⃣ Role-Based Access Control (RBAC)

Realm roles were created to enforce authorization.

```
admin
developer
viewer
```

Users are granted roles through **group membership** or direct role assignment.

---

## 2️⃣ Group-Based Authorization

Groups represent organizational structure.

```
engineering
```

Example membership:

```
testuser → /engineering
```

Groups are mapped into the **JWT token claims** using a **Group Membership mapper**.

---

## 3️⃣ JWT Claim Inspection

The Flask application includes a debugging endpoint to inspect the issued access token.

```
/token
```

The endpoint decodes the JWT and verifies that all required claims exist.

Example decoded token:

```
{
 "preferred_username": "testuser",
 "realm_access": {
   "roles": ["admin"]
 },
 "groups": ["/engineering"],
 "email": "test@infotact.local"
}
```

This confirms that **roles and groups are successfully propagated from Keycloak to the application**.

---

## 4️⃣ Multi-Factor Authentication (MFA)

MFA was enabled using **Time-based One-Time Password (TOTP)**.

Authentication flow:

```
Username + Password
        │
        ▼
OTP Verification (Authenticator App)
        │
        ▼
Access Granted
```

Supported authenticator applications:

```
Google Authenticator
Microsoft Authenticator
FreeOTP
```

Users are required to scan a QR code during the initial login to register their device.

---

# 📂 Project Structure

```
Week-3-Advanced-Policies
│
├── docker-compose.yml
│
├── flask-app-rbac-mfa
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── screenshots
│
└── README.md
```

---

# 🚀 Running the Project

Start the services using Docker.

```
docker compose up --build
```

Services launched:

```
Keycloak Identity Provider
PostgreSQL Database
Flask Protected Application
```

---

# 🔐 Authentication Flow

```
User → Flask App → Keycloak Login
                     │
                     ▼
            Username + Password
                     │
                     ▼
               OTP Challenge
                     │
                     ▼
               JWT Issued
                     │
                     ▼
              Access Granted
```

---

# 🧪 Testing

Login using:

```
http://localhost:5000
```

After authentication, the protected page will display the authenticated user.

```
Welcome testuser
Role: admin
```

To inspect the token:

```
http://localhost:5000/token
```

---

# 📸 Screenshots

Screenshots captured during testing include:

```
OTP QR Code Setup
OTP Login Challenge
Protected Resource Access
Decoded JWT Token
Keycloak Role Configuration
Keycloak Group Configuration
```

These are stored inside:

```
screenshots/
```

---

# 🎯 Week 3 Gate Check

The objective for Week 3 is satisfied when:

```
✔ Access token successfully decoded
✔ Roles appear inside JWT claims
✔ Groups appear inside JWT claims
✔ MFA enforced during authentication
```

All requirements have been successfully implemented and verified.

---

# 📚 Technologies Used

```
Keycloak 24
Docker
PostgreSQL
Flask
OpenID Connect
JWT
TOTP Authentication
```

---

# 🔒 Security Concepts Demonstrated

```
Zero Trust Identity Architecture
Role-Based Access Control
Group-Based Authorization
JWT Claim Verification
Multi-Factor Authentication
```

---

# 📌 Next Phase

Week 4 will focus on:

```
Security auditing
Identity provider hardening
Token security improvements
Authentication policy tuning
```

---

# 👨‍💻 Author

Project: **Centralized Zero Trust Identity Provider**

Cybersecurity Architecture Lab

```
