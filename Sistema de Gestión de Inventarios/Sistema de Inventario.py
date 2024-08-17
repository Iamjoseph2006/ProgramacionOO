# La clase Producto representa un producto en el inventario con atributos únicos para su identificación.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto: ID único, nombre, cantidad y precio.
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Método para representar el producto como una cadena, útil para mostrar información.
    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio}"


# La clase Inventario gestiona una colección de productos y permite realizar varias operaciones sobre ellos.
class Inventario:
    def __init__(self):
        # Se utiliza un diccionario para almacenar los productos, donde las claves son los ID únicos.
        self.productos = {}

    # Método para agregar un producto al inventario. Verifica que el ID sea único.
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")  # Mensaje de error si el producto ya está en el inventario.
        else:
            self.productos[producto.id_producto] = producto  # Añade el producto al diccionario.

    # Método para eliminar un producto del inventario por su ID.
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]  # Elimina el producto si el ID existe.
        else:
            print("Error: Producto no encontrado.")  # Mensaje de error si el producto no se encuentra.

    # Método para actualizar la cantidad y/o precio de un producto existente.
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            # Actualiza la cantidad si se proporciona un nuevo valor.
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            # Actualiza el precio si se proporciona un nuevo valor.
            if precio is not None:
                self.productos[id_producto].precio = precio
        else:
            print("Error: Producto no encontrado.")  # Mensaje de error si el producto no se encuentra.

    # Método para buscar productos por nombre. Permite buscar nombres parciales o similares.
    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            # Realiza la búsqueda ignorando mayúsculas y minúsculas.
            if nombre.lower() in producto.nombre.lower():
                print(producto)  # Muestra los productos que coinciden con la búsqueda.

    # Método para mostrar todos los productos en el inventario.
    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)  # Imprime cada producto en el inventario.


# Función que define la interfaz de usuario para interactuar con el sistema de inventario.
def menu():
    inventario = Inventario()  # Se crea una instancia del inventario.
    while True:
        # Muestra el menú interactivo en la consola.
        print(
            "\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        # Opción para salir del bucle y terminar el programa.
        if opcion == '6':
            break

        # Opción para agregar un nuevo producto.
        elif opcion == '1':
            # Solicita al usuario los detalles del nuevo producto.
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            # Crea una instancia de Producto con los detalles proporcionados.
            producto = Producto(id_producto, nombre, cantidad, precio)
            # Intenta agregar el producto al inventario.
            inventario.agregar_producto(producto)

        # Opción para eliminar un producto existente por su ID.
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        # Opción para actualizar la cantidad o el precio de un producto.
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            # Convertir a entero o float solo si se ingresa un valor, de lo contrario mantener como None.
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            # Actualiza el producto con los valores nuevos o mantiene los existentes.
            inventario.actualizar_producto(id_producto, cantidad, precio)

        # Opción para buscar un producto por nombre.
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        # Opción para mostrar todos los productos en el inventario.
        elif opcion == '5':
            inventario.mostrar_inventario()


# Punto de entrada al programa.
if __name__ == "__main__":
    menu()  # Ejecuta el menú interactivo.
