"""Esquemas de validación Pydantic para la entidad Compra."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class CompraBase(BaseModel):
    """Atributos base de una Compra de auto usado."""
    Precio: float

class CompraCreate(CompraBase):
    """Esquema para registrar una nueva Compra."""
    id_usuario_crea: UUID
    id_Empleado: UUID

class CompraUpdate(BaseModel):
    """Esquema para actualización parcial de una Compra."""
    Precio: Optional[float] = None
    id_usuario_edita: Optional[UUID] = None

class CompraResponse(CompraBase):
    """Esquema de respuesta para una Compra."""
    id_Compra: UUID
    Fecha: Optional[datetime] = None
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    id_usuario_crea: UUID
    id_usuario_edita: Optional[UUID] = None
    id_Empleado: UUID

    model_config = ConfigDict(from_attributes=True)
