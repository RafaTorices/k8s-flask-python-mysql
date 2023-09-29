# Importamos las librerías necesarias
from flask import Flask
import mysql.connector
import os

# Definimos la aplicación flask
app = Flask(__name__)

mysql_host = os.environ['MYSQL_HOST']
mysql_user = os.environ['MYSQL_USER']
mysql_password = os.environ['MYSQL_PASSWORD']
mysql_database = os.environ['MYSQL_DATABASE']

# Función para incrementar el contador de visitas


def incrementar_visita():
    try:
        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO visitas (contador) VALUES (1)")
            conexion.commit()
            cursor.close()
            conexion.close()
    except mysql.connector.Error as error:
        print("Error: {}".format(error))

# Ruta para mostrar el contador de visitas en el navegador


@app.route('/')
def mostrar_contador():
    incrementar_visita()  # Incrementar el contador
    # Obtener el contador de visitas
    contador = obtener_contador()
    # Mostrar el contador de visitas en el navegador
    return f'Contador de visitas: {contador}'

# Función para obtener el contador de visitas


def obtener_contador():
    try:
        # Conexión a la base de datos MySQL
        conexion = mysql.connector.connect(
            host=mysql_host,
            user=mysql_user,
            password=mysql_password,
            database=mysql_database
        )
        if conexion.is_connected():
            cursor = conexion.cursor()
            cursor.execute("SELECT sum(contador) FROM visitas")
            resultado = cursor.fetchone()
            cursor.close()
            conexion.close()
            return resultado[0]
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 0


if __name__ == '__main__':
    app.run(debug=True)
