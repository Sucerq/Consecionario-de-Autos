from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Importar los routers de endpoints
from src.endpoints.autos import router as autos_router
from src.endpoints.mantenimientos import router as mantenimientos_router
from src.endpoints.empleados import router as empleados_router
from src.endpoints.ventas import router as ventas_router
from src.endpoints.compras import router as compras_router
from src.endpoints.clientes import router as clientes_router
from src.endpoints.detalle_ventas import router as detalle_ventas_router
from src.endpoints.sucursales import router as sucursales_router
from src.endpoints.usuarios import router as usuarios_router
from src.endpoints.login import router as login_router

from fastapi.exceptions import HTTPException, RequestValidationError
from src.core.config import get_settings
from src.core.exceptions import AppException
from src.core.error_handlers import (
    app_exception_handler,
    generic_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)

from src.database.config import create_tables
from src.endpoints import (
    usuarios,
    autos,
    clientes,
    compras,
    detalle_ventas,
    empleados,
    mantenimientos,
    sucursales,
    ventas,
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(
    title="API Concesionario de Autos",
    description="API para gestionar inventarios, ventas, compras y mantenimientos de un concesionario.",
    version="1.0.0",
    lifespan=lifespan,
)

# Root path
@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API del Concesionario de Autos"}

_settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=_settings.cors_origins_list(),
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type", "Accept"],
)

app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

# Incluir routers
app.include_router(autos_router)
app.include_router(clientes_router)
app.include_router(empleados_router)
app.include_router(ventas_router)
app.include_router(compras_router)
app.include_router(mantenimientos_router)
app.include_router(detalle_ventas_router)
app.include_router(sucursales_router)
app.include_router(usuarios_router)
app.include_router(login_router)
