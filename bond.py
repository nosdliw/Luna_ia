import json
import os

BOND_FILE = "bond.json"

def load_bond():
    if not os.path.exists(BOND_FILE):
        return 10
    with open(BOND_FILE, "r") as f:
        return json.load(f)

def save_bond(level):
    with open(BOND_FILE, "w") as f:
        json.dump(level, f)

def update_bond(user_input):
    level = load_bond()

    # aumenta vínculo se conversa normal
    if len(user_input) > 3:
        level += 2

    # limite máximo
    if level > 100:
        level = 100

    save_bond(level)
    return level
