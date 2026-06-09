# 🧠 Persistent Memory Chatbot (Multi-Agent RAG)

Un sistema avanzato di chatbot locale con memoria persistente. Il progetto utilizza un'architettura multi-agente basata su Ollama, dove diverse istanze di intelligenza artificiale lavorano in modo asincrono per estrarre, filtrare e ottimizzare il profilo dell'utente nel tempo.

---

## ⚙️ Come funziona l'Architettura

Il progetto non si limita a generare risposte, ma elabora la memoria in background attraverso tre script distinti:

1. **`1-AI.py` (L'Interfaccia Chat)** — Gestisce l'interazione con l'utente usando un modello veloce (`gemma3:4b`). Legge il profilo utente per personalizzare le risposte e salva la cronologia.
2. **`2-AI.py` (L'Estrattore Dati)** — Gira in background (`subprocess`) senza bloccare la chat. Usa un modello più avanzato (`gemma3:12b`) per analizzare **esclusivamente i messaggi dell'utente**, ignorando le risposte dell'IA per evitare "allucinazioni". Estrae solo fatti oggettivi.
3. **`3-AI.py` (L'Ottimizzatore)** — Riceve i dati estratti e li riscrive in un singolo paragrafo pulito, conciso e in terza persona, creando un file `profile.json` perfetto per le sessioni future.

**Flusso dei dati:**
```text
Utente scrive → 1-AI risponde → Salva chat → Lancia 2-AI (in background) → Estrazione fatti → Lancia 3-AI → Ottimizzazione profilo → Aggiorna file

💻 Requisiti

  - Python 3
  - Ollama installato e in esecuzione
  - Modelli gemma3:4b e gemma3:12b scaricati localmente
  - Libreria Python ollama

🚀 Installazione

1.  Installa Ollama: Scaricalo da ollama.com e installalo sul tuo sistema.

2.  Scarica i modelli AI: Il progetto usa due versioni di Gemma 3 per bilanciare
    velocità e capacità di ragionamento:

    ollama pull gemma3:4b
    ollama pull gemma3:12b

3.  Installa le dipendenze Python:

    pip install ollama

4.  Clona il repository:

    git clone https://github.com/andrewino/persistent-memory-chatbot.git
    cd persistent-memory-chatbot

🎮 Utilizzo

Avvia il chatbot eseguendo il primo script:

python3 1-AI.py

Scrivi i tuoi messaggi e premi Invio. Più chatti, più l'IA imparerà a conoscerti
aggiornando il tuo profilo in background.

Comandi speciali nella chat:

  - /exit : Salva la chat ed esce dal programma.
  - /clear : Cancella la cronologia della conversazione ed esce.

📁 File del progetto

| File                | Descrizione                                                         |
| ------------------- | ------------------------------------------------------------------- |
| `1-AI.py`           | Chatbot principale (Front-end e interazione).                       |
| `2-AI.py`           | Agente di estrazione dati (filtra e analizza la cronologia).        |
| `3-AI.py`           | Agente di ottimizzazione (pulisce e compatta il profilo testuale).  |
| `prompt.txt`        | Prompt severo per l'estrazione logica (usato da 2-AI).              |
| `prompt2.txt`       | Prompt di revisione e pulizia stilistica (usato da 3-AI).           |
| `chat_history.json` | Cronologia della conversazione (generato dinamicamente).            |
| `profile.json`      | Profilo utente aggiornato a lungo termine (generato dinamicamente). |

👨‍💻 Autore

Sviluppato da andrewino😎😎😎

