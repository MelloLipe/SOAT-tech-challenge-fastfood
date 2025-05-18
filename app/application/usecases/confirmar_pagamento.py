# app/application/usecases/confirmar_pagamento.py
from app.domain.repositories.pedido_repository import PedidoRepository
from app.domain.entities.pedido import PedidoStatus


class ConfirmarPagamento:
    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def execute(self, pedido_id: str):
        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")

        if pedido.status != PedidoStatus.FINALIZADO:
            raise Exception("Pedido deve estar FINALIZADO para confirmar pagamento.")

        # Confirma pagamento
        pedido.status = PedidoStatus.PAGO

        # Envia automaticamente para cozinha
        pedido.status = PedidoStatus.ENVIADO

        self.pedido_repo.salvar(pedido)
        return pedido
