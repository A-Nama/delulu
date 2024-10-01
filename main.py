import streamlit as st
from app.chatbot import get_chatbot_response
from app.safespaces import get_safespaces

# Home Page
st.set_page_config(page_title="Delulu", layout="centered")

# Homepage logic
if 'page' not in st.session_state:
    st.session_state['page'] = 'home'

def render_homepage():
    st.image("static/images/logo.png", width=150)
    st.title("Reality is what you make it - Delulu helps you make it better")
    if st.button("Let's chat!"):
        st.session_state['page'] = 'safespace'

def render_safespace():
    st.image("static/images/logo.png", width=150)
    st.header("Select Your Safespace")
    safespaces = get_safespaces()
    selected_safespace = st.selectbox("Choose a Safespace", [s['name'] for s in safespaces])
    if st.button("Go to Chat"):
        st.session_state['selected_safespace'] = selected_safespace
        st.session_state['page'] = 'chatbot'

def render_chatbot():
    st.image("static/images/logo.png", width=150)
    st.header(f"Chatbot - {st.session_state['selected_safespace']}")
    user_message = st.text_input("Your Message:")
    if st.button("Send"):
        bot_response = get_chatbot_response(user_message)
        st.text_area("Delulu Bot", value=bot_response, height=200)

# Page routing
if st.session_state['page'] == 'home':
    render_homepage()
elif st.session_state['page'] == 'safespace':
    render_safespace()
elif st.session_state['page'] == 'chatbot':
    render_chatbot()
