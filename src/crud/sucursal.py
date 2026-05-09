from src.crud.clienteApi import _delete, _get, _post, _put


def listar_sucursal() -> list:
    return _get("/sucursal")


def obtener_sucursal(sucursal_id: str) -> dict:
    return _get(f"/sucursal/{sucursal_id}")


def crear_sucursal(nombre: str, telefono: str, direccion: str) -> dict:
    payload = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
    return _post("/sucursal", json=payload)


def actualizar_sucursal(
    sucursal_id: str,
    nombre: str | None = None,
    telefono: str | None = None,
    direccion: str | None = None,
) -> dict:
    payload = {}
    if nombre is not None:
        payload["nombre"] = nombre
    if telefono is not None:
        payload["telefono"] = telefono
    if direccion is not None:
        payload["direccion"] = direccion
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/sucursal/{sucursal_id}", json=payload)


def eliminar_sucursal(sucursal_id: str) -> None:
    _delete(f"/sucursal/{sucursal_id}")
