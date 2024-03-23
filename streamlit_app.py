import streamlit as st



st.title('Bank Marketing Analysis and Modeling')

# Sidebar for EDA and Dataset
st.sidebar.header('Exploratory Data Analysis')
st.sidebar.write('Content for EDA here...')
st.sidebar.header('Dataset')
st.sidebar.write('Content for Dataset here...')

# Main content - Response Predictor
st.header('Response Predictor')

# Collecting user input
job = st.selectbox('Job', ['housemaid', 'technician', 'admin.', '...'])  # Add all job types here
marital = st.selectbox('Marital', ['divorced', 'married', 'single'])
education = st.selectbox('Education', ['primary', 'secondary', 'tertiary'])
previous = st.slider('Previous', min_value=0, max_value=10, value=0)
salary = st.slider('Salary', min_value=0, max_value=50000, value=20000)
balance = st.slider('Balance', min_value=-5000, max_value=50000, value=0)
duration = st.slider('Duration', min_value=0, max_value=2000, value=500)
pdays = st.slider('Pdays', min_value=-1, max_value=871,value=-1)

model_choice = st.selectbox(
    "Model",
    ("Random Forest", "Logistic Regression", "Gradient Boost")
)

if st.button("Predict"):
    prediction = predict(model_choice,
                         job,
                         marital,
                         education,
                         previous,
                         salary,
                         balance,
                         duration,
                         pdays)  # This function should be defined in your ML file

    # Displaying the prediction result
    if prediction == 1:
        st.success("The client is likely to subscribe to a bank term deposit.")
    else:
        st.error("The client is not likely to subscribe to a bank term deposit.")

# Model Evaluation Section
st.header("Model Evaluation")
accuracy_decision_tree = 0.82  # Replace with actual values after training your model
accuracy_logistic_regression = 0.85  
accuracy_gradient_boosting = 0.86  # Replace with actual values after training your model

st.write(f"Random Forest Accuracy: {accuracy_decision_tree}")
st.write(f"Logistic Regression Accuracy: {accuracy_logistic_regression}")
st.write(f"Gradient Boost Accuracy: {accuracy_gradient_boosting}")
