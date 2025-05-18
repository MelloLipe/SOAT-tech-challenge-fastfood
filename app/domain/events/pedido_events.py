# app/domain/events/pedido_events.py

class PedidoIniciado:
    def __init__(self, pedido_id: str):
        self.pedido_id = pedido_id


class ProdutoAdicionadoAoPedido:
    def __init__(self, pedido_id: str, produto_id: str):
        self.pedido_id = pedido_id
        self.produto_id = produto_id


class PedidoFinalizado:
    def __init__(self, pedido_id: str):
        self.pedido_id = pedido_id


class PagamentoConfirmado:
    def __init__(self, pedido_id: str):
        self.pedido_id = pedido_id


class PedidoEnviadoParaCozinha:
    def __init__(self, pedido_id: str):
        self.pedido_id = pedido_id
