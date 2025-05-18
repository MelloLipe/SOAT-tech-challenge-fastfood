# app/application/usecases/identificar_cliente.py
from app.domain.repositories.cliente_repository import ClienteRepository


class IdentificarCliente:
    def __init__(self, cliente_repo: ClienteRepository):
        self.cliente_repo = cliente_repo

    def execute(self, cpf: str):
        return self.cliente_repo.buscar_por_cpf(cpf)
