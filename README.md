
# FastFood API - SOAT Tech Challenge

Este projeto é uma API para um sistema de autoatendimento de lanchonete, desenvolvida com FastAPI, utilizando arquitetura hexagonal e DDD.

## ✅ Funcionalidades Atendidas

- Cadastro de clientes (`POST /clientes`)
- Identificação de clientes por CPF (`GET /clientes/{cpf}`)
- Criar, editar e remover produtos
    - `POST /produtos`
    - `PUT /produtos/{id}`
    - `DELETE /produtos/{id}`
- Buscar produtos por categoria (`GET /produtos/categoria/{categoria}`)
- **Fake checkout** (`POST /pedidos/{id}/checkout`)
    - O pedido é finalizado e enviado para a "fila" (memória)
    - Não há integração com pagamento real
- Listagem de pedidos (`GET /pedidos`)
- Interface HTML para testes (`test_interface_full.html`)

## 📦 Fake Checkout (Requisito V)

O endpoint abaixo simula a finalização do pedido, **enviando os produtos escolhidos para a fila**, conforme o requisito da Fase 1:

```
POST /pedidos/{pedido_id}/checkout
```

Este endpoint:
- Marca o pedido como `FINALIZADO`
- Não exige pagamento
- Simula o envio do pedido para a preparação

## 💡 Extras Implementados

- Controle de status (RECEBIDO, EM_PREPARACAO, PRONTO)
- Simulação de pagamento (QR Code fictício)
- Diagrama de arquitetura e fluxo de eventos
- Interface HTML visual para teste de todos os endpoints
- Eventos de domínio (DDD)

## ▶️ Como rodar localmente

1. Suba com Docker:

```
docker-compose up --build
```

2. Acesse a documentação:

```
http://localhost:3000/docs
```

3. Abra o painel de testes:

Abra o arquivo `test_interface_full.html` com Live Server ou navegador.

## 📁 Estrutura do Projeto

- `app/` - código principal da aplicação
- `README.md` - este arquivo
- `swagger.yaml` - documentação OpenAPI
- `index.html`, `test_interface_full.html` - interfaces HTML de testes
