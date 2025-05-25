from pydantic import BaseModel
from typing import Optional

class CriarProdutoDTO(BaseModel):
    nome: str
    descricao: str
    preco: float
    categoria: str
    imagem_url: Optional[str] = None

class EditarProdutoDTO(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    categoria: Optional[str] = None
    imagem_url: Optional[str] = None

class ProdutoDTO(BaseModel):
    id: str
    nome: str
    descricao: str
    preco: float
    categoria: str
    imagem_url: Optional[str] = None
