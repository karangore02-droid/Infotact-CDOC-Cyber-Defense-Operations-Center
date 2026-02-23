Week 1 – Identity Infrastructure
Project

Centralized Zero Trust Identity Provider (IAM)

Objective

Deploy and configure a containerized Identity Infrastructure using:

Keycloak

PostgreSQL

Docker

The goal was to establish a functional authentication and authorization foundation for Zero Trust architecture.

1. Environment Preparation

Operating System: Kali Linux

Docker Installation
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
Docker Compose Installation
sudo apt install docker-compose -y
Docker Permission Configuration
sudo usermod -aG docker $USER
newgrp docker
2. Architecture Overview

Components:

Keycloak (Identity Provider)

PostgreSQL 15 (Database)

Custom Docker Network (keycloak-net)

Persistent Docker Volume (pgdata)

Flow:

User → Keycloak → PostgreSQL (store realm & user data)

3. Docker Compose Configuration

Services:

postgres:15

quay.io/keycloak/keycloak:24.0.1

Keycloak started in development mode using:

command: start-dev

Port Mapping:

8080 → 8080
4. Deployment
docker-compose up -d

Verification:

docker ps
docker logs keycloak

Admin Console:

http://localhost:8080/admin
5. Identity Configuration
Realm Created

Infotact

Roles Created

Admin

Developer

Viewer

Groups Created

Admin_Group

Dev_Group

Viewer_Group

Role-to-Group mapping implemented.

6. Test User

Username: devuser
Password: user123

User assigned to Dev_Group.

Login URL:

http://localhost:8080/realms/Infotact/account
7. Outcome

Functional Identity Provider deployed

Role-Based Access Control configured

User onboarding tested successfully

Foundation ready for application integration (Week 2)

8. Lessons Learned

Docker containers persist independently of compose files

Proper directory structuring is critical before version control

Volume persistence must be handled carefully

Development mode should not be used in production
