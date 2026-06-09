🧠 Persistent Memory Chatbot (Multi-Agent RAG)

Un sistema avanzato di chatbot locale con memoria persistente. Il progetto
utilizza un'architettura multi-agente basata su Ollama, dove diverse istanze di
intelligenza artificiale lavorano in modo asincrono per estrarre, filtrare e
categorizzare il profilo dell'utente in compartimenti specifici.

⚙️ Come funziona l'Architettura

Il progetto elabora la memoria in background attraverso un sistema di agenti
specializzati che evitano la confusione dei dati:

1.  1-AI.py (L'Interfaccia Chat) — Gestisce l'interazione con l'utente usando un
    modello veloce (gemma3:4b). Legge il profilo globale per personalizzare le
    risposte e salva la cronologia.
2.  Agenti Specializzati (Background) — Girano in parallelo tramite threading
    senza bloccare la chat. Usano il modello gemma3:12b (o 4b a scelta) per
    analizzare la cronologia in base a compiti specifici:
      - Identity-AI.py: Gestisce dati anagrafici e identità.
      - Knowledge-AI.py: Gestisce competenze tecniche e conoscenze.
      - Personal-AI.py: Gestisce hobby, gusti e preferenze.
      - Context-AI.py: Gestisce progetti in corso e situazioni temporanee.
3.  categorie.py (L'Aggregatore) — Raccoglie i risultati di tutti gli agenti e
    li unisce in un unico file profile.json strutturato.

Flusso dei dati:

Utente scrive → 1-AI risponde → Salva chat → Threading asincrono → Agenti (Identity, Knowledge, Personal, Context) → categorie.py → Aggiorna profile.json

💻 Requisiti

  - Python 3
  - Ollama installato e in esecuzione
  - Modelli gemma3:4b e gemma3:12b scaricati localmente
  - Libreria Python ollama

🚀 Installazione

1.  Installa Ollama: Scaricalo da ollama.com e installalo sul tuo sistema.

2.  Scarica i modelli AI:

    ollama pull gemma3:4b
    ollama pull gemma3:12b

3.  Installa le dipendenze Python:

    pip install ollama

4.  Clona il repository:

    git clone https://github.com/andrewino/persistent-memory-chatbot.git
    cd persistent-memory-chatbot

🎮 Utilizzo

Avvia il chatbot eseguendo il file principale:

python3 1-AI.py

Comandi speciali nella chat:

  - /exit : Chiude la chat e salva lo stato.
  - /clear : Svuota la cronologia della conversazione ed esce.

📁 File del progetto

| File                | Descrizione                                                 |
| ------------------- | ----------------------------------------------------------- |
| `1-AI.py`           | Chatbot principale e gestione Threading.                    |
| `Identity-AI.py`    | Agente specializzato in identità e anagrafica.              |
| `Knowledge-AI.py`   | Agente specializzato in competenze e strumenti.             |
| `Personal-AI.py`    | Agente specializzato in preferenze e interessi personali.   |
| `Context-AI.py`     | Agente specializzato in progetti e situazioni attuali.      |
| `categorie.py`      | Unisce i JSON dei singoli agenti nel profilo globale.       |
| `prompt-*.txt`      | Istruzioni specifiche per ogni agente di memoria.           |
| `chat_history.json` | Cronologia completa dei messaggi.                           |
| `profile.json`      | Il database della memoria dell'utente strutturato e pulito. |

👨+💻 Autore

Sviluppato da andrewino😎😎😎
