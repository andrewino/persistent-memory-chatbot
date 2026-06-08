# 🧠 Persistent Memory Chatbot (Multi-Agent RAG)

An advanced local chatbot system with persistent memory. The project uses a multi-agent architecture based on Ollama, where different AI instances work asynchronously to extract, filter, and optimize the user profile over time.

---

## ⚙️ How the Architecture Works

The project doesn't just generate responses — it processes memory in the background through three separate scripts:

1. **`1-AI.py` (The Chat Interface)** — Handles user interaction using a fast model (`gemma3:4b`). Reads the user profile to personalize responses and saves the chat history.
2. **`2-AI.py` (The Data Extractor)** — Runs in the background (`subprocess`) without blocking the chat. Uses a more advanced model (`gemma3:12b`) to analyze **only the user's messages**, ignoring AI responses to avoid "hallucinations". Extracts objective facts only.
3. **`3-AI.py` (The Optimizer)** — Receives the extracted data and rewrites it into a single clean, concise, third-person paragraph, creating a `profile.json` file ready for future sessions.

**Data flow:**
```text
User writes → 1-AI responds → Saves chat → Launches 2-AI (in background) → Fact extraction → Launches 3-AI → Profile optimization → Updates file
```

## 💻 Requirements

- Python 3
- Ollama installed and running
- `gemma3:4b` and `gemma3:12b` models downloaded locally
- `ollama` Python library

## 🚀 Installation

**1. Install Ollama**
Download it from [ollama.com](https://ollama.com) and install it on your system.

**2. Download the AI models**
The project uses two versions of Gemma 3 to balance speed and reasoning capability:

```bash
ollama pull gemma3:4b
ollama pull gemma3:12b
```

**3. Install Python dependencies**

```bash
pip install ollama
```

**4. Clone the repository**

```bash
git clone https://github.com/andrewino/persistent-memory-chatbot.git
cd persistent-memory-chatbot
```

## 🎮 Usage

Start the chatbot by running the first script:

```bash
python3 1-AI.py
```

Type your messages and press Enter. The more you chat, the more the AI will get to know you, updating your profile in the background.

**Special chat commands:**
- `/exit` — Saves the chat and exits the program.
- `/clear` — Clears the conversation history and exits.

## 📁 Project Files

| File                | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| `1-AI.py`           | Main chatbot (front-end and user interaction).                       |
| `2-AI.py`           | Data extraction agent (filters and analyzes chat history).           |
| `3-AI.py`           | Optimization agent (cleans and compacts the text profile).           |
| `prompt.txt`        | Strict prompt for logical extraction (used by 2-AI).                 |
| `prompt2.txt`       | Stylistic review and cleanup prompt (used by 3-AI).                  |
| `chat_history.json` | Conversation history (dynamically generated).                        |
| `profile.json`      | Long-term updated user profile (dynamically generated).              |

## 👨‍💻 Author

Developed by andrewino 😎😎😎
