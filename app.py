import streamlit as st

# Title of the Web App
st.title("🚀 Growth Mindset Challenge")

# Description
st.write("Welcome to the Growth Mindset Challenge! Are you ready to improve yourself?")

# User Input
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Let's start your growth journey!")

# Random Motivational Quote
import random
quotes = [
    "Failure is the opportunity to begin again, more intelligently. - Henry Ford",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill"
]
if st.button("Get a Growth Quote"):
    st.write(random.choice(quotes))
