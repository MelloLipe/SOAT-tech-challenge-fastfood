import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env se existir


class Settings:
    APP_NAME: str = "FastFood API"
    VERSION: str = "1.0.0"

    # Banco de dados (para migração futura)
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://fastfood:fastfood@localhost:5432/pedidos")

    # Categorias fixas para produtos
    CATEGORIAS_PRODUTO = ["LANCHE", "ACOMPANHAMENTO", "BEBIDA", "SOBREMESA"]

    # Status permitidos no fluxo do pedido
    STATUS_PEDIDO = [
        "INICIADO",
        "FINALIZADO",
        "PAGO",
        "ENVIADO",
        "RECEBIDO",
        "EM_PREPARACAO",
        "PRONTO"
    ]

settings = Settings()
