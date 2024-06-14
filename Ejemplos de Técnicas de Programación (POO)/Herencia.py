class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        return f"Driving {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def drive(self):
        return f"Driving a car: {self.brand} {self.model} with {self.doors} doors"

# Uso
my_car = Car("Toyota", "Corolla", 4)
print(my_car.drive())
