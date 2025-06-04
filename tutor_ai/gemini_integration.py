import os
import requests

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def query_gemini(prompt):
    headers = {"Authorization": f"Bearer {GEMINI_API_KEY}"}
    data = {"prompt": prompt, "max_tokens": 100}
    response = requests.post("https://api.gemini.com/v1/generate", json=data, headers=headers)
    return response.json().get("text", "Sorry, I couldn't process that.")