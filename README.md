# Expense Management

## Overview:

1. This project implements an Expense Management System using Streamlit and Firestore.
2. Users can create expenses by entering date & time, price, category, item purchased, and remarks.
3. Users can see and edit expenses on the See Your Expenses Here page.
4. Users can analyze expenses using pie charts and a Monthly Expense Summary table on the Expense Analysis page.

## Prerequisites:

1.	Python 
2. Streamlit 
3. Visual Studio Code
2.	Firebase account with Firestore database
3. Firebase service account JSON file
4.	Python libraries:
streamlit, firebase_admin, matplotlib

## How to set up Firestore account:

1.	Go to Firebase Console
2.	Sign up or log in
3.	Create a new project
4.	Enable Firestore Database
5.	Create a service account → download the JSON file
6.	Save JSON file in project folder and use it in app

## How to store data in Firestore:

On create expense page:
1. User inputs date & time, price, category, item purchased, remarks
2.	Clicks Add Expense
3. App stores data in Firestore:
4. For details refer to this [Create Expense page](pages/1_Create%20Expense.py) 
5. The statement which stores data in database:
```
db.collection("expense-management").add({
    "Date and time": Date_Time_of_Expense,
    "Price": Price,
    "Category": category,
    "Item Purchased": item,
    "Remark": remark
})
```
## How to install and run


### Create .venv environment
1. select the app folder
2. select requirements.txt(containing all libraries to be installed, eg. streamlit, firebase_admin, matplotlib )
3. create environment

### How to add delta changes
1. Add the new libraries to be installed in the requirements.txt
2. Save the file
3. Open the main python file in integrated terminal by right clicking on it and selecting the option of opening in integrated terminal
4. Write the command:
```
streamlit add -r requirements.txt

```
5. The libraries will get installed 

### Running the App:
1.	Open in integrated terminal
2.	Navigate to project folder
3.	Run the app:
```
streamlit run expensemanagement.py
```
4.	Open your browser at:
   http://localhost:8501


## How expenses are displayed:

On See Your Expenses Here page:
1. App retrieves all expenses from Firestore:
   expensedetails = db.collection("expense-management").stream()
2. Data is displayed in a table using st.data_editor
3. Users can edit any cell
4. Changes are saved back to Firestore:
```
db.collection("expense-management").document(row["_doc_id"]).update({
    "Date and time": row["Date and time"],
    "Price": row["Price"],
    "Category": row["Category"],
    "Item Purchased": row["Item Purchased"],
    "Remark": row["Remark"]
})
```
5. For details refer to this [See your expenses page](./pages/2_See%20your%20expenses%20here.py) 

## How analysis works:

On Expense Analysis page:
1. Retrieve all expenses from Firestore
2. Create DataFrame for analysis
3. Generate Pie Charts:
 Money Spent per Category (sum of prices per category)
 Number of Expenses per Category
4. Generate Monthly Expense Summary Table:
5. Group expenses by month
6. Sum Price for each month
7. Display table with month and total spent
8. For details refer to this [Expense Analysis page](./pages/3_Expense%20Analysis.py) 

