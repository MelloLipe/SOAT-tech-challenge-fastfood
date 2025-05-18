# app/domain/entities/item_pedido.py


class ItemPedido:
    def __init__(self, produto_id: str, nome: str, preco_unitario: float, categoria: str, quantidade: int):
        self.produto_id = produto_id
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.categoria = categoria
        self.quantidade = quantidade

    def preco_total(self) -> float:
        return self.preco_unitario * self.quantidade
