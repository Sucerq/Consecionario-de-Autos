"""Endpoints de la API para la gestión de Ventas."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.venta import Venta
from src.schemas.venta_schema import VentaCreate, VentaUpdate, VentaResponse

router = APIRouter(prefix="/ventas", tags=["Ventas"])

@router.get("/", response_model=list[VentaResponse])
def listar_ventas(db: Session = Depends(get_db)):
    """Obtiene la lista de ventas.

    Args:
        db (Session): Dependencia generada de forma automática por FastAPI.

    Returns:
        list[Venta]: Un set array completo con las ventas realizadas.
    """
    return db.query(Venta).all()

@router.get("/{venta_id}", response_model=VentaResponse)
def obtener_venta(venta_id: UUID, db: Session = Depends(get_db)):
    """Obtiene una venta por su ID.

    Args:
        venta_id (UUID): Llave primaria asociada universalmente al registro de venta.
        db (Session): Conexión delegada de base de datos SQL.

    Returns:
        Venta: Recurso individual expuesto.

    Raises:
        HTTPException: Se detiene el proxy con error 404 de no estar alojado.
    """
    venta = db.query(Venta).filter(Venta.id_Venta == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    return venta

@router.post("/", response_model=VentaResponse, status_code=status.HTTP_201_CREATED)
def crear_venta(dato: VentaCreate, db: Session = Depends(get_db)):
    """Registra una venta.

    Args:
        dato (VentaCreate): Input Pydantic con múltiples dependencias (Cliente, Empleado, Usuario).
        db (Session): Módulo session activo por yield en FastAPI de contextlib.

    Returns:
        Venta: Entidad regenerada y construida con su id_Venta propia.
    """
    nueva_venta = Venta(
        Precio_Venta=dato.Precio_Venta,
        Metodo_Pago=dato.Metodo_Pago,
        Fecha=dato.Fecha,
        id_usuario_crea=dato.id_usuario_crea,
        id_Cliente=dato.id_Cliente,
        id_Empleado=dato.id_Empleado
    )
    db.add(nueva_venta)
    db.commit()
    db.refresh(nueva_venta)
    return nueva_venta

@router.put("/{venta_id}", response_model=VentaResponse)
def actualizar_venta(venta_id: UUID, dato: VentaUpdate, db: Session = Depends(get_db)):
    """Actualiza datos de la venta.

    Args:
        venta_id (UUID): Key del ID para filtrado condicional en subrutina de edición.
        dato (VentaUpdate): Objeto Schema con opciones dict-format y none-able.
        db (Session): Manejo unitario transaccional.

    Returns:
        Venta: El cuerpo entero de lo guardado.

    Raises:
        HTTPException: Redirección genérica 404 al faltar un input match.
    """
    venta = db.query(Venta).filter(Venta.id_Venta == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(venta, key, value)
        
    db.commit()
    db.refresh(venta)
    return venta

@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_venta(venta_id: UUID, db: Session = Depends(get_db)):
    """Elimina una venta.

    Args:
        venta_id (UUID): Referenciador explícito físico para extirpación `DELETE` nativo.
        db (Session): Concesionador de SQLAlchemy al engine PostgreSQL.

    Returns:
        None: Retorno explícito vacío dado status code nativo HTTP_204_NO_CONTENT.

    Raises:
        HTTPException: HTTP 404 Error, Not found de no encontrarse la key pedida.
    """
    venta = db.query(Venta).filter(Venta.id_Venta == venta_id).first()
    if not venta:
        raise HTTPException(status_code=404, detail="Venta no encontrada")
    
    db.delete(venta)
    db.commit()
    return None
