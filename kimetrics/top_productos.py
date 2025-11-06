import pandas as pd
import matplotlib.pyplot as plt
import db_connector # Importamos nuestra función de conexión

def obtener_y_graficar_top_productos():
    conn = None
    
    # Consulta SQL que calcula el top 5 de productos vendidos
    sql_top_productos = """
  SELECT
    p.nombre,
	p.marca,
	p.precio_unitario,
    SUM(v.cantidad) AS total_vendido
    FROM
        detalle_venta v
    JOIN
        productos p ON v.producto_id = p.producto_id
    GROUP BY
        p.nombre,p.marca,p.precio_unitario
    ORDER BY
        total_vendido DESC
    LIMIT 10;
    """
    
    try:
        # 1. Obtener la conexión usando el módulo que creamos antes
        conn = db_connector.get_connection()
        
        print("\nEjecutando consulta para obtener el Top 5 de productos...")
        
        # 2. Usar Pandas para leer la consulta SQL directamente en un DataFrame
        df_top_productos = pd.read_sql(sql_top_productos, conn)
        
        print("\nDataFrame con el Top 5:")
        print(df_top_productos)
        
        # 3. Preparar y Generar el Gráfico de Barras
        
        # Separar los datos para el gráfico
        nombres = df_top_productos['nombre']
        cantidades = df_top_productos['total_vendido']
        
        plt.figure(figsize=(10, 6)) # Define el tamaño del gráfico
        
        # Crea el gráfico de barras. El .barh crea barras horizontales
        plt.barh(nombres, cantidades, color='#3498db') 
        
        # Configuraciones del gráfico
        plt.xlabel('Cantidad Total Vendida', fontsize=12)
        plt.ylabel('Producto', fontsize=12)
        plt.title('Top 5 Productos Más Vendidos', fontsize=14, fontweight='bold')
        plt.gca().invert_yaxis() # Invierte el eje Y para que el producto #1 quede arriba
        plt.tight_layout() # Ajusta el diseño para que no se corten las etiquetas
        
        # Mostrar los valores sobre las barras (opcional pero útil)
        for index, value in enumerate(cantidades):
            plt.text(value, index, f' {value}', va='center')
        
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
    obtener_y_graficar_top_productos()