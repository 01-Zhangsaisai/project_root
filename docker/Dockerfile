FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      libreoffice \
      djvulibre-bin \
      ghostscript && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python", "main.py"]
