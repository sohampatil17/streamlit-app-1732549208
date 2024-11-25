import streamlit as st
import numpy as np

# Cache the data
@st.cache_data
def calculate_result(num1, num2, operation):
    try:
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                return num1 / num2
            else:
                return "Error: Division by zero is not allowed"
        else:
            return "Error: Invalid operation"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title("Calculator App")

    # Get user input
    num1 = st.number_input("Enter the first number", min_value=-1000, max_value=1000)
    num2 = st.number_input("Enter the second number", min_value=-1000, max_value=1000)
    operation = st.selectbox("Select an operation", ["add", "subtract", "multiply", "divide"])

    # Calculate result
    result = calculate_result(num1, num2, operation)

    # Display result
    st.write("Result:")
    st.write(result)

    # Display error message if any
    if isinstance(result, str) and result.startswith("Error"):
        st.error(result)

if __name__ == "__main__":
    main()