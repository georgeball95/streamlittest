import streamlit as st
from deta import Deta

# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Data to be written to Deta Base
name = st.text_input("Your name")

#read db
db = deta.Base("default2")
db = deta.Base("default")
#get db
db_content = db.fetch().items

signed_up = []
for i in db_content:
    signed_up.append(i["name"])

if name:
    if name in signed_up:
        st.markdown("you have an account")
    else:
        st.markdown("you do not yet have an account")      
