# app/domain/repositories/cliente_repository.py
from abc import ABC, abstractmethod
from app.domain.entities.cliente import Cliente


class ClienteRepository(ABC):
    @abstractmethod
    def salvar(self, cliente: Cliente):
        pass

    @abstractmethod
    def buscar_por_cpf(self, cpf: str) -> Cliente:
        pass
