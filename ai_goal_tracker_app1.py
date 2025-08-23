Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> visual_features.py
... import streamlit as st
... import matplotlib.pyplot as plt
... import pandas as pd
... 
... def show_progress_chart(data):
...     st.subheader("📊 Learning Progress Over Time")
... 
...     fig, ax = plt.subplots()
...     ax.plot(data["date"], data["score"], marker="o", linestyle="-")
...     ax.set_xlabel("Date")
...     ax.set_ylabel("Score")
...     ax.set_title("Learning Progress")
...     st.pyplot(fig)
... 
... def show_distribution_chart(data):
...     st.subheader("📈 Score Distribution")
... 
...     fig, ax = plt.subplots()
...     ax.hist(data["score"], bins=10, alpha=0.7)
...     ax.set_xlabel("Score")
...     ax.set_ylabel("Frequency")
...     ax.set_title("Score Distribution")
...     st.pyplot(fig)
... from visual_features import show_progress_chart, show_distribution_chart
... 
... # Example usage with dummy data
... import pandas as pd
... 
... data = pd.DataFrame({
...     "date": pd.date_range(start="2025-01-01", periods=10, freq="D"),
...     "score": [60, 65, 70, 72, 74, 80, 78, 82, 85, 90]
... })
... 
... show_progress_chart(data)
... show_distribution_chart(data)
