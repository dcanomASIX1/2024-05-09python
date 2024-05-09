import mysql.connector
global mydb

def conexio_BD():
    global mydb
    mydb = mysql.connector.connect(
            host="shared.daw.cat",
            user="1aa06",
            password="1ASIXdaw*06",
            port="3306",
            database="1aa06_my"
    )
    
    
def desconecxio():
    mydb.close()
