import ollama
import json
import subprocess

history = []

def save_history():
    with open("chat_history.json", "w") as f:
        json.dump(history, f, indent=4)
    
def load_history():
    global history
    try:
        with open("chat_history.json", "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

load_history()

while True:
    user_input = input("Tu: ")
    
    if user_input.lower() == "esci":
        break
    
    history.append({"role": "user", "content": user_input})
    
    profilo = open("profile.json", encoding="utf-8").read()

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
    subprocess.run(["python3", "2-AI.py"])
