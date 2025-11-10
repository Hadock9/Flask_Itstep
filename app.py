from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/chat")
def chat():
    return render_template('chat.html')

@app.route("/api/chat", methods=["POST"])
def chat_api():
    """API endpoint для обробки повідомлень чату"""
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'Повідомлення не може бути порожнім'}), 400
    
    # Тут буде інтеграція з GPT
    # Поки що повертаємо тестову відповідь
    response = {
        'message': f'Ви написали: {user_message}'
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)