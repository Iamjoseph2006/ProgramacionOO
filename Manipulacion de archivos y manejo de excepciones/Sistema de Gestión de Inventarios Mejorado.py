import os

# La clase Producto representa un producto en el inventario con atributos únicos para su identificación.
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # Identificador único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible del producto
        self.precio = round(precio, 2)  # Precio del producto, redondeado a 2 decimales

    def __str__(self):
        # Representación en formato de cadena del producto
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"


# La clase Inventario gestiona una colección de productos y permite realizar varias operaciones sobre ellos.
class Inventario:
    def __init__(self, archivo_inventario):
        self.productos = {}  # Diccionario para almacenar los productos con su ID como clave
        self.archivo_inventario = archivo_inventario  # Nombre del archivo de inventario
        self.cargar_inventario()  # Cargar productos desde el archivo al iniciar el programa

    def cargar_inventario(self):
        """Carga los productos desde un archivo al iniciar el programa."""
        if os.path.exists(self.archivo_inventario):
            try:
                # Usando 'with' para abrir el archivo en modo lectura
                with open(self.archivo_inventario, 'r') as archivo:
                    for linea in archivo:
                        # Leer cada línea y crear un objeto Producto
                        id_producto, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(id_producto, nombre, int(cantidad), round(float(precio), 2))
                        self.productos[id_producto] = producto  # Añadir el producto al diccionario
                print("Inventario cargado exitosamente.")
            except FileNotFoundError:
                # Manejar el caso en que el archivo no se encuentra
                print(f"Archivo {self.archivo_inventario} no encontrado. Se creará un nuevo archivo.")
                self.crear_archivo()  # Crear archivo si no existe
            except PermissionError:
                # Manejar el caso en que no se tiene permiso para acceder al archivo
                print(f"Permiso denegado para acceder al archivo {self.archivo_inventario}.")
            except Exception as e:
                # Manejar otros posibles errores
                print(f"Error al cargar el inventario: {e}")
        else:
            self.crear_archivo()  # Crear archivo si no existe

    def crear_archivo(self):
        """Crea un archivo vacío si no existe para evitar errores posteriores."""
        try:
            # Usando 'with' para abrir el archivo en modo escritura (creándolo si no existe)
            with open(self.archivo_inventario, 'w') as archivo:
                pass  # Solo se crea el archivo vacío
            print(f"Archivo {self.archivo_inventario} creado exitosamente.")
        except PermissionError:
            # Manejar el caso en que no se tiene permiso para crear el archivo
            print(f"Permiso denegado para crear el archivo {self.archivo_inventario}.")
        except Exception as e:
            # Manejar otros posibles errores
            print(f"Error al crear el archivo de inventario: {e}")

    def guardar_inventario(self):
        """Guarda los productos en el archivo después de cualquier cambio."""
        try:
            # Usando 'with' para abrir el archivo en modo escritura
            with open(self.archivo_inventario, 'w') as archivo:
                for producto in self.productos.values():
                    # Escribir cada producto en el archivo con formato CSV
                    archivo.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio:.2f}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            # Manejar el caso en que no se tiene permiso para guardar el archivo
            print(f"Permiso denegado para guardar el archivo {self.archivo_inventario}.")
        except Exception as e:
            # Manejar otros posibles errores
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Añade un nuevo producto al inventario y guarda los cambios en el archivo."""
        if producto.id_producto in self.productos:
            print("Error: Producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto  # Añadir el producto al diccionario
            self.guardar_inventario()  # Guardar los cambios en el archivo

    def eliminar_producto(self, id_producto):
        """Elimina un producto del inventario y guarda los cambios en el archivo."""
        if id_producto in self.productos:
            del self.productos[id_producto]  # Eliminar el producto del diccionario
            self.guardar_inventario()  # Guardar los cambios en el archivo
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad y/o el precio de un producto y guarda los cambios en el archivo."""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = round(float(precio), 2)  # Redondear el precio a 2 decimales
            self.guardar_inventario()  # Guardar los cambios en el archivo
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre e imprime los que coinciden."""
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)  # Imprimir el producto que coincide con el nombre buscado
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)  # Imprimir todos los productos en el inventario


def menu():
    """Muestra un menú de opciones al usuario para gestionar el inventario."""
    inventario = Inventario('inventario.txt')  # Crear una instancia de Inventario
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break  # Salir del bucle y finalizar el programa
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            producto = Producto(id_producto, nombre, cantidad, precio)  # Crear un objeto Producto
            inventario.agregar_producto(producto)  # Agregar el producto al inventario
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)  # Eliminar el producto del inventario
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None  # Convertir a entero si no está vacío
            precio = float(precio) if precio else None  # Convertir a flotante si no está vacío
            inventario.actualizar_producto(id_producto, cantidad, precio)  # Actualizar el producto
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)  # Buscar el producto por nombre
        elif opcion == '5':
            inventario.mostrar_inventario()  # Mostrar todos los productos en el inventario
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")  # Mensaje para opción no válida


if __name__ == "__main__":
    menu()  # Ejecutar el menú si el script se ejecuta como programa principal
