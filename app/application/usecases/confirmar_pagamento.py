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
            raise Exception("Pagamento só pode ser confirmado após o pedido ser FINALIZADO.")

        pedido.status = PedidoStatus.PAGO
        pedido.status = PedidoStatus.ENVIADO  # Política automática: envia à cozinha após pagar
        self.pedido_repo.salvar(pedido)
        return pedido
