from ordens.domain.entities import OrdemServico
from ordens.domain.repositories import OrdemServicoRepository
from datetime import datetime

class CriarOrdemServico:
    def __init__(self, repo: OrdemServicoRepository):
        self.repo = repo

    def execute(self, cliente_id: int, descricao: str) -> OrdemServico:
        nova_ordem = OrdemServico(
            id=None,
            cliente_id=cliente_id,
            descricao=descricao,
            status="aberta",
            data_abertura=datetime.now()
        )
        return self.repo.criar(nova_ordem)
