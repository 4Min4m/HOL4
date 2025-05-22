import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
import subprocess
import sys
import docker
import kubernetes.client
from kubernetes import config

def run_cmd(command):
    try:
        subprocess.run(command, check=True, shell=True)
        return True
    except subprocess.CalledProcessError:
        return False

def build_and_push():
    try:
        # اضافه کردن تنظیمات Docker برای GitHub Actions
        client = docker.DockerClient(base_url='unix://var/run/docker.sock')
        
        # Build image
        client.images.build(
            path=".",
            tag="hello-devops:latest",
            dockerfile="infra/Dockerfile"
        )
        
        # Push to registry (اختیاری - نیاز به تنظیمات اضافه دارد)
        # client.images.push("hello-devops:latest")
        
        return True
    except Exception as e:
        print(f"❌ Docker error: {str(e)}")
        return False

def deploy_k8s():
    try:
        # استفاده از تنظیمات داخل کلاستر برای GitHub Actions
        config.load_incluster_config()
        
        k8s_client = kubernetes.client.AppsV1Api()
        
        # اعمال deployment
        with open("infra/k8s/deployment.yaml") as f:
            dep = yaml.safe_load(f)
            k8s_client.create_namespaced_deployment(
                body=dep,
                namespace="default"
            )
        
        # اعمال service
        with open("infra/k8s/service.yaml") as f:
            svc = yaml.safe_load(f)
            k8s_client.create_namespaced_service(
                body=svc,
                namespace="default"
            )
            
        print("✅ Successfully deployed to Kubernetes")
        return True
        
    except Exception as e:
        print(f"❌ Kubernetes deployment error: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Starting DevOps Pipeline")
    if not run_cmd("pytest tests/"):
        sys.exit(1)
    build_and_push()
    deploy_k8s()
    print("✅ Pipeline Completed!")