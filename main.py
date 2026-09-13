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

# --- ENDPOINTS ---

@app.get(
    "/productos",
    response_model=List[Producto],
    summary="Obtener todos los productos",
    description="Retorna una lista con todos los productos registrados en la base de datos en memoria."
)
def obtener_productos():
    """Retorna la lista completa de productos disponibles."""
    logging.info("GET /productos - Consulta general realizada")
    return db_productos


@app.get(
    "/productos/{id}",
    response_model=Producto,
    summary="Obtener un producto por ID",
    description="Busca y retorna un producto específico según su ID numérico."
)
def obtener_producto(id: int):
    """Busca un producto por su identificador único."""
    for p in db_productos:
        if p.id == id:
            logging.info(f"GET /productos/{id} - Producto encontrado")
            return p

    logging.error(f"GET /productos/{id} - ERROR: Producto no encontrado")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Producto no encontrado"
    )


@app.post(
    "/productos",
    response_model=Producto,
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto",
    description="Agrega un nuevo producto a la base de datos validando que el ID no esté duplicado."
)
def crear_producto(producto: Producto):
    """Registra un nuevo producto en el sistema."""
    for p in db_productos:
        if p.id == producto.id:
            logging.error(f"POST /productos - ERROR: El ID {producto.id} ya existe")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, 
                detail="El ID ya existe"
            )

    db_productos.append(producto)
    logging.info(f"POST /productos - Creado exitosamente: {producto.nombre}")
    return producto


@app.delete(
    "/productos/{id}",
    summary="Eliminar un producto",
    description="Elimina un producto existente de la base de datos según su ID."
)
def eliminar_producto(id: int):
    """Elimina un producto existente del sistema."""
    for p in db_productos:
        if p.id == id:
            db_productos.remove(p)
            logging.info(f"DELETE /productos/{id} - Producto eliminado")
            return {"mensaje": "Producto eliminado exitosamente"}

    logging.error(f"DELETE /productos/{id} - ERROR: Producto no encontrado para eliminar")
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail="Producto no encontrado"
    )
