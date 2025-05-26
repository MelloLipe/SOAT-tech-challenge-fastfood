from app.domain.repositories.pedido_repository import PedidoRepository
from app.domain.entities.pedido import Pedido
from app.domain.repositories.cliente_repository import ClienteRepository
from app.domain.entities.cliente import Cliente
from app.domain.repositories.produto_repository import ProdutoRepository
from app.domain.entities.produto import Produto


# --------------------- PEDIDOS ---------------------
class InMemoryPedidoRepository(PedidoRepository):
    def __init__(self):
        self.storage = {}

    def salvar(self, pedido: Pedido):
        self.storage[pedido.id] = pedido

    def buscar_por_id(self, pedido_id: str) -> Pedido:
        return self.storage.get(pedido_id)

    def listar_todos(self) -> list[Pedido]:
        return list(self.storage.values())


# --------------------- CLIENTES ---------------------
class InMemoryClienteRepository(ClienteRepository):
    def __init__(self):
        self.storage = {}

    def salvar(self, cliente: Cliente):
        self.storage[cliente.cpf] = cliente

    def buscar_por_cpf(self, cpf: str) -> Cliente:
        return self.storage.get(cpf)


# --------------------- PRODUTOS ---------------------
class InMemoryProdutoRepository(ProdutoRepository):
    def __init__(self):
        self.storage = {}

    def salvar(self, produto: Produto):
        existente = self.storage.get(produto.id)
        if existente:
            for attr, value in produto.__dict__.items():
                if value is not None:
                    setattr(existente, attr, value)
        else:
            self.storage[produto.id] = produto

    def remover(self, id: str):
        if id in self.storage:
            del self.storage[id]

    def buscar_por_categoria(self, categoria: str) -> list[Produto]:
        return [p for p in self.storage.values() if p.categoria == categoria]


# Instâncias únicas
pedido_repo_instance = InMemoryPedidoRepository()
cliente_repo_instance = InMemoryClienteRepository()
produto_repo_instance = InMemoryProdutoRepository()
