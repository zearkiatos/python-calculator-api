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