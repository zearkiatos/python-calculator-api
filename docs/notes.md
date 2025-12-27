# Gcloud commands for google registry

```sh
    # Check project configuration

    $ gcloud config get-value project
```

```sh
# If you are not in your project you can choose your project with the next command

# gcloud config set project <ID-PROYECTO>

# For example

$ gcloud config set project miso-cloud-native

```

```sh
# How to create a registry
# For example

$ gcloud artifacts repositories create cloud-native-registry \
    --repository-format=docker \
    --location=us-west1 \
    --description="Docker images repository"
```

```sh
# Authentication to artifactory registry
# gcloud auth configure-docker <REGION>-docker.pkg.dev

$ gcloud auth configure-docker us-central1-docker.pkg.dev

```

```sh
# Command to build the application

# <REGION>-docker.pkg.dev/<ID-PROYECTO>/<NOMBRE-REPOSITORIO>/<IMAGEN>:<TAG>

$ docker build . -t=us-central1-docker.pkg.dev/miso-cloud-native-414617/python-calculator-api/python-calculator-api:1.0

```

```sh
# Post the image in the repository
# docker push <URI>

$ docker push us-central1-docker.pkg.dev/miso-cloud-native-414617/python-calculator-api/python-calculator-api:1.0
```

```sh
# Running the api with the registry
# docker run -p 4000:4000 <URI>

$ docker run -p 4000:4000 us-central1-docker.pkg.dev/miso-cloud-native-414617/python-calculator-api/python-calculator-api:1.0
```

```sh
# Creating a virtual network

# gcloud compute networks create <RED> --project=<ID-PROYECTO> --subnet-mode=custom --mtu=<MTU> --bgp-routing-mode=regional

$ gcloud compute networks create vpn-tutoriales-misw --project=miso-cloud-native-414617 --subnet-mode=custom --mtu=1460 --bgp-routing-mode=regional
```

```sh
# Create a subnet for kubernetes

# gcloud compute networks subnets create <NOMBRE-SUBRED> --range=<RANGO-IP> --network=<RED-PADRE> --region=<REGION> --project=<ID-PROYECTO>

$ gcloud compute networks subnets create red-k8s-tutoriales --range=192.168.32.0/19 --network=vpn-tutoriales-misw --region=us-central1 --project=miso-cloud-native-414617
```

```sh
# Troubleshooting

$ kubectl describe pod <nombre del pod>
$ kubectl logs <nombre del pod> --all-containers
$ kubectl get events
```

```sh
# To delete all deployments
$ kubectl delete all --all -n default
```

```sh
# To delete all deployments
$ kubectl delete all --all -n default
```

```sh
# To delete the ingress
# kubectl delete ingress <gateway-name>
$ kubectl delete ingress python-calculatorv3-ingress
```

```sh
# Connect to the container cluster
# gcloud container clusters get-credentials <CLUSTER_NAME> --region <ZONE_NAME> --project <PROJECT_ID>

$ gcloud container clusters get-credentials uniandes-misw-cloud-native-k8s --region us-central1 --project miso-cloud-native-414617
```
# Observability

## PromQL or MQL query

```mql
 fetch k8s_container
 filter
resource.project_id=
"uandes-native"
&& resource. namespace_name == "default"
 { metric kubernetes.1o/container/cpu/ core usage_time
 rate
 every 1m
 align next_older (2m) :
metric kubernetes 10/container/ cpu/request_cores

| align next_older(2m)|

 group_by (resource. location, resource. cluster_name, resource.namespace_name, metadata. system_labels.top_level_controller_name, metadata. system_labels.top_level_controller_typel. .sun()
outer_join e | div
top 5
scale '%"
```

# Kubernetes command

```sh
# Create a namespace

$ kubectl create namespace monitoring

# Get namespace
$ kubectl get namespace

# Kubectl grafana forward port

$ kubectl port-forward svc/monitoring-grafana 3000:80 -n monitoring

# Forward prometheus 🔥 port

$ kubectl port-forward svc/monitoring-kube-prometheus-prometheus  9090:9090 -n monitoring 

# Kubectl get grafana password

$ kubectl get secret monitoring-grafana -n monitoring -o jsonpath="{.data.admin-password}" | base64 --decod

# Delete a namespace

$ kubectl delete namespace monitoring
```

# Helm commands

```sh
# Adding community repository for charts

$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

# Adding an stable repository

$ helm repo add stable https://charts.helm.sh/stable

# Update repo

$ helm repo update

# Install helm in minikube

$ helm install monitoring prometheus-community/kube-prometheus-stack

# Install inside a specific namespace

$ helm install monitoring prometheus-community/kube-prometheus-stack --namespace monitoring

# List helm namespaces

$ helm list --all-namespaces

# Uninstall pods

$ helm uninstall prometheus -n monitoring

```

