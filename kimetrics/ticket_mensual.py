import pandas as pd
import db_connector # Importamos nuestra función de conexión
import matplotlib.pyplot as plt # Lo usaremos para el gráfico opcional

def calcular_y_graficar_ticket_promedio_mensual():
    conn = None
    
    # Consulta SQL para obtener ingresos y conteo de tickets por mes
    sql_ticket_mensual = """
    SELECT
        DATE_TRUNC('month', fecha_venta) AS mes,
        SUM(total_venta) AS total_ingresos,
        COUNT(DISTINCT venta_id) AS total_tickets
    FROM
        ventas
    GROUP BY
        mes
    ORDER BY
        mes desc;
    """
    
    try:
        # 1. Obtener la conexión
        conn = db_connector.get_connection()
        # 2. Leer la consulta SQL directamente en un DataFrame de Pandas
        df_mensual = pd.read_sql(sql_ticket_mensual, conn)
        # 3. Calcular el Ticket Promedio Mensual (Total Ingresos / Total Tickets)
        df_mensual['ticket_promedio'] = df_mensual['total_ingresos'] / df_mensual['total_tickets']
        # Opcional: Formatear la columna de promedio para mostrar solo dos decimales
        df_mensual['ticket_promedio_formato'] = df_mensual['ticket_promedio'].map('${:,.2f}'.format)
        
        print("\nResultados del Ticket Promedio Mensual:")
        print(df_mensual[['mes', 'total_ingresos', 'total_tickets', 'ticket_promedio_formato']])
        
        # --- 4. Generar el Gráfico de Líneas (Tendencia del Ticket Promedio) ---
        
        plt.figure(figsize=(10, 6)) 
        
        plt.plot(
            df_mensual['mes'], 
            df_mensual['ticket_promedio'], 
            marker='o', 
            linestyle='-', 
            color='#e74c3c'
        )
        
        plt.xlabel('Fecha (Mes)', fontsize=12)
        plt.ylabel('Ticket Promedio ($)', fontsize=12)
        plt.title('Ticket Promedio Mensual (Tendencia)', fontsize=14, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.xticks(rotation=45) 
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"\nSe produjo un error: {e}")
        
    finally:
        # 5. Cerrar la conexión
        if conn:
            conn.close()
            print("\nConexión a PostgreSQL cerrada.")

if __name__ == "__main__":
    calcular_y_graficar_ticket_promedio_mensual()