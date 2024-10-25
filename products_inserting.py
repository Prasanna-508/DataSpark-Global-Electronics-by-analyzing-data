import mysql.connector
from mysql.connector import errorcode
import pandas as pd
cnx = mysql.connector.connect(user = "root",host = "localhost",password ="Savithri@508",database = "dataspark")
cursor = cnx.cursor()

df2 = pd.read_csv('products_data_infos.csv')

query3 = "insert into products(product_key,product_name,brand,color,unit_cost_usd,unit_price_usd,sub_category_key,sub_category,category_key,category) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"



for index,row in df2.iterrows():
    cursor.execute(query3,(row['ProductKey'],row['Product Name'],row['Brand'],row['Color'],row['Unit Cost USD'],row['Unit Price USD'],row['SubcategoryKey'],row['Subcategory'],row['CategoryKey'],row['Category']))
print(cursor.rowcount)
cnx.commit()

cursor.close()
cnx.close()