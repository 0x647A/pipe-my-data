# Kubernetes 

**Kubernetes** is an open-source platform for automating the deployment, scaling, and management of containerized applications. It was developed by Google and donated to the Cloud Native Computing Foundation (CNCF). Kubernetes enables efficient management of container clusters, facilitating the deployment of applications in various environments (locally, public cloud, private cloud, or hybrid).

## Kubernetes Components

1. **Master Node**:
    - **API Server**: The communication interface of Kubernetes, accepting requests from users and other components.
    - **Etcd**: The key-value database that stores all the cluster configuration data.
    - **Controller Manager**: Monitors the state of the cluster and manages controllers like the replication controller.
    - **Scheduler**: Assigns new pods to the appropriate nodes in the cluster.

2. **Worker Node**:
    - **Kubelet**: An agent running on each worker node responsible for starting pods and containers.
    - **Kube-proxy**: Manages network rules and directs network traffic to the correct services.
    - **Container Runtime**: The environment for running containers, e.g., Docker, containerd.

## Key Concepts and Components

- **Pod**: The smallest deployable unit in Kubernetes, which can contain one or more containers.
- **ReplicaSet**: Ensures that a specified number of pod replicas are running at any given time.
- **Deployment**: Provides declarative updates to applications and manages ReplicaSets to ensure the desired state of the application.
- **Service**: An abstraction that defines a logical set of pods and a policy by which to access them, often through a load balancer.
- **Ingress**: Manages external access to services, typically HTTP, providing load balancing, SSL termination, and name-based virtual hosting.
- **ConfigMap and Secret**: Provide configuration data and sensitive information to pods, keeping them decoupled from application logic.
- **PersistentVolume (PV) and PersistentVolumeClaim (PVC)**: Abstract storage resources and allow users to request and use storage as needed.

## Ansible Playbooks for Kubernetes

Ansible playbooks are used to automate the configuration and deployment of Kubernetes. Below is an example Ansible playbook for installing Kubernetes on Ubuntu:

```yaml
---
- name: Install Kubernetes
  hosts: all
  become: yes
  tasks:
    - name: Install dependency packages
      apt:
        name:
          - apt-transport-https
          - ca-certificates
          - curl
          - software-properties-common
        state: present

    - name: Add Docker GPG key
      apt_key:
        url: https://download.docker.com/linux/ubuntu/gpg
        state: present

    - name: Add Docker repository
      apt_repository:
        repo: deb [arch=amd64] https://download.docker.com/linux/ubuntu {{ ansible_distribution_release }} stable
        state: present

    - name: Install Docker
      apt:
        name: docker-ce
        state: present

    - name: Add Kubernetes GPG key
      apt_key:
        url: https://packages.cloud.google.com/apt/doc/apt-key.gpg
        state: present

    - name: Add Kubernetes repository
      apt_repository:
        repo: deb http://apt.kubernetes.io/ kubernetes-xenial main
        state: present

    - name: Install kubelet, kubeadm, and kubectl
      apt:
        name:
          - kubelet
          - kubeadm
          - kubectl
        state: present
```

## Running Kubernetes

Initialize the cluster (on the master node):
```bash
sudo kubeadm init --pod-network-cidr=192.168.0.0/16
```

## Configure kubeconfig for the user
```bash
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

## Install a pod network (e.g., Calico)
```bash
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml
```

### Join worker nodes to the cluster:
On the worker nodes, run the command provided by kubeadm init, for example:
```bash
sudo kubeadm join <master-ip>:<master-port> --token <token> --discovery-token-ca-cert-hash sha256:<hash>
```

## Helm

**Helm** is a package manager for Kubernetes that simplifies the deployment of applications. It works similarly to apt for Ubuntu or yum for CentOS. Helm uses "charts" to describe the resources needed to run an application on Kubernetes.

### Install Helm
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
```

### Using Helm to install an application (e.g., Nginx)
```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install my-nginx bitnami/nginx
```

## Rancher

**Rancher** is a management platform for Kubernetes that simplifies the management of multiple Kubernetes clusters. Rancher provides a user interface for easy monitoring, managing, and configuring Kubernetes clusters.

### Installing Rancher:

1. Run Rancher in a Docker container:
```bash
docker run -d --restart=unless-stopped -p 80:80 -p 443:443 --name rancher rancher/rancher
```

2. Open a browser and go to https://<IP_address> to complete the setup.

Rancher allows you to create and manage Kubernetes clusters through a graphical user interface, making it useful for both beginners and experienced Kubernetes users.