# Description
This is a project of a calculator api ✖️➕➖➗ made in python 🐍. This project is for practice deployment with docker 🐳

# Made with
[![Python](https://img.shields.io/badge/python-2b5b84?style=for-the-badge&logo=python&logoColor=white&labelColor=000000)]()
[![Flask](https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white&labelColor=000000)]()

# Calculadora de números

Para levantar el proyecto en su repositorio local, ejecute los siguientes pasos:

### 1. Instalar ambiente virtual:

En su terminal ejecute:
```
pip install virtualenv
```
Cuando la descarga finalize cree el ambiente virtual mediante:
```
virtualenv vnv
```
Esto creara en la carpeta local, archivos necesarios para aislar un ambiente de dependencias en Python, activelo mediante:
```
source vnv/bin/activate
```
Posteriormente baje las dependencias mediante:
```
pip install -r requirements.txt
```
### 2. Levantar la API:
En su terminal ejecute:
```
python3 -m flask run
``` 
### 3. Curl para sumar el dos números:
```
curl --location --request POST 'http://localhost:4000/suma' \
--header 'Content-Type: application/json' \
--data-raw '{    
    "num_1" : 2,
    "num_2": 3
}'

```

```sh
# Trying exponential

$ curl --location --request POST 'http://34.49.246.5/exponencial' \
--header 'Content-Type: application/json' \
--data-raw '{
    "numero": 2,
    "potencia": 2
}'

```
