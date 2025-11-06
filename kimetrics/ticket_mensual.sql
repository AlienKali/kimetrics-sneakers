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