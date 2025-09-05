# ai_learning_tracker.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from flask import Flask, render_template_string, request, jsonify

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
    * **Personalized Nudges:** A simple sentiment analysis engine suggests a nudge based on your mood.
    """
)

# --- Flask App Section ---
app = Flask(__name__)

# Motivational quotes list
motivational_quotes = [
    "Don't watch the clock; do what it does. Keep going.",
    "The only way to do great work is to love what you do.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "The future belongs to those who believe in the beauty of their dreams.",
    "Believe you can and you're halfway there.",
    "You are not weak, you are in a developing stage of your life.",
    "Strength is the product of continuous struggle, not of effortless progress."
]

@app.route('/')
def home():
    """Serves the main HTML file."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mark Tracker & Goal Setter</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Inter', sans-serif;
                background-color: #1a202c;
                color: #e2e8f0;
            }
            .container {
                max-width: 900px;
                margin: auto;
            }
            .message-box {
                position: fixed;
                top: 20px;
                left: 50%;
                transform: translateX(-50%);
                padding: 1rem 2rem;
                border-radius: 0.5rem;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                z-index: 1000;
                opacity: 0;
                transition: opacity 0.5s ease-in-out;
                pointer-events: none;
            }
            .message-box.show {
                opacity: 1;
                pointer-events: auto;
            }
        </style>
    </head>
    <body class="bg-gray-900 text-gray-100 flex items-center justify-center min-h-screen p-4">
        <!-- (rest of your HTML unchanged) -->
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/analyze_marks', methods=['POST'])
def analyze_marks():
    try:
        marks_data = request.json
        if not marks_data:
            return jsonify({"error": "Invalid input"}), 400

        total_marks = sum(item['marks'] for item in marks_data)
        total_subjects = len(marks_data)
        average_marks = total_marks / total_subjects

        weak_subjects = [item for item in marks_data if item['marks'] < average_marks * 0.8]
        weak_subjects_text = ", ".join([f"{item['subject']} ({item['marks']} marks)" for item in weak_subjects])

        if weak_subjects:
            quote = random.choice(motivational_quotes)
        else:
            quote = "Keep up the great work! Consistency is key to mastery."
        
        return jsonify({
            "weak_subjects_text": weak_subjects_text,
            "motivational_quote": quote
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/set_goal', methods=['POST'])
def set_goal():
    try:
        data = request.json
        days = int(data.get('days', 0))
        if days <= 0:
            return jsonify({"error": "Invalid number of days"}), 400

        message = f"You have {days} days to complete your syllabus. Make a detailed plan, break down your tasks, and stay disciplined. You can do this!"
        return jsonify({"message": message})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
