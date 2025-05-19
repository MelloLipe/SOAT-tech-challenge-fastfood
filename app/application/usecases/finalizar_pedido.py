
class FinalizarPedido:
    def execute(self, pedido_id: str):
        pedido = self.pedido_repo.buscar_por_id(pedido_id)
        if not pedido:
            raise Exception("Pedido não encontrado.")

        pedido.finalizar()  # <--- Aqui ele é marcado como FINALIZADO
        self.pedido_repo.salvar(pedido)
        return pedido



# class FinalizarPedido:
#     def __init__(self, pedido_repo: PedidoRepository):
#         self.pedido_repo = pedido_repo
#
#     def execute(self, pedido_id: str):
#         pedido = self.pedido_repo.buscar_por_id(pedido_id)
#         if not pedido:
#             raise Exception("Pedido não encontrado.")
#
#         pedido.finalizar()
#         self.pedido_repo.salvar(pedido)
#
#         # Dispara os eventos registrados
#         pedido.eventos().despachar()
#
#         return pedido
