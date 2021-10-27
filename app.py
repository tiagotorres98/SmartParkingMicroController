import os
import sys
import time
from multiprocessing import Process

from flask import Flask, jsonify, render_template, request, url_for
from threading import Thread

from werkzeug.utils import redirect

from model import IntegrationArPy
import asyncio

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


@app.route("/command", methods=['POST'])
def command():
    global icCancelaLiberada, sensoresIniciados

    if request.form.get("conectaArd") is not None:
        resetCon()
        ar.start()

    if request.form.get("abreCancela") is not None:
        ar.updateCancela(1)
    elif request.form.get("fechaCancela") is not None:
        ar.updateCancela(0)

    if request.form.get("iniSensor") is not None:
        global sensoresIniciados
        sensoresIniciados = 1
        thread = Thread(target=iniSensor)
        thread.daemon = True
        thread.start()

    return redirect(url_for('.index'))


def arduinoConnected():
    global arduinoConectado
    arduinoConectado = ar.isConected()


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

def resetCon():
    global sensoresIniciados
    sensoresIniciados = 0


