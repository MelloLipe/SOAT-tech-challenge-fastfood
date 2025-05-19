from app.domain.entities.cliente import Cliente
from app.domain.repositories.cliente_repository import ClienteRepository


class CadastrarCliente:
    def __init__(self, cliente_repo: ClienteRepository):
        self.cliente_repo = cliente_repo

    def execute(self, nome: str, email: str, cpf: str):
        cliente = Cliente(nome=nome, email=email, cpf=cpf)
        self.cliente_repo.salvar(cliente)
        return cliente
