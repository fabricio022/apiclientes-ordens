from abc import ABC, abstractmethod
from .entities import Cliente

class ClienteRepository(ABC):
    @abstractmethod
    def listar(self) -> list[Cliente]: pass

    @abstractmethod
    def criar(self, cliente: Cliente) -> Cliente: pass
