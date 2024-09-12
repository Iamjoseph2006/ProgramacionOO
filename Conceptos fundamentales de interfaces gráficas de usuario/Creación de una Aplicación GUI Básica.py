import tkinter as tk
from tkinter import messagebox

def agregar_tarea():
    """
    Obtiene el texto del campo de entrada y lo agrega a la lista de tareas.
    Luego, limpia el campo de entrada.
    """
    tarea = entrada_tarea.get()
    if tarea:  # Verifica que el campo no esté vacío
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de texto después de agregar la tarea
    else:
        messagebox.showwarning("Advertencia", "El campo de entrada está vacío.")  # Muestra una advertencia si el campo está vacío

def limpiar_lista():
    """
    Elimina todas las tareas de la lista.
    """
    lista_tareas.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Tareas")  # Título de la ventana
ventana.geometry("380x500")  # Tamaño de la ventana
ventana.configure(bg="#f0f0f0")  # Color de fondo gris claro

# Crear un marco para agrupar los componentes
marco = tk.Frame(ventana, bg="#ffffff", padx=10, pady=10)
marco.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Etiqueta para el campo de entrada de tareas
etiqueta = tk.Label(marco, text="Ingrese una nueva tarea", font=("Arial", 14, "bold"), bg="#ffffff")
etiqueta.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Campo de texto para ingresar nuevas tareas con borde visible
entrada_tarea = tk.Entry(marco, width=25, font=("Arial", 12), bd=2,
                relief=tk.SOLID, highlightbackground="#4CAF50", highlightcolor="#4CAF50")
entrada_tarea.grid(row=1, column=0, padx=(0, 10), pady=10)

# Botón para agregar una tarea
boton_agregar = tk.Button(marco, text="Agregar", command=agregar_tarea, font=("Arial", 12), bg="#4CAF50", fg="#ffffff", relief=tk.RAISED)
boton_agregar.grid(row=1, column=1, pady=10)

# Crear un marco para la lista con borde negro
marco_lista = tk.Frame(marco, bg="#000000", bd=2, relief=tk.SOLID)  # Marco negro con borde sólido
marco_lista.grid(row=2, column=0, columnspan=2, pady=(10, 10))

# Lista para mostrar las tareas agregadas dentro del marco negro
lista_tareas = tk.Listbox(marco_lista, width=35, height=15, font=("Arial", 12), bg="#ffffff", bd=0, highlightthickness=0)
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Botón para limpiar la lista de tareas
boton_limpiar = tk.Button(marco, text="Limpiar", command=limpiar_lista, font=("Arial", 12), bg="#f44336", fg="#ffffff", relief=tk.RAISED)
boton_limpiar.grid(row=3, column=0, columnspan=2, pady=(10, 0))

# Iniciar el bucle principal de la aplicación
ventana.mainloop()




