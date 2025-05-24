from app.domain.entities.cliente import Cliente
from app.domain.repositories.cliente_repository import ClienteRepository

class CriarCliente:
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    def execute(self, nome: str, email: str, cpf: str):
        cliente = Cliente(nome=nome, email=email, cpf=cpf)
        self.repo.salvar(cliente)
        return cliente
