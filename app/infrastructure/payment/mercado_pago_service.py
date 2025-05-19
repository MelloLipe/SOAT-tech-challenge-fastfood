# import uuid
# import os
#
#
# class MercadoPagoService:
#     def __init__(self):
#         self.access_token = os.getenv("MERCADO_PAGO_ACCESS_TOKEN", "fake-token")
#         self.base_url = os.getenv("MERCADO_PAGO_API_URL", "https://api.mercadopago.com")
#
#     def gerar_qr_code(self, pedido_id: str, valor: float) -> dict:
#         # Simulação com URL fake
#         qr_code_url = f"{self.base_url}/qr/{uuid.uuid4()}"
#         return {
#             "pedido_id": pedido_id,
#             "valor": valor,
#             "qr_code_url": qr_code_url
#         }
#
#     def confirmar_pagamento(self, pedido_id: str) -> bool:
#         # Simula que o pagamento foi confirmado com sucesso
#         return True
