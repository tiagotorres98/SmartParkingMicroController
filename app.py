import os
import sys
import time
from multiprocessing import Process

from flask import Flask, jsonify, render_template, request, url_for
from threading import Thread

from werkzeug.utils import redirect

from model import IntegrationArPy
import asyncio
import json


app = Flask(__name__)
ar = IntegrationArPy.IntegrationArPy()
#loop = asyncio.get_event_loop()
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

sensoresIniciados = 0
icCancelaLiberada = 0
arduinoConectado = 0
icVaga1 = 0
icVaga2 = 0
icVaga3 = 0


@app.route("/")
def index():
    arduinoConnected()
    getCancela()
    getVagas()
    return render_template(
        "index.html",
        sensor=sensoresIniciados,
        cancela=icCancelaLiberada,
        arduino=arduinoConectado,
        v1=icVaga1,
        v2=icVaga2,
        v3=icVaga3
    )

@app.route("/conectaArd", methods=['POST'])
def conectaArd():

    data = request.data
    result = json.loads(data)
    print(result)

    if result == True:
        try:
            global sensoresIniciados
            sensoresIniciados = 0
            ar.start()
            return json.dumps('true')
        except Exception as e: 
            return json.dumps(str(e))
    

@app.route("/connectSensores", methods=['POST'])
def connectSensores():

    data = request.data
    result = json.loads(data)
    print(result)

    if result:
        try:
            global sensoresIniciados
            sensoresIniciados = 1
            thread = Thread(target=iniSensor)
            thread.daemon = True
            thread.start()
            return json.dumps('true') 
        except Exception as e: 
            return json.dumps(str(e))
    else:
        return json.dumps('Não foi possível inciar os sensores')


@app.route("/cancela", methods=['POST'])
def cancela():

    data = request.data
    result = json.loads(data)
    print(result)

    try:
        if result:
            ar.updateCancela(1)
        else:
            ar.updateCancela(0)
        return json.dumps('true')
    except Exception as e: 
            return json.dumps(str(e))

@app.route("/getParam", methods=['GET'])
def getParam():
    getCancela()
    param = {
        'sensoresIniciados' : sensoresIniciados,
        'icCancelaLiberada' : ar.getCancela(),
        'arduinoConectado'  : arduinoConectado
    }
    return json.dumps(param)

@app.route("/getVagas", methods=['GET'])
def getVagasV():
    vagas = ar.getVagas()

    param = {
        'icVaga1' : vagas[0],
        'icVaga2' : vagas[1],
        'icVaga3'  : vagas[2]
    }
    return json.dumps(param)


def arduinoConnected():
    global arduinoConectado
    arduinoConectado = ar.isConected()
    sensoresIniciados = ar.isConected()


def getCancela():
    global icCancelaLiberada
    icCancelaLiberada = ar.getCancela()

def iniSensor():
    ar.run()

def getVagas():
    vagas = ar.getVagas()
    if not vagas is None:
        global icVaga1
        global icVaga2
        global icVaga3
        icVaga1 = vagas[0]
        icVaga2 = vagas[1]
        icVaga3 = vagas[2]

