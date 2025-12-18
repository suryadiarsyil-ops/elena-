# openrouter.py
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_cloud(prompt, api_key, model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are ELENA. Be concise and technical."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6,
        "max_tokens": 800
    }

    r = requests.post(API_URL, headers=headers, json=payload, timeout=30)
    return r.json()["choices"][0]["message"]["content"]
