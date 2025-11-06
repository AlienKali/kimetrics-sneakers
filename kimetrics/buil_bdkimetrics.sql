--Tablas para clasificar y tener la ubicación
--Tabla CATEGORIAS-Clasificacion de productos
CREATE TABLE categorias(
	categoria_id INT PRIMARY KEY,
	nombre_categoria VARCHAR(50) NOT NULL
);

--Tabla sucursales-cadena de tiendas
CREATE TABLE sucursales(
    sucursal_id INT PRIMARY KEY,
    nombre_sucursal VARCHAR(100) NOT NULL,
    direccion VARCHAR(255),
    ciudad VARCHAR(100),
    telefono VARCHAR(15)
);

--Productos
CREATE TABLE productos(
    producto_id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    precio_unitario DECIMAL(10,2) NOT NULL,
    marca VARCHAR(50),
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(categoria_id)
);
--Clientes
CREATE TABLE clientes(
    cliente_id INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    telefono VARCHAR(15),
    direccion VARCHAR(100)
);

--Inventario
CREATE TABLE inventario(
    producto_id INT,
    talla VARCHAR(10) NOT NULL,
    sucursal_id INT,
    stock_actual INT NOT NULL CHECK (stock_actual >=0),--Validar que no sea negativo el stock
    PRIMARY KEY (producto_id,talla,sucursal_id),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id)
);

--ventas
CREATE TABLE ventas(
    venta_id INT PRIMARY KEY,----GENERATED
    cliente_id INT,
    sucursal_id INT,
    fecha_venta TIMESTAMP NOT NULL,
    total_venta DECIMAL(10,2) NOT NULL,
    forma_pago VARCHAR(50),
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id),
    FOREIGN KEY (sucursal_id) REFERENCES sucursales(sucursal_id)
);

---detalle de la venta
CREATE TABLE detalle_venta(
    detalle_id INT PRIMARY KEY,
    venta_id INT,
    producto_id INT,
    cantidad INT NOT NULL,
    precio_unitario_venta DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (venta_id) REFERENCES ventas(venta_id),
    FOREIGN KEY (producto_id) REFERENCES productos(producto_id)
);












