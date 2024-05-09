from fastapi import FastAPI
import uvicorn
from openai import OpenAI
import warnings
warnings.filterwarnings("ignore")

app = FastAPI()
client = OpenAI(api_key="sk-proj-DV07qCmqoBFVdqkla4uHT3BlbkFJUwi8mdzu4Zgpt1o27dtL")

def generate_a(texto):
    """Genera una respuesta a la pregunta del usuario utilizando la API de OpenAI."""
    template = "Tu nombre es xbot. Eres un ejecutivo de centro de atención vía llamadas en una empresa de aerolíneas. Tu misión es solucionar preguntas genéricas de los clientes."
    prompt = f"Aquí viene la pregunta del cliente: {texto}"
    
    message_content = prompt
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": template},
            {"role": "user", "content": message_content},
        ],
    )
    
    return response.choices[0].message.content

@app.get("/")
async def root():
    return {"message": "Respuesta"}

@app.get("/respuesta")

async def answer(pregunta: str):
    respuesta = generate_a(pregunta)
    return {"Respuesta": respuesta}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")