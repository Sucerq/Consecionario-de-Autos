from src.crud.clienteApi import _delete, _get, _post, _put
from datetime import date


def listar_venta() -> list:
    return _get("/venta")


def obtener_venta(venta_id: str) -> dict:
    return _get(f"/venta/{venta_id}")


def crear_venta(
    precio_venta: float,
    metodo_pago: str,
    cliente_id: str,
    empleado_id: str,
) -> dict:
    payload = {
        "precio_venta": precio_venta,
        "metodo_pago": metodo_pago,
        "cliente_id": cliente_id,
        "empleado_id": empleado_id,
    }
    return _post("/venta", json=payload)


def actualizar_venta(
    venta_id: str,
    precio_venta: float | None = None,
    metodo_pago: str | None = None,
    cliente_id: str | None = None,
    empleado_id: str | None = None,
) -> dict:
    payload = {}
    if precio_venta is not None:
        payload["precio_venta"] = precio_venta
    if metodo_pago is not None:
        payload["metodo_pago"] = metodo_pago
    if cliente_id is not None:
        payload["cliente_id"] = cliente_id
    if empleado_id is not None:
        payload["empleado_id"] = empleado_id
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")

    return _put(f"/venta/{venta_id}", json=payload)


def eliminar_venta(venta_id: str) -> None:
    _delete(f"/venta/{venta_id}")
