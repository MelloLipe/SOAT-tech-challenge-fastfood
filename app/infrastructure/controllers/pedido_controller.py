from fastapi import APIRouter
from app.application.usecases.criar_pedido import CriarPedido
from app.application.usecases.adicionar_produto import AdicionarProduto
from app.application.usecases.finalizar_pedido import FinalizarPedido
from app.domain.repositories.pedido_repository import pedido_repo_instance
from app.application.dtos.pedido_dto import CriarPedidoDTO, ProdutoAdicionadoDTO

router = APIRouter()

@router.post("/")
def criar_pedido(dados: CriarPedidoDTO = None):
    use_case = CriarPedido(pedido_repo_instance)
    pedido = use_case.execute(dados)
    return {"id": pedido.id, "status": pedido.status, "total": pedido.total}

@router.post("/adicionar-produto")
def adicionar_produto(dados: ProdutoAdicionadoDTO):
    use_case = AdicionarProduto(pedido_repo_instance)
    pedido = use_case.execute(**dados.dict())
    return {
        "id": pedido.id,
        "itens": [vars(item) for item in pedido.itens],
        "total": pedido.total,
        "status": pedido.status
    }

@router.post("/{pedido_id}/checkout")
def finalizar_pedido(pedido_id: str):
    use_case = FinalizarPedido(pedido_repo_instance)
    pedido = use_case.execute(pedido_id)
    return {
        "id": pedido.id,
        "status": pedido.status,
        "total": pedido.total
    }

@router.get("/")
def listar_pedidos():
    pedidos = pedido_repo_instance.listar_todos()
    return [
        {
            "id": p.id,
            "status": p.status,
            "total": p.total,
            "cliente_id": p.cliente_id,
            "itens": [vars(item) for item in p.itens]
        }
        for p in pedidos
    ]
