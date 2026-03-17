from pydantic import BaseModel, Field
from datetime import datetime, timezone

class EscolherCidades(BaseModel):
    cidade_origem: str 
    cidade_destino: str 
    data: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

