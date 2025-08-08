from clientes.domain.entities import Cliente
from clientes.domain.repositories import ClienteRepository

class CriarCliente:
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    def execute(self, nome: str, email: str, telefone: str) -> Cliente:
        novo_cliente = Cliente(id=None, nome=nome, email=email, telefone=telefone)
        return self.repo.criar(novo_cliente)
