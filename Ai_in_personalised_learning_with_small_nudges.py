import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="AI Learning Goal Tracker", layout="wide")

# ----------------------------
# Session State Initialization
# ----------------------------
if "subjects" not in st.session_state:
    st.session_state["subjects"] = ["Maths", "Science", "English"]

if "test_data" not in st.session_state:
    st.session_state["test_data"] = []

# ----------------------------
# Motivational Quotes
# ----------------------------
quotes = [
    "Believe you can and you're halfway there!",
    "Your hard work will pay off!",
    "Don’t stop until you’re proud.",
    "Difficult roads lead to beautiful destinations.",
    "Consistency is the key to success!"
]

# ----------------------------
# Subject Management
# ----------------------------
st.sidebar.header("📘 Subject Manager")

new_subject = st.sidebar.text_input("Add New Subject")
if st.sidebar.button("➕ Add Subject") and new_subject.strip():
    if new_subject not in st.session_state["subjects"]:
        st.session_state["subjects"].append(new_subject)
        st.success(f"Subject '{new_subject}' added!")

remove_subject = st.sidebar.selectbox("Remove Subject", [""] + st.session_state["subjects"])
if st.sidebar.button("🗑 Remove Subject") and remove_subject:
    st.session_state["subjects"].remove(remove_subject)
    st.success(f"Subject '{remove_subject}' removed!")

# ----------------------------
# Monthly Test Entry
# ----------------------------
st.header("📝 Monthly Test Marks Entry")

col1, col2 = st.columns(2)
with col1:
    month = st.selectbox("Select Month", 
        ["Jan","Feb","Mar","Apr","May","Jun",
         "Jul","Aug","Sep","Oct","Nov","Dec"])
with col2:
    subject = st.selectbox("Select Subject", st.session_state["subjects"])

marks = st.number_input("Enter Marks (0-100)", 0, 100)

col_save, col_nudge = st.columns([1,1])

with col_save:
    if st.button("💾 Save Test Marks"):
        st.session_state["test_data"].append({"month": month, "subject": subject, "marks": marks})
        st.success(f"Saved {marks} marks for {subject} in {month}")

# ----------------------------
# Performance Data
# ----------------------------
df_test = pd.DataFrame(st.session_state["test_data"])

if not df_test.empty:
    st.subheader("📊 Test Performance Data")

    # Highlight subjects with <35
    def highlight_low(val):
        color = 'red' if val < 35 else 'black'
        return f'color: {color}'

    st.dataframe(df_test.style.applymap(highlight_low, subset=["marks"]), use_container_width=True)

    # ----------------------------
    # Get Nudges
    # ----------------------------
    with col_nudge:
        if st.button("💡 Get Nudges"):
            avg_score = df_test["marks"].mean()
            if avg_score >= 75:
                nudge = "Excellent! Keep up the great work!"
            elif avg_score >= 50:
                nudge = "Good! But there’s room for improvement."
            else:
                nudge = "Needs more focus and practice."
            st.info(f"{nudge}\n\n✨ {random.choice(quotes)}")

    # ----------------------------
    # Subject-wise Performance Graph
    # ----------------------------
    st.subheader("📈 Subject-wise Performance Over Months")

    fig, ax = plt.subplots()
    for subj in df_test["subject"].unique():
        subj_df = df_test[df_test["subject"] == subj]
        monthly_avg = subj_df.groupby("month")["marks"].mean().reindex(
            ["Jan","Feb","Mar","Apr","May","Jun",
             "Jul","Aug","Sep","Oct","Nov","Dec"]
        )
        ax.plot(monthly_avg.index, monthly_avg.values, marker="o", label=subj)

    ax.set_ylabel("Marks")
    ax.set_xlabel("Months")
    ax.set_title("Performance per Subject Across Months")
    ax.legend(title="Subjects")
    ax.set_ylim(0, 100)
    st.pyplot(fig)

    # ----------------------------
    # Overall Monthly Percentage Graph
    # ----------------------------
    st.subheader("📊 Overall Monthly Performance (%)")

    monthly_avg = df_test.groupby("month")["marks"].mean().reindex(
        ["Jan","Feb","Mar","Apr","May","Jun",
         "Jul","Aug","Sep","Oct","Nov","Dec"]
    )

    fig2, ax2 = plt.subplots()
    ax2.plot(monthly_avg.index, monthly_avg.values, marker="o", color="blue", linewidth=2)
    ax2.set_ylabel("Percentage")
    ax2.set_xlabel("Months")
    ax2.set_title("Overall Monthly Percentage Performance")
    ax2.set_ylim(0, 100)
    st.pyplot(fig2)
