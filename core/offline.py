# offline.py
import re

RULES = [
    (r"\bls\b", "Gunakan ls untuk melihat isi direktori."),
    (r"\bcd\b", "Gunakan cd <folder> untuk berpindah."),
    (r"\bpwd\b", "pwd menunjukkan direktori saat ini."),
]

def offline_response(text):
    for p, r in RULES:
        if re.search(p, text, re.I):
            return r
    return None
