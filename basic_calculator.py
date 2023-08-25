import streamlit as st

st.title("Simple Calculator")

# Input fields for the user to enter numbers
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")

# Dropdown to select the operation
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate the result based on the selected operation
if operation == "Add":
    result = num1 + num2
elif operation == "Subtract":
    result = num1 - num2
elif operation == "Multiply":
    result = num1 * num2
elif operation == "Divide":
    if num2 != 0:  # Avoid division by zero
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

# Display the result
st.write("Result:", result)

