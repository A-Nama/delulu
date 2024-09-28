import os
import openai

# Load your Gemini API key from .env file
openai.api_key = os.getenv('GEMINI_API_KEY')

def chatbot_response(message):
    # Integrate Gemini API for chatbot response
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message}\nUser tone: Neutral\nResponse:",
        max_tokens=150
    )
    return response.choices[0].text.strip()
