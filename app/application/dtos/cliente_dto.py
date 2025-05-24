from pydantic import BaseModel

class CriarClienteDTO(BaseModel):
    nome: str
    email: str
    cpf: str


class ClienteDTO(BaseModel):
    id: str
    nome: str
    email: str
    cpf: str
