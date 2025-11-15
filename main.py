from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

app = FastAPI()

class SensorData(BaseModel):
    soil: str
    temp: float
    humidity: float
    status: str

@app.post("/animus")
async def animus_persona(data: SensorData):

    prompt = f"""
    You are Animus, a cute houseplant with a soft emotional personality.
    Respond in short, sweet sentences under 10 words.
    Never mention sensors or numbers.
    Soil: {data.soil}
    Temperature: {data.temp}
    Humidity: {data.humidity}
    Overall status: {data.status}
    What are you feeling?
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return {"persona": response.choices[0].message["content"]}
