import pytest
from app.domain.entities.pedido import Pedido, ItemPedido
from app.domain.entities.produto import Produto
from app.domain.repositories.pedido_repository import PedidoRepository

class TestPedidoRepository(PedidoRepository):
    def __init__(self):
        self.storage = {}

    def salvar(self, pedido: Pedido):
        self.storage[pedido.id] = pedido

    def buscar_por_id(self, pedido_id: str):
        return self.storage.get(pedido_id)

    def listar_todos(self):
        return list(self.storage.values())

@pytest.fixture
def repo():
    return TestPedidoRepository()

def test_criar_pedido(repo):
    pedido = Pedido(cliente_id="12345678900")
    repo.salvar(pedido)
    assert pedido.id in repo.storage
    assert pedido.cliente_id == "12345678900"
    assert pedido.status == "CRIADO"

def test_adicionar_item_pedido():
    produto = Produto(nome="Suco", descricao="Laranja", preco=6.0, categoria="Bebida")
    pedido = Pedido()
    pedido.adicionar_item(
        produto_id=produto.id,
        nome=produto.nome,
        preco=produto.preco,
        categoria=produto.categoria,
        quantidade=2
    )
    assert len(pedido.itens) == 1
    assert pedido.total == 12.0
    assert pedido.itens[0].nome == "Suco"


def test_finalizar_pedido():
    pedido = Pedido()
    assert pedido.status == "CRIADO"
    pedido.finalizar()
    assert pedido.status == "FINALIZADO"

def test_listar_todos_pedidos(repo):
    p1 = Pedido()
    p2 = Pedido(cliente_id="99999999999")
    repo.salvar(p1)
    repo.salvar(p2)
    todos = repo.listar_todos()
    assert len(todos) == 2
