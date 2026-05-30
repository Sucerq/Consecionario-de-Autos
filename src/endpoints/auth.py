from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.entities.usuario import Usuario
from src.schemas.login_schema import Login
from src.utils.security import verify_password
from src.core.auth import create_access_token
from src.core.config import get_settings
from src.core.responses import success_response

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(dato: Login, db: Session = Depends(get_db)):
    user = (
        db.query(Usuario).filter(Usuario.nombre_usuario == dato.nombre_usuario).first()
    )

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not verify_password(dato.contraseña, user.contraseña_hash):
        raise HTTPException(status_code=401, detail="Contraseña incorrecta")

    if not user.activo:
        raise HTTPException(status_code=403, detail="Usuario inactivo")

    settings = get_settings()
    access_token = create_access_token(
        subject=str(user.id_Usuario),
        nombre_usuario=user.nombre_usuario,
        settings=settings,
    )
    return {
        "success": True,
        "id_usuario": str(user.id_Usuario),
        "nombre_usuario": user.nombre_usuario,
        "access_token": access_token,
        "token_type": "bearer",
    }
