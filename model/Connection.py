import mysql.connector
import psycopg2

class Connection:

    def __init__(self):
        self.__connection = self.mysqlConnection()

    def getConnection(self):
        return self.__connection

    def mysqlConnection(self):
        return mysql.connector.connect(
            host="localhost",
            user="admin",
            password="*Q]DmTd0]*6PlNbx",
            database="estacionamento"
        )

    def postgreConnection(self):
        return psycopg2.connect(
            host='localhost',
            database='estacionamento',
            user='admin',
            password='*Q]DmTd0]*6PlNbx'
        )
