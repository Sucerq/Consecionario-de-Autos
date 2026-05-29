import logging

from sqlalchemy.orm import Session
from src.database.config import SessionLocal
from src.entities.usuario import Usuario

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def run_seeder():
    """
    Ejecuta la inserción de datos iniciales en la base de datos de manera idempotente.
    """
    logger.info("Iniciando proceso de Data Seeding...")
    db: Session = SessionLocal()
    try:
        # Seeder para Usuario Administrador por defecto
        admin_username = "admin"
        admin_email = "admin@concesionario.com"

        # Validar de forma idempotente que no exista
        existing_admin = (
            db.query(Usuario).filter(Usuario.nombre_usuario == admin_username).first()
        )

        if not existing_admin:
            nuevo_admin = Usuario(
                nombre="Administrador Principal",
                nombre_usuario=admin_username,
                email=admin_email,
                contraseña_hash="$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjIQG8N1zO",  # hash genérico de ejemplo p/ "admin123"
                telefono="000-000-0000",
                activo=True,
            )
            db.add(nuevo_admin)
            db.commit()
            logger.info("Usuario Administrador semilla integrado correctamente.")
        else:
            logger.info(
                "Usuario Administrador ya se encuentra presente en la base de datos (idempotencia cumplida)."
            )

        # Nota: Aquí pueden sumarse otras inserciones para 'Sucursales', 'Catalogos' de refacciones etc.

    except Exception as e:
        db.rollback()
        logger.error(f"Error crítico durante el Seeding de BD: {e}")
        raise
    finally:
        db.close()
        logger.info("Proceso de Data Seeding finalizado.")


if __name__ == "__main__":
    run_seeder()
