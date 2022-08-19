import streamlit as st
from deta import Deta

# Data to be written to Deta Base
name = st.text_input("Your name")

# Create a new database "example-db"
# If you need a new database, just use another name.
db = deta.Base("default")

if name:
    db.put({"name": name, "age": age})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch(user=name).items
st.write(db_content)
