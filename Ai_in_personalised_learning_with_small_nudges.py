# ai_learning_tracker.py

import streamlit as st
import pandas as pd
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK data if not already present
try:
    nltk.data.find('sentiment/vader_lexicon')
except LookupError:
    nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# --- Page Configuration ---
st.set_page_config(
    page_title="AI Learning Goal Tracker",
    page_icon="🧠",
    layout="wide",
)

# --- Inject custom CSS ---
st.markdown(
    """
    <style>
    .main {
        max-width: 900px;
        margin: auto;
        padding: 20px;
    }
    .message-box {
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        padding: 1rem 2rem;
        border-radius: 0.5rem;
        background-color: #2563eb;
        color: white;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        z-index: 1000;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Session State Initialization ---
if "goals" not in st.session_state:
    st.session_state.goals = {}
if "progress" not in st.session_state:
    st.session_state.progress = {}
if "nudge_history" not in st.session_state:
    st.session_state.nudge_history = []
if "user_mood" not in st.session_state:
    st.session_state.user_mood = ""
if "sentiment" not in st.session_state:
    st.session_state.sentiment = 0.0

# --- Nudge Messages and Logic ---
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

def get_nudge(sentiment_score):
    if sentiment_score < -0.1:
        nudge = random.choice(supportive_nudges)
        st.session_state.nudge_history.append(f"Supportive Nudge: {nudge}")
        return nudge
    else:
        nudge = random.choice(motivational_nudges)
        st.session_state.nudge_history.append(f"Motivational Nudge: {nudge}")
        return nudge

# --- Sidebar for Goal Setting ---
with st.sidebar:
    st.title("Set Your Goals")
    st.markdown("Use this to define your learning objectives.")

    new_goal = st.text_input("Enter a new learning goal (e.g., 'Complete Python course')")
    total_steps = st.number_input("Total steps to complete the goal:", min_value=1, value=10, step=1)

    if st.button("Add Goal"):
        if new_goal:
            st.session_state.goals[new_goal] = total_steps
            st.session_state.progress[new_goal] = 0
            st.success(f"Goal '{new_goal}' added!")
        else:
            st.warning("Please enter a goal name.")

# --- Main Application Layout ---
st.title("🧠 AI Learning Goal Tracker")
st.markdown("Track your learning goals and get smart, personalized nudges to stay motivated!")
st.info("💡 **Tip:** Interact with the app to see the nudges appear!")

# --- Progress Tracking and Nudges ---
st.header("Your Progress")

if not st.session_state.goals:
    st.info("You haven't set any goals yet. Use the sidebar to add your first one!")
else:
    for goal, total_steps in st.session_state.goals.items():
        st.subheader(f"🎯 {goal}")

        current_progress_percent = st.slider(
            "Progress:",
            min_value=0,
            max_value=total_steps,
            value=st.session_state.progress.get(goal, 0),
            key=f"slider_{goal}"
        )
        st.session_state.progress[goal] = current_progress_percent

        progress_percentage = (current_progress_percent / total_steps)
        st.progress(progress_percentage)
        st.write(f"{current_progress_percent}/{total_steps} steps complete.")

        if current_progress_percent >= total_steps:
            st.balloons()
            st.success(f"Congratulations! You completed the goal: '{goal}'")

# --- Sentiment-based Nudge Engine ---
st.header("How are you feeling about your progress?")
user_input = st.text_area("Express your feelings here:", key="mood_input", height=50)

if st.button("Get Nudge"):
    if user_input:
        sentiment_score = sia.polarity_scores(user_input)['compound']
        st.session_state.sentiment = sentiment_score
        st.markdown("---")
        st.subheader("Personalized Nudge")
        st.success(get_nudge(sentiment_score))

# --- Historical Nudges ---
if st.session_state.nudge_history:
    st.subheader("Nudge History")
    for nudge in reversed(st.session_state.nudge_history):
        st.caption(nudge)

# --- About this App ---
st.markdown("---")
st.subheader("About This App")
st.markdown(
    """
    This is a prototype of an AI-powered learning goal tracker.
    
    * **Goal Setting:** Set your goals and track your progress.
    * **Progress Monitoring:** See your progress visually with the progress bar.
    * **Personalized Nudges:** Sentiment analysis suggests a motivational or supportive nudge.
    """
)
