# Clase Producto para representar los artículos de la tienda
class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.stock = stock  # Cantidad disponible en stock

    def actualizar_stock(self, cantidad):
        self.stock += cantidad  # Actualiza el stock del producto

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Stock: {self.stock}"


# Clase Cliente para representar a los clientes de la tienda
class Cliente:
    def __init__(self, id_cliente, nombre, correo):
        self.id_cliente = id_cliente  # Identificador único del cliente
        self.nombre = nombre  # Nombre del cliente
        self.correo = correo  # Correo electrónico del cliente

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}"


# Clase Pedido para representar los pedidos realizados por los clientes
class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido  # Identificador único del pedido
        self.cliente = cliente  # Cliente que realizó el pedido
        self.productos = []  # Lista de productos en el pedido

    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.productos.append((producto, cantidad))  # Añade el producto al pedido
            producto.actualizar_stock(-cantidad)  # Reduce el stock del producto
        else:
            print(f"No hay suficiente stock de {producto.nombre} para agregar {cantidad} unidades.")

    def calcular_total(self):
        total = sum(producto.precio * cantidad for producto, cantidad in self.productos)  # Calcula el total del pedido
        return total

    def __str__(self):
        productos_pedido = "\n".join([f"{producto.nombre} (Cantidad: {cantidad})" for producto, cantidad in self.productos])
        return f"Pedido #{self.id_pedido} de {self.cliente.nombre}:\n{productos_pedido}\nTotal: ${self.calcular_total()}"


# Ejemplo de uso de las clases
if __name__ == "__main__":
    # Crear algunos productos
    producto1 = Producto(1, "Laptop", 1000, 10)
    producto2 = Producto(2, "Mouse", 25, 50)
    producto3 = Producto(3, "Teclado", 45, 30)

    # Crear un cliente
    cliente1 = Cliente(1, "José Hernández", "jose@example.com")

    # Crear un pedido para el cliente
    pedido1 = Pedido(1, cliente1)

    # Agregar productos al pedido
    pedido1.agregar_producto(producto1, 1)
    pedido1.agregar_producto(producto2, 2)
    pedido1.agregar_producto(producto3, 1)

    # Mostrar el pedido
    print(pedido1)
