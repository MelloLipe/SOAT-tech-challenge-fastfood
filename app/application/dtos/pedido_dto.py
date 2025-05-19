from __future__ import annotations

from pydantic import BaseModel
from typing import List


class ProdutoAdicionadoDTO(BaseModel):
    pedido_id: str
    produto_id: str
    nome: str
    preco: float
    categoria: str
    quantidade: int


class PedidoCriadoDTO(BaseModel):
    id: str
    status: str
    total: float
    cliente_id: str | None


class PedidoItemDTO(BaseModel):
    produto_id: str
    nome: str
    categoria: str
    preco_unitario: float
    quantidade: int


class PedidoDetalhadoDTO(BaseModel):
    id: str
    status: str
    total: float
    cliente_id: str | None
    itens: List[PedidoItemDTO]
