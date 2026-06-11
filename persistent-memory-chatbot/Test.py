import os
import shutil
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# I file JSON ora si trovano nella sottocartella /data
DATA_DIR = os.path.join(BASE_DIR, "data")

# Elenco dei file da proteggere durante il test
JSON_FILES = [
    "chat_history.json",
    "profile-identity.json",
    "profile-knowledge.json",
    "profile-personal.json",
    "profile-context.json",
    "profile.json"
]

def backup_files():
    print(f"🔒 [TEST MODE] Creazione backup dei file in: {DATA_DIR}")
    # Assicuriamoci che la cartella data esista
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    for file in JSON_FILES:
        path = os.path.join(DATA_DIR, file)
        backup_path = path + ".bak"
        # Se il file esiste, ne crea una copia di sicurezza
        if os.path.exists(path):
            shutil.copy2(path, backup_path)

def restore_files():
    print("\n🧹 [TEST MODE] Ripristino dei file originali nella cartella /data...")
    for file in JSON_FILES:
        path = os.path.join(DATA_DIR, file)
        backup_path = path + ".bak"
        # Ripristina il backup ed elimina il file temporaneo .bak
        if os.path.exists(backup_path):
            shutil.move(backup_path, path)
        else:
            # Se un file non esisteva (es. prima esecuzione), lo crea vuoto
            with open(path, "w") as f:
                if "history" in file:
                    f.write("[]")
                else:
                    f.write("{}")

if __name__ == "__main__":
    backup_files()
    try:
        # Avvia il programma principale MAIN-AI.py che si trova nella root
        print("🚀 [TEST MODE] Avvio MAIN-AI...\n")
        subprocess.run(["python3", os.path.join(BASE_DIR, "MAIN-AI.py")])
    except KeyboardInterrupt:
        pass # Cattura Ctrl+C per uscire puliti
    finally:
        # Eseguito sempre alla chiusura del programma
        restore_files()
        print("✅ [TEST MODE] Test concluso. Cartella /data ripulita.")