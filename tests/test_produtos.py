import pytest
from app.domain.entities.produto import Produto
from app.domain.repositories.produto_repository import ProdutoRepository

class TestProdutoRepository(ProdutoRepository):
    def __init__(self):
        self.storage = {}

    def salvar(self, produto: Produto):
        self.storage[produto.id] = produto

    def remover(self, id: str):
        del self.storage[id]

    def buscar_por_categoria(self, categoria: str):
        return [p for p in self.storage.values() if p.categoria == categoria]

    def buscar_por_id(self, id: str):
        return self.storage.get(id)

@pytest.fixture
def repo():
    return TestProdutoRepository()

def test_criar_produto_valido(repo):
    produto = Produto(nome="Pizza", descricao="Mussarela", preco=30.0, categoria="Lanche")
    repo.salvar(produto)
    assert produto.id in repo.storage
    assert repo.storage[produto.id].nome == "Pizza"

def test_nao_permitir_preco_negativo():
    with pytest.raises(ValueError):
        Produto(nome="X", descricao="Y", preco=-10, categoria="Bebida")

def test_editar_produto_parcial(repo):
    produto = Produto(nome="Água", descricao="500ml", preco=5, categoria="Bebida")
    repo.salvar(produto)
    produto.nome = "Água Mineral"
    repo.salvar(produto)
    assert repo.storage[produto.id].nome == "Água Mineral"

def test_remover_produto(repo):
    produto = Produto(nome="Refri", descricao="Lata", preco=7, categoria="Bebida")
    repo.salvar(produto)
    repo.remover(produto.id)
    assert produto.id not in repo.storage

def test_buscar_por_categoria(repo):
    p1 = Produto(nome="Refri", descricao="Lata", preco=7, categoria="Bebida")
    p2 = Produto(nome="Coxinha", descricao="Frango", preco=6, categoria="Acompanhamento")
    repo.salvar(p1)
    repo.salvar(p2)
    resultado = repo.buscar_por_categoria("Bebida")
    assert len(resultado) == 1
    assert resultado[0].nome == "Refri"
