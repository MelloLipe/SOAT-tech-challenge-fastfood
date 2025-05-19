from app.domain.repositories.pedido_repository import PedidoRepository
from app.domain.entities.pedido import PedidoStatus

class ListarPedidosAtivos:
    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def execute(self):
        todos = self.pedido_repo.listar_todos()
        return [p for p in todos if p.status != PedidoStatus.FINALIZADO]
