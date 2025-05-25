from __future__ import annotations
from pydantic import BaseModel
from typing import Optional

class ProdutoAdicionadoDTO(BaseModel):
    pedido_id: str
    produto_id: str
    nome: str
    preco: float
    categoria: str
    quantidade: int

class CriarPedidoDTO(BaseModel):
    cliente_id: Optional[str] = None

class PedidoItemDTO(BaseModel):
    produto_id: str
    nome: str
    categoria: str
    preco: float
    quantidade: int
