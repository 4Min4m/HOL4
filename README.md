# Hello DevOps Project

## 🛠 Prerequisites
- Python 3.9+
- Docker
- Kubernetes (Minikube)
- kubectl

## 🚀 How to Run
1. **Docker Build:**
   ```bash
   pip install -r infra/requirements.txt
   python app/app.py
   ```
Open: http://localhost:5000

2. **Docker Build:**
   ```bash
    docker build -t hello-devops -f infra/Dockerfile .
    docker run -p 5000:5000 hello-devops
   ```

3. **Kubernetes Deployment:**
   ```bash
    minikube start
    kubectl apply -f infra/k8s/
    minikube service hello-devops-service
   ```

4. **Run CI/CD Pipeline Locally:**
   ```bash
    python ci_cd_pipeline.py
   ```

## 📊 Monitoring

Prometheus: http://localhost:9090 (after deploying)