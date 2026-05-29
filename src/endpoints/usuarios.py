"""Endpoints de la API para la gestión de Usuarios."""

from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.usuario import Usuario
from src.schemas.usuario_schema import UsuarioCreate, UsuarioUpdate, UsuarioResponse

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    """Obtiene la lista de todos los usuarios registrados.

    Args:
        db (Session): Sesión activa generada en Yield de FastAPI.

    Returns:
        list[Usuario]: Listado de todos los modelos devueltos.
    """
    return db.query(Usuario).all()


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    """Busca un usuario específico mediante su identificador.

    Args:
        usuario_id (UUID): Llave primaria UUID del usuario consultado.
        db (Session): Instancia de la clase de sesión en SQLALchemy.

    Returns:
        Usuario: Objeto recuperado de Postgres / SQL DB.

    Raises:
        HTTPException: Notifica NotFound 404 al faltar su ID correcto.
    """
    usuario = db.query(Usuario).filter(Usuario.id_Usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(dato: UsuarioCreate, db: Session = Depends(get_db)):
    """Registra y almacena un nuevo usuario validando credenciales únicas.

    Args:
        dato (UsuarioCreate): Esqueleto Pydantic validador para Request POST.
        db (Session): Capa DBMS de SQLAlchemy activa en el thread.

    Returns:
        Usuario: Usuario insertado con Timezones y UUID resueltos por DB nativa.

    Raises:
        HTTPException: HTTP 400 Bad Request si el nombre o correo pre-existen.
    """
    if db.query(Usuario).filter(Usuario.email == dato.email).first():
        raise HTTPException(
            status_code=400, detail="Este correo ya se encuentra en uso."
        )
    if db.query(Usuario).filter(Usuario.nombre_usuario == dato.nombre_usuario).first():
        raise HTTPException(
            status_code=400, detail="El nombre de usuario no está disponible."
        )

    # En un entorno real se cifraría la contraseña aquí.
    nuevo_usuario = Usuario(
        nombre=dato.nombre,
        nombre_usuario=dato.nombre_usuario,
        email=dato.email,
        contraseña_hash=dato.contraseña_hash,
        telefono=dato.telefono,
        activo=dato.activo,
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(
    usuario_id: UUID, dato: UsuarioUpdate, db: Session = Depends(get_db)
):
    """Actualiza parcialmente los datos de un usuario.

    Args:
        usuario_id (UUID): ID localizador para el bloque en update.
        dato (UsuarioUpdate): JSON recibido en payload parseable para opcionales.
        db (Session): Bloque manejador de Contexto en SQLAlchemy Session.

    Returns:
        Usuario: Instancia actual y regenerada del usuario post-Update.

    Raises:
        HTTPException: HTTPException NotFound al buscar update localizador erróneo.
    """
    usuario = db.query(Usuario).filter(Usuario.id_Usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    update_data = dato.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    """Elimina físicamente a un usuario de la base de datos.

    Args:
        usuario_id (UUID): Llave posicional para la supresión de la base relacional.
        db (Session): Gestor relacional inyectado.

    Returns:
        None: Retorno nulo 204 HTTP.

    Raises:
        HTTPException: 404 Not Found exception handle en caso fallido localizador falso.
    """
    usuario = db.query(Usuario).filter(Usuario.id_Usuario == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    db.delete(usuario)
    db.commit()
    return None
