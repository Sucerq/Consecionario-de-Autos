# src/endpoints/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from src.database.config import get_db
from src.crud.usuario import authenticate_usuario, crear_usuario
from src.schemas.usuario_schema import LoginRequest, TokenResponse, UsuarioCreate, UsuarioRead
from src.core.security import create_access_token, decode_token

router = APIRouter(prefix="/auth", tags=["Autenticación"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    """
    Recibe nombre_usuario + password.
    Retorna un JWT si las credenciales son correctas.
    """
    usuario = authenticate_usuario(db, data.nombre_usuario, data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token = create_access_token(data={"sub": str(usuario.id_Usuario), "username": usuario.nombre_usuario})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register", response_model=UsuarioRead, status_code=201)
def register(data: UsuarioCreate, db: Session = Depends(get_db)):
    """Crea un nuevo usuario en el sistema."""
    nuevo = crear_usuario(db, data)
    return nuevo


# ── Dependency reutilizable para proteger otras rutas ──────────────────────────

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """
    Dependency de FastAPI: extrae y valida el token JWT.
    Úsalo en cualquier endpoint que requiera autenticación:
    
        @router.get("/ruta-protegida")
        def mi_ruta(usuario = Depends(get_current_user)):
            ...
    """
    payload = decode_token(token)
    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user_id = payload.get("sub")
    from src.entities.Usuario import Usuario
    usuario = db.query(Usuario).filter(Usuario.id_Usuario == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario