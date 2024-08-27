import os
import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Inicializa los atributos del producto
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = round(precio, 2)  # Redondea el precio a dos decimales

    def __str__(self):
        # Representación en cadena del producto para impresión
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

    def to_dict(self):
        """Convierte el producto a un diccionario."""
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'cantidad': self.cantidad,
            'precio': self.precio
        }

    @classmethod
    def from_dict(cls, data):
        """Crea una instancia de Producto a partir de un diccionario."""
        return cls(
            id_producto=data['id_producto'],
            nombre=data['nombre'],
            cantidad=data['cantidad'],
            precio=data['precio']
        )

class Inventario:
    def __init__(self, archivo_inventario='inventario.json'):
        """Inicializa el inventario y carga los productos desde un archivo JSON."""
        self.productos = {}  # Diccionario para almacenar productos
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga el inventario desde un archivo JSON, o crea uno nuevo si no existe."""
        if os.path.exists(self.archivo_inventario):
            try:
                with open(self.archivo_inventario, 'r') as archivo:
                    datos = json.load(archivo)
                    self.productos = {p['id_producto']: Producto.from_dict(p) for p in datos}
                print("Inventario cargado exitosamente.")
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error al cargar el inventario: {e}. Se creará un nuevo archivo.")
                self.crear_archivo()
            except PermissionError:
                print(f"Permiso denegado para acceder al archivo {self.archivo_inventario}.")
            except Exception as e:
                print(f"Error inesperado: {e}")
        else:
            self.crear_archivo()

    def crear_archivo(self):
        """Crea un archivo JSON vacío si no existe."""
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                json.dump([], archivo)
            print(f"Archivo {self.archivo_inventario} creado exitosamente.")
        except PermissionError:
            print(f"Permiso denegado para crear el archivo {self.archivo_inventario}.")
        except Exception as e:
            print(f"Error al crear el archivo de inventario: {e}")

    def guardar_inventario(self):
        """Guarda el inventario en un archivo JSON."""
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                datos = [p.to_dict() for p in self.productos.values()]
                json.dump(datos, archivo, indent=4)
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print(f"Permiso denegado para guardar el archivo {self.archivo_inventario}.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        """Añade nuevos productos al inventario."""
        if producto.id_producto in self.productos:
            print("Error: El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        """Elimina productos del inventario por ID."""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto por ID."""
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = round(float(precio), 2)
            self.guardar_inventario()
            print(f"Producto con ID {id_producto} actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca y muestra productos por nombre."""
        encontrado = False
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)
                encontrado = True
        if not encontrado:
            print("No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

def obtener_entero(prompt):
    """Obtiene un entero del usuario con manejo de errores."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Ingrese un número entero válido.")

def obtener_flotante(prompt):
    """Obtiene un flotante del usuario con manejo de errores."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Ingrese un número decimal válido.")

def menu():
    """Menú interactivo para gestionar el inventario."""
    inventario = Inventario()
    while True:
        print("\n1. Añadir Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '6':
            break
        elif opcion == '1':
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = obtener_entero("Ingrese la cantidad del producto: ")
            precio = obtener_flotante("Ingrese el precio del producto: ")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese la nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Ingrese el nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)
        elif opcion == '4':
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)
        elif opcion == '5':
            inventario.mostrar_inventario()
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()



