FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Asegura permisos de ejecución
RUN chmod +x start_runner.sh

# Usa el script de ejecución como entrypoint (puedes comentar Streamlit si no lo usas aquí)
CMD ["./start_runner.sh"]
