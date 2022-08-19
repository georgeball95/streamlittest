import streamlit as st
from deta import Deta

# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Data to be written to Deta Base
name = st.text_input("Your name")

#read db
db = deta.Base("default")
#get db
db_content = db.fetch().items

if name:

    for i in db_content:

        #st.markdown(i)

        if i["name"] == name:

            st.markdown("you have an account")
        else:
            st.markdown("you do not yet have an account")      

    
    #st.write(db_content)
