import pandas as pd
import streamlit as st


import firebase_admin
from firebase_admin import credentials, firestore
from streamlit.logger import get_logger
import matplotlib.pyplot as plt

LOGGER = get_logger(__name__)
if not firebase_admin._apps:
    firebase_credential=dict(st.secrets["google_service_account"])
    cred = credentials.Certificate(st.secrets["firebase_credential"])
    firebase_admin.initialize_app(cred)

st.set_page_config(
    page_title="Expense Analysis",
    page_icon="📊",
)

db = firestore.client()

def run():
    st.title("Expense Analysis")

    expensedetails = db.collection("expense-management").stream()
    expense_list = []

    for expense in expensedetails:
        expense_list.append(expense.to_dict())

    if not expense_list:
        st.info("No expenses found")
        return
    df = pd.DataFrame(expense_list)
    category_sum = df.groupby("Category")["Price"].sum()

    fig1, ax1 = plt.subplots()
    ax1.pie(
        category_sum,
        labels=category_sum.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax1.set_title("Money Spent per Category")

    st.pyplot(fig1)
    category_count = df["Category"].value_counts()

    fig2, ax2 = plt.subplots()
    ax2.pie(
        category_count,
        labels=category_count.index,
        autopct="%1.1f%%",
        startangle=90
    )
    ax2.set_title("Number of Expenses per Category")

    st.pyplot(fig2)
    st.title("Monthly Expense Summary")

    expensedetails = db.collection("expense-management").stream()
    expense_list = []

    for expense in expensedetails:
        expense_list.append(expense.to_dict())

    if expense_list:
        df = pd.DataFrame(expense_list)


        df["Date and time"] = pd.to_datetime(df["Date and time"])


        df["Month"] = df["Date and time"].dt.to_period('M')


        monthly_summary = df.groupby("Month")["Price"].sum().reset_index()
        monthly_summary.rename(columns={"Price": "Total Spent"}, inplace=True)

        monthly_summary["Month"] = monthly_summary["Month"].dt.strftime('%b %Y')

        st.dataframe(monthly_summary)

    else:
        st.info("No expenses found.")


if __name__ == "__main__":
    run()
