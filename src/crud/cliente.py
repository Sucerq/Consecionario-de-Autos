from src.crud.clienteApi import _delete, _get, _post, _put


def listar_cliente() -> list:
    return _get("/cliente")


def obtener_cliente(cliente_id: str) -> dict:
    return _get(f"/cliente/{cliente_id}")


def crear_cliente(
    nombre: str,
    apellido: str,
    telefono: str,
    email: str,
    direccion: str,
    tipo_cliente: str,
) -> dict:
    payload = {
        "nombre": nombre,
        "apellido": apellido,
        "telefono": telefono,
        "email": email,
        "direccion": direccion,
        "tipo_cliente": tipo_cliente,
    }
    return _post("/cliente", json=payload)


def actualizar_cliente(
    cliente_id: str,
    nombre: str | None = None,
    apellido: str | None = None,
    telefono: str | None = None,
    email: str | None = None,
    direccion: str | None = None,
    tipo_cliente: str | None = None,
) -> dict:
    payload = {}
    if nombre is not None:
        payload["nombre"] = nombre
    if apellido is not None:
        payload["apellido"] = apellido
    if telefono is not None:
        payload["telefono"] = telefono
    if email is not None:
        payload["email"] = email
    if direccion is not None:
        payload["direccion"] = direccion
    if tipo_cliente is not None:
        payload["tipo_cliente"] = tipo_cliente
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/cliente/{cliente_id}", json=payload)


def eliminar_cliente(cliente_id: str) -> None:
    _delete(f"/cliente/{cliente_id}")
