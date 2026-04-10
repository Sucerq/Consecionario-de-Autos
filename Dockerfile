FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar requirements primero (para mejor cache)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# Puerto de la app
EXPOSE 8000

# Comando para ejecutar la app
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]