import mysql.connector
import psycopg2

class Connection:

    def __init__(self):
        self.__connection = self.mysqlConnection()

    def getConnection(self):
        return self.__connection

    def mysqlConnection(self):
        return mysql.connector.connect(
            host="smartparking.mysql.uhserver.com",
            user="tts",
            password="Tuosrksti*jo1518",
            database="smartparking"
        )

    def postgreConnection(self):
        return psycopg2.connect(
            host='localhost',
            database='estacionamento',
            user='admin',
            password='*Q]DmTd0]*6PlNbx'
        )
