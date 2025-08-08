from clientes.domain.repositories import ClienteRepository
from clientes.domain.entities import Cliente
from clientes.models import ClienteModel

class DjangoClienteRepository(ClienteRepository):
    def listar(self) -> list[Cliente]:
        return [
            Cliente(id=obj.id, nome=obj.nome, email=obj.email, telefone=obj.telefone)
            for obj in ClienteModel.objects.all()
        ]

    def criar(self, cliente: Cliente) -> Cliente:
        obj = ClienteModel.objects.create(
            nome=cliente.nome, email=cliente.email, telefone=cliente.telefone
        )
        return Cliente(id=obj.id, nome=obj.nome, email=obj.email, telefone=obj.telefone)
