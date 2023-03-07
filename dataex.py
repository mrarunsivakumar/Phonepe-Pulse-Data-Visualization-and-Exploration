import os
import json
import pandas as pd

Looping through phonepe pulse data and extracting the datas from json and repeating the process

# This is to direct the path to get the data as states

path = "data/aggregated/transaction/country/india/state/"
user_state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'Transacion_type': [],
       'Transacion_count': [], 'Transacion_amount': []}
for i in user_state_list:
    p_i = path+i+"/"
    Agg_yr = os.listdir(p_i)
    for j in Agg_yr:
        p_j = p_i+j+"/"
        Agg_yr_list = os.listdir(p_j)
        for k in Agg_yr_list:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']['transactionData']:
                    Name = z['name']
                    count = z['paymentInstruments'][0]['count']
                    amount = z['paymentInstruments'][0]['amount']
                    clm['Transacion_type'].append(Name)
                    clm['Transacion_count'].append(count)
                    clm['Transacion_amount'].append(amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass
# Succesfully created a dataframe
Agg_Trans = pd.DataFrame(clm)
#Agg_Trans.to_csv('Agg_trans.csv')
Agg_Trans
# This is to direct the path to get the data as states
path = "data/aggregated/user/country/india/state/"
user_state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<---------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'Brand': [],
    'Brand_count': [], 'Brand_percentage': []}
for i in user_state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["usersByDevice"]:
                    
                    brand = z['brand']

                    brand_count = z['count']
                    brand_percentage = z["percentage"]
                    clm['Brand'].append(brand)
                    clm['Brand_count'].append(brand_count)
                    clm['Brand_percentage'].append(brand_percentage)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
            except:
                pass 
                

user_by_device = pd.DataFrame(clm)
#user_by_device.to_csv('user_by_device.csv')
user_by_device
path = "data/map/transaction/hover/country/india/state/"
state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<-------------------------------------------------------------------------------------------------------------------->#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Transaction_count': [], 'Transaction_amount': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverDataList"]:
                    district = z['name']
                    transaction_count = z['metric'][0]['count']
                    transaction_amount = z['metric'][0]['amount']
                    clm['District'].append(district)
                    clm['Transaction_count'].append(transaction_count)
                    clm['Transaction_amount'].append(transaction_amount)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass   
                

map_transaction = pd.DataFrame(clm)
#map_transaction.to_csv('district_map_transaction.csv')
map_transaction
path = "data/map/user/hover/country/india/state/"
state_list = os.listdir(path)
#Agg_state_list
# Agg_state_list--> to get the list of states in India

#<------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------>#

# This is to extract the data's to create a dataframe

clm = {'State': [], 'Year': [], 'Quater': [], 'District': [],
    'Registered_user': [], 'App_opening': []}
for i in state_list:
    p_i = path+i+"/"
    year = os.listdir(p_i)
    for j in year:
        p_j = p_i+j+"/"
        file = os.listdir(p_j)
        for k in file:
            p_k = p_j+k
            Data = open(p_k, 'r')
            D = json.load(Data)
            try:
                for z in D['data']["hoverData"]:
                    district = z
                    registered_user =  D['data']["hoverData"][z]["registeredUsers"]
                    app_opening = D['data']["hoverData"][z]["appOpens"]
                    clm['District'].append(district)
                    clm['Registered_user'].append(registered_user)
                    clm['App_opening'].append(app_opening)
                    clm['State'].append(i)
                    clm['Year'].append(j)
                    clm['Quater'].append(int(k.strip('.json')))
# Succesfully created a dataframe
            except:
                pass       
                 

district_registering = pd.DataFrame(clm)
#district_registering.to_csv('district_registering_map.csv')
district_registering
