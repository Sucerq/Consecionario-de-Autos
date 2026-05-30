from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.database.config import create_tables
from src.core.config import get_settings
from src.core.exceptions import AppException
from src.core.error_handlers import (
    app_exception_handler,
    generic_exception_handler,
    http_exception_handler,
    validation_exception_handler,
)

from src.endpoints.autos import router as autos_router
from src.endpoints.mantenimientos import router as mantenimientos_router
from src.endpoints.empleados import router as empleados_router
from src.endpoints.ventas import router as ventas_router
from src.endpoints.compras import router as compras_router
from src.endpoints.clientes import router as clientes_router
from src.endpoints.detalle_ventas import router as detalle_ventas_router
from src.endpoints.sucursales import router as sucursales_router
from src.endpoints.usuarios import router as usuarios_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="API Concesionario de Autos",
    description="API de gestión de autos, usuarios y ventas",
    version="1.0.0",
    lifespan=lifespan,
)


settings = get_settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)


@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}


# ROUTERS
app.include_router(autos_router)
app.include_router(mantenimientos_router)
app.include_router(empleados_router)
app.include_router(ventas_router)
app.include_router(compras_router)
app.include_router(clientes_router)
app.include_router(detalle_ventas_router)
app.include_router(sucursales_router)
app.include_router(usuarios_router)
