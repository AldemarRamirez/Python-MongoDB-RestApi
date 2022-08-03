# SO en el que se ejecutara nuestro sistema
FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

# Instalacion de los modulos en el contenedor
RUN pip3 --no-cache-dir install -r requirements.txt

# Ejecutar el sistema
CMD [ "python3", "src/app.py" ]