import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Configuración de Logs (para guardar fecha, hora y mensaje)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)

app = FastAPI(title="API Productos")

# 2. Estructura de un Producto
class Producto(BaseModel):
  id: int
  nombre: str
  precio: float
  stock: int