# app/domain/entities/cliente.py
import uuid


class Cliente:
    def __init__(self, nome: str, email: str, cpf: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.cpf = cpf
