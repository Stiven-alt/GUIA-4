# 🚀 API REST de Gestión de Productos con Observabilidad en FastAPI

Este proyecto consiste en el desarrollo e implementación de una **API REST de alta disponibilidad y observabilidad** utilizando **FastAPI**, **Pydantic** y el módulo estándar de **`logging`** en Python. 

El proyecto fue diseñado bajo estándares de limpio código, validación de esquemas de datos, manejo formal de códigos de respuesta HTTP y una estrategia de diagnóstico y monitoreo de logs para entornos DevOps.

---

## 👥 Autores y Colaboración

Proyecto desarrollado en colaboración para la entrega académica:
* **Eduardo Stiven Prieto Espitia**
* **Coautora:** [Nombre de tu compañera]

---

## 🛠️ Tecnologías e Infraestructura

* **Lenguaje:** Python 3.10+
* **Framework Web:** FastAPI
* **Servidor ASGI:** Uvicorn
* **Validación de Datos:** Pydantic
* **Observabilidad:** Módulo estándar `logging` de Python
* **Entorno de Ejecución:** Local / GitHub Codespaces

---

## 📋 Endpoints de la API

La API administra un CRUD en memoria para la gestión de productos con validaciones de tipo, restricciones numéricas y manejo de excepciones:

| Método | Ruta | Descripción | Código Éxito | Código Error |
| :--- | :--- | :--- | :--- | :--- |
| `GET` | `/productos` | Obtiene la lista completa de productos | `200 OK` | N/A |
| `GET` | `/productos/{id}` | Busca un producto específico por su ID | `200 OK` | `404 Not Found` |
| `POST` | `/productos` | Registra un nuevo producto (valida ID único) | `201 Created` | `400 Bad Request` |
| `DELETE` | `/productos/{id}` | Elimina un producto por su ID | `200 OK` | `404 Not Found` |

---

## 📊 Matriz de Observabilidad y Logging

El sistema implementa el formateo estandarizado de registros `%(asctime)s [%(levelname)s] %(message)s`:

* **`INFO`**: Utilizado para auditoría de operaciones exitosas (consultas `GET` y creaciones `POST`).
* **`ERROR`**: Utilizado para la captura de fallas de negocio y cliente (intentos de duplicación `400` y búsquedas inexistentes `404`).

---

## ⚙️ Instalación y Ejecución

### 1. Clonar el repositorio
```bash
git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
cd TU_REPOSITORIO
