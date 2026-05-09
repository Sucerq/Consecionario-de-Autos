from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.auth import create_access_token
from src.core.config import get_settings
from src.core.responses import success_response
from src.database.config import get_db
from src.entities.usuario import Usuario
from src.schemas.login_schema import Login
from src.utils.security import verify_password


router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.post("/login")
def login(dato: Login, db: Session = Depends(get_db)):
    """Endpoint para autenticar a un usuario y generar un token JWT.

    Valida las credenciales del usuario (nombre de usuario y contraseña)
    contra los registros en la base de datos. Si son correctas y el usuario
    está activo, genera un JSON Web Token (JWT) de acceso.

    Args:
        dato (Login): Payload con las credenciales ingresadas por el usuario.
        db (Session, optional): Sesión inyectada de la base de datos.

    Returns:
        dict: Un diccionario estructurado con el resultado de la operación,
        el token JWT generado y metadatos adicionales del usuario.

    Raises:
        HTTPException: HTTP 401 si las credenciales son incorrectas o no existe.
        HTTPException: HTTP 403 si el usuario existe pero está inactivo.
    """
    user = (
        db.query(Usuario).filter(Usuario.nombre_usuario == dato.nombre_usuario).first()
    )
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")
    if not verify_password(dato.contraseña, user.contraseña_hash):
        raise HTTPException(
            status_code=401, detail="Contraseña no válida para el usuario"
        )
    if not user.activo:
        raise HTTPException(status_code=403, detail="Usuario inactivo")

    settings = get_settings()
    access_token = create_access_token(
        subject=user.id_Usuario,
        nombre_usuario=user.nombre_usuario,
        rol=user.rol,
        settings=settings,
    )
    data = {
        "resultado": "Login exitoso",
        "id_usuario": str(user.id_Usuario),
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": settings.access_token_expire_minutes * 60,
        "rol": user.rol,
    }
    return success_response(data=data, message="Login exitoso")
