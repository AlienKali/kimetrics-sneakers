INSERT INTO ventas (
    venta_id,
    cliente_id,
    sucursal_id,
    fecha_venta,
    total_venta,
    forma_pago
)
SELECT 
    -- SUMA el máximo ID existente + el número de la serie (s.id)
    (SELECT COALESCE(MAX(venta_id), 0) FROM ventas) + s.id AS venta_id,
    
    -- clente_id: Rango 504 a 550
    FLOOR(RANDOM() * (550 - 504 + 1) + 504)::INT AS cliente_id,
    
    -- sucursal_id: Rango 111 a 410
    FLOOR(RANDOM() * (410 - 111 + 1) + 111)::INT AS sucursal_id,
    
    -- ... [El resto de la generación es igual] ...
    
    (
        '2025-01-01'::timestamp 
        + (FLOOR(RANDOM() * 365) || ' days')::interval 
        + (FLOOR(RANDOM() * 24) || ' hours')::interval
        + (FLOOR(RANDOM() * 60) || ' minutes')::interval
        + (FLOOR(RANDOM() * 60) || ' seconds')::interval
    ) AS fecha_venta,
    
    ROUND((RANDOM() * (5000 - 10) + 10)::NUMERIC, 2) AS total_venta,
    
    CASE FLOOR(RANDOM() * 3)
        WHEN 0 THEN 'Tarjeta'
        WHEN 1 THEN 'Efectivo'
        ELSE 'Transferencia'
    END AS forma_pago
FROM 
    GENERATE_SERIES(1, 1000) AS s(id);