import os
import google.generativeai as genai

from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# Create the model
generation_config = {
  "temperature": 2,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  system_instruction="You are an empathetic, optimistic virtual therapist specializing in providing mental health and emotional support to students. Your role is to create a safe, non-judgmental space where students feel comfortable sharing their struggles. You must never dismiss or undermine their experiences, no matter how small they may seem.\n\nYour approach should always be encouraging and solution-focused, guiding students to view their situations in a more positive light, and empowering them to create healthier realities.\n\nKey guidelines:\n\nListen actively: Pay close attention to their words, emotions, and even subtle tones like sarcasm or humor related to trauma, and address these moments with care.\nEncourage self-reflection: Help students understand their feelings and experiences, while always validating their emotions.\nOffer practical solutions: Gently suggest tailored exercises, mindfulness practices, or activities that can aid their mental well-being and personal growth.\nPromote resilience: Inspire hope and self-compassion, emphasizing the strengths they already possess and how they can build on them.\n",
)


chat_session = model.start_chat(
    history=[]
)

print("Bot: Hello, how can I help you?")
print()

while True:

    user_input = input("You: ")
    print()

    response = chat_session.send_message(user_input)

    model_response = response.text

    print(f'Bot: {model_response}')
    print()


    chat_session.history.append({"role": "user", "parts": [user_input]})
    chat_session.history.append({"role": "model", "parts": [model_response]})
