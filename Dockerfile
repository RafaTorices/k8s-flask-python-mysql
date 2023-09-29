FROM python:3.10-alpine
RUN apk add gcc musl-dev linux-headers curl
WORKDIR /app
COPY ./code/* ./
RUN pip install -r requirements.txt
EXPOSE 5000
# Define las variables de entorno para la app Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000
ENV REDIS_HOST=redis
# Ejecuta la app Flask
CMD flask run
