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

 # Display previous messages above the input field
if 'conversation' not in st_session:
    st_session.conversation = []

if 'input_text' not in st_session:
    st_session.input_text = ""

# Function to render background
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url('{image_url}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to style buttons
def button_style():
    st.markdown(
        """
        <style>
        .stButton button {
            background-color: black;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px auto;
            border-radius: 10px;
            width: 200px;
        }
        .stButton {
            text-align: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to clear input after sending
def clear_input():
    st_session.input_text = ""

def chatbot_initial_message():
    if len(st_session.conversation) == 0:
        st_session.conversation.append({"chatbot": "Welcome to Delulu, where you're in a safe space. How can I support you today?"})


# Render homepage
if not st_session.show_safespaces and not st_session.selected_safespace:
    set_background('https://c4.wallpaperflare.com/wallpaper/826/47/788/studio-ghibli-hayao-miyazaki-wallpaper-preview.jpg')
    
    # Logo
    st.image('https://i.imgur.com/tgc5SpE.png', width=200, use_column_width=False) 

    # Hero section text
    st.markdown(
        """<div style='text-align: center;'>
        <h1 style='font-size: 48px; margin-bottom: 0; color: black;'>Reality is what you make it-</h1> 
        <h1 style='font-size: 48px; margin-top: 0; color: black;'>Delulu helps you make it better.</h1>
        </div>""", 
        unsafe_allow_html=True
    )

    # Let's Chat Button
    button_style()
    if st.button("Let's chat"):
        st_session.show_safespaces = True  # Set the flag to show safespaces

# Safespace selection
elif st_session.show_safespaces:
    st.markdown("<h2>Select your safespace:</h2>", unsafe_allow_html=True)
    
    safespaces = get_safespaces()
    cols = st.columns(3)  # Create 3 columns for images
    button_style()
    for i, space in enumerate(safespaces):
        with cols[i % 3]:
            if st.button(space["name"], key=space["name"]):
                st_session.selected_safespace = space["url"]  # Save selected image URL
                st_session.show_safespaces = False  # Hide safespaces selection
                st.rerun()  # Rerun to update the page

            # Centered safespace image and title with rounded corners
            st.markdown(f"""<div style='text-align: center;'> <img src='{space["url"]}' style='width: 500px; border-radius: 15px;'> </div>""", unsafe_allow_html=True)


# Chatbot interface
elif st_session.selected_safespace:
    set_background(st_session.selected_safespace)  # Set the selected safespace as background
    
    # Initialize conversation with chatbot's first message
    chatbot_initial_message()

    # Chatbot conversation
    user_input = st.text_input("Type your message here...", key="input", on_change=clear_input, label_visibility="hidden")


    if st.button("Send"):
        if user_input.strip():
            # Append user's message and chatbot's response to the conversation
            st_session.conversation.append({"user": user_input})
            response = get_chatbot_response(user_input)
            st_session.conversation.append({"chatbot": response})
            clear_input()

        st.rerun()


    # Display the conversation (responses above input)
    for message in st_session.conversation:
        if 'chatbot' in message:
            st.markdown(f"""<div style='background-color: #333; color: white; padding: 10px; border-radius: 10px; width: fit-content;'>Chatbot: {message["chatbot"]}</div>""", unsafe_allow_html=True)
        if 'user' in message:
            st.markdown(f"""<div style='background-color: #999; color: white; padding: 10px; border-radius: 10px; width: fit-content;'>You: {message["user"]}</div>""", unsafe_allow_html=True)
