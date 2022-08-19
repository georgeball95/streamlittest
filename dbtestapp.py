import streamlit as st
from deta import Deta
import pandas as pd

t = st.text_input("write some text")

# Connect to Deta Base with your Project Key
deta = Deta(st.secrets["deta_key"])

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("example-db")

name = st.text_input("write username")
number = st.number_input("write id")

tick = st.checkbox("submit?")

if tick:

    db.put({"user_id": number, "username": name})

    st.markdown(f"new user profile added: **{name}**")

    db_content = db.fetch().items
    st.write(db_content)

