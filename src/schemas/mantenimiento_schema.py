"""Esquemas de validación Pydantic para la entidad Mantenimiento."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID
from datetime import datetime

class MantenimientoBase(BaseModel):
    """Atributos base de un Mantenimiento."""
    Tipo_Servicio: str
    Costo: float

class MantenimientoCreate(MantenimientoBase):
    """Esquema para crear un registro de Mantenimiento."""
    id_usuario_crea: UUID
    id_Auto: UUID
    id_Empleado: UUID

class MantenimientoUpdate(BaseModel):
    """Esquema para actualización parcial de un Mantenimiento."""
    Tipo_Servicio: Optional[str] = None
    Costo: Optional[float] = None
    id_usuario_edita: Optional[UUID] = None

class MantenimientoResponse(MantenimientoBase):
    """Esquema de respuesta para un Mantenimiento."""
    id_Mantenimiento: UUID
    Fecha: Optional[datetime] = None
    fecha_creacion: datetime
    fecha_edicion: Optional[datetime] = None
    id_usuario_crea: UUID
    id_usuario_edita: Optional[UUID] = None
    id_Auto: UUID
    id_Empleado: UUID

    model_config = ConfigDict(from_attributes=True)
