import uvicorn

from src.app import app  # IMPORTA tu FastAPI app correctamente


def main():
    uvicorn.run(
        "src.app:app",
        host="0.0.0.0",
        port=8000,
        reload=False,  # IMPORTANTE en producción
        log_level="info",
    )


if __name__ == "__main__":
    main()
