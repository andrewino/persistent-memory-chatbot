# 🧠 Persistent Memory Chatbot

A persistent memory chatbot system made up of two AIs that work together to deliver increasingly personalized responses over time.

---

## How it works

The project is split into two Python scripts:

**`1-AI.py`** — The main chatbot. It chats with the user, saves the conversation history, and uses the user profile to personalize its responses.

**`2-AI.py`** — The analysis AI. It runs automatically after every message: reads the conversation history and updates the user profile by extracting relevant information.

```
User writes → 1-AI replies → saves chat → runs 2-AI → 2-AI updates profile → repeats
```

The more you chat, the richer the profile becomes and the more personalized the responses get.

---

## Requirements

- Python 3
- [Ollama](https://ollama.com) installed and running
- `gemma3:4b` model downloaded
- `ollama` Python library

---

## Installation

**1. Install Ollama**

Download it from [ollama.com](https://ollama.com) and install it.

**2. Download the model**

```bash
ollama pull gemma3:4b
```

**3. Install the Python library**

```bash
pip install ollama
```

**4. Clone the repository**

```bash
git clone https://github.com/andrewino/persistent-memory-chatbot.git
cd persistent-memory-chatbot/persistent-memory-chatbot
```

---

## Usage

Start the chatbot:

```bash
python3 1-AI.py
```

Type your messages and press Enter. To quit, type:

```
esci
```

---

## Project files

| File | Description |
|---|---|
| `1-AI.py` | Main chatbot |
| `2-AI.py` | Profile analysis and update AI |
| `prompt.txt` | Prompt used by 2-AI to extract the profile |
| `chat_history.json` | Conversation history (auto-generated) |
| `profile.json` | Updated user profile (auto-generated) |

---

## Author

Developed by [andrewino](https://github.com/andrewino)
