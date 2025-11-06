--TRUNCATE TABLE detalle_venta;


INSERT INTO detalle_venta (
    detalle_id,
    venta_id,
    producto_id,
    cantidad,
    precio_unitario_venta,
    subtotal
)
SELECT
    -- 1. detalle_id: Usamos el número de serie como clave primaria
    t.detalle_id, 
    
    -- 2. venta_id: Aleatorio entre [1, 3000]
    t.venta_id,
    
    -- 3. producto_id: Aleatorio entre [1, 105]
    t.producto_id,
    
    -- 4. cantidad: Aleatorio entre [1, 10]
    t.cantidad,
    
    -- 5. precio_unitario_venta: Valor real traído de la tabla 'productos'
    p.precio_unitario AS precio_unitario_venta,
    
    -- 6. subtotal: Cálculo real (Cantidad * Precio del Producto)
    ROUND((t.cantidad * p.precio_unitario)::NUMERIC, 2) AS subtotal
    
FROM
    -- Subconsulta (o CTE) para generar las claves y la cantidad aleatoria
    (
        SELECT
            s.i AS detalle_id,
            FLOOR(RANDOM() * (3000 - 1 + 1) + 1)::INT AS venta_id,
            FLOOR(RANDOM() * (105 - 1 + 1) + 1)::INT AS producto_id,
            FLOOR(RANDOM() * (10 - 1 + 1) + 1)::INT AS cantidad
        FROM
            generate_series(1, 5000) AS s(i) -- Genera 5000 filas de datos de detalle
    ) AS t -- Alias para la tabla de detalles temporales
INNER JOIN 
    productos p ON t.producto_id = p.producto_id;
    -- AQUI es donde se trae el precio del producto