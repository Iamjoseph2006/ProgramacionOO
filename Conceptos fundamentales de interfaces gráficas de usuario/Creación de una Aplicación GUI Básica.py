import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_elemento():
    elemento = entrada.get()
    if elemento:  # Verifica que el campo de texto no esté vacío
        lista.insert(tk.END, elemento)
        entrada.delete(0, tk.END)  # Limpia el campo de texto después de agregar
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación Básica GUI")

# Crear y ubicar los componentes de la GUI
tk.Label(ventana, text="Ingrese un elemento:").pack(pady=5)

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_elemento)
boton_agregar.pack(pady=5)

lista = tk.Listbox(ventana)
lista.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
