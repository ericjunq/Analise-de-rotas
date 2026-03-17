import httpx
from services.service_distancia import pegar_coordenadas

response = 'https://open-meteo.com/en/docs'


def calcular_clima(cidade_origem, cidade_destino, data):
    lat_origem, lon_origem = pegar_coordenadas(cidade_origem)
    lat_destino, lon_destino = pegar_coordenadas(cidade_destino)

    response_origem = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            'latitude': lat_origem,
            'longitude': lon_origem,
            'daily': "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
            'timezone': 'America/Sao_Paulo',
            'start_date': data, # da pra fazer uma implementação de calcular pelo calculo de tempo entre as cidades, calcular o clima do destino com essa diferença de tempo adicionada
            'end_date': data
            }    
    )

    response_destino = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            'latitude': lat_destino,
            'longitude': lon_destino,
            'daily': "temperature_2m_max,temperature_2m_min,precipitation_sum,weathercode",
            'timezone': 'America/Sao_Paulo',
            'start_date': data,
            'end_date': data
        }
    )

    clima_origem = response_origem.json()['daily']
    clima_destino = response_destino.json()['daily']

    return clima_origem, clima_destino

