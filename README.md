🗺️ Previsão de Viagens
API backend desenvolvida com FastAPI que recebe duas cidades e uma data de viagem e retorna um resumo completo gerado por IA, com distância, duração estimada e previsão do tempo para origem e destino.

🚀 Funcionalidades

Cálculo de distância e duração da viagem por estrada entre duas cidades
Previsão do tempo para a cidade de origem e destino na data da viagem
Geração de texto em linguagem natural com IA resumindo todas as informações


🧱 Tecnologias utilizadas

FastAPI — framework web para construção da API
Uvicorn — servidor ASGI para rodar a aplicação
HTTPX — cliente HTTP para chamadas às APIs externas
Pydantic — validação dos dados de entrada
Python-dotenv — gerenciamento de variáveis de ambiente


🔌 APIs integradas
APIFunçãoCadastro necessárioNominatim (OpenStreetMap)Geocodificação — converte nome de cidade em coordenadasNãoOpenRouteServiceCálculo de distância e duração por estradaSim (gratuito)Open-MeteoPrevisão do tempo por coordenadasNãoGroqGeração de texto com IA (modelo LLaMA 3.3)Sim (gratuito)

📁 Estrutura do projeto
projeto-viagem/
├── main.py                        # Entrada da aplicação e definição das rotas
├── schemas.py                     # Modelos Pydantic para validação dos dados
├── services/
│   ├── service_distancia.py       # Integração com Nominatim e OpenRouteService
│   ├── service_clima.py           # Integração com Open-Meteo
│   └── service_gerar_resposta.py  # Integração com Groq AI
├── .env                           # Chaves de API (não subir para o repositório)
├── .gitignore
└── requirements.txt

⚙️ Como rodar o projeto
1. Clone o repositório
bashgit clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Instale as dependências
bashpip install fastapi uvicorn httpx python-dotenv
3. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com as suas chaves:
KEY_OPENROUTESERVICE=sua_chave_aqui
KEY_GROQ_AI=sua_chave_aqui
4. Rode a aplicação
bashuvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000

📬 Endpoints
POST /escolher_cidades
Recebe os dados da viagem, consulta as APIs externas e retorna um texto gerado por IA.
Body (JSON):
json{
  "cidade_origem": "Caetité",
  "cidade_destino": "Vitória da Conquista",
  "data": "2026-03-17T00:00:00Z"
}
Resposta:
json{
  "texto": "A viagem entre Caetité e Vitória da Conquista tem duração estimada de 3.8 horas e distância de 278 km. O clima em Caetité na data prevista é de temperatura máxima de 29°C e mínima de 18°C, sem previsão de chuva. Em Vitória da Conquista, a temperatura máxima será de 27°C e mínima de 16°C, também sem chuva prevista."
}

⚠️ O campo data é opcional. Se não for informado, será usado o horário atual (UTC).


⚠️ Limitações conhecidas

O OpenRouteService calcula apenas rotas terrestres. Cidades em continentes diferentes (ex: Brasil e EUA) não são suportadas.
A previsão do tempo está disponível para até 16 dias no futuro.
O fuso horário utilizado é America/Sao_Paulo, adequado para a maioria das cidades brasileiras.


🔮 Melhorias futuras

Calcular o clima do destino considerando o horário estimado de chegada (usando previsão por hora com hourly no Open-Meteo)
Adicionar suporte a múltiplos fusos horários automaticamente
Implementar banco de dados para histórico de consultas
Adicionar uma rota GET para buscar o histórico de viagens consultadas
