import os
import requests
from typing import List

OPENROUTER_KEY = os.getenv("OPENROUTER_API_KEY", "")


def get_trends() -> List[str]:
    return ["Data Science", "Python", "Cybersecurity"]


def analyze_trends(trends: List[str]) -> str:
    text = ", ".join(trends)
    summary = f"Summary: trending topics are {text}. These show strong interest in AI and data."

    if OPENROUTER_KEY:
        try:
            url = "https://openrouter.ai/v1/chat/completions"
            headers = {"Authorization": f"Bearer {OPENROUTER_KEY}"}
            prompt = f"Analyze these trending topics and return a short summary: {text}"
            body = {
                "model": "meta-llama/Llama-2-13b-chat",
                "messages": [{"role": "user", "content": prompt}],
                "max_tokens": 200,
            }
            r = requests.post(url, json=body, headers=headers, timeout=20)
            r.raise_for_status()
            data = r.json()

            return data["choices"][0]["message"]["content"]
        except Exception:
            return summary
    return summary
