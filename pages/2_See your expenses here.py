import pandas as pd
import streamlit as st
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

if not firebase_admin._apps:
    cred = credentials.Certificate(
        r'C:\Users\Sachin\Desktop\expense-management\firestore-expense-management.json'
    )
    firebase_admin.initialize_app(cred)

st.set_page_config(
    page_title="See your expenses here!",
    page_icon="💸",
)

db = firestore.client()

def run():
    st.title("Your Expenses")

    expensedetails = db.collection("expense-management").stream()
    expense_list = []

    for expense in expensedetails:
        data = expense.to_dict()
        data["_doc_id"] = expense.id
        expense_list.append(data)

    if not expense_list:
        st.info("No expenses found")
        return

    df = pd.DataFrame(expense_list)
    df["Date and time"] = pd.to_datetime(df["Date and time"])

    df = df[
        [
            "_doc_id",
            "Date and time",
            "Price",
            "Category",
            "Item Purchased",
            "Remark",
        ]
    ]

    edited_df = st.data_editor(
        df,
        disabled=["_doc_id"],
        column_config={
            "_doc_id": None,
            "Date and time": st.column_config.DatetimeColumn(
                "Date and time",
                format="DD MMM YYYY, hh:mm A",
                step=60,
            ),
            "Price": st.column_config.NumberColumn(
                "Price",
                min_value=0,
            ),
        },
        use_container_width=True,
    )

    if st.button("Save Changes"):
        for _, row in edited_df.iterrows():
            db.collection("expense-management").document(row["_doc_id"]).update(
                {
                    "Date and time": row["Date and time"],
                    "Price": row["Price"],
                    "Category": row["Category"],
                    "Item Purchased": row["Item Purchased"],
                    "Remark": row["Remark"],
                }
            )
        st.success("Saved")

if __name__ == "__main__":
    run()
