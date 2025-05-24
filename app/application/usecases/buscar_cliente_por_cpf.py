from app.domain.repositories.cliente_repository import ClienteRepository

class BuscarClientePorCPF:
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    def execute(self, cpf: str):
        return self.repo.buscar_por_cpf(cpf)
