from flask import Flask, request, jsonify, render_template, url_for
from shahadbot import get_cohere_response, synthesize_and_play_speech
from threading import Thread
import os
import time

app = Flask(__name__)


if not os.path.exists("static/audio"):
    os.makedirs("static/audio")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip()
    reply_text = ""


    if user_message.lower() in ["what is your name?", "what's your name", "who are you?", "your name?"]:
        reply_text = "My name is ShahadBot! I'm here to help you"
    elif user_message.lower() in ["who made this website?", "who created you?"]:
        reply_text = "This website was created by Shahad."
    else:
        #user_message = "Answer briefly: " + user_message
        reply_text = get_cohere_response(user_message)

    audio_filename = f"static/audio/response_{int(time.time())}.mp3"


    Thread(target=synthesize_and_play_speech, args=(reply_text, audio_filename, False)).start()

    return jsonify({
        "reply": reply_text,
        "audio_url": url_for("static", filename=os.path.basename(audio_filename))
    })

if __name__ == "__main__":
    app.run(debug=True)
