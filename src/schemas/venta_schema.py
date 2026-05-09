"""Esquemas de validación Pydantic para la entidad Venta."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class VentaBase(BaseModel):
    """Atributos base de una Venta."""
    Precio_Venta: float
    Metodo_Pago: str

class VentaCreate(VentaBase):
    """Esquema para generar una nueva Venta."""
    Fecha: datetime
    id_usuario_crea: UUID
    id_Cliente: UUID
    id_Empleado: UUID

class VentaUpdate(BaseModel):
    """Esquema para actualización parcial de una Venta."""
    Precio_Venta: Optional[float] = None
    Metodo_Pago: Optional[str] = None
    id_usuario_edita: Optional[UUID] = None

class VentaResponse(VentaBase):
    """Esquema de respuesta para una Venta."""
    id_Venta: UUID
    Fecha: datetime
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    id_usuario_crea: UUID
    id_usuario_edita: Optional[UUID] = None
    id_Cliente: UUID
    id_Empleado: UUID

    model_config = ConfigDict(from_attributes=True)
