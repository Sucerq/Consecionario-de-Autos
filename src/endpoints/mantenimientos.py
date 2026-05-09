"""Endpoints de la API para la gestión de Mantenimientos."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.mantenimiento import Mantenimiento
from src.schemas.mantenimiento_schema import MantenimientoCreate, MantenimientoUpdate, MantenimientoResponse

router = APIRouter(prefix="/mantenimientos", tags=["Mantenimientos"])

@router.get("/", response_model=list[MantenimientoResponse])
def listar_mantenimientos(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los mantenimientos registrados.

    Args:
        db (Session): Manejador de bloque SQLAlchemy.

    Returns:
        list[Mantenimiento]: Lista integral de cada ticket de mantenimiento subido antes a BD.
    """
    return db.query(Mantenimiento).all()

@router.get("/{mantenimiento_id}", response_model=MantenimientoResponse)
def obtener_mantenimiento(mantenimiento_id: UUID, db: Session = Depends(get_db)):
    """Obtiene los detalles de un mantenimiento por su ID.

    Args:
        mantenimiento_id (UUID): Primary Key designada para el mantenimiento mecánico.
        db (Session): Dependencia generada de SessionMaker.

    Returns:
        Mantenimiento: Documento consultado con su ID y sus claves foráneas nativas.

    Raises:
        HTTPException: Cede paso al router con flag 404 Not Found si falla la búsqueda.
    """
    mantenimiento = db.query(Mantenimiento).filter(Mantenimiento.id_Mantenimiento == mantenimiento_id).first()
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    return mantenimiento

@router.post("/", response_model=MantenimientoResponse, status_code=status.HTTP_201_CREATED)
def crear_mantenimiento(dato: MantenimientoCreate, db: Session = Depends(get_db)):
    """Registra un nuevo mantenimiento en el sistema.

    Args:
        dato (MantenimientoCreate): Request validado (Pydantic Schema) en la capa media API.
        db (Session): Componente intermedio hacia Base de datos.

    Returns:
        Mantenimiento: Objeto reconstruido luego del refresh de PostgreSQL con UUIDs.
    """
    nuevo_mantenimiento = Mantenimiento(
        Tipo_Servicio=dato.Tipo_Servicio,
        Costo=dato.Costo,
        id_usuario_crea=dato.id_usuario_crea,
        id_Auto=dato.id_Auto,
        id_Empleado=dato.id_Empleado
    )
    db.add(nuevo_mantenimiento)
    db.commit()
    db.refresh(nuevo_mantenimiento)
    return nuevo_mantenimiento

@router.put("/{mantenimiento_id}", response_model=MantenimientoResponse)
def actualizar_mantenimiento(mantenimiento_id: UUID, dato: MantenimientoUpdate, db: Session = Depends(get_db)):
    """Actualiza la información de un ticket de mantenimiento existete de modo parcial.

    Args:
        mantenimiento_id (UUID): Parámetro URL tipo string UUID para buscar el objecto en la ORM.
        dato (MantenimientoUpdate): Formato especial Pydantic donde todo componente opcional es nulo.
        db (Session): Manejador de bloque hacia la DB subyacente de la app web.

    Returns:
        Mantenimiento: Mantenimiento reformado luego del commit y posterior refresh hacia el request response list.
        
    Raises:
        HTTPException: HTTP 404 (Not Found) emitido antes de que el JSON resuelva fallos locales.
    """
    mantenimiento = db.query(Mantenimiento).filter(Mantenimiento.id_Mantenimiento == mantenimiento_id).first()
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(mantenimiento, key, value)
        
    db.commit()
    db.refresh(mantenimiento)
    return mantenimiento

@router.delete("/{mantenimiento_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mantenimiento(mantenimiento_id: UUID, db: Session = Depends(get_db)):
    """Elimina estructuralmente (no logical path) del sistema un registro.

    Args:
        mantenimiento_id (UUID): Key principal a enrutar y filtrar.
        db (Session): Constructor dependiente de SQLAlchemy.

    Returns:
        None: Retorna la nada absoluta luego de completada su ejecución al cliente. HTTP 204.
        
    Raises:
        HTTPException: Dispara respuesta 404 a nivel Swagger o endpoint regular si ese identificante es obsoleto o incorrecto.
    """
    mantenimiento = db.query(Mantenimiento).filter(Mantenimiento.id_Mantenimiento == mantenimiento_id).first()
    if not mantenimiento:
        raise HTTPException(status_code=404, detail="Mantenimiento no encontrado")
    
    db.delete(mantenimiento)
    db.commit()
    return None
