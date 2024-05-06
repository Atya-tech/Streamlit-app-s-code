import streamlit as st
from streamlit_option_menu import option_menu
import psycopg2,time,home
import matplotlib.pyplot as plt
import plotly.express as px   
from datetime import date, timedelta,datetime
from pandas import to_datetime,DataFrame,date_range
#database
def init_connection1():
    return psycopg2.connect(**st.secrets['postgres'])

connection=init_connection1()

def run_query1(query):
    with connection.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

Pharma={'Device1':['temperature','humidity','pressure','co2'],'Device2':['Temperature','Humidity'],'Device3':['BRIGHTNESS SENSOR','COLOR SENSOR','CONTRAST SENSOR','UV LUMINESCENCE SENSOR']}
Agricultural={'Device4':['Temperature','Gas','Humidity','Pressure','Wind'],'Device5':['BRIGHTNESS SENSOR','COLOR SENSOR','CONTRAST SENSOR','UV LUMINESCENCE SENSOR'],'device6':['LABEL SENSOR','OPACITY SENSOR','PARTICULATE MONITORING SENSOR','TIN-SIDE SENSOR'],'Device7':['BRIGHTNESS SENSOR','COLOR SENSOR','CONTRAST SENSOR','UV LUMINESCENCE SENSOR']}
Automotive=['Device13','Device14','device15','Device16','Device17']
Electronics=['Device18','Device19','device20','Device21','Device22']

def dashboard():
    with st.sidebar:
        select=option_menu(
                    menu_title='Applications',
                    options=['Pharma','Node-red','Fault-Finder','Automotive','Electronics','Live'],
                    icons=['house-gear','house-gear','house-gear','house-gear','house-gear','house-gear'],
                    )
    st.cache_data.clear()

    if select=='Pharma':
        industry(Pharma,'Pharma')
    elif select== "Node-red":
        nodered()
    elif select== 'Fault-Finder':
        fault_finder()
    elif select=='Automotive':
        automotive()
    elif select=='Electronics':
        electronics()
    else:
        live_logs()
    '''ind1=select
    while ind1:
        industry(select,ind1)'''
    

def live_logs():
    pass


def industry(devices,industry):
    pass
    

    
def nodered():
    pass


def fault_finder():
     
        def embed_node_red_dashboard():
            node_red_dashboard_url = 'http://localhost:3000/d/ddibh3pxmskcgf/battery-voltage?orgId=1&refresh=5s&from=1713740847703&to=1713762447703'
            st.write(f'<iframe src="{node_red_dashboard_url}" width=100% height=800px frameborder="0"></iframe>', unsafe_allow_html=True)

        embed_node_red_dashboard()
def color(value):
    pass

def electronics():
    pass
def automotive():
    pass