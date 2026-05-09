"""Esquemas de validación Pydantic para la entidad Cliente."""

from pydantic import BaseModel, ConfigDict, EmailStr
from typing import Optional
from uuid import UUID

class ClienteBase(BaseModel):
    """Atributos base de un Cliente."""
    nombre: str
    Apellido: str
    email: EmailStr
    telefono: Optional[str] = None
    Direccion: Optional[str] = None
    Tipo_Cliente: str

class ClienteCreate(ClienteBase):
    """Esquema para creación de un Cliente."""
    pass

class ClienteUpdate(BaseModel):
    """Esquema para actualización parcial de un Cliente."""
    nombre: Optional[str] = None
    Apellido: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    Direccion: Optional[str] = None
    Tipo_Cliente: Optional[str] = None

class ClienteResponse(ClienteBase):
    """Esquema de respuesta para un Cliente."""
    id_Cliente: UUID
    
    model_config = ConfigDict(from_attributes=True)
