from fastapi import APIRouter
from schemas import Libro
from typing import Optional
from repository.ejemplo import libro_por_id, mostrar_diario_controlador, insertar_blog_controlador, insertar_libro_controlador

router = APIRouter(
    prefix="/ejemplo",
    tags=["Ejemplo Basico"]
)

@router.get("/libros/{id}")
def mostrar_libro(id: int):
    return libro_por_id(id)

# Tambien se pueden pasar por link query parameters
# El link seria algo asi: http://localhost:8000/diario?fecha=2021-10-10&published=true
# o http://localhost:8000/diario?fecha=2021-10-10&published=true&limit=10
@router.get("/diario")
def mostrar_diario(fecha: str, published: bool, limit: Optional[int] = None):
    return mostrar_diario_controlador(fecha, published, limit)
    
@router.post("/blogA")
def insertar_blog(title, body):
    return insertar_blog_controlador(title, body)
    
@router.post("/libros")
def insertar_libro(libro: Libro):
    return insertar_libro_controlador(libro)