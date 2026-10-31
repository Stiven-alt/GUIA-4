# tests/test_productos.py
from fastapi.testclient import TestClient
from main import app, db_productos

client = TestClient(app)

def setup_function():
    db_productos.clear()

def test_crear_y_obtener_producto():
    body = {"id": 1, "nombre": "Laptop", "precio": 1200.5, "stock": 3}
    assert client.post("/productos", json=body).status_code == 201
    assert client.get("/productos/1").json()["nombre"] == "Laptop"

def test_id_duplicado_retorna_400():
    body = {"id": 1, "nombre": "A", "precio": 10, "stock": 1}
    client.post("/productos", json=body)
    assert client.post("/productos", json=body).status_code == 400

def test_producto_inexistente_retorna_404():
    assert client.get("/productos/99").status_code == 404

def test_eliminar_producto():
    client.post("/productos", json={"id": 1, "nombre": "A", "precio": 10, "stock": 1})
    assert client.delete("/productos/1").status_code == 200

