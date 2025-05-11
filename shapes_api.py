import requests
from config import SHAPES_API_KEY, SHAPES_API_URL

def ask_shapes(prompt: str, user_id: str, channel_id: str) -> str:
    headers = {
        "Authorization": f"Bearer {SHAPES_API_KEY}",
        "X-User-ID": user_id,
        "X-Channel-ID": channel_id,
        "Content-Type": "application/json"
    }
    json_data = {
        "model": "shapes-1",  # or your available model
        "messages": [{"role": "user", "content": prompt}],
        "stream": False
    }
    response = requests.post(SHAPES_API_URL, headers=headers, json=json_data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
