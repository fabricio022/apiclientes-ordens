from dataclasses import dataclass

@dataclass
class Cliente:
    id: int | None
    nome: str
    email: str
    telefone: str