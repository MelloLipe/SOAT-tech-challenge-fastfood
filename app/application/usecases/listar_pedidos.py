# app/application/usecases/listar_pedidos.py
from app.domain.repositories.pedido_repository import PedidoRepository


class ListarPedidos:
    def __init__(self, repo: PedidoRepository):
        self.repo = repo

    def execute(self):
        return self.repo.listar_todos()
