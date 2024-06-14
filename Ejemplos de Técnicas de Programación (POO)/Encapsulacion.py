class Person:
    def __init__(self, name, age):
        self.__name = name  # Atributo privado
        self.__age = age    # Atributo privado

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")

# Uso
person = Person("Alice", 30)
print(person.get_name())
person.set_age(31)
print(person.get_age())
