from src.crud.usuario import get_usuario_by_nombre_usuario, crear_usuario, authenticate_usuario


from src.crud.sucursal import (
    listar_sucursal,
    obtener_sucursal,
    crear_sucursal,
    actualizar_sucursal,
    eliminar_sucursal,
)

from src.crud.venta import (
    listar_venta,
    obtener_venta,
    crear_venta,
    actualizar_venta,
    eliminar_venta,
)

from src.crud.mantenimiento import (
    listar_mantenimiento,
    obtener_mantenimiento,
    crear_mantenimiento,
    actualizar_mantenimiento,
    eliminar_mantenimiento,
)

from src.crud.empleado import (
    listar_empleado,
    obtener_empleado,
    crear_empleado,
    actualizar_empleado,
    eliminar_empleado,
)

from src.crud.detalle_venta import (
    listar_detalle_venta,
    obtener_detalle_venta,
    crear_detalle_venta,
    actualizar_detalle_venta,
    eliminar_detalle_venta,
)

from src.crud.compra import (
    listar_compra,
    obtener_compra,
    crear_compra,
    actualizar_compra,
    eliminar_compra,
)

from src.crud.cliente import (
    listar_cliente,
    obtener_cliente,
    crear_cliente,
    actualizar_cliente,
    eliminar_cliente,
)

from src.crud.auto import (
    listar_auto,
    obtener_auto,
    crear_auto,
    actualizar_auto,
    eliminar_auto,
)

from src.crud.usuario import (
    listar_usuarios,
    obtener_usuario,
    crear_usuario,
    actualizar_usuario,
    eliminar_usuario,
)
# src/crud/__init__.py


__all__ = [
    "listar_sucursal",
    "obtener_sucursal",
    "crear_sucursal",
    "actualizar_sucursal",
    "eliminar_sucursal",
    "listar_venta",
    "obtener_venta",
    "crear_venta",
    "actualizar_venta",
    "eliminar_venta",
    "listar_mantenimiento",
    "obtener_mantenimiento",
    "crear_mantenimiento",
    "actualizar_mantenimiento",
    "eliminar_mantenimiento",
    "listar_empleado",
    "obtener_empleado",
    "crear_empleado",
    "actualizar_empleado",
    "eliminar_empleado",
    "listar_detalle_venta",
    "obtener_detalle_venta",
    "crear_detalle_venta",
    "actualizar_detalle_venta",
    "eliminar_detalle_venta",
    "listar_compra",
    "obtener_compra",
    "crear_compra",
    "actualizar_compra",
    "eliminar_compra",
    "listar_cliente",
    "obtener_cliente",
    "crear_cliente",
    "actualizar_cliente",
    "eliminar_cliente",
    "listar_auto",
    "obtener_auto",
    "crear_auto",
    "actualizar_auto",
    "eliminar_auto",
    "listar_usuarios",
    "obtener_usuario",
    "crear_usuario",
    "actualizar_usuario",
    "eliminar_usuario",
]
