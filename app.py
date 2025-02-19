
import pickle
import streamlit as st
import pandas as pd


# load the file that contains the model (model.pkl)
with open("model.pkl", "rb") as f:
  model = pickle.load(f)

# give the Streamlit app page a title
st.title("Housing Predictor")

# input widget for getting user values for X (feature matrix value)
latitude = st.slider("latitude", min_value=0, max_value=100, value=20)
housing_median_age = st.slider("housing_median_age", min_value=0, max_value=100, value=20)
total_rooms = st.slider("total_rooms", min_value=0, max_value=40000, value=100)
median_income = st.slider("median_income", min_value=0, max_value=100, value=20)
ocean_proximity = st.slider("<1H OCEAN", min_value=0, max_value=1, value=1)

# After selecting features, the user then submits the median house value
if st.button("Predict"):
  # take the house value, and format the value the right way
  prediction = model.predict([[latitude, housing_median_age, total_rooms, median_income, ocean_<1H OCEAN]])[0].round(2)
  st.write("The predicted median house value is", prediction, "dollars")
