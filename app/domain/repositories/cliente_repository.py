
class ClienteRepository:
    def __init__(self):
        self.clientes = {}

    def salvar(self, cliente):
        self.clientes[cliente.cpf] = cliente

    def buscar_por_cpf(self, cpf):
        return self.clientes.get(cpf)

cliente_repo_instance = ClienteRepository()
