from app.domain.repositories.pedido_repository import PedidoRepository

class AdicionarProduto:
    def __init__(self, repo: PedidoRepository):
        self.repo = repo

    def execute(self, pedido_id: str, produto_id: str, nome: str, preco: float, categoria: str, quantidade: int):
        pedido = self.repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")
        pedido.adicionar_item(produto_id, nome, preco, categoria, quantidade)
        self.repo.salvar(pedido)
        return pedido
