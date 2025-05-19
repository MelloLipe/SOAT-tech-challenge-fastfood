import uuid


class Produto:
    def __init__(self, nome: str, descricao: str, preco: float, categoria: str, imagem_url: str, id: str = None):
        self.id = id or str(uuid.uuid4())
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria  # Ex: 'LANCHE', 'BEBIDA'
        self.imagem_url = imagem_url
