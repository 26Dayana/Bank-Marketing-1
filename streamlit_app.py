# app.py
import streamlit as st
st.title('Bank Term Deposit Subscription Prediction')

# Main function
def main():

    # SIDEBAR CONTENT
    st.sidebar.title("Bank Customer Term Deposit Predictor")
    st.sidebar.write(
        """
        The ability to accurately predict customer tendencies in subscribing to a term deposit holds immense significance for banks. 
    \nBy leveraging machine learning techniques, banks can gain valuable insights into customer behavior and preferences, enabling them to make informed decisions regarding their marketing strategies and product offerings. 
    \nThis predictive capability allows banks to optimize their resources, tailor their communication efforts, and effectively allocate their marketing budgets, ultimately leading to improved customer acquisition, retention, and profitability. 
    \nFurthermore, by identifying potential customers who are more likely to subscribe to a term deposit, banks can enhance their overall risk management and optimize their loan portfolios, thereby strengthening their financial stability and resilience.
        """
    )

    # Social Hubs
    st.sidebar.markdown(

    """
    <div stlye="{}">
        <h3> Follow My Social Hubs For More Content </h3>
        <ul>
            <li><a href="https://medium.com/@bauglir">Medium</a></li>
            <li><a href="https://www.kaggle.com/dfavenfre">Kaggle</a></li>
            <li><a href="https://github.com/dfavenfre">GitHub</a></li>
            <li><a href="https://www.linkedin.com/in/tolga-%C5%9Fakar-575b86136">LinkedIn</a></li>
         </ul>  
    
    """, unsafe_allow_html=True

    )
    # MAIN PAGE CONTENT
    st.title("Predict Customer Tendency")
