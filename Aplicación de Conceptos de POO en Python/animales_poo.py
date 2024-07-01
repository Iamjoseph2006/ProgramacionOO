# Definición de la clase base (Clase Padre)
class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad  # Atributo encapsulado

    def sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases hijas")

    def descripcion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}"


# Definición de la clase derivada (Clase Hija) que hereda de Animal
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    # Sobrescribir el método sonido (Polimorfismo)
    def sonido(self):
        return "Guau"

    # Sobrescribir el método descripción para agregar más detalles
    def descripcion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Raza: {self.raza}"


class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    # Sobrescribir el método sonido (Polimorfismo)
    def sonido(self):
        return "Miau"

    # Sobrescribir el método descripción para agregar más detalles
    def descripcion(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Color: {self.color}"


# Crear instancias de las clases y demostrar la funcionalidad
perro1 = Perro("Fido", 5, "Labrador")
gato1 = Gato("Whiskers", 3, "Negro")

print(perro1.descripcion())  # Nombre: Fido, Edad: 5, Raza: Labrador
print(perro1.sonido())  # Guau

print(gato1.descripcion())  # Nombre: Whiskers, Edad: 3, Color: Negro
print(gato1.sonido())  # Miau
