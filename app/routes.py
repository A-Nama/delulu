from flask import Blueprint, render_template, request, redirect, url_for
from .chatbot import chatbot_response
from .safespaces import get_safespaces

main = Blueprint('main', __name__)

# Home Page
@main.route('/')
def index():
    return render_template('index.html')

# SafeSpace selection page
@main.route('/safespace', methods=['GET', 'POST'])
def safespace():
    safespaces = get_safespaces()
    if request.method == 'POST':
        selected_safespace = request.form.get('safespace')
        return redirect(url_for('main.chatbot', safespace=selected_safespace))
    return render_template('safespace.html', safespaces=safespaces)

# Chatbot page
@main.route('/chatbot/<safespace>', methods=['GET', 'POST'])
def chatbot(safespace):
    if request.method == 'POST':
        user_message = request.form['message']
        bot_response = chatbot_response(user_message)
        return render_template('chatbot.html', safespace=safespace, user_message=user_message, bot_response=bot_response)
    return render_template('chatbot.html', safespace=safespace)
