import streamlit as st
import random
import time

st.title("🔍 Quiz Application")

# List of quiz questions
questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["🏙️ Karachi", "🏰 Lahore", "🏛️ Islamabad", "🕌 Peshawar"],
        "answer": "🏛️ Islamabad"
    },
    {
        "question": "Who is known as the founder of Pakistan?",
        "options": ["📜 Allama Iqbal", "🤝 Liaquat Ali Khan", "👨‍⚖️ Muhammad Ali Jinnah", "📖 Sir Syed Ahmed Khan"],
        "answer": "👨‍⚖️ Muhammad Ali Jinnah"
    },
    {
        "question": "Which language is the national language of Pakistan?",
        "options": ["🗣️ Punjabi", "📝 Urdu", "📚 Sindhi", "🗨️ Pashto"],
        "answer": "📝 Urdu"
    },
    {
        "question": "When did Pakistan gain independence?",
        "options": ["🎆 14th August 1947", "🎇 15th August 1947", "📜 23rd March 1940", "🇮🇳 26th January 1950"],
        "answer": "🎆 14th August 1947"
    },
    {
        "question": "Which is the largest province of Pakistan by area?",
        "options": ["🌾 Punjab", "🏝️ Sindh", "⛰️ Khyber Pakhtunkhwa", "🏜️ Balochistan"],
        "answer": "🏜️ Balochistan"
    }
]

# Initialize session state for current question
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question
st.subheader("❓ " + question["question"])

selected_option = st.selectbox("🤔 Choose your answer", question["options"],)

if st.button("🚀 Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error(f"❌ Wrong! The correct answer is: {question['answer']}")
        
    time.sleep(2)
    st.session_state.current_question = random.choice(questions)
    st.rerun()
