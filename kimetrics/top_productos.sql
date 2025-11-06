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