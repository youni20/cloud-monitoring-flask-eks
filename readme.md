# 🌩️ Cloud Monitoring App (Flask + AWS EKS)

A lightweight cloud infrastructure monitoring app built with **Flask**, containerized with **Docker**, and deployed to **Amazon EKS (Elastic Kubernetes Service)**. It provides real-time system metrics like CPU, memory, and disk usage via a simple REST API and web dashboard.

---

## 🔧 Features

- 🔍 View real-time CPU, memory, and disk usage
- 🚨 CPU threshold alerts
- 📦 Dockerized Flask app
- ☸️ Deployed on Kubernetes (EKS)
- 📡 API endpoints for data access

---

## 📁 Project Structure

```

cloud-monitoring-app/
├── app.py                 # Flask app
├── templates/
│   └── index.html         # Dashboard UI
├── Dockerfile             # Container build file
├── requirements.txt       # Python dependencies
├── eks.py                 # (Optional) EKS helper script
├── deployment.yaml        # Kubernetes Deployment config
├── service.yaml           # Kubernetes Service config
└── README.md              # You're here!

```

---

## 🚀 Live Demo (Optional)

> If deployed with a `LoadBalancer`, your app will be available at:

```

http\://<EXTERNAL-IP>:5000/

````

You can also run it locally:

```bash
kubectl port-forward pod/<pod-name> 5000:5000
````

---

## 🐳 Docker

### Build the Docker image:

```bash
docker build -t cloud-monitoring-app .
```

### Run locally:

```bash
docker run -p 5000:5000 cloud-monitoring-app
```

---

## ☸️ Kubernetes (EKS)

### 1. Deploy to EKS

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 2. Check Pod & Service

```bash
kubectl get pods
kubectl get svc
```

To access locally:

```bash
kubectl port-forward pod/<pod-name> 5000:5000
```

Or to expose publicly:

```bash
kubectl patch svc my-flask-service -p '{"spec": {"type": "LoadBalancer"}}'
```

---

## 🧪 API Endpoints

* `/` – Web dashboard (HTML)
* `/api/status` – Full system metrics
* `/api/cpu` – CPU usage only

---

## 🧰 Requirements

* Python 3.8+
* Flask
* psutil
* Docker
* AWS CLI + EKSCTL
* kubectl

---

## 🛡️ Notes

* The app is using Flask's built-in dev server – not recommended for production.
* Consider using **Gunicorn** or **uWSGI** for production deployments.
* This project is intended for learning and demo purposes.

---

## 📄 License

© 2025 Younus Mashoor