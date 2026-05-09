"""Esquemas de validación Pydantic para la entidad Sucursal."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class SucursalBase(BaseModel):
    """Atributos base de una Sucursal."""
    Nombre: str
    Telefono: str
    Direccion: str

class SucursalCreate(SucursalBase):
    """Esquema para creación de una Sucursal."""
    pass

class SucursalUpdate(BaseModel):
    """Esquema para actualización parcial de Sucursal."""
    Nombre: Optional[str] = None
    Telefono: Optional[str] = None
    Direccion: Optional[str] = None

class SucursalResponse(SucursalBase):
    """Esquema de respuesta para Sucursal."""
    id_Sucursal: UUID

    model_config = ConfigDict(from_attributes=True)
