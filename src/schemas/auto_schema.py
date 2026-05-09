"""Esquemas de validación Pydantic para la entidad Auto."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class AutoBase(BaseModel):
    """Atributos base de un Auto."""
    Marca: str
    Modelo: str
    Tipo_Auto: str
    Precio: float
    Estado: Optional[bool] = True

class AutoCreate(AutoBase):
    """Esquema para creación de un Auto."""
    id_usuario_crea: UUID
    id_Sucursal: UUID
    id_Compra: UUID

class AutoUpdate(BaseModel):
    """Esquema para actualización parcial de un Auto."""
    Marca: Optional[str] = None
    Modelo: Optional[str] = None
    Tipo_Auto: Optional[str] = None
    Precio: Optional[float] = None
    Estado: Optional[bool] = None
    id_usuario_edita: Optional[UUID] = None

class AutoResponse(AutoBase):
    """Esquema de respuesta para un Auto."""
    id_Auto: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    id_usuario_crea: UUID
    id_usuario_edita: Optional[UUID] = None
    id_Sucursal: UUID
    id_Compra: UUID

    model_config = ConfigDict(from_attributes=True)
