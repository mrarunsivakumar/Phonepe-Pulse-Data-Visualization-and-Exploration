# Phonepe-Pulse-Data-Visualization-and-Exploration


#Data extraction:

#Extract data from the Phonepe pulse Github repository using git bash

#$git clone https://github.com/PhonePe/pulse.git


#Data transformation

#transforming the data into a format suitable for analysis and visualization.

#convert the data into csv format using pandas 


#install necessary package

import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_option_menu import option_menu
import mysql.connector
import plotly.graph_objects as go
import json


#Database insertion

#Use the "mysql-connector-python" library in Python to connect to a MySQL database and insert the transformed data using SQL
#commands.

#create table arun

from mysql.connector import Error
try:
    conn = msql.connect(host='localhost', user='root',  
                        password='arunsiva')#give ur username, password
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE arun")
        print("Database is created")
except Error as e:
    print("Error while connecting to MySQL", e)


#import phonepe pulse data csv file got from github respirosity to mysql database
 
 import mysql.connector as mysql
from mysql.connector import Error
try:
    conn = mysql.connect(host='localhost', database='phonepe', user='root', password='arunsiva')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS aggregated_user_device;')
        print('Creating table....')

# in the below line please pass the create table statement which you want #to create
        
        cursor.execute("CREATE TABLE aggregated_user_device(id int,aggregated_by varchar(255),aggregate_name varchar(255),year int,start_date varchar(255),end_date  varchar(255),brand varchar(255),count int,percentage float(10))")
        print("Table is created....")
        
        #loop through the data frame
        
        for i,row in empdata2.iterrows():
            
            #here %S means string values 
            sql = "INSERT INTO phonepe.aggregated_user_device VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
           
           # the connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)   



#Data retrieval

#"mysql-connector-python" library to connect to the MySQL database and fetch the data into a Pandas dataframe

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="arunsiva",
  database="arun" 
)

query = 'select * from aggregated_user'
df = pd.read_sql(query, db)
query ='select * from aggregated_user_device'
df1 = pd.read_sql(query, db)
query ='select * from aggregated_transaction'
df2 = pd.read_sql(query, db)
query ='select * from top_transaction'
df3 = pd.read_sql(query, db)
query ='select * from top_user'
df4 = pd.read_sql(query, db)

#dataframe created

df.to_csv('aggregated_user_device.csv', index=False)
df = pd.read_csv('aggregated_user_device.csv')

df1.to_csv('aggregated_user_device.csv', index=False)
df1 = pd.read_csv('aggregated_user_device.csv')

df2.to_csv('aggregated_transaction.csv', index=False)
df2 = pd.read_csv('aggregated_transaction.csv')

df3.to_csv('top_transaction.csv', index=False)
df3 = pd.read_csv('top_transaction.csv')

df4.to_csv('top_user.csv', index=False)
df4 = pd.read_csv('top_user.csv')


#title for streamlit app
st.title("Phonepe Pulse Data Visualization and Exploration")


chart_visual = st.sidebar.selectbox('Select Charts/Plot type', 
                                    ('Line Chart', 'Bar Chart', 'Bubble Chart'))


st.sidebar.checkbox("Show Analysis by amount", True, key = 1)
selected_status = st.sidebar.selectbox('Select transaction',
                                       options = ['amount', 
                                                  'count'])
  
fig = go.Figure()
  
if chart_visual == 'Line Chart':
    if selected_status == 'amount':
        fig.add_trace(go.Scatter(x = df3.aggregate_name, y = df4.amount,
                                 mode = 'lines',
                                 name = 'amount'))
    if selected_status == 'count':
        fig.add_trace(go.Scatter(x = df3.aggregate_name, y = df4.count,
                                 mode = 'lines', name = 'count'))
    
  
elif chart_visual == 'Bar Chart':
    if selected_status == 'amount':
        fig.add_trace(go.Bar(x=df3.aggregate_name, y=df4.amount,
                             name='amount'))
    if selected_status == 'count':
        fig.add_trace(go.Bar(x=df3.aggregate_name, y=df4.count,
                             name='count'))
# Show the map or chart
st.plotly_chart(fig)
