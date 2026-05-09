"""Esquemas de validación Pydantic para la entidad Empleado."""

from pydantic import BaseModel, ConfigDict
from typing import Optional
from uuid import UUID

class EmpleadoBase(BaseModel):
    """Atributos base de un Empleado."""
    Nombre: str
    Cargo: str
    Telefono: str
    Salario: float

class EmpleadoCreate(EmpleadoBase):
    """Esquema para registrar un nuevo Empleado."""
    pass

class EmpleadoUpdate(BaseModel):
    """Esquema para actualización parcial de un Empleado."""
    Nombre: Optional[str] = None
    Cargo: Optional[str] = None
    Telefono: Optional[str] = None
    Salario: Optional[float] = None

class EmpleadoResponse(EmpleadoBase):
    """Esquema de respuesta para un Empleado."""
    id_Empleado: UUID

    model_config = ConfigDict(from_attributes=True)
