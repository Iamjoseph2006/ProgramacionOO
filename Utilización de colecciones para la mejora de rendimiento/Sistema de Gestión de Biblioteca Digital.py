import json

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"

    def to_dict(self):
        # Convierte el objeto Libro en un diccionario para almacenar en JSON.
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'categoria': self.categoria,
            'isbn': self.isbn
        }

    @classmethod
    def from_dict(cls, data):
        # Crea un objeto Libro a partir de un diccionario.
        return cls(data['titulo'], data['autor'], data['categoria'], data['isbn'])

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if libro not in self.libros_prestados:
            self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Nombre: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}"

    def to_dict(self):
        # Convierte el objeto Usuario en un diccionario para almacenar en JSON.
        return {
            'nombre': self.nombre,
            'id_usuario': self.id_usuario,
            'libros_prestados': [libro.to_dict() for libro in self.libros_prestados]
        }

    @classmethod
    def from_dict(cls, data):
        # Crea un objeto Usuario a partir de un diccionario.
        usuario = cls(data['nombre'], data['id_usuario'])
        usuario.libros_prestados = [Libro.from_dict(libro) for libro in data['libros_prestados']]
        return usuario

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()
        self.cargar_datos()

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro '{libro.titulo}' añadido a la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado de la biblioteca.")
        else:
            print(f"No se encontró un libro con ISBN {isbn}.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado con ID {usuario.id_usuario}.")
        else:
            print(f"El ID de usuario {usuario.id_usuario} ya está en uso.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)
            print(f"Libro '{libro.titulo}' prestado a {usuario.nombre}.")
        else:
            print("Préstamo no realizado. Verifica el ID del usuario y el ISBN del libro.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.devolver_libro(libro)
            print(f"Libro '{libro.titulo}' devuelto por {usuario.nombre}.")
        else:
            print("Devolución no realizada. Verifica el ID del usuario y el ISBN del libro.")

    def buscar_libro(self, titulo=None, autor=None, categoria=None):
        resultados = []
        for libro in self.libros.values():
            if (titulo and titulo.lower() in libro.titulo.lower()) or \
               (autor and autor.lower() in libro.autor.lower()) or \
               (categoria and categoria.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def mostrar_resultados(self, resultados):
        if resultados:
            print("Resultados de la búsqueda:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con los criterios.")

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print(f"No se encontró un usuario con ID {id_usuario}.")

    def guardar_datos(self):
        # Guarda los datos de la biblioteca en un archivo JSON.
        data = {
            'libros': {isbn: libro.to_dict() for isbn, libro in self.libros.items()},
            'usuarios': {id_usuario: usuario.to_dict() for id_usuario, usuario in self.usuarios.items()},
            'ids_usuarios': list(self.ids_usuarios)
        }
        with open('datos_biblioteca.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Datos guardados exitosamente.")

    def cargar_datos(self):
        # Carga los datos de la biblioteca desde un archivo JSON.
        try:
            with open('datos_biblioteca.json', 'r') as f:
                data = json.load(f)
                self.libros = {isbn: Libro.from_dict(libro) for isbn, libro in data['libros'].items()}
                self.usuarios = {id_usuario: Usuario.from_dict(usuario) for id_usuario, usuario in data['usuarios'].items()}
                self.ids_usuarios = set(data['ids_usuarios'])
            print("Datos cargados exitosamente.")
        except FileNotFoundError:
            print("No se encontraron datos previos, se iniciará una nueva biblioteca.")

# Menú interactivo en la consola
def menu():
    biblioteca = Biblioteca()  # Crea una instancia de Biblioteca y carga los datos si existen.

    while True:
        # Muestra el menú de opciones al usuario.
        print("\n--- Menú de Biblioteca ---")
        print("1. Añadir libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libro")
        print("8. Listar libros prestados")
        print("9. Guardar y Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            # Opción para añadir un nuevo libro.
            titulo = input("Título del libro: ")
            autor = input("Autor del libro: ")
            categoria = input("Categoría del libro: ")
            isbn = input("ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.añadir_libro(libro)

        elif opcion == "2":
            # Opción para quitar un libro por ISBN.
            isbn = input("ISBN del libro a quitar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            # Opción para registrar un nuevo usuario.
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            # Opción para dar de baja a un usuario por ID.
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            # Opción para prestar un libro a un usuario.
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            # Opción para devolver un libro de un usuario.
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            # Opción para buscar libros por título, autor o categoría.
            criterio = input("Buscar por (1) Título, (2) Autor, (3) Categoría: ")
            if criterio == "1":
                titulo = input("Título: ")
                resultados = biblioteca.buscar_libro(titulo=titulo)
            elif criterio == "2":
                autor = input("Autor: ")
                resultados = biblioteca.buscar_libro(autor=autor)
            elif criterio == "3":
                categoria = input("Categoría: ")
                resultados = biblioteca.buscar_libro(categoria=categoria)
            else:
                print("Opción no válida.")
                continue
            biblioteca.mostrar_resultados(resultados)

        elif opcion == "8":
            # Opción para listar los libros prestados a un usuario.
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_prestados(id_usuario)

        elif opcion == "9":
            # Opción para guardar los datos y salir del sistema.
            biblioteca.guardar_datos()
            print("Saliendo del sistema de biblioteca.")
            break

        else:
            # Opción para manejar entradas no válidas.
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú
menu()




