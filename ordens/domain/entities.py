from dataclasses import dataclass
from datetime import datetime

@dataclass
class OrdemServico:
    id: int | None
    cliente_id: int
    descricao: str
    status: str
    data_abertura: datetime
