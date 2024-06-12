# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Semana tiene 7 días
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    total = sum(temperaturas)
    promedio = total / len(temperaturas)
    return promedio

# Función principal
def main():
    # Ingresar las temperaturas
    temperaturas = ingresar_temperaturas()
    # Calcular el promedio
    promedio_semanal = calcular_promedio(temperaturas)
    # Mostrar el promedio
    print(f"El promedio semanal de las temperaturas es: {promedio_semanal:.2f} °C")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
