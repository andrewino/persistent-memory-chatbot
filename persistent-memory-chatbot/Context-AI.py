import ollama
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL = "gemma3:4b"

CHAT_HISTORY = os.path.join(BASE_DIR, "chat_history.json")
PROFILE = os.path.join(BASE_DIR, "profile-context.json")
PROMPT = os.path.join(BASE_DIR, "prompt-context.txt")


def load_json(path, default):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return default


def load_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except:
        return ""


def save_text(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main():

    history = load_json(CHAT_HISTORY, [])

    old_profile = load_text(PROFILE)

    prompt = load_text(PROMPT)

    message = f"""
{prompt}

Profilo attuale:

{old_profile}

Cronologia:

{json.dumps(history, ensure_ascii=False, indent=2)}
"""

    response = ollama.chat(
        model="gemma3:12b",
        format="json",
        messages=[
            {
                "role": "user",
                "content": message
            }
        ]
    )

    new_profile = response["message"]["content"].strip()

    save_text(PROFILE, new_profile)


if __name__ == "__main__":
    main()
