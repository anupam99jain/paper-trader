import requests

def ask_llm(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:7b",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    return response.json()["response"].strip()
