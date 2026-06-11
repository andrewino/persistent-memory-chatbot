

# 🧠 Persistent Memory Chatbot (Multi-Agent RAG)

> [!IMPORTANT]
> Avvia il progetto eseguendo **`MAIN-AI.py`**.

Un sistema avanzato di chatbot locale con memoria persistente. Il progetto utilizza un'architettura multi-agente basata su Ollama, con un sistema di **Smart Routing** per un aggiornamento della memoria efficiente e veloce.

---

## ⚙️ Come funziona l'Architettura

Il progetto è stato ottimizzato per essere veloce anche su hardware consumer, grazie a una gestione intelligente dei processi:

1. **`MAIN-AI.py` (L'Interfaccia Chat)** — Gestisce l'interazione in **streaming** con l'utente usando `gemma3:4b`. Utilizza lo **Slicing della memoria** (legge solo gli ultimi 10 messaggi) per rimanere veloce anche dopo lunghe conversazioni.
2. **Smart Router (Filtro Intelligente)** — Prima di attivare gli agenti pesanti, il chatbot usa il modello 4b per analizzare se l'ultimo messaggio contiene informazioni da ricordare. Se non ci sono novità, non attiva nulla, risparmiando il 90% delle risorse.
3. **Agenti Specializzati (`AI-profile/`)** — Se il router identifica una categoria, attiva in background solo l'agente necessario (usando `gemma3:12b` per la massima precisione):
   - **`Identity-AI.py`**: Identità e dati anagrafici.
   - **`Knowledge-AI.py`**: Competenze tecniche e professionali.
   - **`Personal-AI.py`**: Hobby, gusti e preferenze.
   - **`Context-AI.py`**: Progetti attuali, scadenze e relazioni.
4. **`categorie.py`** — Sincronizza i database locali e unisce tutto nel file globale `profile.json`.

**Flusso dei dati:**
```text
Utente scrive → Risposta AI (Streaming) → Smart Router (Background) 
   ↳ Se info rilevante → Esegue Agente Specifico → categorie.py → Update profile.json
   ↳ Se info irrilevante → Fine processo (Risparmio CPU/VRAM)
```

---

## 📁 Struttura del Progetto

Il progetto è ora organizzato in modo modulare:

```text
📂 persistent-memory-chatbot/
├── 📂 AI-profile/          # Gli "operai" della memoria (Identity, Knowledge, ecc.)
├── 📂 data/                # Database JSON (Cronologia e Profili)
├── 📂 prompts/             # Istruzioni di sistema (prompt-*.txt)
├── MAIN-AI.py              # Script principale della Chat
├── categorie.py            # Aggregatore della memoria
├── Test.py                 # Ambiente di test con backup/ripristino automatico
└── README.md
```

---

## 💻 Requisiti

- Python 3.x
- [Ollama](https://ollama.com) installato
- Modelli: `ollama pull gemma3:4b` e `ollama pull gemma3:12b`
- Libreria Python: `pip install ollama`

---

## 🎮 Utilizzo

Avvia il chatbot:
```bash
python3 MAIN-AI.py
```

**Comandi speciali:**
- `/exit` : Chiude la chat.
- `/clear` : Svuota la cronologia e resetta la sessione attuale.

### 🛠 Modalità Test
Se vuoi testare il bot senza sporcare i tuoi file di memoria reali, usa:
```bash
python3 Test.py
```
*Questo script crea un backup automatico dei tuoi dati, avvia la chat e ripristina tutto allo stato originale alla chiusura.*

---

## 👨‍💻 Autore
Sviluppato da **andrewino** 😎

---

### Novità dell'ultima versione:
- ✅ **Organizzazione in cartelle**: Dati, prompt e script ora sono separati.
- ✅ **Smart Router**: Aggiorna la memoria solo quando serve veramente.
- ✅ **Streaming**: Risposte dell'AI visibili in tempo reale.
- ✅ **Memory Slicing**: La chat non rallenta più all'aumentare dei messaggi.
