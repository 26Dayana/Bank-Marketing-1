# app.py
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict(term_deposit_data):
    # Assuming your model takes a DataFrame as input
    prediction = model.predict(term_deposit_data)
    return prediction

def main():
    st.title('Bank Term Deposit Subscription Prediction')

    # Sidebar
    st.sidebar.header('User Input Features')
    # You can add input fields here for user input features

    # Load example data
    example_data = pd.read_csv('example_data.csv')  # Load some example data for demonstration
    st.subheader('Example Data')
    st.write(example_data)

    # Make predictions
    if st.button('Predict'):
        prediction = predict(example_data)
        st.subheader('Prediction')
        st.write(prediction)

if __name__ == '__main__':
    main()
