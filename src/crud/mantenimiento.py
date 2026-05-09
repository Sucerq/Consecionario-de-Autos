from src.crud.clienteApi import _delete, _get, _post, _put
from datetime import date


def listar_mantenimiento() -> list:
    return _get("/mantenimiento")


def obtener_mantenimiento(mantenimiento_id: str) -> dict:
    return _get(f"/mantenimiento/{mantenimiento_id}")


def crear_mantenimiento(
     tipo_servicio: str, costo: float, auto_id: str, id_empleado: str
) -> dict:
    payload = {
        "tipo_servicio": tipo_servicio,
        "costo": costo,
        "auto_id": auto_id,
        "id_empleado": id_empleado,
    }
    return _post("/mantenimiento", json=payload)


def actualizar_mantenimiento(
    mantenimiento_id: str,
    tipo_servicio: str | None = None,
    costo: float | None = None,
    auto_id: str | None = None,
    id_empleado: str | None = None,
) -> dict:
    payload = {}
    if tipo_servicio is not None:
        payload["tipo_servicio"] = tipo_servicio
    if costo is not None:
        payload["costo"] = costo
    if auto_id is not None:
        payload["auto_id"] = auto_id
    if id_empleado is not None:
        payload["id_empleado"] = id_empleado
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/mantenimiento/{mantenimiento_id}", json=payload)


def eliminar_mantenimiento(mantenimiento_id: str) -> None:
    _delete(f"/mantenimiento/{mantenimiento_id}")
