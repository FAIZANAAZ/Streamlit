import streamlit as st
import random
from datetime import datetime, timedelta

# Set page config
st.set_page_config(page_title="Growth Mindset Mastery", page_icon="🌱", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #e6f3ff;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Description
st.title("🌱 Growth Mindset Mastery")
st.write("Embark on a journey of personal growth and unlock your full potential!")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Daily Challenge", "Progress Tracker", "Resources"])

if page == "Home":
    # User Input
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Welcome, {name}! Let's nurture your growth mindset!")

    # Motivational Quote
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
        "Believe you can and you're halfway there. - Theodore Roosevelt",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The mind is everything. What you think you become. - Buddha",
        "Everything you've ever wanted is on the other side of fear. - George Addair"
    ]
    if st.button("Get Inspired"):
        st.info(random.choice(quotes))

    # Growth Mindset Quiz
    st.subheader("Quick Growth Mindset Quiz")
    q1 = st.radio("1. Do you believe your abilities can be developed through dedication and hard work?", ["Yes", "No", "Sometimes"])
    q2 = st.radio("2. How do you view challenges?", ["As opportunities to grow", "As threats to avoid", "It depends"])
    q3 = st.radio("3. When you face setbacks, do you:", ["Learn from them and try again", "Get discouraged and give up", "Blame others or circumstances"])

    if st.button("Submit Quiz"):
        score = 0
        if q1 == "Yes": score += 1
        if q2 == "As opportunities to grow": score += 1
        if q3 == "Learn from them and try again": score += 1
        
        st.balloons()
        st.success(f"Your Growth Mindset Score: {score}/3")
        if score == 3:
            st.write("Excellent! You have a strong growth mindset!")
        elif score == 2:
            st.write("Good job! You're on the right track. Keep nurturing your growth mindset!")
        else:
            st.write("There's room for improvement. Remember, with effort and persistence, you can develop a growth mindset!")

elif page == "Daily Challenge":
    st.header("Daily Growth Challenge")
    
    challenges = [
        "Learn something new today and share it with a friend.",
        "Embrace a challenge you've been avoiding.",
        "Practice gratitude by writing down three things you're thankful for.",
        "Step out of your comfort zone and try something new.",
        "Reflect on a recent failure and identify three lessons learned.",
        "Give a genuine compliment to three different people today.",
        "Set a small goal and create an action plan to achieve it."
    ]
    
    # Use the current date as a seed for consistent daily challenges
    random.seed(datetime.now().date().toordinal())
    daily_challenge = random.choice(challenges)
    
    st.subheader("Today's Challenge:")
    st.info(daily_challenge)
    
    completion = st.checkbox("I've completed today's challenge!")
    if completion:
        st.success("Great job! Keep up the good work!")
        st.balloons()

elif page == "Progress Tracker":
    st.header("Track Your Growth")
    
    # Simulated progress data
    dates = [datetime.now().date() - timedelta(days=i) for i in range(7)]
    progress = [random.randint(1, 10) for _ in range(7)]
    
    st.line_chart(dict(zip(dates, progress)))
    st.write("This chart shows your growth mindset score over the past week.")
    
    # Goal setting
    st.subheader("Set a Growth Goal")
    goal = st.text_input("What's your next growth goal?")
    deadline = st.date_input("Set a deadline")
    if st.button("Set Goal"):
        st.success(f"Goal set: Achieve '{goal}' by {deadline}")

elif page == "Resources":
    st.header("Growth Mindset Resources")
    
    st.subheader("Recommended Books")
    st.write("1. 'Mindset: The New Psychology of Success' by Carol S. Dweck")
    st.write("2. 'Grit: The Power of Passion and Perseverance' by Angela Duckworth")
    st.write("3. 'Atomic Habits' by James Clear")
    
    st.subheader("Inspiring TED Talks")
    st.video("https://www.youtube.com/watch?v=_X0mgOOSpLU")
    st.caption("The power of believing that you can improve | Carol Dweck")
    
    st.subheader("Daily Affirmations")
    affirmations = [
        "I embrace challenges as opportunities to grow.",
        "My potential is limitless.",
        "I learn from my mistakes and become better.",
        "With effort and persistence, I can achieve anything.",
        "I am constantly evolving and improving."
    ]
    st.info(random.choice(affirmations))

# Footer
st.markdown("---")
st.write("Remember, growth is a journey, not a destination. Keep growing! 🌱")