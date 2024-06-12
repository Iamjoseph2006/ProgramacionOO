class Clima:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        for i in range(7):  # Semana tiene 7 días
            temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio

def main():
    # Crear una instancia de la clase Clima
    clima_semanal = Clima()
    # Ingresar las temperaturas
    clima_semanal.ingresar_temperaturas()
    # Calcular el promedio
    promedio_semanal = clima_semanal.calcular_promedio()
    # Mostrar el promedio
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f} °C")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
