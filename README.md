# Phonepe-Pulse-Data-Visualization-and-Exploration

PhonePe-Pulse-Data-2018-2022-Analysis

Data extraction: git Clone https://github.com/PhonePe/pulse.git to clone the data from phonepe pulse repositories. 
after cloning write code for data extraction and then  convert to csv.

Data transformation: Use a scripting language such as Python, along with
libraries such as Pandas, to manipulate and pre-process the data

Database insertion: Use the "mysql-connector-python" library in Python to
connect to a MySQL database and insert the transformed data using SQL
commands


Dashboard creation:
create a dashboard to visualize Phonepe pulse Github repository data using Streamlit and Plotly in Python
create menu bar for geo_analysis,Device_analysis,payment_analysis,transac_yearwise.

1)Geo-Visualization:The India map shows the Total Transactions of PhonePe in both state wide and District wide.

map created with  give year and quarter input to show how the data changed over time
Plotlys scatter_geo for plotting districts in indian map.
Plotlys coropleth for drawing the states in India map .   

2)User Device analysis:
In this BAR chart show the analysis of user device used in diiferent states for different years and different quaters.

3)payment_analysis:
In this bar chart and donut chart shows the transaction type take place for different states in different years.

4)Transaction yearwise:
In this BAR chart shows combine analysis of transaction type and transaction count or  transaction amount of different state yearwise.
 


