import mysql.connector
from mysql.connector import errorcode
import pandas as pd
cnx = mysql.connector.connect(user = "root",host = "localhost",password ="Savithri@508",database = "DataSpark")
cursor = cnx.cursor()
df4 = pd.read_csv('ExchangeData.csv')

query5 = "insert into exchange_rates(date_current,currency,exchange) values(%s,%s,%s)"


for index,row in df4.iterrows():
    cursor.execute(query5,(row['Date'],row['Currency'],row['Exchange']))
print(cursor.rowcount)

cnx.commit()

cursor.close()
cnx.close()

