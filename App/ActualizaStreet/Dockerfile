# toma la imagen base
FROM python:3.8.0-alpine

# cambia el directorio de trabajo
WORKDIR /usr/src/ActualizaStreet

# cambia variables ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# instala dependencias
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/ActualizaStreet/requirements.txt
RUN pip install -r requirements.txt

# copia el proyecto
COPY . /usr/src/ActualizaStreet/

