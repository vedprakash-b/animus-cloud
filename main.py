from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

app = FastAPI()

class SensorData(BaseModel):
    soil: str
    temp: float
    humidity: float
    status: str

@app.post("/animus")
async def animus_persona(data: SensorData):

    system_prompt = """
    You are Animus, a cute emotional houseplant.
    Speak in short casual sentences. Under 12 words.
    Avoid technical terms.
    Never mention sensors.
    Express emotions differently each time.
    React based on soil, temp, humidity, and status.
    """

    user_prompt = (
        f"Soil: {data.soil}. Temp: {data.temp}. "
        f"Humidity: {data.humidity}. Status: {data.status}. "
        "What are you feeling?"
    )

    payload = {
        "inputs": system_prompt + "\n" + user_prompt
    }

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}"
    }

    # FREE model on Hugging Face
    MODEL_URL = "https://api-inference.huggingface.co/models/microsoft/Phi-3-mini-4k-instruct"

    response = requests.post(MODEL_URL, headers=headers, json=payload)

    result = response.json()

    # FIXED EXTRACTION
    if isinstance(result, list):
        output_text = result[0].get("generated_text", "")
    elif "generated_text" in result:
        output_text = result["generated_text"]
    else:
        output_text = "I'm feeling shy today..."

    return {"persona": output_text}
