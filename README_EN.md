# 🧠 Persistent Memory Chatbot (Multi-Agent RAG)

> [!IMPORTANT]
> Start the project by running **`MAIN-AI.py`**.


An advanced local chatbot with persistent memory. The project uses a multi-agent architecture powered by Ollama, where multiple AI instances work asynchronously to extract, filter, and categorize the user's profile into dedicated memory compartments.

---

## ⚙️ How the Architecture Works

The project processes memory in the background through a system of specialized agents, preventing data from becoming mixed or cluttered.

1. **`MAIN-AI.py` (Chat Interface)** — Handles user interactions using a fast model (`gemma3:4b`). It reads the global user profile to personalize responses and saves the conversation history.
2. **Specialized Agents (Background)** — Run in parallel using `threading` without blocking the chat. They use the `gemma3:12b` model (or optionally `4b`) to analyze the conversation history according to specific tasks:
   - **`Identity-AI.py`**: Manages identity and personal information.
   - **`Knowledge-AI.py`**: Manages technical skills and knowledge.
   - **`Personal-AI.py`**: Manages hobbies, interests, and personal preferences.
   - **`Context-AI.py`**: Manages ongoing projects and temporary situations.
3. **`categorie.py` (Aggregator)** — Collects the output from all agents and merges it into a single structured `profile.json` file.

**Data Flow:**
```text
User sends a message → MAIN-AI responds → Saves chat history → Asynchronous threading → Agents (Identity, Knowledge, Personal, Context) → categorie.py → Updates profile.json
```

## 💻 Requirements

- Python 3
- Ollama installed and running
- `gemma3:4b` and `gemma3:12b` models downloaded locally
- Python `ollama` library

## 🚀 Installation

1. **Install Ollama:** Download it from https://ollama.com and install it on your system.

2. **Download the AI models:**
   ```bash
   ollama pull gemma3:4b
   ollama pull gemma3:12b
   ```

3. **Install the Python dependency:**
   ```bash
   pip install ollama
   ```

4. **Clone the repository:**
   ```bash
   git clone https://github.com/andrewino/persistent-memory-chatbot.git
   cd persistent-memory-chatbot
   ```

## 🎮 Usage

Start the chatbot by running the main file:

```bash
python3 MAIN-AI.py
```

**Special chat commands:**
- `/exit` : Closes the chat and saves the current state.
- `/clear` : Clears the conversation history and exits.

## 📁 Project Files

| File | Description |
|------|-------------|
| `MAIN-AI.py` | Main chatbot and threading management. |
| `Identity-AI.py` | Specialized agent for identity and personal information. |
| `Knowledge-AI.py` | Specialized agent for technical skills and knowledge. |
| `Personal-AI.py` | Specialized agent for personal preferences and interests. |
| `Context-AI.py` | Specialized agent for ongoing projects and current context. |
| `categorie.py` | Merges all agent JSON files into the global user profile. |
| `prompt-*.txt` | Agent-specific instructions for memory extraction. |
| `chat_history.json` | Complete conversation history. |
| `profile.json` | The structured and cleaned persistent user memory database. |

---

## 👨‍💻 Author

Developed by **andrewino** 😎😎😎
