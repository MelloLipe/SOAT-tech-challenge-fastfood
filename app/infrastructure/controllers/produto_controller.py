from fastapi import APIRouter, HTTPException
from app.infrastructure.persistence.db import produto_repo_instance
from app.application.usecases.crud_produto import CriarProduto, EditarProduto, RemoverProduto
from app.application.usecases.buscar_produtos_categoria import BuscarProdutosPorCategoria
from app.application.dtos.produto_dto import CriarProdutoDTO, EditarProdutoDTO, ProdutoDTO

router = APIRouter()


@router.post("/", summary="Criar produto", response_model=ProdutoDTO)
def criar_produto(produto: CriarProdutoDTO):
    use_case = CriarProduto(produto_repo_instance)
    resultado = use_case.execute(**produto.dict())
    return resultado


@router.put("/{id}", summary="Editar produto", response_model=ProdutoDTO)
def editar_produto(id: str, produto: EditarProdutoDTO):
    use_case = EditarProduto(produto_repo_instance)
    resultado = use_case.execute(id=id, **produto.dict())
    return resultado


@router.delete("/{id}", summary="Remover produto")
def remover_produto(id: str):
    use_case = RemoverProduto(produto_repo_instance)
    use_case.execute(id)
    return {"message": f"Produto {id} removido com sucesso."}


@router.get("/categoria/{categoria}", summary="Buscar produtos por categoria", response_model=list[ProdutoDTO])
def buscar_por_categoria(categoria: str):
    use_case = BuscarProdutosPorCategoria(produto_repo_instance)
    produtos = use_case.execute(categoria)
    return produtos
