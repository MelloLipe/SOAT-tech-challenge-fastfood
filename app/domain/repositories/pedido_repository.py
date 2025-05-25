
class PedidoRepository:
    def __init__(self):
        self.pedidos = {}

    def salvar(self, pedido):
        self.pedidos[pedido.id] = pedido

    def buscar_por_id(self, id):
        return self.pedidos.get(id)

    def listar_todos(self):
        return list(self.pedidos.values())

pedido_repo_instance = PedidoRepository()
