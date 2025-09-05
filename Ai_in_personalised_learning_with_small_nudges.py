import streamlit as st
import pandas as pd
import random
import nltk
import datetime
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer

# --- Setup NLTK ---
try:
    nltk.data.find("sentiment/vader_lexicon")
except LookupError:
    nltk.download("vader_lexicon")

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
    st.title("⚙️ Goal & Subject Settings")

    # Goal Management
    st.subheader("🎯 Add New Goal")
    goal = st.text_input("Goal Name")
    chapters = st.number_input("Total Chapters", 1, 100, 10)
    deadline = st.date_input("Deadline", datetime.date.today() + datetime.timedelta(days=7))

    if st.button("Add Goal"):
        st.session_state.goals[goal] = {"chapters": chapters, "deadline": deadline}
        st.session_state.progress[goal] = 0
        st.success(f"✅ Added goal: {goal}")

    # Subject Manager
    st.subheader("📚 Manage Subjects")
    new_subject = st.text_input("➕ Add Subject")
    if st.button("Add Subject"):
        if new_subject and new_subject not in st.session_state.subjects:
            st.session_state.subjects.append(new_subject)
            st.success(f"✅ Added subject: {new_subject}")
        elif new_subject in st.session_state.subjects:
            st.warning("⚠️ Subject already exists.")

    if st.session_state.subjects:
        remove_subject = st.selectbox("➖ Remove Subject", st.session_state.subjects)
        if st.button("Remove Subject"):
            st.session_state.subjects.remove(remove_subject)
            st.success(f"❌ Removed subject: {remove_subject}")

# --- Main UI ---
st.title("🧠 AI Learning Goal Tracker")
st.markdown("Track progress, test performance, get nudges, and stay motivated!")

# --- Goal Progress Tracker ---
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
            key=f"goal_{g}"
        )
        st.session_state.progress[g] = progress
        st.progress(progress / info["chapters"])
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

# --- Mood Check ---
st.header("💬 How do you feel?")
mood = st.text_area("Write your thoughts...")

# --- Monthly Test Marks ---
st.header("📚 Monthly Test Performance")
month = st.selectbox(
    "Select Month", 
    ["January","February","March","April","May","June","July","August",
     "September","October","November","December"]
)

marks_data = {}
for subject in st.session_state.subjects:
    marks_data[subject] = st.number_input(f"Enter {subject} marks (out of 100)", 0, 100, 50, key=f"{month}_{subject}")

col1, col2 = st.columns(2)
with col1:
    if st.button("Save Test Marks"):
        for subject, marks in marks_data.items():
            st.session_state.tests.append({"month": month, "subject": subject, "marks": marks})
        st.success(f"✅ Saved subject-wise marks for {month}")

with col2:
    if st.button("Get Nudges"):
        if st.session_state.tests:
            df_test = pd.DataFrame(st.session_state.tests)
            avg_score = df_test.groupby("subject")["marks"].mean().mean()

            # Generate nudge
            if avg_score >= 75:
                st.success("🚀 Outstanding! You're consistently performing well! ⭐")
                st.info("💡 Quote: 'Success is the sum of small efforts, repeated day in and day out.'")
            elif avg_score >= 50:
                st.info("🙂 Good job! Keep pushing to reach higher scores 💪")
                st.info("💡 Quote: 'Consistency is the key to mastery.'")
            else:
                st.warning("⚠️ You need more practice. Focus on weak subjects 🔎")
                st.info("💡 Quote: 'Failure is simply the opportunity to begin again, this time more intelligently.'")

# --- Display Test Marks & Graphs ---
if st.session_state.tests:
    df_test = pd.DataFrame(st.session_state.tests)

    # Highlight marks < 35
    st.subheader("📊 Test Marks Data")
    def highlight_low(val):
        return "color: red; font-weight: bold;" if val < 35 else "color: black"
    styled_df = df_test.style.applymap(highlight_low, subset=["marks"])
    st.dataframe(styled_df)

    # Subject-wise Performance Graph
    st.subheader("📈 Subject-wise Performance")
    fig, ax = plt.subplots()
    for subj in df_test["subject"].unique():
        sub_df = df_test[df_test["subject"] == subj]
        ax.bar(subj, sub_df["marks"].mean())
    ax.set_ylabel("Average Marks")
    ax.set_xlabel("Subjects")
    ax.set_title("Average Marks per Subject")
    st.pyplot(fig)

# --- Analytics Section ---
st.header("📊 Goal Progress Analytics")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    # Line Chart: Progress over time
    st.subheader("Progress Over Time")
    fig, ax = plt.subplots()
    for goal in df["goal"].unique():
        sub_df = df[df["goal"] == goal]
        ax.plot(sub_df["date"], sub_df["progress"], marker="o", label=goal)
    ax.set_xlabel("Date")
    ax.set_ylabel("Chapters Completed")
    ax.legend()
    st.pyplot(fig)

    # Bar Chart: Latest Progress
    st.subheader("Latest Goal Progress")
    latest = df.groupby("goal")["progress"].max().reset_index()
    fig, ax = plt.subplots()
    ax.bar(latest["goal"], latest["progress"], color="skyblue")
    ax.set_ylabel("Chapters Completed")
    ax.set_title("Latest Goal Progress")
    st.pyplot(fig)
