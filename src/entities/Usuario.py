"""
Entidad ORM que representa la tabla ``tbl_usuario`` en la base de datos.

Define el modelo SQLAlchemy del usuario del sistema, incluyendo sus
credenciales de acceso, información de contacto, rol de autorización
y campos de auditoría.
"""

import uuid

from sqlalchemy import Boolean, Column, DateTime, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from src.database.config import Base


class Usuario(Base):
    """Modelo ORM de la tabla ``tbl_usuario``.

    Attributes:
        id_Usuario (UUID): Identificador único del usuario (PK).
        nombre (str): Nombre completo del usuario.
        nombre_usuario (str): Nombre de usuario único para login.
        email (str): Correo electrónico único del usuario.
        contraseña_hash (str): Contraseña cifrada con bcrypt.
        telefono (str | None): Teléfono de contacto, opcional.
        rol (str): Rol del usuario en el sistema (ej. 'admin', 'user').
        activo (bool): Indica si el usuario está habilitado para acceder.
        fecha_creacion (datetime): Timestamp de creación del registro.
        fecha_edicion (datetime | None): Timestamp de la última modificación.
    """

    __tablename__ = "tbl_usuario"

    id_Usuario = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True,
    )
    nombre = Column(String(100), nullable=False)
    nombre_usuario = Column(
        String(50), unique=True, index=True, nullable=False
    )
    email = Column(String(150), unique=True, index=True, nullable=False)
    contraseña_hash = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    # Rol de autorización requerido por core/auth.py para generar el JWT.
    # Valores posibles: 'admin' | 'user'
    rol = Column(String(20), nullable=False, server_default="user")
    activo = Column(Boolean, default=True)
    fecha_creacion = Column(DateTime(timezone=True), server_default=func.now())
    fecha_edicion = Column(DateTime(timezone=True), onupdate=func.now())