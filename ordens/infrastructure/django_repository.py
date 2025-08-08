from ordens.domain.repositories import OrdemServicoRepository
from ordens.domain.entities import OrdemServico
from ordens.models import OrdemServicoModel

class DjangoOrdemServicoRepository(OrdemServicoRepository):
    def listar(self) -> list[OrdemServico]:
        return [
            OrdemServico(
                id=obj.id,
                cliente_id=obj.cliente_id,
                descricao=obj.descricao,
                status=obj.status,
                data_abertura=obj.data_abertura
            )
            for obj in OrdemServicoModel.objects.all()
        ]

    def criar(self, ordem: OrdemServico) -> OrdemServico:
        obj = OrdemServicoModel.objects.create(
            cliente_id=ordem.cliente_id,
            descricao=ordem.descricao,
            status=ordem.status,
            data_abertura=ordem.data_abertura
        )
        return OrdemServico(
            id=obj.id,
            cliente_id=obj.cliente_id,
            descricao=obj.descricao,
            status=obj.status,
            data_abertura=obj.data_abertura
        )
