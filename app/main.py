from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.controllers.pedido_controller import router as pedido_router
from app.infrastructure.controllers.produto_controller import router as produto_router
from app.infrastructure.controllers.cliente_controller import router as cliente_router

app = FastAPI(
    title="FastFood API",
    version="1.0.0",
    description="API para autoatendimento de lanchonete"
)

# Middleware CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de rotas
app.include_router(cliente_router, prefix="/clientes", tags=["Clientes"])
app.include_router(produto_router, prefix="/produtos", tags=["Produtos"])
app.include_router(pedido_router, prefix="/pedidos", tags=["Pedidos"])
