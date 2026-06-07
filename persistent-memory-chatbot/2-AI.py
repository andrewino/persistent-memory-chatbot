import ollama
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

history = []

def save_profile():
    with open(os.path.join(BASE_DIR, "profile.json"), "w", encoding="utf-8") as f:
        f.write(reply)

def load_history():
    global history
    try:
        with open(os.path.join(BASE_DIR, "chat_history.json"), "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

load_history()

def main():
    global reply
    stringa = open(os.path.join(BASE_DIR, "prompt.txt"), encoding="utf-8").read()
    messaggio = stringa + "\n\n" + json.dumps(history, ensure_ascii=False)

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": messaggio}]
    )

    reply = response.message.content
    save_profile()

main()
