"""Esquemas de validación Pydantic para el Detalle de Venta."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class DetalleVentaBase(BaseModel):
    """Atributos base de un Detalle de Venta (tabla intermedia)."""
    pass

class DetalleVentaCreate(DetalleVentaBase):
    """Esquema para crear un registro en Detalle de Venta."""
    id_usuario_crea: UUID
    id_Venta: UUID
    id_Auto: UUID

class DetalleVentaUpdate(BaseModel):
    """Esquema para actualización de Detalle de Venta."""
    id_usuario_edita: Optional[UUID] = None

class DetalleVentaResponse(DetalleVentaBase):
    """Esquema de respuesta para Detalle de Venta."""
    id_Detalle_Venta: UUID
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    id_usuario_crea: UUID
    id_usuario_edita: Optional[UUID] = None
    id_Venta: UUID
    id_Auto: UUID

    model_config = ConfigDict(from_attributes=True)
