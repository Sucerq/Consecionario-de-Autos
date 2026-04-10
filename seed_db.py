"""
Seeder para Concesionario de Autos
Datos iniciales idempotentes para dev/QA/prod.
Compatible con GitHub Actions.

Uso:
  python seed_db.py
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# PYTHONPATH para imports locales + GitHub Actions
sys.path.insert(0, str(Path(__file__).resolve().parent))

# Cargar .env solo localmente
if "GITHUB_ACTIONS" not in os.environ:
    load_dotenv(Path(__file__).resolve().parent / ".env")

from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session

from src.database.config import SessionLocal

# IMPORTS DE TUS ENTIDADES (ajustados a tu proyecto)
from src.entities.sucursal import Sucursal
from src.entities.empleado import Empleado
from src.entities.clientes import Cliente  # Ajusta nombre si es clientes
from src.entities.autos import Auto
try:
    from src.entities.Usuario import Usuario
except ImportError:
    Usuario = None  # Si no existe

# Datos iniciales para CONCESIONARIO
SUCURSAL_PRINCIPAL = {
    "nombre": "Concesionario Central",
    "direccion": "Cra 50 # 75-100",
    "ciudad": "Medellín",
    "telefono": "+57 300 1234567",
}

EMPLEADO_ADMIN = {
    "nombre": "Admin Concesionario",
    "cedula": "12345678",
    "email": "admin@concesionario.com",
    "telefono": "+57 300 9876543",
    "cargo": "Gerente General",
}

CLIENTE_PRUEBA = {
    "nombre": "Juan Pérez",
    "cedula": "90012345",
    "email": "juan@prueba.com",
    "telefono": "+57 300 1112223",
}

AUTO_DEMO = {
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2024,
    "precio": 85000000,
    "kilometraje": 10,
    "estado": "Nuevo",
    "color": "Blanco",
    "vin": "JT2AE81B000123456",  # VIN único
}

def get_or_create_sucursal(db: Session) -> Sucursal:
    """Sucursal principal si no existe."""
    sucursal = db.query(Sucursal).filter(Sucursal.nombre == SUCURSAL_PRINCIPAL["nombre"]).first()
    if sucursal:
        print("   Sucursal ya existe")
        return sucursal
    
    sucursal = Sucursal(**SUCURSAL_PRINCIPAL)
    db.add(sucursal)
    db.commit()
    db.refresh(sucursal)
    print("   Sucursal creada:", sucursal.nombre)
    return sucursal

def get_or_create_empleado_admin(db: Session, sucursal_id: int) -> Empleado:
    """Empleado admin si no existe."""
    empleado = db.query(Empleado).filter(Empleado.cedula == EMPLEADO_ADMIN["cedula"]).first()
    if empleado:
        print("   Empleado admin ya existe")
        return empleado
    
    empleado = Empleado(
        **EMPLEADO_ADMIN,
        id_sucursal=sucursal_id
    )
    db.add(empleado)
    db.commit()
    db.refresh(empleado)
    print("   Empleado admin creado:", empleado.nombre)
    return empleado

def get_or_create_cliente_prueba(db: Session) -> Cliente:
    """Cliente de prueba si no existe."""
    cliente = db.query(Cliente).filter(Cliente.cedula == CLIENTE_PRUEBA["cedula"]).first()
    if cliente:
        print("   Cliente prueba ya existe")
        return cliente
    
    cliente = Cliente(**CLIENTE_PRUEBA)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    print("   Cliente prueba creado:", cliente.nombre)
    return cliente

def get_or_create_auto_demo(db: Session, sucursal_id: int) -> 'Auto':
    """Auto demo si no existe."""
    from src.entities.autos import Auto  # Import local
    auto = db.query(Auto).filter(Auto.vin == AUTO_DEMO["vin"]).first()
    if auto:
        print("   Auto demo ya existe")
        return auto
    
    auto = Auto(
        **AUTO_DEMO,
        id_sucursal=sucursal_id
    )
    db.add(auto)
    db.commit()
    db.refresh(auto)
    print("   Auto demo creado:", f"{auto.marca} {auto.modelo}")
    return auto

def main():
    """Función principal idempotente."""
    try:
        db: Session = SessionLocal()
        try:
            print("🌱 === SEED CONCESIONARIO ===")
            
            # 1. Sucursal principal
            sucursal = get_or_create_sucursal(db)
            
            # 2. Empleado admin
            empleado = get_or_create_empleado_admin(db, sucursal.id_sucursal)
            
            # 3. Cliente prueba
            cliente = get_or_create_cliente_prueba(db)
            
            # 4. Auto demo
            auto_demo = get_or_create_auto_demo(db, sucursal.id_sucursal)
            
            print(" === SEED COMPLETADO ===")
            print(f"   Sucursales: {sucursal.id_sucursal}")
            print(f"   Empleados: {empleado.id_empleado}")
            print(f"   Clientes: {cliente.id_cliente}")
            print(f"   Autos: {auto_demo.id_auto}")
            
        finally:
            db.close()
            
    except OperationalError as e:
        print(f"❌ Error BD: {e}")
        raise SystemExit(1)
    except Exception as e:
        print(f"❌ Error general: {e}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()