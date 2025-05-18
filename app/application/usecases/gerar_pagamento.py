from app.domain.repositories.pedido_repository import PedidoRepository
from app.infrastructure.payment.mercado_pago_service import MercadoPagoService


class GerarPagamento:
    def __init__(self, pedido_repo: PedidoRepository, pagamento_service: MercadoPagoService):
        self.pedido_repo = pedido_repo
        self.pagamento_service = pagamento_service

    def execute(self, pedido_id: str):
        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")

        if pedido.status != "FINALIZADO":
            raise Exception("Pedido precisa estar FINALIZADO para gerar pagamento.")

        return self.pagamento_service.gerar_qr_code(pedido.id, pedido.total)
