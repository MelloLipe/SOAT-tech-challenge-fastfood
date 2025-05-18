# app/application/usecases/adicionar_produto.py
from app.domain.repositories.pedido_repository import PedidoRepository
from app.domain.entities.item_pedido import ItemPedido


class AdicionarProdutoAoPedido:
    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def execute(self, pedido_id: str, produto_id: str, nome: str, preco: float, categoria: str, quantidade: int):
        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")

        item = ItemPedido(produto_id, nome, preco, categoria, quantidade)
        pedido.adicionar_item(item)
        self.pedido_repo.salvar(pedido)
        return pedido
