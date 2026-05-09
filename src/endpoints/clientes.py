"""Endpoints de la API para la gestión de Clientes."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.clientes import Cliente
from src.schemas.clientes_schema import ClienteCreate, ClienteUpdate, ClienteResponse

router = APIRouter(prefix="/clientes", tags=["Clientes"])

@router.get("/", response_model=list[ClienteResponse])
def listar_clientes(db: Session = Depends(get_db)):
    """Obtiene la lista de clientes.

    Args:
        db (Session): Sesión a BD.

    Returns:
        list[Cliente]: Lista de entidades Cliente en base de datos.
    """
    return db.query(Cliente).all()

@router.get("/{cliente_id}", response_model=ClienteResponse)
def obtener_cliente(cliente_id: UUID, db: Session = Depends(get_db)):
    """Obtiene un cliente por su ID.

    Args:
        cliente_id (UUID): Identificador único del cliente.
        db (Session): Sesión de conexión activa.

    Returns:
        Cliente: Entidad del cliente encontrado.

    Raises:
        HTTPException: Status 404 si el cliente no está persistido.
    """
    cliente = db.query(Cliente).filter(Cliente.id_Cliente == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cliente

@router.post("/", response_model=ClienteResponse, status_code=status.HTTP_201_CREATED)
def crear_cliente(dato: ClienteCreate, db: Session = Depends(get_db)):
    """Registra y valida un nuevo cliente en DB.

    Args:
        dato (ClienteCreate): Los datos de registro correspondientes al JSON body.
        db (Session): Sesión de escritura a la DB.

    Returns:
        Cliente: Objeto del nuevo cliente ya persistido.

    Raises:
        HTTPException: Código 400 en caso de recibir duplicidad de Email.
    """
    # Validación correo único
    if db.query(Cliente).filter(Cliente.email == dato.email).first():
        raise HTTPException(status_code=400, detail="El correo ya se encuentra registrado.")

    nuevo_cliente = Cliente(
        nombre=dato.nombre,
        Apellido=dato.Apellido,
        email=dato.email,
        telefono=dato.telefono,
        Direccion=dato.Direccion,
        Tipo_Cliente=dato.Tipo_Cliente
    )
    db.add(nuevo_cliente)
    db.commit()
    db.refresh(nuevo_cliente)
    return nuevo_cliente

@router.put("/{cliente_id}", response_model=ClienteResponse)
def actualizar_cliente(cliente_id: UUID, dato: ClienteUpdate, db: Session = Depends(get_db)):
    """Escribe actualización parcial en los datos del cliente.

    Args:
        cliente_id (UUID): Key del cliente alojado en la BD a modificar.
        dato (ClienteUpdate): Payload de información (Patch).
        db (Session): Sesión abierta a DBMS.

    Returns:
        Cliente: Cliente provisto de la data fresca en la BD.

    Raises:
        HTTPException: Status 404 de no encontrar los params.
    """
    cliente = db.query(Cliente).filter(Cliente.id_Cliente == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(cliente, key, value)
        
    db.commit()
    db.refresh(cliente)
    return cliente

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id: UUID, db: Session = Depends(get_db)):
    """Borrado paramétrico de cliente de PostgreSQL u otro.

    Args:
        cliente_id (UUID): La PK o ID genérico.
        db (Session): Sesión de DBMS en curso de FastAPI.

    Returns:
        None: Retorno sin data visible, Status HTTP 204 natural.

    Raises:
        HTTPException: 404 ante un requerimiento falso (Id falso).
    """
    cliente = db.query(Cliente).filter(Cliente.id_Cliente == cliente_id).first()
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    db.delete(cliente)
    db.commit()
    return None
