
# 🧠 Persistent Memory Chatbot (Multi-Agent RAG)

> [!IMPORTANT]
> Start the project by running **`MAIN-AI.py`**.

An advanced local chatbot system with persistent long-term memory. This project utilizes a multi-agent architecture powered by Ollama, featuring a **Smart Routing** system for efficient and high-performance memory updates.

---

## ⚙️ How the Architecture Works

The project is optimized for speed and efficiency on consumer hardware through intelligent process management:

1. **`MAIN-AI.py` (Chat Interface)** — Handles **streaming** user interaction using `gemma3:4b`. It employs **Memory Slicing** (reading only the last 10 messages) to maintain high performance even during long conversations.
2. **Smart Router (Intelligence Filter)** — Before activating heavy background agents, the chatbot uses the 4b model to analyze if the last message contains information worth remembering. If no new info is detected, it skips the update, saving 90% of CPU/VRAM resources.
3. **Specialized Agents (`AI-profile/`)** — If the router identifies a relevant category, it triggers the specific agent in the background (using `gemma3:12b` for maximum extraction precision):
   - **`Identity-AI.py`**: Personal data and demographics.
   - **`Knowledge-AI.py`**: Technical and professional skills.
   - **`Personal-AI.py`**: Hobbies, tastes, and preferences.
   - **`Context-AI.py`**: Current projects, deadlines, and relationships.
4. **`categorie.py`** — Synchronizes local databases and merges everything into the global `profile.json` file.

**Data Flow:**
```text
User writes → AI Response (Streaming) → Smart Router (Background) 
   ↳ If info is relevant → Run Specific Agent → categorie.py → Update profile.json
   ↳ If info is irrelevant → End process (CPU/VRAM Savings)
```

---

## 📁 Project Structure

The project is now modularly organized:

```text
📂 persistent-memory-chatbot/
├── 📂 AI-profile/          # Memory "workers" (Identity, Knowledge, etc.)
├── 📂 data/                # JSON Databases (History and Profiles)
├── 📂 prompts/             # System instructions (prompt-*.txt)
├── MAIN-AI.py              # Main Chat Script
├── categorie.py            # Memory Aggregator
├── Test.py                 # Test environment with auto backup/restore
└── README.md
```

---

## 💻 Requirements

- Python 3.x
- [Ollama](https://ollama.com) installed and running
- Models: `ollama pull gemma3:4b` and `ollama pull gemma3:12b`
- Python Library: `pip install ollama`

---

## 🎮 Usage

Start the chatbot:
```bash
python3 MAIN-AI.py
```

**Special Commands:**
- `/exit` : Closes the chat.
- `/clear` : Clears history and resets the current session.

### 🛠 Test Mode
If you want to test the bot without modifying your real memory files, use:
```bash
python3 Test.py
```
*This script automatically backs up your data, starts the chat, and restores everything to its original state upon exit.*

---

## 👨‍💻 Author
Developed by **andrewino** 😎

---

### Latest Updates:
- ✅ **Directory Organization**: Data, prompts, and scripts are now separated.
- ✅ **Smart Router**: Updates memory only when truly necessary.
- ✅ **Streaming**: AI responses are visible in real-time.
- ✅ **Memory Slicing**: Prevents chat slowdowns regardless of conversation length.
