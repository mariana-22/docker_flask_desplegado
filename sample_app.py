from flask import Flask
import pymysql
import os

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
        db_status = "Conexión exitosa a la base de datos prueba para C.I, CD para despliegue continuo"
    except Exception as e:
        db_status = f"Error al conectar a la base de datos: {e}"
        
    return f"<h1>Bienvenido a la aplicación Flask</h1><p>{db_status}</p>"

if __name__ == "__main__":
    # debug=False evita B201 y 127.0.0.1 evita B104 para desarrollo local
    sample.run(host="0.0.0.0", port=5050, debug=False)
