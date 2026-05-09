"""Endpoints de la API para la gestión de Sucursales."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.sucursal import Sucursal
from src.schemas.sucursal_schema import SucursalCreate, SucursalUpdate, SucursalResponse

router = APIRouter(prefix="/sucursales", tags=["Sucursales"])

@router.get("/", response_model=list[SucursalResponse])
def listar_sucursales(db: Session = Depends(get_db)):
    """Obtiene la lista de todas las sucursales.

    Args:
        db (Session): Sesión activa generada por FastAPI.

    Returns:
        list[Sucursal]: Arreglo conteniendo las sucursales de la base.
    """
    return db.query(Sucursal).all()

@router.get("/{sucursal_id}", response_model=SucursalResponse)
def obtener_sucursal(sucursal_id: UUID, db: Session = Depends(get_db)):
    """Obtiene una sucursal específica por su ID.

    Args:
        sucursal_id (UUID): Llave primaria de la Sucursal en UUID format.
        db (Session): Componente para manipulación de SQLAlchemy.

    Returns:
        Sucursal: El dato singular encontrado en base de datos.
    
    Raises:
        HTTPException: HTTP 404 cuando no se encuentra dicho registro.
    """
    sucursal = db.query(Sucursal).filter(Sucursal.id_Sucursal == sucursal_id).first()
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    return sucursal

@router.post("/", response_model=SucursalResponse, status_code=status.HTTP_201_CREATED)
def crear_sucursal(dato: SucursalCreate, db: Session = Depends(get_db)):
    """Crea una nueva sucursal en el sistema.

    Args:
        dato (SucursalCreate): Request object dictado por esquema Pydantic.
        db (Session): Handler en el ciclo de DB principal.

    Returns:
        Sucursal: Estructura ya rehidratada con su primary key fresca.
    """
    nueva_sucursal = Sucursal(
        Nombre=dato.Nombre,
        Telefono=dato.Telefono,
        Direccion=dato.Direccion
    )
    db.add(nueva_sucursal)
    db.commit()
    db.refresh(nueva_sucursal)
    return nueva_sucursal

@router.put("/{sucursal_id}", response_model=SucursalResponse)
def actualizar_sucursal(sucursal_id: UUID, dato: SucursalUpdate, db: Session = Depends(get_db)):
    """Actualiza parcialmente los datos de una sucursal.

    Args:
        sucursal_id (UUID): String UUID representativo posicional en endpoint.
        dato (SucursalUpdate): Objeto Pydantic especial para modo PATCH/Update nulos.
        db (Session): Referencia del contexto de DB activa.

    Returns:
        Sucursal: Sucursal final luego de asimilar el PATCH dict.

    Raises:
        HTTPException: Retorna Exception handler si falla o hay id_Sucursal en falso.
    """
    sucursal = db.query(Sucursal).filter(Sucursal.id_Sucursal == sucursal_id).first()
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(sucursal, key, value)
        
    db.commit()
    db.refresh(sucursal)
    return sucursal

@router.delete("/{sucursal_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_sucursal(sucursal_id: UUID, db: Session = Depends(get_db)):
    """Elimina físicamente una sucursal de la base de datos.

    Args:
        sucursal_id (UUID): UUID del target a suprimir globalmente.
        db (Session): Sesión transaccional autocommit del motor engine.

    Returns:
        None: Retorno de estado limpio 204 HTTP Request.

    Raises:
        HTTPException: Throw 404 si el UUID referenciado nunca formó parte de la BD.
    """
    sucursal = db.query(Sucursal).filter(Sucursal.id_Sucursal == sucursal_id).first()
    if not sucursal:
        raise HTTPException(status_code=404, detail="Sucursal no encontrada")
    
    db.delete(sucursal)
    db.commit()
    return None
