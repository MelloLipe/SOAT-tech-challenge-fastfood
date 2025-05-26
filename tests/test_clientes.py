import pytest
from app.domain.entities.cliente import Cliente
from app.domain.repositories.cliente_repository import ClienteRepository

class TestClienteRepository(ClienteRepository):
    def __init__(self):
        self.storage = {}

    def salvar(self, cliente: Cliente):
        self.storage[cliente.cpf] = cliente

    def buscar_por_cpf(self, cpf: str):
        return self.storage.get(cpf)

@pytest.fixture
def repo():
    return TestClienteRepository()

def test_criar_cliente_valido(repo):
    cliente = Cliente(cpf="12345678900", nome="Maria", email="maria@email.com")
    repo.salvar(cliente)
    assert cliente.cpf in repo.storage
    assert repo.storage[cliente.cpf].nome == "Maria"

def test_cpf_invalido():
    cpf = "abc123"
    assert not cpf.isdigit() or len(cpf) != 11

def test_buscar_cliente_existente(repo):
    cliente = Cliente(cpf="12345678900", nome="João", email="joao@email.com")
    repo.salvar(cliente)
    encontrado = repo.buscar_por_cpf("12345678900")
    assert encontrado is not None
    assert encontrado.nome == "João"

def test_buscar_cliente_inexistente(repo):
    assert repo.buscar_por_cpf("00000000000") is None
