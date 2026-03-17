import httpx
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()

KEY_GROQ_AI = os.getenv('KEY_GROQ_AI')

def gerar_texto(cidade_origem, cidade_destino, data, distancia, duracao, clima_origem, clima_destino):
    response = httpx.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            'Authorization': f'Bearer {KEY_GROQ_AI}',
            'content-type': 'application/json'
        },
        json={
            'model': 'llama-3.3-70b-versatile',
            'messages': [
                {
                    'role': 'user',
                    'content': f'''
                        Você é um assistente de viagens. Responda em português de forma direta e objetiva, sem entusiasmo exagerado.

Gere um texto corrido com as seguintes informações:
- Diga que a viagem entre {cidade_origem} e {cidade_destino} tem duração de {duracao:.1f} horas e distância de {distancia:.0f} km
- Diga como está o clima em {cidade_origem} na data {data}: temperatura máxima de {clima_origem['temperature_2m_max'][0]}°C, mínima de {clima_origem['temperature_2m_min'][0]}°C e {clima_origem['precipitation_sum'][0]}mm de chuva
- Diga como está o clima em {cidade_destino} na mesma data: temperatura máxima de {clima_destino['temperature_2m_max'][0]}°C, mínima de {clima_destino['temperature_2m_min'][0]}°C e {clima_destino['precipitation_sum'][0]}mm de chuva
- A viagem é terrestre, de carro
- Não use markdown, não use asteriscos, não use tópicos
                    '''
                }
            ]
        }
    )
    dados = response.json()
    texto = dados['choices'][0]['message']['content']

    return texto