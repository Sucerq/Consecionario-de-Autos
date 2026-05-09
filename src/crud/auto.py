from src.crud.clienteApi import _delete, _get, _post, _put


def listar_auto() -> list:
    return _get("/auto")


def obtener_auto(auto_id: str) -> dict:
    return _get(f"/auto/{auto_id}")


def crear_auto(
    marca: str,
    modelo: str,
    tipo_auto: str,
    precio: float,
    sucursal_id: str,
    compra_id: str,
    estado: bool = True,
) -> dict:
    payload = {
        "marca": marca,
        "modelo": modelo,
        "tipo_auto": tipo_auto,
        "precio": precio,
        "sucursal_id": sucursal_id,
        "compra_id": compra_id,
        "estado": estado,
    }
    return _post("/auto", json=payload)


def actualizar_auto(
    auto_id: str,
    marca: str | None = None,
    modelo: str | None = None,
    tipo_auto: str | None = None,
    precio: float | None = None,
    sucursal_id: str | None = None,
    compra_id: str | None = None,
    estado: bool | None = None,
) -> dict:
    payload = {}
    if marca is not None:
        payload["marca"] = marca
    if modelo is not None:
        payload["modelo"] = modelo
    if tipo_auto is not None:
        payload["tipo_auto"] = tipo_auto
    if precio is not None:
        payload["precio"] = precio
    if sucursal_id is not None:
        payload["sucursal_id"] = sucursal_id
    if compra_id is not None:
        payload["compra_id"] = compra_id
    if estado is not None:
        payload["estado"] = estado
    if not payload:
        raise ValueError("Debe enviar al menos un campo para actualizar")
    return _put(f"/auto/{auto_id}", json=payload)


def eliminar_auto(auto_id: str) -> None:
    _delete(f"/auto/{auto_id}")
