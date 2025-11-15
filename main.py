from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

app = FastAPI()

class SensorData(BaseModel):
    soil: str
    temp: float
    humidity: float
    status: str

@app.post("/animus")
async def animus_persona(data: SensorData):
    system_prompt = """
    You are Animus, a cute houseplant with a soft, emotional personality.
    Speak in short sentences under 10 words.
    Never use numbers or technical terms.
    Never mention sensors.
    """

    user_prompt = f"Soil is {data.soil}. Temperature is {data.temp}. Humidity is {data.humidity}. Status is {data.status}. What are you thinking?"

    model = genai.GenerativeModel("models/chat-bison-001")

    response = model.generate_content(system_prompt + user_prompt)

    return {"persona": response.text}
