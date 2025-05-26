from fastapi import APIRouter, HTTPException
from app.domain.repositories.produto_repository import produto_repo_instance
from app.application.usecases.criar_produto import CriarProduto
from app.application.usecases.atualizar_produto import AtualizarProduto
from app.application.usecases.remover_produto import RemoverProduto
from app.application.usecases.buscar_produtos_por_categoria import BuscarProdutosPorCategoria
from app.application.dtos.produto_dto import CriarProdutoDTO, EditarProdutoDTO

router = APIRouter(prefix="/produtos", tags=["Produtos"])

@router.post("/")
def criar_produto(dados: CriarProdutoDTO):
    use_case = CriarProduto(produto_repo_instance)
    produto = use_case.execute(dados)
    return vars(produto)

@router.put("/{id}")
def atualizar_produto(id: str, dados: EditarProdutoDTO):
    try:
        campos = dados.dict(exclude_unset=True)
        if not campos:
            raise HTTPException(status_code=400, detail="Nenhum campo para atualizar.")
        usecase = AtualizarProduto(produto_repo_instance)
        return vars(usecase.execute(id=id, **campos))
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{id}")
def remover_produto(id: str):
    use_case = RemoverProduto(produto_repo_instance)
    use_case.execute(id)
    return {"mensagem": "Produto removido"}

@router.get("/categoria/{categoria}")
def buscar_por_categoria(categoria: str):
    use_case = BuscarProdutosPorCategoria(produto_repo_instance)
    produtos = use_case.execute(categoria)
    return [vars(p) for p in produtos]
