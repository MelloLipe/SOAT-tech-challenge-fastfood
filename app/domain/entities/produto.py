import uuid

class Produto:
    def __init__(self, nome, descricao, preco, categoria, imagem_url=None):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
        self.imagem_url = imagem_url
