from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import main  # Your existing chatbot logic

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST", "GET"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    if not user_message:
        return jsonify({"response": "Please enter a valid message."})
    
    bot_response = main.generate(user_message)
    
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run()
