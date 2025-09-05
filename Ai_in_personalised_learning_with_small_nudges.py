# ai_learning_tracker.py

# Import necessary libraries
import streamlit as st
import pandas as pd
import random
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK data if not already present
# The 'vader_lexicon' is used for a simple sentiment analysis
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
        A positive mood gets a motivational nudge, while a negative mood gets a supportive one.
        from flask import Flask, render_template_string, request, jsonify
import random

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

        <div id="app" class="bg-gray-800 p-8 rounded-2xl shadow-2xl w-full max-w-2xl">
            <div id="message-container" class="message-box bg-blue-600 text-white"></div>
            <h1 class="text-3xl sm:text-4xl font-bold mb-6 text-center text-blue-400">Mark Tracker & Goal Setter</h1>
            <p class="text-center mb-6 text-gray-400">Enter your marks for each subject to see where you can improve and get motivated!</p>

            <form id="marks-form" class="space-y-6">
                <div class="space-y-4">
                    <!-- Subject Input Fields -->
                </div>
                <div class="flex flex-col sm:flex-row space-y-4 sm:space-y-0 sm:space-x-4">
                    <button type="button" id="add-subject-btn" class="w-full sm:w-1/2 bg-gray-600 hover:bg-gray-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-300 transform hover:scale-105">Add Subject</button>
                    <button type="submit" class="w-full sm:w-1/2 bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-300 transform hover:scale-105">Analyze Marks</button>
                </div>
            </form>

            <div id="result-area" class="mt-8 hidden">
                <div id="weak-subjects-section" class="mb-6 p-6 bg-gray-700 rounded-lg shadow-inner">
                    <h2 class="text-2xl font-semibold text-red-400 mb-4">Subjects to Focus On:</h2>
                    <p id="weak-subjects-list" class="text-lg text-gray-300"></p>
                    <div id="quote-area" class="mt-4 p-4 bg-gray-600 rounded-lg border-l-4 border-blue-400">
                        <p class="italic text-gray-300"></p>
                    </div>
                </div>

                <div id="goal-setting-section" class="p-6 bg-gray-700 rounded-lg shadow-inner">
                    <h2 class="text-2xl font-semibold text-green-400 mb-4">Set Your Study Goal:</h2>
                    <div class="relative mb-4">
                        <label for="goal-time" class="block text-sm font-medium text-gray-400 mb-2">How many days do you have to complete your syllabus?</label>
                        <input type="number" id="goal-time" class="w-full p-3 pr-10 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="e.g., 30" required>
                    </div>
                    <button id="set-goal-btn" class="w-full bg-green-600 hover:bg-green-700 text-white font-semibold py-3 px-6 rounded-lg transition duration-300 transform hover:scale-105">Set Goal</button>
                    <div id="goal-message" class="mt-4 text-center p-4 bg-gray-600 rounded-lg border-l-4 border-green-400 hidden">
                        <p class="text-lg font-medium"></p>
                    </div>
                </div>
            </div>
        </div>

        <script>
            const marksForm = document.getElementById('marks-form');
            const addSubjectBtn = document.getElementById('add-subject-btn');
            const resultArea = document.getElementById('result-area');
            const weakSubjectsList = document.getElementById('weak-subjects-list');
            const quoteArea = document.getElementById('quote-area').querySelector('p');
            const setGoalBtn = document.getElementById('set-goal-btn');
            const goalMessage = document.getElementById('goal-message').querySelector('p');
            const goalMessageContainer = document.getElementById('goal-message');
            const messageContainer = document.getElementById('message-container');

            function showMessage(text, isError = false) {
                messageContainer.textContent = text;
                messageContainer.className = isError
                    ? 'message-box show bg-red-600 text-white'
                    : 'message-box show bg-blue-600 text-white';
                setTimeout(() => {
                    messageContainer.className = 'message-box';
                }, 3000);
            }

            function addSubjectInput() {
                const subjectCount = marksForm.querySelectorAll('.subject-input-group').length;
                const newSubjectDiv = document.createElement('div');
                newSubjectDiv.className = 'subject-input-group flex items-center space-x-2';
                newSubjectDiv.innerHTML = `
                    <div class="relative w-full">
                        <label for="subject-${subjectCount + 1}" class="block text-sm font-medium text-gray-400 mb-1">Subject Name</label>
                        <input type="text" id="subject-${subjectCount + 1}" class="w-full p-3 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="e.g., Math" required>
                    </div>
                    <div class="relative w-full">
                        <label for="marks-${subjectCount + 1}" class="block text-sm font-medium text-gray-400 mb-1">Marks</label>
                        <input type="number" id="marks-${subjectCount + 1}" class="w-full p-3 bg-gray-800 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500" placeholder="e.g., 75" min="0" max="100" required>
                    </div>
                    <button type="button" class="remove-subject-btn bg-red-600 hover:bg-red-700 text-white font-semibold py-3 px-4 rounded-lg transition duration-300 transform hover:scale-105" aria-label="Remove Subject">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm6 0a1 1 0 012 0v6a1 1 0 11-2 0V8z" clip-rule="evenodd" />
                        </svg>
                    </button>
                `;
                marksForm.querySelector('.space-y-4').appendChild(newSubjectDiv);

                // Add event listener to the new remove button
                newSubjectDiv.querySelector('.remove-subject-btn').addEventListener('click', () => {
                    newSubjectDiv.remove();
                });
            }

            // Add the initial subject input fields
            addSubjectInput();
            addSubjectInput();

            addSubjectBtn.addEventListener('click', addSubjectInput);

            marksForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                const subjectInputs = marksForm.querySelectorAll('.subject-input-group');
                const marksData = [];
                let isValid = true;

                subjectInputs.forEach(group => {
                    const subject = group.querySelector('input[type="text"]').value;
                    const marks = parseFloat(group.querySelector('input[type="number"]').value);

                    if (subject.trim() === '' || isNaN(marks) || marks < 0 || marks > 100) {
                        isValid = false;
                        return;
                    }

                    marksData.push({ subject, marks });
                });

                if (!isValid || marksData.length === 0) {
                    showMessage("Please enter valid marks between 0 and 100 for all subjects.", true);
                    return;
                }

                try {
                    const response = await fetch('/analyze_marks', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify(marksData),
                    });

                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }

                    const result = await response.json();
                    
                    if (result.weak_subjects_text) {
                        weakSubjectsList.textContent = result.weak_subjects_text;
                        quoteArea.textContent = `"${result.motivational_quote}"`;
                        document.getElementById('weak-subjects-section').classList.remove('hidden');
                    } else {
                        weakSubjectsList.textContent = "You are doing great in all subjects! Keep up the hard work.";
                        quoteArea.textContent = `"Keep up the great work! Consistency is key to mastery."`;
                    }
                    resultArea.classList.remove('hidden');
                    showMessage("Marks analyzed successfully!");

                } catch (error) {
                    console.error('Error:', error);
                    showMessage("An error occurred during analysis.", true);
                }
            });

            setGoalBtn.addEventListener('click', async () => {
                const goalTime = document.getElementById('goal-time').value;
                if (!goalTime || goalTime <= 0) {
                    showMessage("Please enter a valid number of days.", true);
                    return;
                }

                try {
                    const response = await fetch('/set_goal', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ days: goalTime }),
                    });

                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    
                    const result = await response.json();
                    goalMessage.textContent = result.message;
                    goalMessageContainer.classList.remove('hidden');
                    showMessage("Goal set successfully!");

                } catch (error) {
                    console.error('Error:', error);
                    showMessage("An error occurred while setting the goal.", true);
                }
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/analyze_marks', methods=['POST'])
def analyze_marks():
    """Receives marks data and returns analysis results."""
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
    """Receives goal data and returns a motivational message."""
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

    
    This app is a starting point. It can be extended with more sophisticated AI models for richer personalization!
    """
)
