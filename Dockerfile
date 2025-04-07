FROM python:3.10-slim

WORKDIR /app

COPY . .
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080", "--reload", "--log-level", "debug"]