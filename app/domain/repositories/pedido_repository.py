# app/domain/repositories/pedido_repository.py
from abc import ABC, abstractmethod
from app.domain.entities.pedido import Pedido


class PedidoRepository(ABC):
    @abstractmethod
    def salvar(self, pedido: Pedido):
        pass

    @abstractmethod
    def buscar_por_id(self, pedido_id: str) -> Pedido:
        pass

    @abstractmethod
    def listar_todos(self) -> list[Pedido]:
        pass
