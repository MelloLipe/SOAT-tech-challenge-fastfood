
class ItemPedido:
    def __init__(self, produto_id, nome, preco, categoria, quantidade):
        self.produto_id = produto_id
        self.nome = nome
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade

    def total(self):
        return self.preco * self.quantidade
