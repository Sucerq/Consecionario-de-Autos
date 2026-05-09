from src.crud.clienteApi import _delete, _get, _post, _put


def listar_detalle_venta() -> list:
    return _get("/detalle_venta")


def obtener_detalle_venta(detalle_venta_id: str) -> dict:
    return _get(f"/detalle_venta/{detalle_venta_id}")


def crear_detalle_venta(
    venta_id: str,
    auto_id: str,
) -> dict:
    payload = {"venta_id": venta_id, "auto_id": auto_id}
    return _post("/detalle_venta", json=payload)


def actualizar_detalle_venta(
    detalle_venta_id: str, venta_id: str | None = None, auto_id: str | None = None
) -> dict:
    payload = {}
    if venta_id is not None:
        payload["venta_id"] = venta_id
    if auto_id is not None:
        payload["auto_id"] = auto_id
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/detalle_venta/{detalle_venta_id}", json=payload)


def eliminar_detalle_venta(detalle_venta_id: str) -> None:
    _delete(f"/detalle_venta/{detalle_venta_id}")
