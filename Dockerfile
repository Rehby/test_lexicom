# Используем образ Python
FROM python:3.9-slim

# Устанавливаем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Устанавливаем Redis
RUN apt-get update && apt-get install -y redis-server

# Копируем код приложения
COPY app /app

# Запускаем Redis
CMD ["redis-server"]

# Запускаем приложение FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
