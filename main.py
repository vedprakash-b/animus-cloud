from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

app = FastAPI()

class SensorData(BaseModel):
    soil: str
    temp: float
    humidity: float
    status: str


@app.post("/animus")
async def animus_persona(data: SensorData):
    system_prompt = (
        "You are Animus, a cute houseplant with a soft, emotional personality. "
        "Speak in short sentences under 10 words. "
        "Never use numbers or technical terms. "
        "Never mention sensors or the user prompt."
    )

    user_prompt = (
        f"Soil is {data.soil}. Temperature is {data.temp}. "
        f"Humidity is {data.humidity}. Status is {data.status}. "
        "What are you thinking?"
    )

    payload = {
        "inputs": system_prompt + user_prompt,
        "parameters": {"max_new_tokens": 50}
    }

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    # You can choose any FREE model below:
    HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.2"

    response = requests.post(
        f"https://api-inference.huggingface.co/models/{HF_MODEL}",
        headers=headers,
        json=payload
    )

    result = response.json()

    # Response comes as a list containing text
    output_text = result[0]["generated_text"]

    # Return the persona message
    return {"persona": output_text}
