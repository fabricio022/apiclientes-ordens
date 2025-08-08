from abc import ABC, abstractmethod
from .entities import OrdemServico

class OrdemServicoRepository(ABC):
    @abstractmethod
    def listar(self) -> list[OrdemServico]:
        pass

    @abstractmethod
    def criar(self, ordem: OrdemServico) -> OrdemServico:
        pass
