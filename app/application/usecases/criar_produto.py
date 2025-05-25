from app.domain.entities.produto import Produto
from app.domain.repositories.produto_repository import ProdutoRepository
from app.application.dtos.produto_dto import CriarProdutoDTO

class CriarProduto:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, dados: CriarProdutoDTO) -> Produto:
        produto = Produto(**dados.dict())
        self.repo.salvar(produto)
        return produto
