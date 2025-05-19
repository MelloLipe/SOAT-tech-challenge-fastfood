from app.application.dtos.pedido_dto import ProdutoAdicionadoDTO, PedidoDetalhadoDTO, PedidoItemDTO
from app.application.usecases.adicionar_produto import AdicionarProdutoAoPedido
from app.infrastructure.controllers.produto_controller import router
from app.infrastructure.persistence.db import pedido_repo_instance
from app.application.usecases.gerar_pagamento import GerarPagamento
from app.infrastructure.payment.mercado_pago_service import MercadoPagoService
from app.application.usecases.confirmar_pagamento import ConfirmarPagamento
from app.application.usecases.listar_pedidos_ativos import ListarPedidosAtivos
from app.application.usecases.atualizar_status_pedido import AtualizarStatusPedido

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

@router.get("/ativos")
def listar_pedidos_ativos():
    use_case = ListarPedidosAtivos(pedido_repo_instance)
    pedidos = use_case.execute()
    return [
        {
            "id": p.id,
            "status": p.status,
            "total": p.total,
            "cliente_id": p.cliente_id,
            "itens": [vars(item) for item in p.itens]
        } for p in pedidos
    ]

@router.patch("/{pedido_id}/status")
def atualizar_status(pedido_id: str, novo_status: str):
    use_case = AtualizarStatusPedido(pedido_repo_instance)
    pedido = use_case.execute(pedido_id, novo_status)
    return {
        "id": pedido.id,
        "status": pedido.status
    }

@router.post("/{pedido_id}/pagamento")
def gerar_pagamento(pedido_id: str):
    use_case = GerarPagamento(pedido_repo_instance, MercadoPagoService())
    resultado = use_case.execute(pedido_id)
    return resultado

@router.post("/{pedido_id}/confirmar-pagamento")
def confirmar_pagamento(pedido_id: str):
    use_case = ConfirmarPagamento(pedido_repo_instance)
    pedido = use_case.execute(pedido_id)
    return {
        "id": pedido.id,
        "status": pedido.status,
        "total": pedido.total
    }
