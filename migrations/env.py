from logging.config import fileConfig
import os

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Importar configuración de base de datos y modelos
# Esto asegura que los metadatos de las entidades se registren antes de correr migraciones
from src.database.config import Base, DATABASE_URL

# Cargar todas las entidades para que Base.metadata las detecte
import src.entities.autos
import src.entities.clientes
import src.entities.compra
import src.entities.detalle_venta
import src.entities.empleado
import src.entities.mantenimiento
import src.entities.sucursal
import src.entities.usuario
import src.entities.venta

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = DATABASE_URL or config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # Inyectar url desde variables de entorno para que Github Actions o Neon la tome correctamente
    configuration = config.get_section(config.config_ini_section)
    if configuration is not None:
        configuration["sqlalchemy.url"] = DATABASE_URL or configuration.get("sqlalchemy.url")
        
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
