import httpx
from dotenv import load_dotenv
import os 

load_dotenv()

KEY_OPENROUTESERVICE = os.getenv('KEY_OPENROUTESERVICE')

def pegar_coordenadas(cidade):
    response = httpx.get(
        "https://nominatim.openstreetmap.org/search",
        params={
            'q': cidade,
            'format': 'json'
        },
        headers={
            'User-Agent': 'previsao-de-viagens'
        }
        )
    
    resultado = response.json()[0]
    lat = float(resultado['lat'])
    lon = float(resultado['lon'])

    return lat, lon 

def calcular_distancia(cidade_origem, cidade_destino):
    lat_origem, lon_origem = pegar_coordenadas(cidade_origem)
    lat_destino, lon_destino = pegar_coordenadas(cidade_destino)

    response = httpx.post(
        'https://api.openrouteservice.org/v2/directions/driving-car',
        headers={
            'Authorization': KEY_OPENROUTESERVICE   
        },
        json={
            'coordinates': [
                [lon_origem, lat_origem],
                [lon_destino, lat_destino]
            ]
        }
    )

    dados = response.json()
    distancia_km = dados['routes'][0]['summary']['distance'] / 1000
    tempo_horas = dados['routes'][0]['summary']['duration'] / 3600

    return distancia_km, tempo_horas


def calcular_horario_final(cidade_origem, cidade_destino):
    distancia, tempo = calcular_distancia(cidade_origem, cidade_destino)
    return f'{tempo:.1f}'
