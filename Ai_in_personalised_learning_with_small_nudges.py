import streamlit as st
import pandas as pd
import random
import nltk
import datetime
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

# --- Setup ---
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# --- Page Config ---
st.set_page_config(page_title="AI Learning Goal Tracker", page_icon="🧠", layout="wide")

# --- State ---
if "goals" not in st.session_state:
    st.session_state.goals = {}
if "progress" not in st.session_state:
    st.session_state.progress = {}
if "history" not in st.session_state:
    st.session_state.history = []  # (goal, progress, date)
if "tests" not in st.session_state:
    st.session_state.tests = []  # (month, subject, marks)
if "subjects" not in st.session_state:
    st.session_state.subjects = ["Maths", "Science", "English", "Social Studies", "Computer"]

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Goal Settings")
    goal = st.text_input("🎯 New Goal", key="goal_input")
    chapters = st.number_input("Total Chapters", 1, 100, 10, key="chapters_input")
    deadline = st.date_input("Deadline", datetime.date.today() + datetime.timedelta(days=7), key="deadline_input")

    if st.button("Add Goal", key="add_goal_btn"):
        if goal.strip() != "":
            st.session_state.goals[goal] = {"chapters": chapters, "deadline": deadline}
            st.session_state.progress[goal] = 0
            st.success(f"Added goal: {goal}")

    st.markdown("---")
    st.subheader("📘 Subjects")
    new_subject = st.text_input("Add new subject", key="new_subject_input")
    if st.button("➕ Add Subject", key="add_subject_btn"):
        if new_subject.strip() != "" and new_subject not in st.session_state.subjects:
            st.session_state.subjects.append(new_subject)
            st.success(f"Added subject: {new_subject}")

# --- Main UI ---
st.title("🧠 AI Learning Goal Tracker")
st.markdown("Track progress, test performance, get nudges, and stay motivated!")

if not st.session_state.goals:
    st.info("No goals yet. Add one from the sidebar 👉")
else:
    for g, info in st.session_state.goals.items():
        st.subheader(f"🎯 {g}")
        progress = st.slider(
            f"{g} progress (in chapters)",
            0,
            info["chapters"],
            st.session_state.progress[g],
            key=f"{g}_progress"
        )
        st.session_state.progress[g] = progress
        st.progress(progress/info["chapters"])
        days_left = (info["deadline"] - datetime.date.today()).days
        st.caption(f"{progress}/{info['chapters']} chapters | Deadline: {info['deadline']} | ⏳ {days_left} days left")

        # Save history
        st.session_state.history.append({"goal": g, "progress": progress, "date": datetime.date.today()})

        # Countdown Nudges
        if days_left <= 3 and progress < info["chapters"] * 0.5:
            st.warning("⚠️ Deadline is very close! Push harder 💪")
        elif days_left <= 7:
            st.info("⏳ Deadline is approaching — stay consistent!")

        if progress >= info["chapters"]:
            st.success("✅ Goal Completed!")
            st.balloons()

# --- Monthly Test Marks ---
st.header("📚 Monthly Test Performance")
month = st.selectbox(
    "Select Month",
    ["January","February","March","April","May","June","July","August","September","October","November","December"],
    key="month_select"
)

marks_data = {}
for subject in st.session_state.subjects:
    marks_data[subject] = st.number_input(
        f"Enter {subject} marks (out of 100)",
        0, 100, 50,
        key=f"{month}_{subject}_marks"
    )

col1, col2 = st.columns(2)
with col1:
    save_marks = st.button("💾 Save Test Marks", key="save_marks_btn")
with col2:
    get_nudge = st.button("💡 Get Nudge", key="get_nudge_btn")

if save_marks:
    for subject, marks in marks_data.items():
        st.session_state.tests.append({"month": month, "subject": subject, "marks": marks})
    st.success(f"✅ Saved subject-wise marks for {month}")

if get_nudge:
    st.info("🔎 Analyzing your marks...")
    if st.session_state.tests:
        df_test = pd.DataFrame(st.session_state.tests)
        for subj in df_test["subject"].unique():
            sub_df = df_test[df_test["subject"] == subj]
            if len(sub_df) > 1:
                if sub_df["marks"].iloc[-1] > sub_df["marks"].iloc[-2]:
                    st.success(f"📈 {subj}: Great improvement this month! 🚀")
                elif sub_df["marks"].iloc[-1] < sub_df["marks"].iloc[-2]:
                    st.warning(f"📉 {subj}: Marks dropped — focus more on this subject 🔎")
                else:
                    st.info(f"➖ {subj}: Consistent marks — aim to push higher!")

if st.session_state.tests:
    df_test = pd.DataFrame(st.session_state.tests)

    # Ensure all 12 months appear in chart
    all_months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    all_data = []
    for subj in st.session_state.subjects:
        for m in all_months:
            val = df_test[(df_test["month"] == m) & (df_test["subject"] == subj)]
            if not val.empty:
                all_data.append({"month": m, "subject": subj, "marks": val["marks"].values[0]})
            else:
                all_data.append({"month": m, "subject": subj, "marks": 0})
    df_test_full = pd.DataFrame(all_data)

    # Display raw marks table
    st.subheader("📊 Test Marks Data")
    st.dataframe(df_test_full)

    # Line chart: subject-wise performance trend
    st.subheader("📈 Subject-wise Performance Trend (Full Year)")
    fig, ax = plt.subplots()
    for subj in df_test_full["subject"].unique():
        sub_df = df_test_full[df_test_full["subject"] == subj]
        ax.plot(sub_df["month"], sub_df["marks"], marker="o", label=subj)
    ax.set_ylabel("Marks")
    ax.set_xlabel("Month")
    ax.set_title("Subject-wise Performance (Jan–Dec)")
    ax.legend()
    st.pyplot(fig)

# --- Analytics Section ---
st.header("📊 Goal Progress Analytics")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    # --- Line Chart: Progress over time ---
    st.subheader("Progress Over Time")
    fig, ax = plt.subplots()
    for goal in df["goal"].unique():
        sub_df = df[df["goal"] == goal]
        ax.plot(sub_df["date"], sub_df["progress"], marker="o", label=goal)
    ax.set_xlabel("Date")
    ax.set_ylabel("Chapters Completed")
    ax.legend()
    st.pyplot(fig)

    # --- Bar Chart: Latest Progress ---
    st.subheader("Latest Goal Progress")
    latest = df.groupby("goal")["progress"].max().reset_index()
    fig, ax = plt.subplots()
    ax.bar(latest["goal"], latest["progress"], color="skyblue")
    ax.set_ylabel("Chapters Completed")
    ax.set_title("Latest Goal Progress")
    st.pyplot(fig)
