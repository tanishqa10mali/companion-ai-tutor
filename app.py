from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/feedback", methods=["POST"])
def feedback():
    data = request.json
    user_input = data.get("text", "").strip().lower()

    responses = []

    
    if not user_input:
        responses.append("Please type a question or paste your code so we can begin.")
        return jsonify({"feedback": responses})

    
    forbidden_phrases = [
        "give full code",
        "correct code",
        "final code",
        "write complete code",
        "solve this"
    ]

    if any(phrase in user_input for phrase in forbidden_phrases):
        responses.append(
            "I can't provide the full corrected code. "
            "But I'll gladly help you fix it step by step and explain what's going wrong."
        )
        return jsonify({"feedback": responses})

    
    if "?" in user_input or "how" in user_input or "why" in user_input:
        responses.append(
            "Let's think about this together. What do you expect your code to do?"
        )
        responses.append(
            "Try explaining your logic in words first — that often reveals the issue."
        )
        return jsonify({"feedback": responses})

   
    if "for" in user_input and ":" not in user_input:
        responses.append("Your loop seems incomplete. Think about how Python knows where a loop starts.")

    if "for" in user_input and "print" in user_input and "\nprint" in user_input:
        responses.append("Your output statement may not be inside the loop. Indentation matters in Python.")

    if "print" not in user_input:
        responses.append("How will you see the result? Consider displaying output.")

    if not responses:
        responses.append("Nice attempt! The structure looks okay. Can you explain what each line is doing?")

    return jsonify({"feedback": responses})



if __name__ == "__main__":
    app.run(debug=True)
