import mysql.connector
from mysql.connector import errorcode



cnx = mysql.connector.connect(user = "root",host = "localhost",password ="Savithri@508",database = "dataspark")
cursor = cnx.cursor()
query1 = "create table customers(customer_key int primary key,customer_name varchar(40) not null,gender varchar(6) not null,city varchar(40) not null,state_code varchar(4) not null,state varchar(30) not null,zipcode varchar(7) not null,country varchar(30) not null,continent varchar(30) not null,birthday date);"
query2 = "create table products(product_key int primary key,product_name varchar(100) not null,brand varchar(20) not null,color varchar(10) not null,unit_cost_usd int not null,unit_price_usd int not null,sub_category_key int not null,sub_category varchar(30) not null,category_key int not null,category varchar(25) not null);"
query3 = "create table sales(order_number int,line_item int,order_date date not null,delivery_date date,customer_key int,store_key int,product_key int,quantity int,currency_code char(3),constraint sales_pk primary key(order_number,line_item));"
query4 = "create table stores(store_key int primary key,country varchar(30) not null,state varchar(30) not null,square_meters int,open_date date not null);"
query5 = "create table exchange_rates(date_current date,currency char(3),exchange int not null,constraint exchange_rates_pk primary key(date_current,currency));"


cursor.execute(query1)
cursor.execute(query2)
cursor.execute(query3)
cursor.execute(query4)
cursor.execute(query5)

cursor.execute("SHOW TABLES")

for x in cursor:
    print(x)

cursor.close()
cnx.close()

