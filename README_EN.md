# 🧠 Persistent Memory Chatbot (Multi-Agent RAG)

An advanced local chatbot system with persistent memory. The project utilizes a multi-agent architecture powered by Ollama, where multiple AI instances work asynchronously to extract, filter, and categorize the user's profile into specific compartments.

---

## ⚙️ How the Architecture Works

The project processes memory in the background through a system of specialized agents to ensure data accuracy and organization:

1. **`1-AI.py` (The Chat Interface)** — Manages interaction with the user using a fast model (`gemma3:4b`). It reads the global profile to personalize responses and saves the chat history.
2. **Specialized Agents (Background)** — These run in parallel via `threading` without blocking the chat. They use the `gemma3:12b` model (or `4b`) to analyze the history based on specific tasks:
   - **`Identity-AI.py`**: Handles demographic data and identity.
   - **`Knowledge-AI.py`**: Handles technical skills and expertise.
   - **`Personal-AI.py`**: Handles hobbies, tastes, and personal preferences.
   - **`Context-AI.py`**: Handles ongoing projects and temporary situations.
3. **`categorie.py` (The Aggregator)** — Collects the results from all agents and merges them into a single, structured `profile.json` file.

**Data Flow:**
```text
User writes → 1-AI responds → Save chat → Asynchronous Threading → Agents (Identity, Knowledge, Personal, Context) → categorie.py → Update profile.json