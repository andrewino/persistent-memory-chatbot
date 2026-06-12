import ollama
import json
import subprocess
import os
import threading

color_reset = "\033[0m"
color_user = "\033[94m"
color_ai = "\033[92m"
color_red = "\033[91m"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# --- PERCORSI AGGIORNATI SECONDO LA NUOVA STRUTTURA ---
PATH_HISTORY = os.path.join(BASE_DIR, "data", "chat_history.json")
PATH_PROFILE_GLOBAL = os.path.join(BASE_DIR, "data", "profile.json")
PATH_AI_PROFILE_SCRIPTS = os.path.join(BASE_DIR, "AI-profile")
PATH_CATEGORIE_SCRIPT = os.path.join(BASE_DIR, "categorie.py")

history = []
memory_lock = threading.Lock() 

def smart_memory_update(user_input):
    # Messaggio iniziale per confermare che il thread è partito
    # print(f"\n{color_red}[DEBUG] Router in ascolto...{color_reset}") 

    router_prompt = f"""
    Analizza questo messaggio dell'utente: "{user_input}"
    Scegli UNA SOLA tra queste categorie:
    - IDENTITY (nome, età, provenienza, lavoro)
    - KNOWLEDGE (competenze, linguaggi, strumenti)
    - PERSONAL (hobby, gusti, interessi, passioni)
    - CONTEXT (obiettivi, progetti, appuntamenti, relazioni)
    - NONE (nessuna informazione da ricordare)
    Rispondi SOLO con il nome della categoria (es: IDENTITY).
    """
    try:
        response = ollama.chat(
            model="gemma3:4b", 
            options={"temperature": 0.0}, 
            messages=[{"role": "user", "content": router_prompt}]
        )
        
        # Pulizia della risposta (rimuove spazi, invii e trasforma in maiuscolo)
        category = response['message']['content'].strip().upper()
        
        # DEBUG: Vedi cosa ha deciso il router
        # print(f"{color_red}[DEBUG] Categoria rilevata: {category}{color_reset}")

        with memory_lock:
            if "IDENTITY" in category:
                print(f"\n{color_red}[SYSTEM] Aggiornamento Identity...{color_reset}")
                subprocess.run(["python3", os.path.join(PATH_AI_PROFILE_SCRIPTS, "Identity-AI.py")])
            elif "KNOWLEDGE" in category:
                print(f"\n{color_red}[SYSTEM] Aggiornamento Knowledge...{color_reset}")
                subprocess.run(["python3", os.path.join(PATH_AI_PROFILE_SCRIPTS, "Knowledge-AI.py")])
            elif "PERSONAL" in category:
                print(f"\n{color_red}[SYSTEM] Aggiornamento Personal...{color_reset}")
                subprocess.run(["python3", os.path.join(PATH_AI_PROFILE_SCRIPTS, "Personal-AI.py")])
            elif "CONTEXT" in category:
                print(f"\n{color_red}[SYSTEM] Aggiornamento Context...{color_reset}")
                subprocess.run(["python3", os.path.join(PATH_AI_PROFILE_SCRIPTS, "Context-AI.py")])
            else:
                # Se è NONE, usciamo senza stampare [SYSTEM]
                return 

            # Unisce i JSON dopo l'aggiornamento
            subprocess.run(["python3", PATH_CATEGORIE_SCRIPT])
            # print(f"{color_red}[SYSTEM] Database memoria sincronizzato.{color_reset}")
            
    except Exception as e:
        print(f"\n{color_red}[SYSTEM ERROR] Errore router: {e}{color_reset}")

def save_history():
    with open(PATH_HISTORY, "w") as f:
        json.dump(history, f, indent=4)

def load_history():
    global history
    try:
        with open(PATH_HISTORY, "r") as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

load_history()

print(f"{color_red}type '/exit' to exit.{color_reset}")
print(f"{color_red}type '/clear' to clear chat history and exit.{color_reset}")

memory_thread = None

while True:
    if memory_thread is not None:
        memory_thread.join()
        memory_thread = None

    user_input = input(f"{color_user}Tu: {color_reset}")

    if user_input.lower() == "/exit":
        break
    elif user_input.lower() == "/clear":
        open(PATH_HISTORY, "w").write("[]")
        break

    history.append({"role": "user", "content": user_input})

    try:
        with open(PATH_PROFILE_GLOBAL, encoding="utf-8") as f:
            profilo = f.read()
    except FileNotFoundError:
        profilo = ""

    # --- SLICING: LEGGE SOLO GLI ULTIMI 10 MESSAGGI ---
    # Questo evita rallentamenti quando la chat diventa lunga
    history_limitata = history[-10:]

    response = ollama.chat(
        model="gemma3:4b",
        stream=True,
        messages=[
            {
                "role": "system",
                "content": f"Queste sono le informazioni che conosci sull'utente:\n{profilo}\nUsale per personalizzare le tue risposte."
            }
        ] + history_limitata # Usiamo solo la parte finale della storia
    )

    print(f"{color_ai}AI: ", end="", flush=True)
    reply = ""
    for chunk in response:
        parola = chunk['message']['content']
        print(parola, end="", flush=True)
        reply += parola
    print(f"{color_reset}\n")

    history.append({"role": "assistant", "content": reply})
    save_history()

    memory_thread = threading.Thread(target=smart_memory_update, args=(user_input,), daemon=True)
    memory_thread.start()
