# app/application/usecases/atualizar_status_pedido.py
from app.domain.repositories.pedido_repository import PedidoRepository
from app.domain.entities.pedido import PedidoStatus


class AtualizarStatusPedido:
    STATUS_VALIDOS = {
        PedidoStatus.ENVIADO,
        "RECEBIDO",
        "EM_PREPARACAO",
        "PRONTO",
        PedidoStatus.FINALIZADO
    }

    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def execute(self, pedido_id: str, novo_status: str):
        if novo_status not in self.STATUS_VALIDOS:
            raise ValueError(f"Status inválido: {novo_status}")

        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")

        pedido.status = novo_status
        self.pedido_repo.salvar(pedido)
        return pedido
