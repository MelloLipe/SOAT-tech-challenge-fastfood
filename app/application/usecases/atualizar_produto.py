from app.domain.repositories.produto_repository import ProdutoRepository
from app.application.dtos.produto_dto import EditarProdutoDTO

class AtualizarProduto:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, id: str, dados: EditarProdutoDTO):
        produto = self.repo.buscar_por_id(id)
        if not produto:
            raise Exception("Produto não encontrado.")

        # ⚠️ Esta linha abaixo é a chave:
        for campo, valor in dados.dict(exclude_unset=True).items():
            setattr(produto, campo, valor)

        self.repo.salvar(produto)
        return produto
