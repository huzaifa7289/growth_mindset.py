import streamlit as st
import random

# List of Growth Mindset Challenges
challenges = [
    "Try something new that you’ve never done before.",
    "Replace 'I can’t' with 'I can’t yet' in your thinking.",
    "Ask for feedback on a project and use it to improve.",
    "Identify a past failure and write down what you learned from it.",
    "Teach someone else a skill you’ve recently learned.",
    "Step out of your comfort zone and take on a difficult task.",
    "Reframe a negative thought into a positive one.",
    "Write down 3 things you struggled with today and how you can improve.",
    "Listen to a podcast or read a book about personal growth.",
    "Celebrate a small success and acknowledge your effort."
]

# Streamlit App UI
st.title("🌱 Growth Mindset Challenge")
st.subheader("Daily Challenge to Strengthen Your Mindset")

st.write("Click the button below to get your challenge for today!")

if st.button("Get Challenge"):
    challenge = random.choice(challenges)
    st.success(f"💡 **Your Challenge:** {challenge}")

st.write("Keep growing and embracing challenges! 🚀")
