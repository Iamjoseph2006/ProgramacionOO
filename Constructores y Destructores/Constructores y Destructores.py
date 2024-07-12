class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Inicializa el atributo 'nombre' con el valor proporcionado
        self.edad = edad      # Inicializa el atributo 'edad' con el valor proporcionado
        print(f'Se ha creado a {self.nombre}')  # Imprime un mensaje al crear la instancia de Persona

    def __del__(self):
        print(f'Se está eliminando a {self.nombre}')  # Imprime un mensaje al eliminar la instancia de Persona

# Creación de objetos Persona
persona1 = Persona('Juan', 30)  # Crea una nueva instancia de Persona con nombre 'Juan' y edad '30'
persona2 = Persona('María', 25)  # Crea una nueva instancia de Persona con nombre 'María' y edad '25'

# Los destructores pueden ser llamados implícitamente por el recolector de basura
# Pero podemos simularlo con 'del' para mostrar su funcionamiento
del persona1  # Simula la eliminación de persona1
del persona2  # Simula la eliminación de persona2