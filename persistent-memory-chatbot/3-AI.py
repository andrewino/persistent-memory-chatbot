import ollama
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

prompt = open(os.path.join(BASE_DIR, "prompt2.txt"), encoding="utf-8").read()

try:
    with open(os.path.join(BASE_DIR, "profile.json"), encoding="utf-8") as f:
        profilo = f.read()
except FileNotFoundError:
    profilo = ""

messaggio = prompt + "\n\nJSON profile:\n" + profilo

response = ollama.chat(
    model="gemma3:4b",
    messages=[{"role": "user", "content": messaggio}]
)

reply = response.message.content

with open(os.path.join(BASE_DIR, "profile.json"), "w", encoding="utf-8") as f:
    f.write(reply)
