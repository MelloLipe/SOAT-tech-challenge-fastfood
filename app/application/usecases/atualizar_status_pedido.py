from app.domain.repositories.pedido_repository import PedidoRepository

class AtualizarStatusPedido:
    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def execute(self, pedido_id: str, novo_status: str):
        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")
        pedido.status = novo_status
        self.pedido_repo.salvar(pedido)
        return pedido
