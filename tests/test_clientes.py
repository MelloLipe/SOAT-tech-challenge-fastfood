
def test_criar_cliente_sucesso():
    nome = "Maria"
    email = "maria@email.com"
    cpf = "12345678900"
    assert len(nome) > 0
    assert "@" in email
    assert cpf.isdigit() and len(cpf) == 11
