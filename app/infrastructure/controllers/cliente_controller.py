from fastapi import APIRouter, HTTPException
from app.infrastructure.persistence.db import cliente_repo_instance
from app.application.usecases.cadastrar_cliente import CadastrarCliente
from app.application.usecases.identificar_cliente import IdentificarCliente
from app.application.dtos.cliente_dto import ClienteCadastroDTO, ClienteDTO

router = APIRouter()


@router.post("/", summary="Cadastrar cliente", response_model=ClienteDTO)
def cadastrar_cliente(dados: ClienteCadastroDTO):
    use_case = CadastrarCliente(cliente_repo_instance)
    cliente = use_case.execute(**dados.dict())
    return cliente


@router.get("/{cpf}", summary="Buscar cliente por CPF", response_model=ClienteDTO)
def identificar_cliente(cpf: str):
    use_case = IdentificarCliente(cliente_repo_instance)
    cliente = use_case.execute(cpf)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente
