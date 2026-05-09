"""
Menú por consola que usa el CRUD (cliente de la API Banco).
Al ejecutar main.py se inicia la API en segundo plano (uvicorn) y luego el menú.
"""

import sys
import threading
import time


# main.py
import uvicorn
from src.app import app

if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)











sys.path.insert(0, ".")

from src.crud import (
    actualizar_auto,
    actualizar_cliente,
    actualizar_compra,
    actualizar_detalle_venta,
    actualizar_empleado,
    actualizar_mantenimiento,
    actualizar_sucursal,
    actualizar_usuario,
    actualizar_venta,



    crear_auto,
    crear_cliente,
    crear_compra,
    crear_detalle_venta,
    crear_empleado,
    crear_mantenimiento,
    crear_sucursal,
    crear_usuario,
    crear_venta,


    eliminar_auto,
    eliminar_cliente,
    eliminar_compra,
    eliminar_detalle_venta,
    eliminar_empleado,
    eliminar_mantenimiento,
    eliminar_sucursal,
    eliminar_usuario,
    eliminar_venta,


    listar_auto,
    listar_cliente,  
    listar_compra,
    listar_detalle_venta,
    listar_empleado,
    listar_mantenimiento,
    listar_sucursal,
    listar_usuarios,
    listar_venta,



    obtener_auto,
    obtener_cliente,
    obtener_compra,
    obtener_detalle_venta,
    obtener_empleado,
    obtener_mantenimiento,
    obtener_sucursal,
    obtener_usuario,
    obtener_venta
)


def _err_conexion(e):
    err = str(e)
    if "10061" in err or "Connection refused" in err or "denegó" in err.lower():
        print(
            "  No se pudo conectar a la API. Espera unos segundos y vuelve a intentar."
        )
    else:
        print(f"  Error: {e}")


def menu_usuarios() -> None:
    while True:
        print("\n--- Usuarios ---")
        print("1. Listar  2. Ver uno  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                usuarios = listar_usuarios()
                if not usuarios:
                    print("  No hay usuarios.")
                else:
                    for u in usuarios:
                        print(
                            f"  {u['id']} | {u['nombre_usuario']} | {u['email']} | activo={u['activo']}"
                        )
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            uid = input("ID usuario: ").strip()
            if uid:
                try:
                    u = obtener_usuario(uid)
                    print(f"  {u}")
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            nombre = input("Nombre: ").strip()
            nombre_usuario = input("Nombre usuario: ").strip()
            email = input("Email: ").strip()
            contraseña = input("Contraseña: ").strip()
            if nombre and nombre_usuario and email and contraseña:
                try:
                    crear_usuario(nombre, nombre_usuario, email, contraseña)
                    print("  Usuario creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan datos.")
        elif op == "4":
            uid = input("ID usuario: ").strip()
            if not uid:
                continue
            nombre = input("Nombre (vacío=no cambiar): ").strip()
            email = input("Email (vacío=no cambiar): ").strip()
            try:
                kwargs = {}
                if nombre:
                    kwargs["nombre"] = nombre
                if email:
                    kwargs["email"] = email
                actualizar_usuario(uid, **kwargs)
                print("  Usuario actualizado.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            uid = input("ID usuario a eliminar: ").strip()
            if uid:
                try:
                    eliminar_usuario(uid)
                    print("  Usuario eliminado.")
                except Exception as e:
                    _err_conexion(e)


def menu_auto():
    while True:
        print("\n--- auto ---")
        print("1. Listar  2. Ver una  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_auto()
                if not items:
                    print("  No hay auto.")
                else:
                    for s in items:
                        print(f"  {s['auto_id']} | {s['marca']} | {s.get('modelo') | {s('precio')}  or '-'}")
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            sid = input("ID auto: ").strip()
            if sid:
                try:
                    print(obtener_auto(sid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            marca = input("marca: ").strip()
            if marca:
                try:
                    crear_auto(
                        marca,
                        input("modelo: ").strip(),
                        input(" tipo_auto: ").strip(),
                        input(" precio: ").strip() ,
                        input(" sucursal_id: ").strip() ,
                        input(" compra_id: ").strip() ,               
                    )
                    print("  Auto Creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Falta Marca.")
        elif op == "4":
            sid = input("ID Auto: ").strip()
            if not sid:
                continue
            marca = input("marca (vacío=no cambiar): ").strip()
            try:
                actualizar_auto(sid, marca=marca if marca else None)
                print(" marca actualizada.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            sid = input("ID auto a eliminar: ").strip()
            if sid:
                try:
                    eliminar_auto(sid)
                    print("  auto eliminada.")
                except Exception as e:
                    _err_conexion(e)


def menu_Cliente():
    while True:
        print("\n--- Clientes ---")
        print("1. Listar  2. Ver uno  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_cliente()
                if not items:
                    print("  No hay clientes")
                else:
                    for t in items:
                        print(f"  {t['clienet_id']} | {t['nombre']} | {t['email']} | {t['tipo_cliente']}")
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            tid = input("ID cliente: ").strip()
            if tid:
                try:
                    print(obtener_cliente(tid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            nombre = input(" Nommbre: ").strip()
            apellido = input(" Apellido: ").strip()
            telefono = input(" Telefono: ").strip()
            email = input(" Email: ").strip()
            direccion = input(" Direccion: ").strip()
            tipo_cliente = input(" Direccion: ").strip()
            if nombre and apellido and telefono and email and direccion and tipo_cliente:
                try:
                    crear_cliente(nombre, apellido,telefono,email,direccion,tipo_cliente)
                    print("  Cliente creado exitosamente")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan campos por llenar.")
        elif op == "4":
            tid = input("ID cliente: ").strip()
            if not tid:
                continue
            apellido = input("apellido (vacío=no cambiar): ").strip()
            nombre = input("Nombre (vacío=no cambiar): ").strip()
            try:
                actualizar_cliente(
                    tid, apellido= apellido or None, nombre=nombre or None
                )
                print("  Cliente actualizado.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            tid = input("ID cliente a eliminar: ").strip()
            if tid:
                try:
                    eliminar_cliente(tid)
                    print("  cliente eliminado.")
                except Exception as e:
                    _err_conexion(e)


def menu_compra():
    while True:
        print("\n--- Compra ---")
        print("1. Listar  2. Ver una  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_compra()
                if not items:
                    print("  No hay compras.")
                else:
                    for c in items:
                        print(
                            f"  {c['compra_id']} | {c['fecha']} | {c['precio']}"
                        )
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            cid = input("ID compra: ").strip()
            if cid:
                try:
                    print(obtener_compra(cid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            empleado = input("ID empleado : ").strip()
            precio = input("precio: ").strip()

            if  precio and empleado :
                try:
                    crear_compra( precio,empleado)
                    print("  compra creada.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan datos.")
        elif op == "4":
            cid = input("ID Compra: ").strip()
            if not cid:
                continue
            Precio = input("Nuevo Precio (vacío=no cambiar): ").strip()
            empleado = input("Nuevo Empleado (vacío=no cambiar): ").strip()
            try:
                actualizar_compra(Precio, empleado_id=empleado if empleado else None)
                print("  compra actualizada.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            cid = input("ID cuenta a eliminar: ").strip()
            if cid:
                try:
                    eliminar_compra(cid)
                    print("  compra eliminada.")
                except Exception as e:
                    _err_conexion(e)


def menu_detalle_venta():
    while True:
        print("\n--- detalle ventas ---")
        print("1. Listar  2. Ver uno  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_detalle_venta()
                if not items:
                    print("  No hay detalles de ventas.")
                else:
                    for t in items:
                        print(f"  {t['detalle_venta_id']}")
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            tid = input("ID detalle venta: ").strip()
            if tid:
                try:
                    print(obtener_detalle_venta(tid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            id = input("id Detalle venta: ").strip()
            if id :
                try:
                    crear_detalle_venta(id)
                    print("  detalle venta creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan campos" )
        elif op == "4":
            tid = input("ID detalle venta: ").strip()
            if not tid:
                continue
            venta_id = input("venta_id (vacío=no cambiar): ").strip()
            try:
                actualizar_detalle_venta(
                    tid, venta_id==venta_id or None
                )
                print("  detalle venta  actualizado.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            tid = input("ID detalle venta a eliminar: ").strip()
            if tid:
                try:
                    eliminar_detalle_venta(tid)
                    print("  detalle venta eliminado.")
                except Exception as e:
                    _err_conexion(e)


def menu_empleado():
    while True:
        print("\n--- Empleados ---")
        print("1. Listar  2. Ver una  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_empleado()
                if not items:
                    print("  No hay Empleados.")
                else:
                    for t in items:
                        print(
                            f"  {t['empleado_id']} | nombre={t['nombre']} | telefono={t['telefono']} "
                        )
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            tid = input("ID Empleado: ").strip()
            if tid:
                try:
                    print(obtener_empleado(tid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            nombre = input("nombre: ").strip()
            cargo = input("Cargo: ").strip()
            telefono = input("telefono: ").strip()
            salario = input("Salario: ").strip()
           
            if nombre and cargo and telefono and salario:
                try:
                    crear_empleado(nombre=nombre, cargo=cargo, telefono= telefono, salario=salario)
                    print("  empleado creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan campos por llenar")
        elif op == "4":
            tid = input("ID Empleado: ").strip()
            if not tid:
                continue
            Salario = input("Salario (vacío=no cambiar): ").strip()
            try:
                actualizar_empleado(tid, salario=salario if salario else None)
                print("  empleado actualizado.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            tid = input("ID Empleado a eliminar: ").strip()
            if tid:
                try:
                    eliminar_empleado(tid)
                    print("  Empleado eliminado.")
                except Exception as e:
                    _err_conexion(e)

def menu_mantenimiento():
    while True:
        print("\n--- Mantenimientos ---")
        print("1. Listar  2. Ver una  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_mantenimiento()
                if not items:
                    print("  No hay mantenimientos.")
                else:
                    for t in items:
                        print(
                            f"  {t['mantenimiento_id']} | costo={t['costo']} | tipo de servicio={t['tipo_servisio']} "
                        )
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            tid = input("ID Mantenimiento: ").strip()
            if tid:
                try:
                    print(obtener_mantenimiento(tid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            tipo_servicio = input("Tipo_servicio: ").strip()
            costo = input("costo: ").strip()
            auto = input("ID auto: ").strip()
            empleado = input("ID Empleado: ").strip()
           
            if tipo_servicio and costo and auto and empleado:
                try:
                    crear_mantenimiento(tipo_servicio=tipo_servicio, costo=costo, auto= auto, empleado=empleado)
                    print("  mantenimiento creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan campos por llenar")
        elif op == "4":
            tid = input("ID Mantenimiento: ").strip()
            if not tid:
                continue
            tipo_servicio = input("tipo servicio (vacío=no cambiar): ").strip()
            costo = input(" Nuevo costo (vacío=no cambiar): ").strip()
            auto = input(" ID auto (vacío=no cambiar): ").strip()
            empleado = input("ID Empleado  (vacío=no cambiar): ").strip()
            try:
                actualizar_mantenimiento(tid, tipo_servicio=tipo_servicio if tipo_servicio else None, costo=costo if costo else None, auto_id=auto if auto else None, id_empleado= empleado if empleado else None)
                print(" Mantenimiento actualizado.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            tid = input("ID Mantenimiento a eliminar: ").strip()
            if tid:
                try:
                    eliminar_mantenimiento(tid)
                    print("  Mantenimiento eliminado.")
                except Exception as e:
                    _err_conexion(e)

def menu_sucursal():
    while True:
        print("\n--- Sucursales ---")
        print("1. Listar  2. Ver una  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_sucursal()
                if not items:
                    print("  No hay sucursales.")
                else:
                    for t in items:
                        print(
                            f"  {t['sucursal_id']} | tipo Servicio={t['tipo_servicio']} | costo={t['costo']} | Empleado ={['id_empleado']} "
                        )
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            tid = input("ID sucursal: ").strip()
            if tid:
                try:
                    print(obtener_sucursal(tid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            nombre = input("nombre: ").strip()
            telefono = input("Telefono: ").strip()
            direccion = input("Direccion: ").strip()
            
           
            if nombre and direccion and telefono :
                try:
                    crear_sucursal(nombre=nombre, telefono= telefono, direccion=direccion)
                    print("  Sucursal creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan campos por llenar")
        elif op == "4":
            tid = input("ID Sucursal: ").strip()
            if not tid:
                continue
            nombre = input("nombre (vacío=no cambiar): ").strip()
            telefono = input("Telefono (vacío=no cambiar): ").strip()
            direccion = input("Direccion (vacío=no cambiar): ").strip()
            try:
                actualizar_sucursal(tid,nombre=nombre if nombre else None, telefono= telefono if telefono else None,direccion=direccion if direccion else None)
                print("  Sucursal actualizada.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            tid = input("ID Sucursal a eliminar: ").strip()
            if tid:
                try:
                    eliminar_sucursal(tid)
                    print("  Sucursal eliminada.")
                except Exception as e:
                    _err_conexion(e)

def menu_venta():
    while True:
        print("\n--- Ventas ---")
        print("1. Listar  2. Ver una  3. Crear  4. Actualizar  5. Eliminar  0. Volver")
        op = input("Opción: ").strip()
        if op == "0":
            break
        if op == "1":
            try:
                items = listar_venta()
                if not items:
                    print("  No hay Ventas.")
                else:
                    for t in items:
                        print(
                            f"  {t['venta_id']} | Cliente={t['cliente_id']} | empleado={t['empleado_id']} | Precio venta ={t['precio_venta']} "
                        )
            except Exception as e:
                _err_conexion(e)
        elif op == "2":
            tid = input("ID venta: ").strip()
            if tid:
                try:
                    print(obtener_venta(tid))
                except Exception as e:
                    _err_conexion(e)
        elif op == "3":
            precio_venta = input("precio_venta: ").strip()
            metodo_pago = input("Metodo De Pago: ").strip()
            cliente = input("ID Cliente: ").strip()
            empleado = input("ID Empleado: ").strip()
            
           
            if  precio_venta and metodo_pago and cliente and empleado :
                try:
                    crear_venta(precio_venta= precio_venta, metodo_pago= metodo_pago, cliente_id= cliente, empleado_id= empleado)
                    print("  venta creado.")
                except Exception as e:
                    _err_conexion(e)
            else:
                print("  Faltan campos por llenar")
        elif op == "4":
            tid = input("ID Venta: ").strip()
            if not tid:
                continue
            Precio_venta = input("Precio venta (vacío=no cambiar): ").strip()
            metodo_pago = input("Metodo Pago (vacío=no cambiar): ").strip()
            cliente = input("ID cliente (vacío=no cambiar): ").strip()
            empleado = input("ID Empleado (vacío=no cambiar): ").strip()
            try:
                actualizar_venta(tid, Precio_venta= Precio_venta if Precio_venta else None,metodo_pago=metodo_pago if metodo_pago else None,cliente_id=cliente if cliente else None,empleado_id=empleado if empleado else None  )
                print("  Venta actualizada.")
            except Exception as e:
                _err_conexion(e)
        elif op == "5":
            tid = input("ID Venta a eliminar: ").strip()
            if tid:
                try:
                    eliminar_venta(tid)
                    print("  Venta eliminada.")
                except Exception as e:
                    _err_conexion(e)

def _iniciar_api():
    import uvicorn

    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, log_level="warning")


def main():
    print("API Banco - Menú por consola")
    print("Iniciando API en http://localhost:8000 ...")
    server = threading.Thread(target=_iniciar_api, daemon=True)
    server.start()
    time.sleep(1.5)
    print("API lista.\n")
    while True:
        print("\n========== MENÚ BANCO ==========")
        print(
            "1. Usuarios  2. auto  3. Tipos cuenta  4. Cuentas  5. Tipos transacción  6. Transacciones  0. Salir"
        )
        op = input("Opción: ").strip()
        if op == "0":
            print("Hasta luego.")
            break
        if op == "1":
            menu_usuarios()
        elif op == "2":
            menu_auto()
        elif op == "3":
            menu_Cliente()
        elif op == "4":
            menu_compra()
        elif op == "5":
            menu_detalle_venta()
        elif op == "6":
            menu_empleado()
        elif op == "7":
            menu_mantenimiento()
        elif op == "8":
            menu_sucursal()
        elif op == "9":
            menu_venta()
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()