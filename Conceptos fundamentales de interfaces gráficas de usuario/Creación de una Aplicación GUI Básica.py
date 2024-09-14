import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta cuando el usuario presiona el botón "Agregar"
def agregar_tarea():
    """
    Obtiene el texto del campo de entrada y lo agrega a la lista de tareas.
    Luego, limpia el campo de entrada.
    """
    tarea = entrada_tarea.get()  # Obtiene el texto de la entrada
    if tarea:  # Verifica que el campo no esté vacío
        lista_tareas.insert(tk.END, tarea)  # Inserta la tarea en la lista de tareas al final
        entrada_tarea.delete(0, tk.END)  # Limpia el campo de texto después de agregar la tarea
    else:
        # Muestra una advertencia si el campo de entrada está vacío
        messagebox.showwarning("Advertencia", "El campo de entrada está vacío.")

# Función que se ejecuta cuando el usuario presiona el botón "Limpiar"
def limpiar_lista():
    """
    Elimina todas las tareas de la lista.
    """
    lista_tareas.delete(0, tk.END)  # Elimina todos los elementos de la lista

# Crear la ventana principal
ventana = tk.Tk()  # Inicializa la ventana principal de tkinter
ventana.title("Gestor de Tareas")  # Título de la ventana
ventana.geometry("380x500")  # Tamaño de la ventana (ancho x alto)
ventana.configure(bg="#f0f0f0")  # Color de fondo gris claro

# Crear un marco para agrupar los componentes
marco = tk.Frame(ventana, bg="#ffffff", padx=10, pady=10)  # Frame con fondo blanco y margen interno
marco.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Empaca el frame dentro de la ventana principal con márgenes

# Etiqueta para el campo de entrada de tareas
etiqueta = tk.Label(marco, text="Ingrese una nueva tarea", font=("Arial", 14, "bold"), bg="#ffffff")
# Posiciona la etiqueta dentro del marco usando grid, abarcando dos columnas y con margen inferior
etiqueta.grid(row=0, column=0, columnspan=2, pady=(0, 10))

# Campo de texto para ingresar nuevas tareas con borde visible
entrada_tarea = tk.Entry(marco, width=25, font=("Arial", 12), bd=2, relief=tk.SOLID,
                         highlightbackground="#4CAF50", highlightcolor="#4CAF50")  # Campo de entrada con borde verde
entrada_tarea.grid(row=1, column=0, padx=(0, 10), pady=10)  # Posiciona el campo de entrada con margen a la derecha

# Botón para agregar una tarea
boton_agregar = tk.Button(marco, text="Agregar", command=agregar_tarea, font=("Arial", 12),
                          bg="#4CAF50", fg="#ffffff", relief=tk.RAISED)  # Botón verde para agregar una tarea
boton_agregar.grid(row=1, column=1, pady=10)  # Posiciona el botón a la derecha del campo de entrada

# Crear un marco para la lista con borde negro
marco_lista = tk.Frame(marco, bg="#000000", bd=2, relief=tk.SOLID)  # Frame negro con borde sólido para contener la lista
marco_lista.grid(row=2, column=0, columnspan=2, pady=(10, 10))  # Posiciona el frame de la lista con márgenes

# Lista para mostrar las tareas agregadas dentro del marco negro
lista_tareas = tk.Listbox(marco_lista, width=35, height=15, font=("Arial", 12),
                          bg="#ffffff", bd=0, highlightthickness=0)  # Lista blanca para mostrar las tareas
lista_tareas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)  # Empaca la lista dentro del marco de manera expansiva

# Botón para limpiar la lista de tareas
boton_limpiar = tk.Button(marco, text="Limpiar", command=limpiar_lista, font=("Arial", 12),
                          bg="#f44336", fg="#ffffff", relief=tk.RAISED)  # Botón rojo para limpiar la lista
boton_limpiar.grid(row=3, column=0, columnspan=2, pady=(10, 0))  # Posiciona el botón al final del marco

# Iniciar el bucle principal de la aplicación
ventana.mainloop()  # Lanza el bucle principal de la interfaz gráfica





