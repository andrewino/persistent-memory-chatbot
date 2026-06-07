import ollama
import json
import os
import subprocess

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

    try:
        profilo_esistente = open(os.path.join(BASE_DIR, "profile.json"), encoding="utf-8").read()
    except FileNotFoundError:
        profilo_esistente = ""

    messaggio = stringa + "\n\nProfilo esistente:\n" + profilo_esistente + "\n\nNuova conversazione:\n" + json.dumps(history, ensure_ascii=False)

    response = ollama.chat(
        model="gemma3:12b",
        messages=[{"role": "user", "content": messaggio}]
    )

    reply = response.message.content
    save_profile()
    subprocess.run(["python3", os.path.join(BASE_DIR, "3-AI.py")])



main()
