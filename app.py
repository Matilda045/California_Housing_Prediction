
import pickle
import streamlit as st
import pandas as pd


# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Housing Predictor")

# Input widgets for getting user values for X (feature matrix value)

housing_median_age = st.slider("housing_median_age", min_value=0, max_value=100, value=20)

# Changed to number input
total_rooms = st.number_input("total_rooms", min_value=0, max_value=40000, value=100)  
median_income = st.number_input("median_income", min_value=0.0, max_value=100.0, value=20.0) 


# After selecting features, the user then submits the median house value
if st.button("Predict"):
  # take the house value, and format the value the right way
  prediction = model.predict([[housing_median_age, total_rooms, median_income]])[0].round(2)
  st.write("The predicted median house value is", prediction, "dollars")
