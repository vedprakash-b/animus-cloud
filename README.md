# OVERVIEW
Project Animus is a solar-powered AIoT system that monitors plant health using environmental sensor data and converts it into contextual, human like plant responses through cloud hosted AI models.

Instead of displaying only raw sensor values, the system interprets plant conditions and generates personality based outputs such as: “I’m feeling thirsty today.”
This project combines IoT, cloud computing, FastAPI, and generative AI to create an intelligent, low power smart plant ecosystem.

# FEATURES
Solar-powered low-power system design

Soil moisture, temperature, and humidity monitoring

FastAPI cloud backend deployment on Render

AI-generated plant persona using prompt engineering

REST API communication between edge device and cloud

Flexible integration with Hugging Face / OpenRouter / other LLM APIs

# SYSTEM ARCHITECTURE

Sensors / ESP32 -> HTTP POST Request -> FastAPI Backend (Render) -> Prompt Engineering Layer -> LLM API (Hugging Face / OpenRouter) -> Plant Persona Response -> LED / App / Dashboard Output

# TECH STACK
Backend / Cloud


-Python

-FastAPI

-Uvicorn

-Render

-REST APIs

AI

-Generative AI APIs

-Prompt Engineering

-Hugging Face / OpenRouter

IoT

-ESP32 (planned integration)

-Solar-powered edge system


# INSTALLATION
git clone https://github.com/vedprakash-b/animus-cloud.git

cd animus-cloud

pip install -r requirements.txt

# ENVIRONMENT VARIABLES
HF_API_KEY=your_api_key_here

OPENROUTER_API_KEY=your_api_key_here

# RUN LOCALLY
uvicorn main:app --reload

access-
http://127.0.0.1:8000/docs

# API ENDPOINT

example request:
{
  "soil": "dry",
  "temp": 30,
  "humidity": 35,
  "status": "stressed"
}
example response -
{
  "persona": "I feel thirsty today."
}

# KEY LEARNING OUTCOMES
FastAPI backend development

Cloud deployment

REST API architecture

Prompt engineering

LLM integration

Edge-cloud AI system design

# FUTURE IMPROVEMENTS
Plant species-specific responses

Mobile dashboard

Notification system

OLED / LED integration
TinyML fallback system

Author
Vedprakash B
GitHub: github.com/vedprakash-b
