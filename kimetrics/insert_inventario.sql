INSERT INTO INVENTARIO (producto_id, talla, sucursal_id, stock_actual)
SELECT
    -- Producto_ID: Aleatorio entre 1 y 105
    (random() * 104 + 1)::int AS producto_id,
    
    -- Talla: Asigna una de las tallas comunes (S, M, L, XL)
    CASE (i % 4)
        WHEN 0 THEN 'S'
        WHEN 1 THEN 'M'
        WHEN 2 THEN 'L'
        ELSE 'XL'
    END AS talla,
    
    -- Sucursal_ID: Aleatorio entre 111 y 410
    (random() * 299 + 111)::int AS sucursal_id,
    
    -- Stock_Actual: Aleatorio entre 10 y 50
    (random() * 40 + 10)::int AS stock_actual
FROM 
    generate_series(1, 300) AS i
ON CONFLICT DO NOTHING;