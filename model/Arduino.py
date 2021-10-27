import serial


class Arduino:

    def __init__(self):
        self.__conexao = serial.Serial()
        self.__conexao.set_buffer_size(9600)
        self.__conexao.setPort("COM3")

    def start(self):
        self.__conexao = serial.Serial()
        self.__conexao.set_buffer_size(9600)
        self.__conexao.setPort("COM3")
        self.__conexao.open()

    def setPort(self, port):
        try:
            self.__conexao.setPort(port)
            if not self.isArduinoConnected():
                self.openConnection()
        except:
            return False

    def isArduinoConnected(self):
        try:
            self.__conexao.read()
            return 1
        except serial.serialutil.SerialException:
            return 0

    def openConnection(self):
        if not self.__conexao.isOpen():
            self.__conexao.open()

    def closeConnection(self):
        self.__conexao.close()

    def readValues(self):
        value = self.__conexao.read().decode()
        return value

    def writeValues(self, value):
        self.__conexao.write(value.encode())

    def waiting(self):
        return self.__conexao.inWaiting();

    def getDataOnArray(self, command):
        cod = []
        aux = ""
        i = 0

        self.writeValues(command)
        for i in range(4):
                aux = self.readValues()
                if aux != '_':
                        cod.append(aux)
        if len(cod) == 3:
            return cod
        else:
            return None
