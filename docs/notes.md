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