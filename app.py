# app.py

import streamlit as st
from chatbot import chatbot_response

# App title and description
st.set_page_config(page_title="Customer Service Chatbot", page_icon="🤖")
st.title("🤖 Customer Service Chatbot")
st.write("Welcome! Ask me questions about orders, returns, cancellations, payments, and more.")

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input box
user_input = st.text_input("You:", "")

if user_input:
    # Get bot response
    response = chatbot_response(user_input)
    
    # Save to chat history
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for speaker, text in st.session_state.history:
    if speaker == "You":
        st.markdown(f"**🧑‍💻 {speaker}:** {text}")
    else:
        st.markdown(f"**🤖 {speaker}:** {text}")
