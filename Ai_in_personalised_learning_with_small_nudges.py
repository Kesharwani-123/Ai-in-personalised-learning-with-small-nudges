import streamlit as st
import pandas as pd
import random
import nltk
import datetime
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

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

# --- Sidebar ---
with st.sidebar:
    st.title("⚙️ Goal Settings")
    goal = st.text_input("🎯 New Goal")
    steps = st.number_input("Total Steps", 1, 100, 10)
    deadline = st.date_input("Deadline", datetime.date.today() + datetime.timedelta(days=7))

    if st.button("Add Goal"):
        st.session_state.goals[goal] = {"steps": steps, "deadline": deadline}
        st.session_state.progress[goal] = 0
        st.success(f"Added goal: {goal}")

# --- Main UI ---
st.title("🧠 AI Learning Goal Tracker")
st.markdown("Track progress, get nudges, and stay motivated!")

if not st.session_state.goals:
    st.info("No goals yet. Add one from the sidebar 👉")
else:
    for g, info in st.session_state.goals.items():
        st.subheader(f"🎯 {g}")
        progress = st.slider(f"{g} progress", 0, info["steps"], st.session_state.progress[g], key=g)
        st.session_state.progress[g] = progress
        st.progress(progress/info["steps"])
        st.caption(f"{progress}/{info['steps']} steps | Deadline: {info['deadline']}")

        # Save history
        st.session_state.history.append({"goal": g, "progress": progress, "date": datetime.date.today()})

        if progress >= info["steps"]:
            st.success("✅ Goal Completed!")
            st.balloons()

# --- Mood Check ---
st.header("💬 How do you feel?")
mood = st.text_area("Write your thoughts...")
if st.button("Get Nudge") and mood:
    score = sia.polarity_scores(mood)['compound']
    if score > 0.2:
        st.success("🚀 You're on fire! Keep the energy alive 🔥")
    elif score < -0.2:
        st.warning("😔 Feeling low? Take a break, then get back stronger 💪")
    else:
        st.info("🙂 Stay consistent, you’re on the right track!")

# --- Analytics Section ---
st.header("📊 Progress Analytics")
if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)
    line_chart = px.line(df, x="date", y="progress", color="goal", markers=True, title="Progress Over Time")
    st.plotly_chart(line_chart, use_container_width=True)

    latest = df.groupby("goal")["progress"].max().reset_index()
    bar_chart = px.bar(latest, x="goal", y="progress", title="Latest Goal Progress", text="progress")
    st.plotly_chart(bar_chart, use_container_width=True)
