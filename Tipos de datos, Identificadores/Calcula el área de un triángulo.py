# Programa para calcular el área de un triángulo
# Este programa solicita la base y la altura de un triángulo al usuario,
# calcula el área y muestra el resultado. Utiliza diferentes tipos de datos
# y sigue la convención snake_case para identificadores.

def calcular_area_triangulo(base, altura):
    """
    Función que calcula el área de un triángulo.
    :param base: float, la base del triángulo
    :param altura: float, la altura del triángulo
    :return: float, el área del triángulo
    """
    return (base * altura) / 2

def es_numero_valido(numero):
    """
    Función que verifica si un valor ingresado es un número válido.
    :param numero: str, el valor ingresado
    :return: bool, True si es un número válido, False en caso contrario
    """
    try:
        float(numero)
        return True
    except ValueError:
        return False

# Solicitar la base del triángulo al usuario
base_str = input("Ingrese la base del triángulo: ")

# Verificar si la base ingresada es un número válido
if es_numero_valido(base_str):
    base = float(base_str)
else:
    print("La base ingresada no es un número válido.")
    exit()

# Solicitar la altura del triángulo al usuario
altura_str = input("Ingrese la altura del triángulo: ")

# Verificar si la altura ingresada es un número válido
if es_numero_valido(altura_str):
    altura = float(altura_str)
else:
    print("La altura ingresada no es un número válido.")
    exit()

# Calcular el área del triángulo
area_triangulo = calcular_area_triangulo(base, altura)

# Mostrar el resultado
print(f"El área del triángulo con base {base} y altura {altura} es {area_triangulo}.")
