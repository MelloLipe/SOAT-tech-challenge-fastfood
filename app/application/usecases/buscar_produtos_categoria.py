# app/application/usecases/buscar_produtos_categoria.py
from app.domain.repositories.produto_repository import ProdutoRepository


class BuscarProdutosPorCategoria:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, categoria: str):
        return self.repo.buscar_por_categoria(categoria)
