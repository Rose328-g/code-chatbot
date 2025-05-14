# app.py
import streamlit as st
from groq_api import ask_groq
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Page config
st.set_page_config(page_title="Code Chatbot - Tasbirul", page_icon="🤖")

# Title
st.markdown("# 💬 Code Chatbot")
st.markdown("Built by **Tasbirul** using Groq + LLaMA 3")
st.markdown("Ask any coding-related question!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
user_input = st.chat_input("Type your coding question...")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Generate and add assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = ask_groq(user_input)
            except Exception as e:
                response = f"❌ Error: {e}"
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
