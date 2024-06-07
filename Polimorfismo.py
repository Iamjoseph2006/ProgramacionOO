class Bird:
    def make_sound(self):
        return "Chirp"

class Duck(Bird):
    def make_sound(self):
        return "Quack"

class Chicken(Bird):
    def make_sound(self):
        return "Cluck"

# Uso
birds = [Duck(), Chicken()]
for bird in birds:
    print(bird.make_sound())
