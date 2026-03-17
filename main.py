from fastapi import FastAPI
from services.service_clima import calcular_clima
from services.service_distancia import calcular_distancia
from services.service_gerar_resposta import gerar_texto
from schemas import EscolherCidades

app = FastAPI()


@app.post('/escolher_cidades')
def analisar_rota_cidades(dados: EscolherCidades):
    cidade_origem = dados.cidade_origem,
    cidade_destino = dados.cidade_destino,
    data = dados.data

    data_formatada = data.strftime('%Y-%m-%d')

    distancia, duracao = calcular_distancia(cidade_origem, cidade_destino)
    clima_origem, clima_destino = calcular_clima(cidade_origem, cidade_destino, data_formatada)
    texto = gerar_texto(cidade_origem, cidade_destino, data_formatada, distancia, duracao, clima_origem, clima_destino)

    return {'texto': texto}