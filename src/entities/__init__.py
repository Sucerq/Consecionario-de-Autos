"""
Paquete de entidades ORM del proyecto Concesionario de Autos.

Centraliza las importaciones de todos los modelos SQLAlchemy para que
``Base.metadata`` los registre correctamente antes de ejecutar
migraciones con Alembic o crear tablas con ``create_all()``.

Módulos exportados:
    Auto          - Vehículos del inventario.
    Cliente       - Clientes del concesionario.
    Compra        - Compras de vehículos a proveedores.
    Detalle_Venta - Líneas de detalle de una venta.
    Empleado      - Empleados del concesionario.
    Mantenimiento - Registros de mantenimiento de vehículos.
    Sucursal      - Sucursales del concesionario.
    Usuario       - Usuarios del sistema con autenticación JWT.
    Venta         - Ventas de vehículos a clientes.
"""

from src.entities.usuario import Usuario
from src.entities.autos import Auto
from src.entities.clientes import Cliente
from src.entities.compra import Compra
from src.entities.detalle_venta import Detalle_Venta
from src.entities.empleado import Empleado
from src.entities.mantenimiento import Mantenimiento
from src.entities.sucursal import Sucursal
from src.entities.venta import Venta

__all__ = [
    "Usuario",
    "Auto",
    "Cliente",
    "Compra",
    "Detalle_Venta",
    "Empleado",
    "Mantenimiento",
    "Sucursal",
    "Venta",
]