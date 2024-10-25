import mysql.connector
from mysql.connector import errorcode

cnx = mysql.connector.connect(user = "root",host = "localhost",password ="Savithri@508")
cursor = cnx.cursor()

cursor.execute("CREATE DATABASE DataSpark")


cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)

    