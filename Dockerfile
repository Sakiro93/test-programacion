FROM python:3.8-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Instalar libpq-dev y build-essential para psycopg2
RUN apt-get update && apt-get install -y libpq-dev build-essential

# Crear y activar el entorno virtual
RUN python -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Copiar el archivo requirements.txt e instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecuta la aplicación
EXPOSE 8000