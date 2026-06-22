from flask import Flask, request, jsonify, render_template
import os
from google import genai
import json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

key = os.getenv("API_KEY")
client = genai.Client(api_key=key)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    topic = data.get("topic", "").strip()

    if not topic:
        return jsonify({"error": "No topic provided"})

    prompt = f"""
    Create exactly 5 flashcard questions and answers about: {topic}

    Rules:
    - Questions must be accurate and factually correct — double check each one before including it
    - Answers must be concise (1-2 sentences max)
    - Match the difficulty and subject level implied by the topic
    - Cover different aspects of the topic, not just one angle

    Respond ONLY with a valid JSON array, no markdown, no backticks, no explanation. Format:
    [
        {{"question": "...", "answer": "..."}},
        {{"question": "...", "answer": "..."}},
        {{"question": "...", "answer": "..."}},
        {{"question": "...", "answer": "..."}},
        {{"question": "...", "answer": "..."}}
    ]
    """

    try:
        chat = client.chats.create(model="gemini-2.5-flash")
        response = chat.send_message(prompt)
        raw = response.text.strip().replace("```json", "").replace("```", "")
        cards = json.loads(raw)
        return jsonify({"cards": cards})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)