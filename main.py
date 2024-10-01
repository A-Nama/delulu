import streamlit as st
from streamlit import session_state as st_session
from app.chatbot import get_chatbot_response
from app.safespaces import get_safespaces

# Set page configuration
st.set_page_config(page_title="Delulu - Mental Health Chatbot", layout="wide")

# Initialize session state variables
if 'selected_safespace' not in st_session:
    st_session.selected_safespace = None

if 'show_safespaces' not in st_session:
    st_session.show_safespaces = False

# Function to render background
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .main {{
            background-image: url('{image_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
            text-align: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Render homepage
if not st_session.show_safespaces and not st_session.selected_safespace:
    set_background('https://c4.wallpaperflare.com/wallpaper/826/47/788/studio-ghibli-hayao-miyazaki-wallpaper-preview.jpg')
    
    # Logo
    st.image('https://i.imgur.com/tgc5SpE.png', width=100, use_column_width=False) 

    # Hero section text
    st.markdown("<h1 style='font-size: 48px;'>Reality is what you make it - Delulu helps you make it better.</h1>", unsafe_allow_html=True)

    # Button to start the chat
    if st.button("Let's chat"):
        st_session.show_safespaces = True  # Set the flag to show safespaces

# Safespace selection
elif st_session.show_safespaces:
    st.markdown("<h2>Select your safespace:</h2>", unsafe_allow_html=True)
    
    safespaces = get_safespaces()
    cols = st.columns(3)  # Create 3 columns for images
    for i, space in enumerate(safespaces):
        with cols[i % 3]:
            if st.button(space["name"], key=space["name"]):
                st_session.selected_safespace = space["url"]  # Save selected image URL
                st_session.show_safespaces = False  # Hide safespaces selection
                st.experimental_rerun()  # Rerun to update the page

            st.image(space["url"], width=200)  # Display image

# Chatbot interface
elif st_session.selected_safespace:
    set_background(st_session.selected_safespace)  # Set the selected safespace as background
    
    # Top-left logo on chatbot page
    st.image('https://i.imgur.com/tgc5SpE.png', width=100, use_column_width=False)  
    st.header("Chat with our AI Chatbot")
    
    user_input = st.text_input("Type your message here...")
    if st.button("Send"):
        response = get_chatbot_response(user_input)
        st.markdown(f"<p style='color: white;'>Chatbot: {response}</p>", unsafe_allow_html=True)
