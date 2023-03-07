#import necessary packages
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import mysql.connector as mysql
from streamlit_option_menu import option_menu

#connect to mysql database
db = mysql.connect(
  host="localhost",
  user="root",
  password="Your password",
  database="phonepe" 
)
#get data from mysql database
query = 'select * from agg_trans'
df = pd.read_sql(query, db)
query ='select * from Longitude_Latitude_State_Table'
df1 = pd.read_sql(query, db)
query ='select * from data_map_districts_longitude_latitude'
df2 = pd.read_sql(query, db)
query ='select * from district_map_transaction'
df3 = pd.read_sql(query, db)
query ='select * from district_registering_map'
df4 = pd.read_sql(query, db)
query ='select * from user_by_device'
df5 = pd.read_sql(query, db)


#dataframe created
df.to_csv('Agg_Trans.csv')
df = pd.read_csv('Agg_Trans.csv',index_col=0)

df1.to_csv('Longitude_Latitude_State_Table')
state = pd.read_csv('Longitude_Latitude_State_Table')

df2.to_csv('Data_Map_Districts_Longitude_Latitude')
districts = pd.read_csv('Data_Map_Districts_Longitude_Latitude')

df3.to_csv('district_map_transaction.csv')
districts_tran = pd.read_csv('district_map_transaction.csv',index_col=0)

df4.to_csv('district_registering_map.csv')
app_opening = pd.read_csv('district_registering_map.csv',index_col=0)

df5.to_csv('user_device.csv')
user_device = pd.read_csv('user_device.csv',index_col=0)


#title
st.title(':red[PhonePe Pulse Data Analysis:signal_strength:]')

# option menu
with st.sidebar:
  selected = option_menu(menu_title=None, options=["geo_analysis","Device_analysis","payment_analysis","transac_yearwise"], icons=["clipboard-data","award","capslock-fill","coin"], orientation="horizontal")


#geo_analysis menu page
  if selected=="geo_analysis":
    
    Year = st.selectbox('Please select the Year',
                    ('2018', '2019', '2020', '2021', '2022'))
    
    Quarter = st.selectbox('Please select the Quarter',
                       ('1', '2', '3', '4'))
    
    


#Device_analysis menu page
  if selected=="Device_analysis":
     bar_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                          'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                          'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                          'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                          'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                          'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                          'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                          'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                          'uttarakhand', 'west-bengal'), index=10, key='tree_map_state')
     bar_state_year = int(st.selectbox('Please select the Year',
                                       ('2018', '2019', '2020', '2021', '2022'),  key='tree_map_state_year'))
     bar_state_quater = int(st.selectbox('Please select the Quarter',
                                         ('1', '2', '3', '4'),  key='tree_map_state_quater'))



#payment_analysis menu page
  if selected=="payment_analysis":
     pie_pay_mode_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                              'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                              'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                              'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                              'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                              'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                              'uttarakhand', 'west-bengal'), index=10, key='pie_pay_mode_state')
     pie_pay_mode_year = int(st.selectbox('Please select the Year',
                                     ('2018', '2019', '2020', '2021', '2022'),  key='pie_pay_year'))
     pie_pay_mode__quarter = int(st.selectbox('Please select the Quarter',
                                        ('1', '2', '3', '4'),  key='pie_pay_quater'))
     pie_pay_mode_values = st.selectbox(
        'Please select the values to visualize', ('Transaction_count', 'Transacion_amount'))


 #transac_yearwise menu page
  if selected=="transac_yearwise":
     transac_state = st.selectbox('Please select State', ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
                                                         'assam', 'bihar', 'chandigarh', 'chhattisgarh',
                                                         'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
                                                         'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
                                                         'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                                                         'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
                                                         'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
                                                         'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
                                                         'uttarakhand', 'west-bengal'), index=10, key='transac')
   

     transac__quarter = int(st.selectbox('Please select the Quarter',
                                   ('1', '2', '3', '4'), key='trans_quarter'))
     transac_type = st.selectbox('Please select the Mode',
                                ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'), key='transactype')
     transac_values = st.selectbox(
        'Please select the values to visualize', ('Transaction_count', 'Transacion_amount'), key='transacvalues')



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ INDIA MAP ANALYSIS @@@@@@@@@@@@@@@@@@@@
state = state.sort_values(by='state')
state = state.reset_index(drop=True)
df2 = df.groupby(['State']).sum()[['Transaction_count', 'Transacion_amount']]
df2 = df2.reset_index()

choropleth_data = state.copy()

for column in df2.columns:
    choropleth_data[column] = df2[column]
choropleth_data = choropleth_data.drop(labels='State', axis=1)

df.rename(columns={'State': 'state'}, inplace=True)
sta_list = ['andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
            'assam', 'bihar', 'chandigarh', 'chhattisgarh',
            'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
            'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand',
            'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
            'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland',
            'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim',
            'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
            'uttarakhand', 'west-bengal']
state['state'] = pd.Series(data=sta_list)
state_final = pd.merge(df, state, how='outer', on='state')
districts_final = pd.merge(districts_tran, districts,
                           how='outer', on=['State', 'District'])







#geo_analysis
if selected=="geo_analysis":
    st.subheader(':violet[Transaction analysis->State and Districtwise:]')
    st.write(' ')
    Year = int(Year)
    Quarter = int(Quarter)
    plot_district = districts_final[(districts_final['Year'] == Year) & (
        districts_final['Quarter'] == Quarter)]
    plot_state = state_final[(state_final['Year'] == Year)
                             & (state_final['Quarter'] == Quarter)]
    plot_state_total = plot_state.groupby(
        ['state', 'Year', 'Quarter', 'Latitude', 'Longitude']).sum()
    plot_state_total = plot_state_total.reset_index()
    state_code = ['AN', 'AD', 'AR', 'AS', 'BR', 'CH', 'CG', 'DNHDD', 'DL', 'GA',
                  'GJ', 'HR', 'HP', 'JK', 'JH', 'KA', 'KL', 'LA', 'LD', 'MP', 'MH',
                  'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PB', 'RJ', 'SK', 'TN', 'TS',
                  'TR', 'UP', 'UK', 'WB']
    plot_state_total['code'] = pd.Series(data=state_code)
    # ------------------------------------------- Geo-visualization of transacion data ------------------------------------------------------
    fig1 = px.scatter_geo(plot_district,
                          lon=plot_district['Longitude'],
                          lat=plot_district['Latitude'],
                          color=plot_district['Transacion_amount'],
                          size=plot_district['Transaction_count'],
                          hover_name="District",
                          hover_data=['State', 'Transacion_amount', 
                                      'Transaction_count', 'Year', 'Quarter'],
                          title='District',
                          size_max=22,)
    fig1.update_traces(marker={'color': "red",
                               'line_width': 1})
    fig2 = px.scatter_geo(plot_state_total,
                          lon=plot_state_total['Longitude'],
                          lat=plot_state_total['Latitude'],
                          hover_name='state',
                          text=plot_state_total['code'],
                          hover_data=['Transaction_count',
                                      'Transacion_amount', 'Year', 'Quarter'],
                          )
    fig2.update_traces(marker=dict(color="yellow", size=10))
    fig = px.choropleth(
        choropleth_data,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='Transacion_amount',
        color_continuous_scale='twilight',
        hover_data=['Transaction_count', 'Transacion_amount']
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.add_trace(fig1.data[0])
    fig.add_trace(fig2.data[0])
    fig.update_layout(height=800, width=800)
    st.write(' ')
    st.write(' ')
    st.plotly_chart(fig)
    st.info(
    """
    Details of Map:
    - Darker color ---> Total Transactions of States
    - Darker state ---> Higher Transactions
    - Circles -->     Total Transactions Dictrict wise
    - Bigger  Circle ---> Higher  Transactions
    - Hover data ---> Transaction count, Total amount
    """
    )

#Device_analysis      
if selected=="Device_analysis":      
      
    st.subheader(':violet[User Device analysis->Statewise:]')
    
    user_device_bar = user_device[(user_device['State'] == bar_state) & (user_device['Year'] == bar_state_year) &
                                      (user_device['Quarter'] == bar_state_quater)]
    user_device_bar['Brand_count'] = user_device_bar['Brand_count'].astype(
        str)
    
    
    # ---------------------------------------- Barchart view of user device -----------------------------------------------------------------
    bar_user = px.bar(user_device_bar, x='Brand', y='Brand_count', color='Brand',
                      title='Bar chart analysis', color_continuous_scale='sunset',)
    st.plotly_chart(bar_user)

#payment_analysis      
if selected=="payment_analysis":
    st.subheader(':violet[Payment type Analysis -> 2018 - 2022:]')
    # querypa = 'select * from agg_transaction_table'
    # payment_mode = pd.read_sql(querypa, con=connection)
    payment_mode = pd.read_csv('Agg_Trans.csv',index_col=0)
    
    pie_payment_mode = payment_mode[(payment_mode['Year'] == pie_pay_mode_year) & (
        payment_mode['Quarter'] == pie_pay_mode__quarter) & (payment_mode['State'] == pie_pay_mode_state)]
    # -------------------------------- Pie chart analysis of Payment mode --------------------------------------------------------------------
    pie_pay_mode = px.pie(pie_payment_mode, values=pie_pay_mode_values,
                          names='Transaction_type', hole=.5, hover_data=['Year'])
    # ------------------------------------- Bar chart analysis of payment mode ----------------------------------------------------------------
    pay_bar = px.bar(pie_payment_mode, x='Transaction_type',
                     y=pie_pay_mode_values, color='Transaction_type')
    st.plotly_chart(pay_bar)
    st.plotly_chart(pie_pay_mode)

#transac_yearwise analysis      
if selected=="transac_yearwise":
   st.subheader(':violet[Transaction analysis->Statewise:]')
   payment_mode_yearwise =  pd.read_csv('Agg_Trans.csv',index_col=0)
   new_df = payment_mode_yearwise.groupby(
        ['State', 'Year', 'Quarter', 'Transaction_type']).sum()
   new_df = new_df.reset_index()
   chart = new_df[(new_df['State'] == transac_state) &
                   (new_df['Transaction_type'] == transac_type) & (new_df['Quarter'] == transac__quarter)]
    # ------------------------------- Bar chart analysis of transacion data statewise --------------------------------------------------------
   year_fig = px.bar(chart, x=['Year'], y=transac_values, color=transac_values, color_continuous_scale='armyrose',
                      title='Transaction analysis '+transac_state + ' regarding to '+transac_type)
   st.plotly_chart(year_fig)

    
      
      


