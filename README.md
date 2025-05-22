# Hello DevOps Project

Traditional CI/CD pipelines often rely on YAML-based configurations (GitHub Actions, GitLab CI, etc.), but what if you could leverage Python's flexibility to build more powerful and dynamic workflows?

𝗪𝗵𝘆 𝗣𝘆𝘁𝗵𝗼𝗻 𝗳𝗼𝗿 𝗖𝗜/𝗖𝗗?

✅ 𝗙𝘂𝗹𝗹 𝗣𝗿𝗼𝗴𝗿𝗮𝗺𝗺𝗮𝗯𝗶𝗹𝗶𝘁𝘆 – Complex logic, API calls, and dynamic workflows become trivial with Python.
✅ 𝗥𝗲𝘂𝘀𝗮𝗯𝗹𝗲 𝗖𝗼𝗺𝗽𝗼𝗻𝗲𝗻𝘁𝘀 – Modular functions and classes eliminate YAML duplication.
✅ 𝗗𝗲𝗯𝘂𝗴𝗴𝗶𝗻𝗴 & 𝗧𝗲𝘀𝘁𝗶𝗻𝗴 – Use Python’s rich tooling (logging, unit tests) for pipeline reliability.
✅ 𝗦𝗲𝗮𝗺𝗹𝗲𝘀𝘀 𝗜𝗻𝘁𝗲𝗴𝗿𝗮𝘁𝗶𝗼𝗻𝘀 – Native support for Kubernetes (kubernetes-client), Docker (docker-py), and cloud SDKs.

𝗛𝗼𝘄 𝗜𝘁 𝗪𝗼𝗿𝗸𝘀

In my latest project, I built a Python-powered CI/CD pipeline that:
1️⃣ 𝗕𝘂𝗶𝗹𝗱𝘀 a Flask app
2️⃣ 𝗥𝘂𝗻𝘀 𝘁𝗲𝘀𝘁𝘀 with pytest
3️⃣ 𝗗𝗲𝗽𝗹𝗼𝘆𝘀 to Kubernetes (Minikube)
4️⃣ 𝗠𝗼𝗻𝗶𝘁𝗼𝗿𝘀 with Prometheus
All orchestrated via a single Python script (ci_cd_pipeline.py) – no YAML spaghetti!

𝗞𝗲𝘆 𝗧𝗮𝗸𝗲𝗮𝘄𝗮𝘆𝘀

🐍 Python > YAML for complex workflows
🔧 Customizability beats rigid syntax
📦 Container/Docker-friendly by design


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
