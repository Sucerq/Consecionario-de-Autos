"""Endpoints de la API para la gestión del Detalle de las Ventas."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.detalle_venta import Detalle_Venta
from src.schemas.detalle_venta_schema import DetalleVentaCreate, DetalleVentaUpdate, DetalleVentaResponse

router = APIRouter(prefix="/detalle-ventas", tags=["Detalles de Venta"])

@router.get("/", response_model=list[DetalleVentaResponse])
def listar_detalles(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los detalles de venta registrados.

    Args:
        db (Session): Sesión de conexión a base de datos instanciada.

    Returns:
        list[Detalle_Venta]: Un arreglo nativo de FastAPI con todos los detalles persistidos.
    """
    return db.query(Detalle_Venta).all()

@router.post("/", response_model=DetalleVentaResponse, status_code=status.HTTP_201_CREATED)
def crear_detalle(dato: DetalleVentaCreate, db: Session = Depends(get_db)):
    """Registra y asocia un nuevo detalle a una Venta y un Auto.

    Args:
        dato (DetalleVentaCreate): Las llaves foráneas a enlazar para el Detalle de Venta.
        db (Session): Dependencia abierta en el pipeline para SQL.

    Returns:
        Detalle_Venta: El registro puente nuevo con su Id.
    """
    nuevo_detalle = Detalle_Venta(
        id_usuario_crea=dato.id_usuario_crea,
        id_Venta=dato.id_Venta,
        id_Auto=dato.id_Auto
    )
    db.add(nuevo_detalle)
    db.commit()
    db.refresh(nuevo_detalle)
    return nuevo_detalle

@router.delete("/{detalle_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_detalle(detalle_id: UUID, db: Session = Depends(get_db)):
    """Elimina físicamente un detalle de venta de la base de datos.

    Args:
        detalle_id (UUID): Llave referencial principal del registro a demoler.
        db (Session): Sesión instanciada al ORM interno genérico.

    Returns:
        None: Null debido al standard 204.

    Raises:
        HTTPException: HTTP 404 de no validarse un ID en PostgreSQL.
    """
    detalle = db.query(Detalle_Venta).filter(Detalle_Venta.id_Detalle_Venta == detalle_id).first()
    if not detalle:
        raise HTTPException(status_code=404, detail="Detalle no encontrado")
    
    db.delete(detalle)
    db.commit()
    return None
