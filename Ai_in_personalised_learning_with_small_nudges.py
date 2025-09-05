# ai_learning_tracker.py

import streamlit as st
import pandas as pd
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# --- NLTK setup ---
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# --- Session State ---
if "goals" not in st.session_state:
    st.session_state.goals = {}
if "progress" not in st.session_state:
    st.session_state.progress = {}
if "nudge_history" not in st.session_state:
    st.session_state.nudge_history = []

# --- Motivational Quotes ---
motivational_quotes = [
    "Don't watch the clock; do what it does. Keep going.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Believe you can and you're halfway there.",
    "You are not weak, you are in a developing stage of your life.",
    "Strength is the product of continuous struggle, not of effortless progress."
]

# --- Nudge Messages ---
motivational_nudges = [
    "You're doing great! Keep up the fantastic work.",
    "A small step forward is still a step forward. You've got this!",
    "Remember why you started. Every effort counts!",
    "Don't give up! The best projects take time and dedication.",
    "Progress isn't always linear. You're learning, and that's what matters."
]

supportive_nudges = [
    "It's okay to feel stuck. Try taking a short break and come back with fresh eyes.",
    "Having a tough time? Maybe try a different approach or break the problem into smaller pieces.",
    "Remember that frustration is part of the learning process. You can overcome this!",
]

def get_nudge(sentiment_score: float) -> str:
    """Return a motivational or supportive nudge based on sentiment score."""
    if sentiment_score < -0.1:
        nudge = random.choice(supportive_nudges)
    else:
        nudge = random.choice(motivational_nudges)
    st.session_state.nudge_history.append(nudge)
    return nudge

# --- Marks Analysis (converted from Flask endpoint) ---
def analyze_marks(marks_data: list) -> dict:
    """Analyze marks and return weak subjects + a motivational quote."""
    if not marks_data:
        return {"error": "No marks provided."}
    
    total_marks = sum(item['marks'] for item in marks_data)
    total_subjects = len(marks_data)
    average_marks = total_marks / total_subjects

    weak_subjects = [item for item in marks_data if item['marks'] < average_marks * 0.8]
    weak_subjects_text = ", ".join([f"{item['subject']} ({item['marks']} marks)" for item in weak_subjects])

    if weak_subjects:
        quote = random.choice(motivational_quotes)
    else:
        quote = "Keep up the great work! Consistency is key to mastery."
    
    return {"weak_subjects_text": weak_subjects_text, "motivational_quote": quote}

# --- Goal Setter (converted from Flask endpoint) ---
def set_goal(days: int) -> str:
    """Return a motivational goal-setting message based on given days."""
    if days <= 0:
        return "⚠️ Invalid number of days."
    return f"You have {days} days to complete your syllabus. Make a detailed plan, break down your tasks, and stay disciplined. You can do this!"

# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="AI Learning Goal Tracker", page_icon="🧠", layout="wide")

# Sidebar
with st.sidebar:
    st.title("🎯 Set Your Goals")
    new_goal = st.text_input("Enter a new learning goal")
    total_steps = st.number_input("Total steps to complete goal:", min_value=1, value=10, step=1)
    if st.button("Add Goal"):
        if new_goal:
            st.session_state.goals[new_goal] = total_steps
            st.session_state.progress[new_goal] = 0
            st.success(f"Goal '{new_goal}' added!")

# Main UI
st.title("🧠 AI Learning Goal Tracker")

# Progress Tracker
if not st.session_state.goals:
    st.info("No goals yet. Add one from the sidebar.")
else:
    for goal, total_steps in st.session_state.goals.items():
        progress = st.slider(
            f"Progress for {goal}", 
            0, total_steps, 
            st.session_state.progress[goal], 
            key=goal
        )
        st.session_state.progress[goal] = progress
        st.progress(progress/total_steps)
        if progress >= total_steps:
            st.balloons()
            st.success(f"✅ Goal '{goal}' completed!")

# Mood + Nudge Section
st.subheader("💬 How are you feeling about your progress?")
user_input = st.text_area("Type your thoughts here:")

if st.button("Get Nudge"):
    if user_input:
        sentiment_score = sia.polarity_scores(user_input)['compound']
        st.write("Sentiment Score:", sentiment_score)
        st.success(get_nudge(sentiment_score))

# Show Nudge History
if st.session_state.nudge_history:
    st.subheader("📜 Nudge History")
    for nudge in reversed(st.session_state.nudge_history):
        st.caption(nudge)

# Marks Analyzer
st.subheader("📊 Analyze Your Marks")
sample_marks = [
    {"subject": "Math", "marks": 40},
    {"subject": "Science", "marks": 55},
    {"subject": "English", "marks": 70},
]
if st.button("Run Sample Marks Analysis"):
    result = analyze_marks(sample_marks)
    st.write("Weak Subjects:", result["weak_subjects_text"])
    st.info("💡 " + result["motivational_quote"])

# Goal Setter
st.subheader("📅 Goal Setter")
days = st.number_input("Enter days remaining:", min_value=1, value=30, step=1)
if st.button("Set Goal Plan"):
    st.info(set_goal(days))
