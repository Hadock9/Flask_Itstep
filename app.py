from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv
from groq import Groq

# Завантаження змінних середовища з .env файлу
load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/api/chat", methods=["POST"])
def chat_api():
    user_message = request.get_json().get('message', '')
    if not user_message:
        return jsonify({'error': 'Повідомлення порожнє'}), 400
    
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": "Ти корисний асистент. Відповідай українською мовою."},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
        max_tokens=500,
        reasoning_effort="medium",
       
    )
    return jsonify({'message': completion.choices[0].message.content.strip()})

if __name__ == '__main__':
    app.run(debug=True)