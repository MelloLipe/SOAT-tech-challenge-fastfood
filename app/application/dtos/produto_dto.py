from pydantic import BaseModel


class CriarProdutoDTO(BaseModel):
    nome: str
    descricao: str
    preco: float
    categoria: str
    imagem_url: str


class EditarProdutoDTO(BaseModel):
    nome: str
    descricao: str
    preco: float
    categoria: str
    imagem_url: str


class ProdutoDTO(BaseModel):
    id: str
    nome: str
    descricao: str
    preco: float
    categoria: str
    imagem_url: str
