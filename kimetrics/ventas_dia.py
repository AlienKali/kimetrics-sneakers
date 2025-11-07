import pandas as pd
import matplotlib.pyplot as plt
import db_connector # Importamos nuestra función de conexión

def obtener_y_graficar_ventas_diarias():
    conn = None
    
    # Consulta SQL para obtener la suma de ventas agrupada por día.
    sql_ventas_diarias = """
        SELECT
            DATE(fecha_venta) AS dia,
            SUM(total_venta) AS total_vendido
        FROM ventas
        GROUP BY
            dia
        ORDER BY
            dia DESC;;
    """
    
    try:
        # 1. Obtener la conexión
        conn = db_connector.get_connection()
        
        print("\nEjecutando consulta para obtener ventas por día...")
        
        # 2. Usar Pandas para leer la consulta SQL
        df_ventas_diarias = pd.read_sql(sql_ventas_diarias, conn)
        
        print("\nDataFrame con Ventas Diarias:")
        print(df_ventas_diarias.head())
        
        # --- 3. Preparar y Generar el Gráfico de Líneas ---
        
        # Convertir la columna 'dia' a tipo datetime (si no lo hizo Pandas automáticamente)
        df_ventas_diarias['dia'] = pd.to_datetime(df_ventas_diarias['dia'])
        
        plt.figure(figsize=(12, 6)) # Define el tamaño del gráfico
        
        # Crea el gráfico de líneas
        plt.plot(
            df_ventas_diarias['dia'], 
            df_ventas_diarias['total_vendido'], 
            marker='o', 
            linestyle='-', 
            color='#1abc9c'
        ) 
        
        # Configuraciones del gráfico
        plt.xlabel('Fecha', fontsize=12)
        plt.ylabel('Total de Unidades Vendidas', fontsize=12)
        plt.title('Tendencia de Ventas por Día', fontsize=14, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.xticks(rotation=45) # Rota las etiquetas del eje X para mejor lectura
        plt.tight_layout()
        
        # 4. Mostrar el gráfico
        plt.show()

    except Exception as e:
        print(f"\nSe produjo un error: {e}")
        
    finally:
        # 5. Cerrar la conexión
        if conn:
            conn.close()
            print("\nConexión a PostgreSQL cerrada.")

if __name__ == "__main__":
    obtener_y_graficar_ventas_diarias()