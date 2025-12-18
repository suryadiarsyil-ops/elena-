
# elena.py

import os

from core.brain import think

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = "openai/gpt-3.5-turbo"

print("ELENA AI READY. Commands: /auto /pwd /ls /read <file>")

while True:
    user = input(">> ").strip()
    if user in ("exit", "quit"):
        break
    if user == "/auto":
        autonomous = not autonomous
        print("Autonomous:", autonomous)
        continue

    out, mode = think(user, API_KEY, MODEL, autonomous)
    print(f"[{mode}]\n{out}\n")
