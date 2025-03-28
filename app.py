import g4f  # Import GPT4Free API
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello, this is your Therapy Session AI!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")  # Get user input from request
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are a helpful therapist."},
                      {"role": "user", "content": user_input}]
        )
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
