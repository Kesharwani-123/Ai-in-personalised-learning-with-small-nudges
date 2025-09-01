# This file tells Streamlit where to find your main application.
import src.main_app
import streamlit as st
from analytics.visualizations import display_user_progress_chart

def main():
    """
    Main function to run the Streamlit application.
    """
    st.title("Personalized Learning Dashboard")
    st.write("Welcome to your dashboard! Here's a summary of your progress.")
    
    # Display the user progress chart from the visualizations module
    display_user_progress_chart()

if __name__ == "__main__":
    main()
