
class ProdutoRepository:
    def __init__(self):
        self.produtos = {}

    def salvar(self, produto):
        self.produtos[produto.id] = produto

    def buscar_por_id(self, id):
        return self.produtos.get(id)

    def remover(self, id):
        if id in self.produtos:
            del self.produtos[id]

    def buscar_por_categoria(self, categoria):
        return [p for p in self.produtos.values() if p.categoria == categoria]

produto_repo_instance = ProdutoRepository()
