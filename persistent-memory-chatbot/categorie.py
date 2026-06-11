import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

FILES = {
    "identity": os.path.join(DATA_DIR, "profile-identity.json"),
    "knowledge": os.path.join(DATA_DIR, "profile-knowledge.json"),
    "personal": os.path.join(DATA_DIR, "profile-personal.json"),
    "context": os.path.join(DATA_DIR, "profile-context.json")
}

OUTPUT = os.path.join(DATA_DIR, "profile.json")

def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def main():
    profile = {}
    for category, filepath in FILES.items():
        profile[category] = load_json(filepath)

    with open(OUTPUT, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()