import uuid
from app.domain.entities.item_pedido import ItemPedido

class Pedido:
    def __init__(self, cliente_id=None):
        self.id = str(uuid.uuid4())
        self.cliente_id = cliente_id
        self.status = "CRIADO"
        self.itens = []
        self.total = 0.0

    def adicionar_item(self, produto_id, nome, preco, categoria, quantidade):
        item = ItemPedido(produto_id, nome, preco, categoria, quantidade)
        self.itens.append(item)
        self.total += item.total()

    def finalizar(self):
        self.status = "FINALIZADO"
