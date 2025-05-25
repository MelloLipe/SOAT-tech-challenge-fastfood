from app.domain.repositories.produto_repository import ProdutoRepository

class RemoverProduto:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, id: str):
        self.repo.remover(id)
