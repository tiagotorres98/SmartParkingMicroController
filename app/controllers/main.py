import asyncio
import json
import os
import sys
import time
from multiprocessing import Process
import _thread
from urllib.parse import quote_plus
from app import app, db
from flask import render_template
from flask import Flask, jsonify, render_template, request, url_for
from app.models.arduino.arduino import Arduino
from app.models.tables import Gate_Status, Vacante_Status
from datetime import datetime
import binascii
from sqlalchemy import desc

sensoresIniciados = 0
icCancelaLiberada = 0
arduinoConectado = 0
icVaga1 = 0
icVaga2 = 0
icVaga3 = 0

arduino = Arduino() 

@app.route("/")
def index():
    global arduinoConectado
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
    global arduinoConectado
    if arduinoConectado == 0:
        arduino.iniciarConexao()
        result = arduino.arduinoConectado()
        arduinoConectado = int(result)
        return json.dumps(str(result))
    

@app.route("/connectSensores", methods=['POST'])
def connectSensores():
    global sensoresIniciados
    if sensoresIniciados == 0:
        data = request.data
        result = json.loads(data)
        _thread.start_new_thread(getDataOnArray,())
        sensoresIniciados = 1
        return json.dumps("trude")

@app.route("/cancela", methods=['POST'])
def cancela():
    gate = Gate_Status(1,0,datetime.today())

    data = request.data
    result = json.loads(data)
    gate.ic_open = int(result)

    db.session.merge(gate)
    db.session.commit()
    return json.dumps(str("e"))

@app.route("/getParam", methods=['GET'])
def getParam():
    global sensoresIniciados
    global arduinoConectado
    
    icCancelaLiberada = ord(db.session.query(Gate_Status).first().ic_open)
    param = {
        'sensoresIniciados' : sensoresIniciados,
        'icCancelaLiberada' : icCancelaLiberada,
        'arduinoConectado'  : arduinoConectado
    }

    db.session.commit()
    return json.dumps(param)

@app.route("/getVagas", methods=['GET'])
def getVagasV():
    global icVaga1
    global icVaga2
    global icVaga3
    param = {
        'icVaga1' : icVaga1,
        'icVaga2' : icVaga2,
        'icVaga3' : icVaga3
    }
    return json.dumps(param)

def getDataOnArray():
    while True:
        command = "123"
        cod = []
        aux = ""
        i = 0
        vacancie = Vacante_Status(None,0,0,0,datetime.today())

        global icCancelaLiberada
        icCancelaLiberada = ord(db.session.query(Gate_Status).first().ic_open)
        lastVacancie = db.session.query(Vacante_Status).order_by(desc("id")).first()

        if icCancelaLiberada == 1:
            command += "4"
        elif icCancelaLiberada == 0:
            command += "5"
        
        arduino.writeValues(command)
        for i in range(4):
                aux = arduino.readValues()
                if aux != '_':
                        cod.append(aux)
        if len(cod) == 3:
            global icVaga1
            global icVaga2
            global icVaga3

            result = dePara(cod)
            if icVaga1 != ord(lastVacancie.v1) or icVaga2 != ord(lastVacancie.v2) or icVaga3 != ord(lastVacancie.v3):
                vacancie.v1 = result[0]
                vacancie.v2 = result[1]
                vacancie.v3 = result[2]
                db.session.merge(vacancie)
                
            icVaga1 = result[0]
            icVaga2 = result[1]
            icVaga3 = result[2]

        
        db.session.commit()


def dePara(comands):
        lista = [0, 0, 0]
        for i in range(len(comands)):
            if comands[i] == 'e':
                # print('vaga 1 estacionada')
                lista[0] = 1
            if comands[i] == 'f':
                # print('vaga 1 não estacionada')
                lista[0] = 0

            if comands[i] == 'c':
                # print('vaga 2 estacionada')
                lista[1] = 1
            if comands[i] == 'd':
                # print('vaga 2 não estacionada')
                lista[1] = 0

            if comands[i] == 'a':
                # print('vaga 3 estacionada')
                lista[2] = 1
            if comands[i] == 'b':
                # print('vaga 3 não estacionada')
                lista[2] = 0

        return lista
