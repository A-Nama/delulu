import os
import streamlit as st
import google.generativeai as genai
# if running locally include:- from dotenv import load_dotenv



# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Generation configuration for the chatbot
generation_config = {
    "temperature": 2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction=(
        "You are an empathetic, optimistic virtual therapist specializing in providing mental health and emotional support to students. Your role is to create a safe, non-judgmental space where students feel comfortable sharing their struggles. You must never dismiss or undermine their experiences, no matter how small they may seem.\n\nYour approach should always be encouraging and solution-focused, guiding students to view their situations in a more positive light, and empowering them to create healthier realities.\n\nKey guidelines:\n\nListen actively: Pay close attention to their words, emotions, and even subtle tones like sarcasm or humor related to trauma, and address these moments with care.\nEncourage self-reflection: Help students understand their feelings and experiences, while always validating their emotions.\nOffer practical solutions: Gently suggest tailored exercises, mindfulness practices, or activities that can aid their mental well-being and personal growth.\nPromote resilience: Inspire hope and self-compassion, emphasizing the strengths they already possess and how they can build on them.\n"
    )
)

def get_chatbot_response(user_input):
    # Check if chat session exists, if not create a new one
    if 'chat_session' not in st.session_state:
        st.session_state['chat_session'] = model.start_chat(history=[])

    # Send user input and get the response
    response = st.session_state['chat_session'].send_message(user_input)
    return response.text
