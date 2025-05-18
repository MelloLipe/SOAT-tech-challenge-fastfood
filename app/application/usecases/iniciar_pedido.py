# app/application/usecases/iniciar_pedido.py
from app.domain.entities.pedido import Pedido
from app.domain.repositories.pedido_repository import PedidoRepository


class IniciarPedido:
    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def execute(self, cliente_id: str = None) -> Pedido:
        pedido = Pedido(cliente_id)
        self.pedido_repo.salvar(pedido)
        return pedido
