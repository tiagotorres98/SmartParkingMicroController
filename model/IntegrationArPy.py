from time import sleep

from model import CommunicatorArdPy
from threading import Thread

comunicador = CommunicatorArdPy.CommunicatorArdPy()


class IntegrationArPy:

    def run(self):
        while True:
            sleep(1)
            comunicador.startComArduino()

    def isConected(self):
        return comunicador.isConected()

    def getCancela(self):
        return comunicador.getCancela()

    def updateCancela(self,valor):
        comunicador.updateCancela(valor)

    def start(self):
        comunicador.startArduino()

    def getVagas(self):
        return comunicador.getVagas()
