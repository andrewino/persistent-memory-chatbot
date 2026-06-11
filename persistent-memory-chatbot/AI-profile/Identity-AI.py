import ollama
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

CHAT_HISTORY = os.path.join(ROOT_DIR, "data", "chat_history.json")
PROFILE = os.path.join(ROOT_DIR, "data", "profile-identity.json")
PROMPT = os.path.join(ROOT_DIR, "prompts", "prompt-identity.txt")

def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except: return default

def load_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except: return ""

def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    history = load_json(CHAT_HISTORY, [])
    old_profile = load_text(PROFILE)
    prompt = load_text(PROMPT)
    history_limitata = history[-10:]

    message = f"{prompt}\n\nProfilo attuale:\n{old_profile}\n\nCronologia recente:\n{json.dumps(history_limitata, ensure_ascii=False, indent=2)}"

    try:
        response = ollama.chat(
            model="gemma3:12b",
            format="json",
            messages=[{"role": "user", "content": message}]
        )
        save_text(PROFILE, response["message"]["content"].strip())
    except Exception as e:
        print(f"Errore Identity-AI: {e}")

if __name__ == "__main__":
    main()