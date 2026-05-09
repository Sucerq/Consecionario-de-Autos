"""Endpoints de la API para la gestión de Empleados."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.empleado import Empleado
from src.schemas.empleado_schema import EmpleadoCreate, EmpleadoUpdate, EmpleadoResponse

router = APIRouter(prefix="/empleados", tags=["Empleados"])

@router.get("/", response_model=list[EmpleadoResponse])
def listar_empleados(db: Session = Depends(get_db)):
    """Obtiene la lista de empleados.

    Args:
        db (Session): Sesión abierta a la BD SQL.

    Returns:
        list[Empleado]: Arreglo completo con los empleados persitidos.
    """
    return db.query(Empleado).all()

@router.get("/{empleado_id}", response_model=EmpleadoResponse)
def obtener_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    """Obtiene un empleado por su ID.

    Args:
        empleado_id (UUID): La llave principal del registro del Empleado.
        db (Session): Sesión de conexión iniciada en la base de datos.

    Returns:
        Empleado: Objeto Empleado devuelto por la entidad SQLAlchemy asociada.

    Raises:
        HTTPException: Se lanza con código HTTP 404 si el ID no es real.
    """
    empleado = db.query(Empleado).filter(Empleado.id_Empleado == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

@router.post("/", response_model=EmpleadoResponse, status_code=status.HTTP_201_CREATED)
def crear_empleado(dato: EmpleadoCreate, db: Session = Depends(get_db)):
    """Registra y enlista un empleado nuevo al concesionario.

    Args:
        dato (EmpleadoCreate): El body JSON parseado para la validación.
        db (Session): Interacción genérica con la BD mediante el ORM.

    Returns:
        Empleado: Registro recién subido y retornado fresco (201 Created).
    """
    nuevo_empleado = Empleado(
        Nombre=dato.Nombre,
        Cargo=dato.Cargo,
        Telefono=dato.Telefono,
        Salario=dato.Salario
    )
    db.add(nuevo_empleado)
    db.commit()
    db.refresh(nuevo_empleado)
    return nuevo_empleado

@router.put("/{empleado_id}", response_model=EmpleadoResponse)
def actualizar_empleado(empleado_id: UUID, dato: EmpleadoUpdate, db: Session = Depends(get_db)):
    """Actualiza parcialmente los datos y estructura logica del empleado.

    Args:
        empleado_id (UUID): La UUID inmutable del usuario de nómina a sobre-escribir.
        dato (EmpleadoUpdate): Datos a parchear que pasaron la validación de Pydantic.
        db (Session): Context Manager de inserciones SQL.

    Returns:
        Empleado: El empleado mutado hacia su forma final en BD.

    Raises:
        HTTPException: De no ubicarse el ID saldrá una excepción y error nativo 404 HTTP.
    """
    empleado = db.query(Empleado).filter(Empleado.id_Empleado == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(empleado, key, value)
        
    db.commit()
    db.refresh(empleado)
    return empleado

@router.delete("/{empleado_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_empleado(empleado_id: UUID, db: Session = Depends(get_db)):
    """Ejecuta un hard-delete del registro de la base.

    Args:
        empleado_id (UUID): Referencia unívoca del registro de Postgresql/SQLAlchemy.
        db (Session): Componente intermedio de persistencia de FastAPI.

    Returns:
        None: Retorna explícitamente contenido cero en base a standard 204.

    Raises:
        HTTPException: Provoca un catch del framework de no hallar tal empleado (404).
    """
    empleado = db.query(Empleado).filter(Empleado.id_Empleado == empleado_id).first()
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    
    db.delete(empleado)
    db.commit()
    return None
