from typing import Optional

def libro_por_id(id: int):
    return {"id": id}

def mostrar_diario_controlador(fecha: str, published: bool, limit: Optional[int] = None):
    if published:
        if limit is not None:
            return {"El diario es del día": fecha, "Publicado": "Si", "Limit": limit}
        else:
            return {"El diario es del día": fecha, "Publicado": "Si"}
    else:
        if limit is not None:
            return {"El diario es del día": fecha, "Publicado": "No", "Limit": limit}
        else:
            return {"El diario es del día": fecha, "Publicado": "No"}
        
def insertar_blog_controlador(title, body):
    return {"title": title, "body": body}

def insertar_libro_controlador(libro):
    return {"message": f"Libro {libro.titulo} insertado correctamente"}
    