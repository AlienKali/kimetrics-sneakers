import psycopg2
from psycopg2 import OperationalError

def get_connection():
    """
    Establece y devuelve una nueva conexión a la base de datos PostgreSQL.
    Lanza una excepción si la conexión falla.
    """
    # --- ¡IMPORTANTE! Reemplaza con tus datos de conexión ---
    db_params = {
        "host": "awsrds-kimetrics.c9gciya28sq3.us-east-2.rds.amazonaws.com",
        "database": "bdkimetrics",
        "user": "postgres",
        "password": "kimetrics123",
        "port": "5432"
    }
    # -------------------------------------------------------

    conn = None
    try:
        conn = psycopg2.connect(**db_params)
        print("✅ Conexión a PostgreSQL establecida.")
        return conn
    except OperationalError as e:
        print(f"❌ Error de Conexión: No se pudo conectar a la base de datos.")
        print(f"Detalle: {e}")
        # Relanzamos la excepción para que el script llamador la maneje
        raise

# Opcional: Pequeña prueba para verificar la conexión si ejecutas este archivo directamente
if __name__ == "__main__":
    try:
        test_conn = get_connection()
        if test_conn:
            print("Prueba exitosa. Cerrando conexión de prueba.")
            test_conn.close()
    except OperationalError:
        print("La conexión falló. Revisa tus parámetros.")