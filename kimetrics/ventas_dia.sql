SELECT
    DATE(fecha_venta) AS dia,
    SUM(total_venta) AS total_vendido
FROM
    ventas
GROUP BY
    dia
ORDER BY
    dia DESC;