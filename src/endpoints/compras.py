"""Endpoints de la API para la gestión de Compras de autos usados."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.compra import Compra
from src.schemas.compra_schema import CompraCreate, CompraUpdate, CompraResponse

router = APIRouter(prefix="/compras", tags=["Compras"])

@router.get("/", response_model=list[CompraResponse])
def listar_compras(db: Session = Depends(get_db)):
    """Obtiene la lista de compras de vehículos de segunda.

    Args:
        db (Session): Sesión conectada a la BD primaria.

    Returns:
        list[Compra]: Lista de objetos Compra.
    """
    return db.query(Compra).all()

@router.get("/{compra_id}", response_model=CompraResponse)
def obtener_compra(compra_id: UUID, db: Session = Depends(get_db)):
    """Obtiene una compra por su ID.

    Args:
        compra_id (UUID): La llave UUID de la transacción.
        db (Session): Sesión de conexión activa a BD.

    Returns:
        Compra: Datos de la compra consultada.

    Raises:
        HTTPException: HTTP 404 si la compra no fue hallada.
    """
    compra = db.query(Compra).filter(Compra.id_Compra == compra_id).first()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return compra

@router.post("/", response_model=CompraResponse, status_code=status.HTTP_201_CREATED)
def crear_compra(dato: CompraCreate, db: Session = Depends(get_db)):
    """Registra una compra en el concesionario.

    Args:
        dato (CompraCreate): Payload con los datos mínimos de transaccionalidad.
        db (Session): Sesión hacia PostgreSQL u otra BD SQL.

    Returns:
        Compra: Objeto final de la compra guardada y generada.
    """
    nueva_compra = Compra(
        Precio=dato.Precio,
        id_usuario_crea=dato.id_usuario_crea,
        id_Empleado=dato.id_Empleado
    )
    db.add(nueva_compra)
    db.commit()
    db.refresh(nueva_compra)
    return nueva_compra

@router.put("/{compra_id}", response_model=CompraResponse)
def actualizar_compra(compra_id: UUID, dato: CompraUpdate, db: Session = Depends(get_db)):
    """Actualiza datos de la compra.

    Args:
        compra_id (UUID): ID original de la compra instanciada.
        dato (CompraUpdate): Patch con los campos que se van a re-escribir.
        db (Session): Sesión iniciada a la BD por FastAPI.

    Returns:
        Compra: Objeto compra recargado de forma parcial.

    Raises:
        HTTPException: HTTP 404 si el UUID no existe.
    """
    compra = db.query(Compra).filter(Compra.id_Compra == compra_id).first()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(compra, key, value)
        
    db.commit()
    db.refresh(compra)
    return compra

@router.delete("/{compra_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_compra(compra_id: UUID, db: Session = Depends(get_db)):
    """Elimina un registro de compra.

    Args:
        compra_id (UUID): PK o llave principal del recurso.
        db (Session): Dependencia generada automáticamente hacia la capa de datos.

    Returns:
        None: Retorna un código 204 HTTP vacío y sin payload.

    Raises:
        HTTPException: HTTP 404 en caso de no encontrarse.
    """
    compra = db.query(Compra).filter(Compra.id_Compra == compra_id).first()
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    
    db.delete(compra)
    db.commit()
    return None
