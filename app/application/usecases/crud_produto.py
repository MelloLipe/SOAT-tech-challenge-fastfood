# app/application/usecases/crud_produto.py
from app.domain.entities.produto import Produto
from app.domain.repositories.produto_repository import ProdutoRepository


class CriarProduto:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, nome, descricao, preco, categoria, imagem_url):
        produto = Produto(nome, descricao, preco, categoria, imagem_url)
        self.repo.salvar(produto)
        return produto

class EditarProduto:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, id, nome, descricao, preco, categoria, imagem_url):
        produto = Produto(nome, descricao, preco, categoria, imagem_url, id=id)
        self.repo.salvar(produto)
        return produto

class RemoverProduto:
    def __init__(self, repo: ProdutoRepository):
        self.repo = repo

    def execute(self, id):
        self.repo.remover(id)
