
import ollama
import json

history = []

def save_history():
    with open("profile.json", "w") as f:
        json.dump(reply, f)

def load_history():
    global history
    try:
        with open("chat_history.json", "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

load_history()

def main():
    global reply
    stringa = open("prompt.txt", encoding="utf-8").read()
    
    # Combina il prompt con la historyå
    messaggio = stringa + "\n\n" + json.dumps(history, ensure_ascii=False)
    
    response = ollama.chat(
        model="gemma3:4b",
        messages=[{"role": "user", "content": messaggio}]
    )
    
    reply = response.message.content
    
    save_history()

main()
