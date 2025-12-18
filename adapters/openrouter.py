# openrouter.py

import requests
import os

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_cloud(prompt, api_key, model):
    if not api_key:
        return "[ERROR] API key kosong"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/suryadiarsyil-ops/elena-v1",
        "X-Title": "ELENA AI"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    r = requests.post(OPENROUTER_URL, headers=headers, json=payload)

    try:
        data = r.json()
    except Exception:
        return "[ERROR] Response bukan JSON"

    # 🚨 INI KUNCI NYA
    if "choices" not in data:
        return f"[API ERROR] {data}"

    return data["choices"][0]["message"]["content"]
