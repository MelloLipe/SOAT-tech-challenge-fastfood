from app.domain.repositories.pedido_repository import PedidoRepository
from app.infrastructure.payment.mercado_pago_service import MercadoPagoService
from app.domain.entities.pedido import PedidoStatus


class ConfirmarPagamentoReal:
    def __init__(self, pedido_repo: PedidoRepository, pagamento_service: MercadoPagoService):
        self.pedido_repo = pedido_repo
        self.pagamento_service = pagamento_service

    def execute(self, pedido_id: str):
        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")

        if pedido.status != PedidoStatus.FINALIZADO:
            raise Exception("Pagamento só pode ser confirmado após o pedido ser finalizado.")

        pagamento_confirmado = self.pagamento_service.confirmar_pagamento(pedido.id)

        if pagamento_confirmado:
            pedido.status = PedidoStatus.ENVIADO
            self.pedido_repo.salvar(pedido)
            return pedido
        else:
            raise Exception("Falha na confirmação do pagamento.")
