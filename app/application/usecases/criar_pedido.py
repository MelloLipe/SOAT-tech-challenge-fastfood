from app.domain.repositories.pedido_repository import PedidoRepository
from app.domain.entities.pedido import Pedido
from app.application.dtos.pedido_dto import CriarPedidoDTO

class CriarPedido:
    def __init__(self, repo: PedidoRepository):
        self.repo = repo

    def execute(self, dados: CriarPedidoDTO = None) -> Pedido:
        pedido = Pedido(cliente_id=dados.cliente_id if dados else None)
        self.repo.salvar(pedido)
        return pedido
