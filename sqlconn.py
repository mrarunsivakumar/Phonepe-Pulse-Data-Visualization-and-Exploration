
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error




agg = pd.read_csv('Agg_Trans.csv', index_col=0, delimiter = ',')
agg.head()




Data = pd.read_csv('Data_Map_Districts_Longitude_Latitude.csv', index_col=False, delimiter = ',')
Data.head()


district = pd.read_csv('district_map_transaction.csv', index_col=0, delimiter = ',')
district.head()


map = pd.read_csv('district_registering_map.csv', index_col=0, delimiter = ',')
map.head()


state = pd.read_csv('Longitude_Latitude_State_Table.csv', index_col=False, delimiter = ',')
state.head()


user = pd.read_csv('user_by_device.csv', index_col=0, delimiter = ',')
user.head()


import mysql.connector as msql
from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password=' your password')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE phonepe")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)




try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE Agg_Trans(State varchar(50),Year int,Quater int,Transacion_type varchar(50),Transacion_count int,Transacion_amount float(10))")
        print("Table is created....")
        #loop through the data frame
        for i,row in agg.iterrows():
            #here %S means string values 
            sql = "INSERT INTO phonepe.Agg_Trans VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)



try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE Data_Map_Districts_Longitude_Latitude(State varchar(50),District varchar(50),Latitude float(10),Longitude float(50))")
        print("Table is created....")
        #loop through the data frame
        for i,row in Data.iterrows():
            #here %S means string values 
            sql = "INSERT INTO phonepe.Data_Map_Districts_Longitude_Latitude VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)




try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE district_map_transaction(State varchar(50),Year int,Quater int,District varchar(50),Transacion_count int,Transacion_amount float(10))")
        print("Table is created....")
        #loop through the data frame
        for i,row in district.iterrows():
            #here %S means string values 
            sql = "INSERT INTO phonepe.district_map_transaction VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)




try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE district_registering_map(State varchar(50),Year int,Quater int,District varchar(50),Registered_user int,App_opening int)")
        print("Table is created....")
        #loop through the data frame
        for i,row in map.iterrows():
            #here %S means string values 
            sql = "INSERT INTO phonepe.district_registering_map VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)




try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE Longitude_Latitude_State_Table(code varchar(50),Latitude float(10),Longitude float(10),state varchar(50))")
        print("Table is created....")
        #loop through the data frame
        for i,row in state.iterrows():
            #here %S means string values 
            sql = "INSERT INTO phonepe.Longitude_Latitude_State_Table VALUES (%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)




try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='password')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE user_by_device(State varchar(50),Year int,Quater int,Brand varchar(50),Brand_count int,Brand_percentage float(10))")
        print("Table is created....")
        #loop through the data frame
        for i,row in user.iterrows():
            #here %S means string values 
            sql = "INSERT INTO phonepe.user_by_device VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)




sql = "SELECT * FROM phonepe.Agg_Trans"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)




sql = "SELECT * FROM phonepe.Data_Map_Districts_Longitude_Latitude"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)




sql = "SELECT * FROM phonepe.district_map_transaction"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)




sql = "SELECT * FROM phonepe.district_registering_map"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)




sql = "SELECT * FROM phonepe.Longitude_Latitude_State_Table"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)




sql = "SELECT * FROM phonepe.user_by_device"
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)







