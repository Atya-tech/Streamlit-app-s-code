import streamlit as st
from streamlit_option_menu import option_menu
import home,account,about,contact,products,application1,services

st.set_page_config(page_title='My App',layout='wide')
st.markdown(f'''<style> .appview-container .main .block-container {{ 
            padding-top: 2rem;
            padding-bottom:2rem;
            padding-left:2rem;
            padding-right:2rem;
            color:white;
            background-color:#020b4f; 
            }}
            
            </style>''',unsafe_allow_html=True)
def run():
        select=option_menu(
                menu_title='Menu bar',
                options=['Home','Products','Applications','Services','About Us','Contact Us','Account'],
                icons=["house","cpu-fill",'window','person-gear',"envelope","person-lines-fill","person-circle",],
                orientation='horizontal',
                )
        if select=='Applications':
            application1.dashboard()
        if select=='Home':
            home.app()
        if select=='Account':
            account.app()
        if select=='About Us':
            about.app()
        if select=='Contact Us':  
            contact.app()
        if select=='Products':
            products.app()
        if select=='Services':
            services.app()
        
if __name__ =='__main__':
    run()

