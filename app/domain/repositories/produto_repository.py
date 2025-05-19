from abc import ABC, abstractmethod
from app.domain.entities.produto import Produto


class ProdutoRepository(ABC):
    @abstractmethod
    def salvar(self, produto: Produto):
        pass

    @abstractmethod
    def remover(self, id: str):
        pass

    @abstractmethod
    def buscar_por_categoria(self, categoria: str) -> list[Produto]:
        pass
