# 🚀 Jenkins + Docker CI/CD Pipeline for Flask App

This project demonstrates a CI/CD pipeline using Jenkins and Docker Desktop to build, containerize, and deploy a Flask application.

## 📌 Overview

- Jenkins runs inside a Docker container
- Jenkins communicates with Docker Desktop using `/var/run/docker.sock`
- CI pipeline builds Docker image for Flask app
- CD pipeline deploys the container
- Build ID is passed from upstream to downstream job for dynamic image tagging
- Pipeline error handling tested using `catchError` and `try-catch`

---

## 🐳 Install Docker Desktop on Windows

- Download Docker Desktop
- Open PowerShell as Administrator: 

```
docker desktop start
wsl -l -v  #lists docker-desktop
wsl --shutdown #stops running docker-desktop
wsl --install --no-distribution #if not installed already
wsl --update  #if required**

```

## 🐳 Jenkins Container Setup

```
docker run -d --name jenkins --restart unless-stopped \
  -p 8080:8080 -p 50000:50000 \
  -v jenkins_backup:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -e TZ=Asia/Kolkata \
  jenkins/jenkins:lts
```

## 🔐 Fix Docker Socket Permissions

```
docker exec -u root -it jenkins chmod 666 /var/run/docker.sock
```

## 🐳 Install Docker CLI inside Jenkins container

```
docker exec -u root -it jenkins bash -lc \
'curl -fsSL https://get.docker.com -o get-docker.sh && sh get-docker.sh'
```

## 🔍 Verify Docker Inside Jenkins

```
docker exec -it jenkins bash -lc 'docker version && docker ps'
```

## 🌐 Access Application

```
http://localhost:9045
```
