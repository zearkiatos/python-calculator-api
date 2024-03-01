

from flask import Flask
from flask import request
import requests
from os import environ
from model.model import Number, db
import os

app = Flask(__name__)

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv('SQLALCHEMY_DATABASE_URI') if environ.get('SQLALCHEMY_DATABASE_URI') != 'default' else 'sqlite:///conversion_system.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTION'] = True
    return app


app = create_app('default')
app_context = app.app_context()
app_context.push()
app.debug = True
db.init_app(app)
db.create_all()

@app.route('/guardar_numero',methods = ['POST'])
def SaveNumber():
    number = request.json["num_1"]
    new_number = Number(value=number)
    db.session.add(new_number)
    db.session.commit()
    return {"mensaje": f"numero {new_number.value} guardado correctamente."}


@app.route('/ultimo_numero',methods = ['GET'])
def GetNumber():
    last_record = db.session.query(Number).order_by(Number.id.desc()).first()
    return {"ultimo_valor": last_record.value}

@app.route('/suma_numeros',methods = ['POST'])
def Suma():
    message = ""
    user_name = os.getenv("user_name")
    
    if request.method == 'POST':
        try:
            numero1, numero2 = request.json["num_1"], request.json["num_2"]
        except:
            return {"message": EscribirResultado("Indique dos numeros para ser sumados", user_name,None,None)}, 404
        
        message = f"suma de los dos numeros es: {numero1 + numero2}" 
        message = user_name + " la " + message if user_name else "La " + message  

        return {"message": EscribirResultado(message, user_name, numero1, numero2), "result": numero1 + numero2}, 200

@app.route('/multiplicar',methods = ['POST'])
def Multiply():
    message = ""
    user_name = os.getenv("user_name")
    
    if request.method == 'POST':
        try:
            numero1, numero2 = request.json["num_1"], request.json["num_2"]
        except:
            return {"message": EscribirResultado("Indique dos numeros para ser multiplicados", user_name,None,None)}, 404
        
        message = f"multiplicacion de los dos numeros es: {numero1 * numero2}" 
        message = user_name + " la " + message if user_name else "La " + message  

        return {"message": EscribirResultado(message, user_name, numero1, numero2), "result": numero1 * numero2}, 200

def EscribirResultado(message, user_name ,a ,b):
    write = "not_show" if not os.getenv("write_result") else os.getenv("write_result") 
    if write == "not_show" or not a or not b:
        return message
    f = open("./data_file/resultado.txt", "w")
    f.write(f"Hola {user_name}! Al sumar {a} y {b} se obtiene como resultado {a+b} ")
    f.close()
    return message

@app.route('/exponencial',methods = ['POST'])
def Exponencial():
    multiplicacion_url = os.getenv("MULTIPLICACION_MS")
    
    if request.method == 'POST':
        try:
            numero , potencia = request.json["numero"], request.json["potencia"]
        except:
            return {"message": ""}

        resultado = numero
        for _ in range(potencia-1):
            obj = {'num_1': resultado, 'num_2': numero}
            req = requests.post(multiplicacion_url + '/multiplicar', json = obj)
            if req.status_code != 200:
                raise Exception(req.text)
            resultado = req.json()["result"]

        return {"message": f"Elevando {numero} a la {potencia} se obtiene {resultado}" , "result": resultado}, 200


@app.route('/health',methods = ['GET'])
def Health():
    return "ok", 200
    
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(debug=True, host='0.0.0.0', port=port)