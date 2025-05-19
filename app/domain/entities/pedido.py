import uuid
from datetime import datetime
from typing import List
from app.domain.entities.item_pedido import ItemPedido
from app.domain.events.pedido_events import PedidoFinalizado
from app.domain.event_dispatcher import DomainEventDispatcher


class PedidoStatus:
    INICIADO = "INICIADO"
    FINALIZADO = "FINALIZADO"
    PAGO = "PAGO"
    ENVIADO = "ENVIADO"
    RECEBIDO = "RECEBIDO"
    EM_PREPARACAO = "EM_PREPARACAO"
    PRONTO = "PRONTO"

class Pedido:
    def __init__(self, cliente_id: str = None):
        self.id = str(uuid.uuid4())
        self.cliente_id = cliente_id
        self.status = PedidoStatus.INICIADO
        self.itens: List[ItemPedido] = []
        self.total = 0.0
        self.criado_em = datetime.utcnow()
        self._event_dispatcher = DomainEventDispatcher()

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)
        self.total += item.preco_total()

    def finalizar(self):
        if not self.itens:
            raise Exception("Pedido não pode ser finalizado sem itens.")
        self.status = PedidoStatus.FINALIZADO
        self._event_dispatcher.registrar(PedidoFinalizado(self.id))

    def eventos(self):
        return self._event_dispatcher
