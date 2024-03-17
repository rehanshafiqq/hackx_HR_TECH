import streamlit as st
from datetime import date

expenses = []

def add_expense():
  date = st.date_input("Date")
  category = st.selectbox("Category", ["Food", "Transportation", "Rent", "Utilities", "Other"])
  amount = st.number_input("Amount", min_value=0.01)
  description = st.text_input("Description (optional)")

  if all([date, category, amount]):
    expenses.append({"date": date.strftime("%Y-%m-%d"), "category": category, "amount": amount, "description": description})
    st.success("Expense added successfully!")
  else:
    st.warning("Please fill in all required fields!")

def view_expenses():
  if not expenses:
    st.info("No expenses found!")
    return
  st.subheader("Expenses")
  # Display total expenses
  total_amount = sum(expense["amount"] for expense in expenses)
  st.write(f"Total Expenses: {total_amount:.2f}")
  st.table(expenses)

def delete_expense(index):
  expenses.pop(index)
  st.success("Expense deleted successfully!")

st.title("Employee Expense Management System")

# Add expense section
st.header("Add Expense")
add_expense()

# View expenses section
st.header("View Expenses")
view_expenses()

# Delete expense functionality
if expenses:
  for index, expense in enumerate(expenses):
    if st.button(f"Delete Expense: {expense['date']} - {expense['category']}", key=index):
      delete_expense(index)
      break

