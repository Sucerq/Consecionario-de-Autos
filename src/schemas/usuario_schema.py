from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid


class UsuarioCreate(BaseModel):
    nombre: str
    nombre_usuario: str
    email: EmailStr
    password: str
    telefono: Optional[str] = None


class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    nombre_usuario: Optional[str] = None
    email: Optional[EmailStr] = None
    telefono: Optional[str] = None
    activo: Optional[bool] = None


class UsuarioRead(BaseModel):
    id_Usuario: uuid.UUID
    nombre: str
    nombre_usuario: str
    email: str
    telefono: Optional[str] = None
    activo: bool

    model_config = {"from_attributes": True}


# Alias para compatibilidad con endpoints que usan UsuarioResponse
UsuarioResponse = UsuarioRead


class LoginRequest(BaseModel):
    nombre_usuario: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"