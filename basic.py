import streamlit as st

st.title("First Application - Sum, Subtract 2 numbers")

operation = st.selectbox("Select Operation",['Sum','Subtract'])
num1=st.number_input("Enter First Number")
num2=st.number_input("Enter Second Number ")



if operation == 'Sum':
    output = num1+num2
elif operation == "Subtract":
    output = num1-num2
else:
    pass



st.write(output)

