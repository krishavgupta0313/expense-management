import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)
if not firebase_admin._apps:
    firebase_credential=dict(st.secrets["google_service_account"])
    cred = credentials.Certificate(firebase_credential)
    firebase_admin.initialize_app(cred)
st.set_page_config(
page_title="Create Expense!",
page_icon="💸",) 

db = firestore.client()   
def run():
    Date_Time_of_Expense= st.datetime_input("Enter the date and time of the expense:")
    st.write("Date and time of Expense:",Date_Time_of_Expense)                                  
    Price=st.number_input("Enter money spent:")
    st.write("The price is",Price)
    categories = ["Food","Groceries","Travel","Transport","Shopping","Clothing","Bills & Utilities","Rent","Education","Healthcare","Entertainment","Subscriptions","Electronics","Personal Care","Home Maintenance","Gifts & Donations","Insurance","Fitness","Pets","Other"]
    category=st.selectbox("Select category of expense:",categories)
    st.write("The category of expense:",category)
    item=st.text_input("Enter the item purchased")
    st.write("The thing purchased:",item)
    remark=st.text_input("Any remark or comment about expense:")
    st.write("Remark or comment of expense:",remark)
    if st.button("Add Expense"):
        st.success("Expense added successfully!")
        db.collection("expense-management").add({
        "Date and time": Date_Time_of_Expense,
        "Price": Price,
        "Category": category,
        "Item Purchased": item,
        "Remark": remark,
        
        
    })

if __name__ == "__main__":
    run()
    

