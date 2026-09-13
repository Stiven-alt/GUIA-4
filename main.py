import logging
from typing import List
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Configuración de Logs
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = FastAPI(
    title="API de Productos",
    description="Una API sencilla para la gestión de productos en memoria.",
    version="1.0.0",
)


# 2. Estructura de un Producto con validaciones y documentación de campos
class Producto(BaseModel):
    id: int = Field(..., example=1, description="Identificador único del producto")
    nombre: str = Field(..., example="Laptop Gamer", description="Nombre comercial del producto")
    precio: float = Field(..., gt=0, example=1200.50, description="Precio unitario (mayor a 0)")
    stock: int = Field(..., ge=0, example=15, description="Cantidad disponible en inventario")


# Base de datos simulada
db_productos: List[Producto] = []
