import os

from flask import Flask

import pymysql

sample = Flask(__name__)


@sample.route("/")
def home():

    try:
        # Credenciales obtenidas desde variables de entorno
        db_host = os.getenv("DB_HOST")
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")

        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        conn.close()

        db_status = "Conexión exitosa a la base de datos prueba para CI/CD"

    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"

    return f"<h1>Bienvenido a la aplicación Flask</h1><p>{db_status}</p>"


if __name__ == "__main__":
    # Escuchar en 0.0.0.0 permite que Docker exponga la app correctamente
    sample.run(
        host="0.0.0.0",
        port=5050,
        debug=False
    )