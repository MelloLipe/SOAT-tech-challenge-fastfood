from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.infrastructure.controllers.pedido_controller import router as pedido_router
from app.infrastructure.controllers.produto_controller import router as produto_router
from app.infrastructure.controllers.cliente_controller import router as cliente_router

app = FastAPI(
    title="FastFood API",
    version="1.0.0",
    description="API do sistema de autoatendimento para lanchonete - SOAT Tech Challenge"
)

# ✅ Permitir requisições do frontend (via browser/Live Server)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:5500"] se quiser restringir
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Rotas da aplicação
app.include_router(pedido_router, prefix="/pedidos", tags=["Pedidos"])
app.include_router(produto_router, prefix="/produtos", tags=["Produtos"])
app.include_router(cliente_router, prefix="/clientes", tags=["Clientes"])
