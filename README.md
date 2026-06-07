# 🧠 Persistent Memory Chatbot

Un sistema di chatbot con memoria persistente composto da due AI che lavorano insieme per offrire risposte sempre più personalizzate nel tempo.

---

## Come funziona

Il progetto è diviso in due script Python:

**`1-AI.py`** — Il chatbot principale. Chatta con l'utente, salva la cronologia della conversazione e usa il profilo utente per personalizzare le risposte.

**`2-AI.py`** — L'AI di analisi. Viene eseguita automaticamente dopo ogni messaggio: legge la cronologia e aggiorna il profilo utente estraendo informazioni rilevanti.

```
Utente scrive → 1-AI risponde → salva chat → lancia 2-AI → 2-AI aggiorna profilo → ricomincia
```

Più si conversa, più il profilo diventa ricco e le risposte più personalizzate.

---

## Requisiti

- Python 3
- [Ollama](https://ollama.com) installato e in esecuzione
- Modello `gemma3:4b` scaricato
- Libreria Python `ollama`

---

## Installazione

**1. Installa Ollama**

Scaricalo da [ollama.com](https://ollama.com) e installalo.

**2. Scarica il modello**

```bash
ollama pull gemma3:4b
```

**3. Installa la libreria Python**

```bash
pip install ollama
```

**4. Clona il repository**

```bash
git clone https://github.com/andrewino/persistent-memory-chatbot.git
cd persistent-memory-chatbot/persistent-memory-chatbot
```

---

## Utilizzo

Avvia il chatbot:

```bash
python3 1-AI.py
```

Scrivi i tuoi messaggi e premi Invio. Per uscire digita:

```
esci
```

---

## File del progetto

| File | Descrizione |
|---|---|
| `1-AI.py` | Chatbot principale |
| `2-AI.py` | AI di analisi e aggiornamento profilo |
| `prompt.txt` | Prompt usato da 2-AI per estrarre il profilo |
| `chat_history.json` | Cronologia della conversazione (generato automaticamente) |
| `profile.json` | Profilo utente aggiornato (generato automaticamente) |

---

## Autore

Sviluppato da [andrewino](https://github.com/andrewino)
