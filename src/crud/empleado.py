from src.crud.clienteApi import _delete, _get, _post, _put


def listar_empleado() -> list:
    return _get("/empleado")


def obtener_empleado(empleado_id: str) -> dict:
    return _get(f"/empleado/{empleado_id}")


def crear_empleado(
    nombre: str,
    cargo: str,
    telefono: str,
    salario: float,
) -> dict:
    payload = {
        "nombre": nombre,
        "cargo": cargo,
        "telefono": telefono,
        "salario": salario,
    }
    return _post("/empleado", json=payload)


def actualizar_empleado(
    empleado_id: str,
    nombre: str | None = None,
    cargo: str | None = None,
    telefono: str | None = None,
    salario: float | None = None,
) -> dict:
    payload = {}
    if nombre is not None:
        payload["nombre"] = nombre
    if cargo is not None:
        payload["cargo"] = cargo
    if telefono is not None:
        payload["telefono"] = telefono
    if salario is not None:
        payload["salario"] = salario
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/empleado/{empleado_id}", json=payload)


def eliminar_empleado(empleado_id: str) -> None:
    _delete(f"/empleado/{empleado_id}")
