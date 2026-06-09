import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FILES = {
    "identity": "profile-identity.json",
    "knowledge": "profile-knowledge.json",
    "personal": "profile-personal.json",
    "context": "profile-context.json"
}

OUTPUT = "profile.json"


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def main():
    profile = {}

    for category, filename in FILES.items():
        filepath = os.path.join(BASE_DIR, filename)
        profile[category] = load_json(filepath)

    output_path = os.path.join(BASE_DIR, OUTPUT)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()