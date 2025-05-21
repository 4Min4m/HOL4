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
    client = docker.from_env()
    client.images.build(path=".", tag="hello-devops:latest")

def deploy_k8s():
    config.load_kube_config()
    k8s_client = kubernetes.client.AppsV1Api()
    with open("infra/k8s/deployment.yaml") as f:
        dep = kubernetes.utils.create_from_yaml(k8s_client, f.read())

if __name__ == "__main__":
    print("🚀 Starting DevOps Pipeline")
    if not run_cmd("pytest tests/"):
        sys.exit(1)
    build_and_push()
    deploy_k8s()
    print("✅ Pipeline Completed!")