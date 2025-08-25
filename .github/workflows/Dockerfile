FROM python:3.12-slim

WORKDIR /app

COPY CalculadoraImc.py .
RUN pip install --no-cache-dir -r CalculadoraImc.py

COPY . .

CMD ["python", "app.py"]
