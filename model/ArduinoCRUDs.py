import datetime
import sys
from time import sleep

from model import Connection
from model import AInterpreter

class ArduinoCRUDs:

    def __init__(self):
        self.connect()
        self.__AI = AInterpreter.AInterpreter()

    def connect(self):
        self.__conexao = Connection.Connection().getConnection()
        self.__cursor = self.__conexao.cursor(buffered=True)

    def insert_vagas_values(self, v1, v2, v3):
        self.connect()
        sql = "INSERT INTO tb_status_vagas (VAGA1, VAGA2, VAGA3, Last_Modified_Date) VALUES (%s, %s, %s, %s)"
        data = (v1, v2, v3, datetime.datetime.today())
        self.__cursor.execute(sql, data)
        self.__conexao.commit()
        self.__cursor.close()
        self.__conexao.close()
        print("Vagas Atualizadas: " + str(v1) + " |  " + str(v2) + " | " + str(v3))

    def setVagaValues(self,lista):
        vl = self.__AI.dePara(lista)
        self.insert_vagas_values(vl[0],vl[1],vl[2])

    def getCancela(self):
        self.connect()
        sql = "SELECT IC_LIBERADO FROM TB_STATUS_CANCELA ORDER BY ID DESC LIMIT 0,1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        self.__cursor.reset()
        return result[0]

    def updateCancela(self,valor):
        sleep(1)
        self.connect()
        now = datetime.datetime.now()  # current date and time
        data = now.strftime("%Y-%m-%d %H:%M:%S")
        update = "UPDATE TB_STATUS_CANCELA SET LAST_MODIFIED_DATE = '"+str(data)+"' ,IC_LIBERADO = " + str(valor)
        self.__cursor.execute(update)
        self.__conexao.commit()
        self.__cursor.reset()

    def getVagas(self):
        sleep(1)
        self.connect()
        sql = "SELECT VAGA1, VAGA2, VAGA3 FROM TB_STATUS_VAGAS ORDER BY ID DESC LIMIT 0,1"
        self.__cursor.execute(sql)
        result = self.__cursor.fetchone()
        self.__conexao.commit()
        self.__cursor.close()
        self.__conexao.close()
        return result