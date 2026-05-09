from sqlalchemy.orm import Session
from src.entities.Usuario import Usuario
from src.core.security import hash_password, verify_password
from src.schemas.usuario_schema import UsuarioCreate
from typing import Optional


def get_usuario_by_nombre_usuario(db: Session, nombre_usuario: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.nombre_usuario == nombre_usuario).first()


def authenticate_usuario(db: Session, nombre_usuario: str, password: str) -> Optional[Usuario]:
    usuario = get_usuario_by_nombre_usuario(db, nombre_usuario)
    if not usuario:
        return None
    if not verify_password(password, usuario.contraseña_hash):
        return None
    return usuario


def listar_usuarios(db: Session) -> list:
    return db.query(Usuario).all()


def obtener_usuario(db: Session, usuario_id: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.id_Usuario == usuario_id).first()


def crear_usuario(db: Session, data: UsuarioCreate) -> Usuario:
    nuevo = Usuario(
        nombre=data.nombre,
        nombre_usuario=data.nombre_usuario,
        email=data.email,
        contraseña_hash=hash_password(data.password),
        telefono=data.telefono,
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def actualizar_usuario(db: Session, usuario_id: str, datos: dict) -> Optional[Usuario]:
    usuario = obtener_usuario(db, usuario_id)
    if not usuario:
        return None
    for campo, valor in datos.items():
        setattr(usuario, campo, valor)
    db.commit()
    db.refresh(usuario)
    return usuario


def eliminar_usuario(db: Session, usuario_id: str) -> bool:
    usuario = obtener_usuario(db, usuario_id)
    if not usuario:
        return False
    db.delete(usuario)
    db.commit()
    return True