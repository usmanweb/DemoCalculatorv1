import streamlit as st

# Set the title
st.title("Simple Calculator")

# Input numbers
num1 = st.number_input("Enter the first number:", value=0.0, step=1.0, format="%.2f")
num2 = st.number_input("Enter the second number:", value=0.0, step=1.0, format="%.2f")

# Choose operation
operation = st.selectbox("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Add":
        result = num1 + num2
    elif operation == "Subtract":
        result = num1 - num2
    elif operation == "Multiply":
        result = num1 * num2
    elif operation == "Divide":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed!")

    # Display result
    if result is not None:
        st.success(f"The result is: {result}")
