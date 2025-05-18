from app.application.dtos.pedido_dto import ProdutoAdicionadoDTO, PedidoDetalhadoDTO, PedidoItemDTO
from app.application.usecases.adicionar_produto import AdicionarProdutoAoPedido
from app.infrastructure.controllers.produto_controller import router
from app.infrastructure.persistence.db import pedido_repo_instance
from app.application.usecases.gerar_pagamento import GerarPagamento
from app.infrastructure.payment.mercado_pago_service import MercadoPagoService


@router.post("/adicionar-produto", response_model=PedidoDetalhadoDTO)
def adicionar_produto(dados: ProdutoAdicionadoDTO):
    use_case = AdicionarProdutoAoPedido(pedido_repo_instance)
    pedido = use_case.execute(**dados.dict())
    return PedidoDetalhadoDTO(
        id=pedido.id,
        status=pedido.status,
        total=pedido.total,
        cliente_id=pedido.cliente_id,
        itens=[
            PedidoItemDTO(
                produto_id=item.produto_id,
                nome=item.nome,
                categoria=item.categoria,
                preco_unitario=item.preco_unitario,
                quantidade=item.quantidade
            )
            for item in pedido.itens
        ]
    )


@router.post("/{pedido_id}/pagamento")
def gerar_pagamento(pedido_id: str):
    use_case = GerarPagamento(pedido_repo_instance, MercadoPagoService())
    resultado = use_case.execute(pedido_id)
    return resultado
