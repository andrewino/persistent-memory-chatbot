import ollama
import json
import subprocess
import os

color_reset = "\033[0m"
color_user = "\033[94m"
color_ai = "\033[92m"
color_red = "\033[91m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

history = []
analyzer_process = None

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
    print(f"{color_red}type '/exit' to exit.{color_reset}")
    print(f"{color_red}type '/clear' to clear chat history and exit.{color_reset}")
    user_input = input(f"{color_user}Tu: {color_reset}")

    if user_input.lower() == "/exit":
        break
    elif user_input.lower() == "/clear":
        open(os.path.join(BASE_DIR, "chat_history.json"), "w").write("[]")
        break

    history.append({"role": "user", "content": user_input})

    try:
        with open(os.path.join(BASE_DIR, "profile.json"), encoding="utf-8") as f:
            profilo = f.read()
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

    print(f"{color_ai}AI: {reply}{color_reset}\n")
    save_history()

    if analyzer_process is None or analyzer_process.poll() is not None:
        analyzer_process = subprocess.Popen(["python3", os.path.join(BASE_DIR, "2-AI.py")])
