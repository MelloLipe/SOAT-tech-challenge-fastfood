
# FastFood Backend - SOAT Tech Challenge Fase 1

Este projeto implementa o sistema de autoatendimento para uma lanchonete em expansão, conforme os requisitos do desafio proposto na Fase 1 do Tech Challenge da SOAT.

---

## 📦 Tecnologias Utilizadas

- Python 3.11
- FastAPI
- Docker e Docker Compose
- PostgreSQL (pronto para migração futura)
- Swagger (OpenAPI) para documentação de APIs

---

## 🧱 Estrutura do Projeto

```
app/
├── main.py                  # Ponto de entrada FastAPI
├── domain/                 # Entidades e repositórios
├── application/            # Casos de uso
├── infrastructure/         # Controllers, persistência fake/mock
├── config.py               # Configurações gerais
Dockerfile
docker-compose.yml
requirements.txt
swagger.yaml
```

---

## 🚀 Como Executar Localmente

### Pré-requisitos

- Docker
- Docker Compose

### Passos

```bash
# 1. Clone o repositório
git clone <url-do-repo>
cd <nome-do-repo>

# 2. Suba o ambiente
docker-compose up --build

# 3. Acesse a API
http://localhost:3000/docs
```

---

## 🔌 Principais Endpoints

- `POST /clientes` - Cadastro de cliente
- `GET /clientes/{cpf}` - Identificação de cliente via CPF
- `POST /produtos` - Criar produto
- `GET /produtos/categoria/{categoria}` - Buscar por categoria
- `POST /pedidos` - Criar pedido
- `POST /pedidos/adicionar-produto` - Adicionar produto ao pedido
- `POST /pedidos/{pedido_id}/checkout` - Finalizar pedido
- `POST /pedidos/{pedido_id}/confirmar-pagamento` - Confirmar pagamento
- `PATCH /pedidos/{pedido_id}/status` - Atualizar status do pedido
- `GET /pedidos/ativos` - Listar pedidos em andamento

Para mais detalhes, consulte o arquivo [`swagger.yaml`](./swagger.yaml).

---

## 🧪 Testes e Validação

- Utilize o Swagger em `http://localhost:3000/docs`
- Ou importe `swagger.yaml` no Swagger Editor ou Postman

---

## 📄 Entrega

- Código-fonte hospedado em repositório privado
- Adicionar `soat-architecture` como colaborador
- Incluir link do vídeo demonstrando o sistema via Docker
- Submeter documentação e diagrama no Portal do Aluno

---

## 👥 Participantes

- Felipe Mello Lima - Discord: @melloFelipe

