# app.py
import streamlit as st
st.title('Bank Term Deposit Subscription Prediction')

st.text("This Streamlit app visualizes bank marketing data and allows you to use different machine learning models to predict a customer's likelihood to subscribe to a term deposit.")

# Exploratory Data Analysis (EDA) Section Header
st.header('Exploratory Data Analysis')

# Add your EDA code here - assuming you have a separate script for this
# ...

# Model Section Header
st.header('Model')

#  Dropdown to select which ML model to use
selected_model = st.selectbox('Select Model', ('Random Forest', 'Logistic Regression', 'Gradient Boosting'))

# Call your machine learning model function based on selection
if selected_model == 'Random Forest':
    # Call your Random Forest model function here
    # ...
elif selected_model == 'Logistic Regression':
    # Call your Logistic Regression model function here
    # ...
else:
    # Call your Gradient Boosting model function here
    # ...

# Model Evaluation Section Header
st.header('Model Evaluation')

# Add your model evaluation metrics here - assuming you have them in separate variables
# ...

# Display metrics
st.write('Accuracy:', accuracy)
st.write('Precision:', precision)
st.write('Recall:', recall)
st.write('F1-Score:', f1_score)

