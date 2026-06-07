import ollama
import json
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

history = []

def save_history():
    with open(os.path.join(BASE_DIR, "chat_history.json"), "w") as f:
        json.dump(history, f, indent=4)

def load_history():
    global history
    try:
        with open(os.path.join(BASE_DIR, "chat_history.json"), "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

load_history()

while True:
    user_input = input("Tu: ")

    if user_input.lower() == "esci":
        break

    history.append({"role": "user", "content": user_input})

    try:
        profilo = open(os.path.join(BASE_DIR, "profile.json"), encoding="utf-8").read()
    except FileNotFoundError:
        profilo = ""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "system",
                "content": f"Queste sono le informazioni che conosci sull'utente:\n{profilo}\nUsale per personalizzare le tue risposte."
            }
        ] + history
    )

    reply = response.message.content
    history.append({"role": "assistant", "content": reply})

    print(f"AI: {reply}\n")
    save_history()
    subprocess.Popen(["python3", os.path.join(BASE_DIR, "2-AI.py")])
