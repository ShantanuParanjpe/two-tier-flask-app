FROM python:3.9-slim 

WORKDIR /app 

RUN apt-get update -y \
    && apt-get install -y gcc python3-dev default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt 

COPY . .
