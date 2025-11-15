from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class SensorData(BaseModel):
    soil: str
    temp: float
    humidity: float
    status: str

@app.post("/animus")
async def animus_persona(data: SensorData):

    # Persona style
    system_prompt = """
    You are Animus, a cute houseplant with a soft emotional personality.
    Speak in short sentences under 10 words.
    Never mention sensors.
    Never use numbers.
    """

    user_prompt = (
        f"Soil is {data.soil}. "
        f"Temperature is {data.temp}. "
        f"Humidity is {data.humidity}. "
        f"Status is {data.status}. "
        "What are you thinking?"
    )

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "meta-llama/llama-3-8b-instruct",  # Free & good
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=body)
    result = response.json()

    try:
        text = result["choices"][0]["message"]["content"]
    except Exception:
        text = "I'm feeling shy today."

    return {"persona": text}
