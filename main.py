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

# 3. Base de datos simulada (Lista en memoria)
db_productos = []
# --- ENDPOINTS ---

# Obtener todos los productos
@app.get("/productos")
def obtener_productos():
  logging.info("GET /productos - Consulta general realizada")
  return db_productos

# Obtener un producto por su ID
@app.get("/productos/{id}")
def obtener_producto(id: int):
  for p in db_productos:
    if p.id == id:
      logging.info(f"GET /productos/{id} - Producto encontrado")
      return p

  # Si no lo encuentra tras revisar la lista:
  logging.error(f"GET /productos/{id} - ERROR: Producto no encontrado")
  raise HTTPException(status_code=404, detail="Producto no encontrado")

# Crear un producto
@app.post("/productos")
def crear_producto(producto: Producto):
  for p in db_productos:
    if p.id == producto.id:
      logging.error(f"POST /productos - ERROR: El ID {producto.id} ya existe")
      raise HTTPException(status_code=400, detail="El ID ya existe")

  db_productos.append(producto)
  logging.info(f"POST /productos - Creado exitosamente: {producto.nombre}")
  return producto

# Eliminar un producto
@app.delete("/productos/{id}")
def eliminar_producto(id: int):
  for p in db_productos:
    if p.id == id:
      db_productos.remove(p)
      logging.info(f"DELETE /productos/{id} - Producto eliminado")
      return {"mensaje": "Producto eliminado exitosamente"}

  logging.error(
      f"DELETE /productos/{id} - ERROR: Producto no encontrado para eliminar"
  )
  raise HTTPException(status_code=404, detail="Producto no encontrado")
