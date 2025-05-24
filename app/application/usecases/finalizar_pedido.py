from app.domain.repositories.pedido_repository import PedidoRepository

class FinalizarPedido:
    def __init__(self, repo: PedidoRepository):
        self.repo = repo

    def execute(self, pedido_id: str):
        pedido = self.repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")
        pedido.finalizar()
        self.repo.salvar(pedido)
        return pedido
