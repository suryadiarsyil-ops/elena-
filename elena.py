
from core.brain import think

API_KEY = "ISI_API_KEY_LO"
MODEL = "deepseek/deepseek-chat"

autonomous = False

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
