"""Endpoints de la API para la gestión de Autos."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.autos import Auto
from src.schemas.auto_schema import AutoCreate, AutoUpdate, AutoResponse

router = APIRouter(prefix="/autos", tags=["Autos"])

@router.get("/", response_model=list[AutoResponse])
def listar_autos(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los autos registrados.

    Args:
        db (Session): Sesión de conexión a la base de datos de SQLAlchemy.

    Returns:
        list[Auto]: Una lista conteniendo todos los Autos de la base de datos.
    """
    return db.query(Auto).all()

@router.get("/{auto_id}", response_model=AutoResponse)
def obtener_auto(auto_id: UUID, db: Session = Depends(get_db)):
    """Obtiene los detalles de un auto específico por su ID.

    Args:
        auto_id (UUID): Identificador único del auto.
        db (Session): Sesión de conexión a la base de datos de SQLAlchemy.

    Returns:
        Auto: El objeto auto encontrado.

    Raises:
        HTTPException: 404 (Not Found) si el auto no existe.
    """
    auto = db.query(Auto).filter(Auto.id_Auto == auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    return auto

@router.post("/", response_model=AutoResponse, status_code=status.HTTP_201_CREATED)
def crear_auto(dato: AutoCreate, db: Session = Depends(get_db)):
    """Registra un nuevo auto en el sistema.

    Args:
        dato (AutoCreate): Modelo Pydantic con los datos de entrada requeridos.
        db (Session): Sesión de conexión a la base de datos de SQLAlchemy.

    Returns:
        Auto: El nuevo auto creado con su ID generado.
    """
    # Validación simple: Evitar duplicados exactos si se requiere (opcional)
    # Por ahora insertamos directamente
    nuevo_auto = Auto(
        Marca=dato.Marca,
        Modelo=dato.Modelo,
        Tipo_Auto=dato.Tipo_Auto,
        Precio=dato.Precio,
        Estado=dato.Estado,
        id_usuario_crea=dato.id_usuario_crea,
        id_Sucursal=dato.id_Sucursal,
        id_Compra=dato.id_Compra
    )
    db.add(nuevo_auto)
    db.commit()
    db.refresh(nuevo_auto)
    return nuevo_auto

@router.put("/{auto_id}", response_model=AutoResponse)
def actualizar_auto(auto_id: UUID, dato: AutoUpdate, db: Session = Depends(get_db)):
    """Actualiza la información de un auto existente.

    Args:
        auto_id (UUID): ID único del auto a modificar.
        dato (AutoUpdate): Campos opcionales a modificar (patch).
        db (Session): Sesión de conexión a la base de datos de SQLAlchemy.

    Returns:
        Auto: El registro del auto ya modificado y guardado.
        
    Raises:
        HTTPException: 404 (Not Found) si el auto no existe en base de datos.
    """
    auto = db.query(Auto).filter(Auto.id_Auto == auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(auto, key, value)
        
    db.commit()
    db.refresh(auto)
    return auto

@router.delete("/{auto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_auto(auto_id: UUID, db: Session = Depends(get_db)):
    """Elimina un auto del sistema de forma física.

    Args:
        auto_id (UUID): ID del auto que se desea borrar del catálogo.
        db (Session): Sesión de conexión a la base de datos de SQLAlchemy.

    Returns:
        None: Respuesta sin contenido (status 204) al ser eliminado exitosamente.
        
    Raises:
        HTTPException: 404 (Not Found) si el auto no se halló.
    """
    auto = db.query(Auto).filter(Auto.id_Auto == auto_id).first()
    if not auto:
        raise HTTPException(status_code=404, detail="Auto no encontrado")
    
    db.delete(auto)
    db.commit()
    return None
