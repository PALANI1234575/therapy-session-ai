import g4f  # Import GPT4Free API
from flask import Flask, request, jsonify
import time
import os

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello, this is your Therapy Session AI!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        print("Received Data:", data)  # Debugging output
        if not data or "message" not in data:
            return jsonify({"error": "Invalid request, missing 'message'"}), 400

        user_input = data["message"]
        response = {"response": f"Echo: {user_input}"}  # Temporary response

        return jsonify({"response": response_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == "__main__":
  port = int(os.environ.get("PORT", 10000))  # Use Render's PORT if available
app.run(host="0.0.0.0", port=port)
