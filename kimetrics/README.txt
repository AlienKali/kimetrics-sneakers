Para crear la base de datos bdkimetrics se requiere segir los siguientes pasos

1. Tener instalado pgAdmin 4 así tambien instalar las librerias python descritos en requirements.txt y como recomendacion activar
el entorno virtual de python kimetrics-env\Scripts\activate.
2. Crear la base de dados con el nombre bdkimetrics o utilizar el archivo create_db.py
3. Comenzar con la creacion de las tablas en orden con el archivo buil_bdkimetrics.sql
4. Poblar las tablas en orden
    insert_categorias.sql
    insert_sucursales.sql
    insert_productos.sql
    insert_clientes.sql
    insert_inventario.sql
    insert_ventas.sql
    insert_detalle_venta.sql
5. Una vez poblada bdkimetrics esta lista para su exploracion, y analisis.
6. Los archivos 
    ventas_dia.sql
    ventas_dia.py
    top_productos.sql
    top_productos.py
    ticket_mensual.sql
    ticket_mensual.py

    fueron desarrollados con la finalida de mostrar datos relevantes de nuestra base de datos
