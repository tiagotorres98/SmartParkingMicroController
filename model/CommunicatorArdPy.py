from model import ArduinoCRUDs
from model import AInterpreter
from model import Arduino


class CommunicatorArdPy:

    def __init__(self):
        self.__interpretador = AInterpreter.AInterpreter()
        self.__ACRUD = ArduinoCRUDs.ArduinoCRUDs()
        self.__arduino = Arduino.Arduino()
        self.__arduino.setPort("COM3")
        self.__lista = ['0', '0', '0']
        self.__listaAux = ['0', '0', '0']

    def startComArduino(self):
        comandos = self.controlador()
        self.__listaAux = self.__arduino.getDataOnArray(comandos)
        if self.__listaAux is not None:
            if set(self.__lista) != set(self.__listaAux):
                self.__lista = self.__listaAux
                self.__ACRUD.setVagaValues(self.__lista)


    def getCancela(self):
        return self.__ACRUD.getCancela()

    def controlador(self):
        comandos = "123"
        if self.getCancela() == 0:
            comandos += "5"
        elif self.getCancela() == 1:
            comandos += "4"

        return comandos

    def isConected(self):
        return self.__arduino.isArduinoConnected()

    def updateCancela(self, valor):
        self.__ACRUD.updateCancela(valor)

    def startArduino(self):
        self.__arduino.start()

    def getVagas(self):
        return self.__ACRUD.getVagas()