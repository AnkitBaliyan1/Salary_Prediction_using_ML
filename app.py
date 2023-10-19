import streamlit as st
import pandas as pd
#from sklearn.linear_model import LinearRegression   
import joblib


st.title("Predict Salary")
st.subheader("Predict salary based on Experience of Candidate")


# user input
name = st.text_input("Name")
experience = st.number_input('Enter the Experience:')
skills = st.number_input("Enter Number of Skills")

# create input dataframe
user_input = pd.DataFrame({
    'x1_experience':[experience],
    'x2_experience ' : [skills]
})
# model
model = joblib.load('output/predict_salary_model.pkl')
predicted_salary = model.predict(user_input)


# Displaying the preidcted output
st.write(name + "'s Predicted Salary(LPA):",predicted_salary[0])


