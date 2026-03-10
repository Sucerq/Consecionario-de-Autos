# Concesionario de Autos API

Sistema integral para la gestión de un concesionario de vehículos. Permite administrar de forma centralizada el inventario de autos, clientes, empleados, sucursales, así como el flujo completo de compras, ventas y servicios de mantenimiento.

Cuenta con una sólida API RESTful desarrollada con **FastAPI** y una interfaz interactiva de línea de comandos (CLI) integrada para el manejo directo de la aplicación.

## Características Principales

- **API RESTful Rápida y Moderna**: Diseñada para alto rendimiento utilizando FastAPI y asincronía.
- **Base de Datos Relacional**: Integración nativa a través de SQLAlchemy y PostgreSQL (psycopg2).
- **Arquitectura Basada en Componentes**: Código estructurado por responsabilidades (Rutas, Esquemas, Modelos de Base de Datos y Lógica CRUD).
- **Consola Interactiva (CLI)**: Permite administrar operaciones básicas (Crear, Editar, Borrar, Leer).

## Estructura del Proyecto

```text
Consecionario-de-Autos/
├── main.py                 # Punto de entrada (CLI interactivo + arranque de Uvicorn)
├── __init_db__.py          # Script para inicializar tablas de base de datos
├── requirements.txt        # Dependencias principales del proyecto
├── .env                    # Variables de entorno (Configuración de DB, etc.)
│
└── src/
    ├── app.py              # Definición de la app FastAPI y carga de routers
    ├── crud/               # Lógica de manipulación de la BD (Capa de servicio)
    ├── database/           # Configuración de sesión y motor de conexión
    ├── endpoints/          # Controladores y definición de rutas de la API
    ├── entities/           # Modelos ORM (Entities/Tablas de SQLAlchemy)
    ├── schemas/            # Pydantic Models para serialización y validación de datos
    └── utils/              # Funciones auxiliares genéricas
```

## Requisitos y Versiones Técnicas

El proyecto está desarrollado y validado preferentemente con entornos modernos de Python. Las versiones principales utilizadas en el desarrollo son:

- **Python**: 3.9+
- **FastAPI**: 0.104.1
- **Uvicorn**: 0.24.0 (con [standard] para asincronía)
- **SQLAlchemy**: 2.0.23 (Base de datos y ORM)
- **Pydantic**: 2.5.0 (Validaciones y schemas, incluyendo soporte para email validation)
- **Psycopg2**: 2.9.9 (Adaptador para PostgreSQL)
- **Bcrypt**: >=4.0.1 (Hasheo de credenciales)
- **Httpx**: 0.25.0

## Instalación y Configuración

Sigue estos pasos para desplegar el entorno de desarrollo localmente:

1. **Clonar el repositorio y ubicarse en el directorio raíz**
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Consecionario-de-Autos
   ```

2. **Crear y activar un entorno virtual aislable**
   ```bash
   # En Windows:
   python -m venv venv
   venv\Scripts\activate
   
   # En macOS/Linux:
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias del proyecto**
   ```bash
   pip install -r requirements.txt
   ```

4. **Variables de Entorno**
   - Asegúrate de tener o crear un archivo `.env` en la raíz del proyecto.
   - Debe contener las cadenas de conexión (DB_URL, credenciales, secret keys) necesarias para ejecutar la app.

5. **Inicializar la Base de Datos** (Creación de tablas referenciales)
   ```bash
   python __init_db__.py
   ```

## Ejecución del Sistema

El proyecto dispone del archivo `main.py` que inicia tanto el servidor de la API como la consola interactiva integrada.

```bash
python main.py
```

Una vez ejecutado:
- El servidor **FastAPI** quedará disponible levantado en segundo plano en: `http://localhost:8000`
- La **Documentación Interactiva Automática** (Swagger UI) está accesible en: `http://localhost:8000/docs`
- La ventana de tu consola se convertirá en un **Menú Interactivo** para manejar las entidades CRUD.

## Módulos y Entidades de la API

La API cuenta con endpoints específicos para administrar:
- `/autos/`: Registro de inventario y estado.
- `/clientes/`: Control de compradores potenciales y compradores finales.
- `/compras/` y `/ventas/` (con `detalle_ventas`): Motor de transacciones comerciales.
- `/empleados/`: Personal y su asignación.
- `/mantenimientos/`: Servicios de postventa.
- `/sucursales/`: Ubicaciones físicas operativas del concesionario.
- `/usuarios/`: Gestión de inicio de sesión y perfiles de sistema.
