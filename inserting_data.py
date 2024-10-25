import mysql.connector
from mysql.connector import errorcode
import pandas as pd
cnx = mysql.connector.connect(user = "root",host = "localhost",password ="Savithri@508",database = "DataSpark")
cursor = cnx.cursor()

df = pd.read_csv('Customers_data_info.csv')
df1 = pd.read_csv('StoreData.csv')
df2 = pd.read_csv('Products_Data_Info.csv')
df3 = pd.read_csv('Sales_Data5.csv')
df4 = pd.read_csv('ExchangeData.csv')

query1= "insert into customers(customer_key,gender,customer_name,city,state,zipcode,country,continent,birthday) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query2 = "insert into stores(store_key,country,state,square_meters,open_date) values(%s,%s,%s,%s,%s)"
query3 = "insert into products(product_key,product_name,brand,color,unit_cost_usd,unit_price_usd,sub_category_key,sub_category,category_key,category) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
query4 = "insert into sales(order_number,line_item,order_date,customer_key,store_key,product_key,quantity,currency_code) values(%s,%s,%s,%s,%s,%s,%s,%s)"
query5 = "insert into exchange_rates(date_current,currency,exchange) values(%s,%s,%s)"

for index,row in df.iterrows():
    values = tuple((row['CustomerKey'],row['Gender'],row['Name'],row['City'],row['State'],row['Zip Code'],row['Country'],row['Continent'],row['Birthday']))
    cursor.execute(query1,values)
print(cursor.rowcount)
for index,row in df1.iterrows():
    cursor.execute(query2,(row['StoreKey'],row['Country'],row['State'],row['Square Meters'],row['Open Date']))
print(cursor.rowcount)
for index,row in df2.iterrows():
    cursor.execute(query3,(row['ProductKey'],row['Product Name'],row['Brand'],row['Color'],row['Unit Cost USD'],row['Unit Price USD'],row['SubcategoryKey'],row['Subcategory'],row['CategoryKey'],row['Category']))
print(cursor.rowcount)

for index,row in df3.iterrows():
    cursor.execute(query4,(row['Order Number'],row['Line Item'],row['Order Date'],row['CustomerKey'],row['StoreKey'],row['ProductKey'],row['Quantity'],row['Currency Code']))

print(cursor.rowcount)

for index,row in df4.iterrows():
    cursor.execute(query5,(row['Date'],row['Currency'],row['Exchange']))
print(cursor.rowcount)

cnx.commit()

cursor.close()
cnx.close()


