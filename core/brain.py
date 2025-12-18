# core/brain.py

from core.offline import offline_response
from core.memory import recall, store_memory
from core.planner import plan
from core.executor import execute
from adapters.openrouter import ask_cloud


def think(user_input, api_key, model, autonomous=False):
    # 1. OFFLINE FIRST (TETAP)
    offline = offline_response(user_input)
    if offline:
        return offline, "offline"

    # 2. AUTONOMOUS MODE (BARU)
    if autonomous:
        tasks = plan(user_input)
        output = "Autonomous execution plan:\n"

        for i, task in enumerate(tasks, 1):
            result = execute(task)
            output += f"\nStep {i}: {task}\n→ {result}\n"

        # simpan hanya jika substansial
        if len(output) > 80:
            store_memory(user_input)
            store_memory(output)

        return output, "autonomous"

    # 3. NORMAL MODE (KODE ASLI KAMU)
    memories = recall(user_input)
    prompt = ""

    if memories:
        prompt += "Relevant past context:\n"
        for m in memories:
            prompt += f"- {m}\n"
        prompt += "\n"

    prompt += user_input

    response = ask_cloud(prompt, api_key, model)

    # simpan hanya yang penting
    if len(response) > 50:
        store_memory(user_input)
        store_memory(response)

    return response, "cloud+memory"
