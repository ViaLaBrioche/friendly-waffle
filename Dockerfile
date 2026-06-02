FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    ca-certificates \
    apt-transport-https \
    chromium \
    chromium-driver \
    firefox-esr \
    socat \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs reports/allure

ENTRYPOINT ["sh", "-c", "socat TCP-LISTEN:8081,fork TCP:host.docker.internal:8081 & pytest \"$@\"", "--"]