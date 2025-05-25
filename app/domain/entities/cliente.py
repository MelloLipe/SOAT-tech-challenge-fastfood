import uuid

class Cliente:
    def __init__(self, nome, email, cpf):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.email = email
        self.cpf = cpf
