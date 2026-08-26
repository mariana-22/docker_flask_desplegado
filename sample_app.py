import os

from flask import Flask

import pymysql

sample = Flask(__name__)


@sample.route("/")
def home():

    try:
        # Se leen las credenciales desde variables de entorno
        db_host = os.getenv("DB_HOST", "servidor-bd-082")
        db_user = os.getenv("DB_USER", "root")
        db_password = os.getenv("DB_PASSWORD", "")
        db_name = os.getenv("DB_NAME", "082_db")

        conn = pymysql.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        conn.close()

        db_status = "Conexión exitosa a la base de datos prueba para CI, CD para despliegue continuo"

    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"

    # FALLO INTENCIONAL PARA EL EJERCICIO
    return f"<h1>Error intencional</h1><p>{db_status}</p>", 500


if __name__ == "__main__":
    # FALLO INTENCIONAL PARA BANDIT
    sample.run(
        host="127.0.0.1",
        port=5050,
        debug=False
    )