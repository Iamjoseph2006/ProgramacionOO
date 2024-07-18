import os
import subprocess

def ejecutar_script(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        subprocess.run(["python", ruta_script_absoluta], check=True)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el archivo: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Aplicación de Conceptos de POO en Python/animales_poo.py',
        '2': 'Comparación de Programación Tradicional y POO/Programación Orientada a Objetos (POO).py',
        '3': 'Comparación de Programación Tradicional y POO/Programación Tradicional.py',
        '4': 'Constructores y Destructores/Constructores y Destructores.py',
        '5': 'Ejemplos de Técnicas de Programación (POO)/EjemplosMundoReal_POO.py',
        '6': 'Organización de un proyecto orientado a objetos',
        '7': 'Tipos de datos, Identificadores',
        '8': 'Dashboard.py'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ejecutar o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            ejecutar_script(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()


