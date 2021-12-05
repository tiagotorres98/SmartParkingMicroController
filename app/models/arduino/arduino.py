from serial import Serial

class Arduino:

    def iniciarConexao(self):
        try:
            self.conexao = Serial()
            self.conexao.set_buffer_size(9600)
            self.conexao.setPort("COM3")
            self.conexao.open()
        except Exception as e:
            return str(e)
    
    def arduinoConectado(self):
        try:
            return self.conexao.isOpen()
        except:
            return False

    def readValues(self):
        value = self.conexao.read().decode()
        return value

    def writeValues(self, value):
        self.conexao.write(value.encode())