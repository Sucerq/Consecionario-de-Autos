from src.crud.clienteApi import _delete, _get, _post, _put
from datetime import date

def listar_compra() -> list:
    return _get("/compra")


def obtener_compra(compra_id: str) -> dict:
    return _get(f"/compra/{compra_id}")


def crear_compra(
    precio: float,
    empleado_id: str,
) -> dict:
    payload = { "precio": precio, "empleado_id": empleado_id}
    return _post("/compra", json=payload)


def actualizar_compra(
    compra_id: str,
    precio: float | None = None,
    empleado_id: str | None = None,
) -> dict:
    payload = {}
    if precio is not None:
        payload["precio"] = precio
    if empleado_id is not None:
        payload["empleado_id"] = empleado_id
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/compra/{compra_id}", json=payload)


def eliminar_compra(compra_id: str) -> None:
    _delete(f"/compra/{compra_id}")
