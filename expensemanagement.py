import streamlit as st
from streamlit.logger import get_logger
LOGGER = get_logger(__name__)
st.set_page_config(
page_title="Expense Management!",
page_icon="💸",)
def run():
    st.title("Expense Management 💸 !")
    st.subheader("You can manage your day to day expenses here!")

    st.sidebar.success("Select a tab above.")
        

if __name__ == "__main__":
    run()


