# app/main.py
from fastapi import FastAPI
from app.infrastructure.controllers.pedido_controller import router as pedido_router
from app.infrastructure.controllers.cliente_controller import router as cliente_router
from app.infrastructure.controllers.produto_controller import router as produto_router

app = FastAPI(title="FastFood API", version="1.0.0")

app.include_router(pedido_router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(cliente_router, prefix="/clientes", tags=["Clientes"])
app.include_router(produto_router, prefix="/produtos", tags=["Produtos"])
