from fastapi import APIRouter
from app.domain.repositories.cliente_repository import cliente_repo_instance
from app.application.usecases.criar_cliente import CriarCliente
from app.application.usecases.buscar_cliente_por_cpf import BuscarClientePorCPF
from app.application.dtos.cliente_dto import CriarClienteDTO

router = APIRouter()



@router.post("/")
def criar_cliente(cliente: CriarClienteDTO):
    use_case = CriarCliente(cliente_repo_instance)
    resultado = use_case.execute(cliente.nome, cliente.email, cliente.cpf)
    return vars(resultado)

@router.get("/{cpf}")
def buscar_cliente(cpf: str):
    use_case = BuscarClientePorCPF(cliente_repo_instance)
    resultado = use_case.execute(cpf)
    return vars(resultado) if resultado else {"erro": "Cliente não encontrado"}
