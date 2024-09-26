import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x450")
        self.root.config(bg="#f7f7f7")  # Establecer el color de fondo de la ventana

        # Crear la interfaz gráfica
        self.create_widgets()

    def create_widgets(self):
        # Frame principal para contener todos los elementos
        main_frame = tk.Frame(self.root, bg="#f7f7f7")
        main_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Instrucciones para el usuario
        instructions = tk.Label(main_frame, text="Ingresa una Nueva Tarea",
                                justify=tk.CENTER, font=('Arial', 12), bg="#f7f7f7")
        instructions.pack(pady=10)

        # Frame para el campo de entrada de tareas
        entry_frame = tk.Frame(main_frame, bg="#f7f7f7")
        entry_frame.pack(pady=5)

        # Campo de entrada de texto para nuevas tareas
        self.task_entry = tk.Entry(entry_frame, width=40, font=('Arial', 12))
        self.task_entry.grid(row=0, column=0, padx=5)
        self.task_entry.focus()  # Poner el foco en el campo de entrada al iniciar la aplicación

        # Botón para añadir tarea
        self.add_task_button = tk.Button(entry_frame, text="Añadir Tarea", command=self.add_task,
                                          bg="#4CAF50", fg="white", font=('Arial', 10, 'bold'))
        self.add_task_button.grid(row=0, column=1, padx=5)

        # Frame para los botones de acción
        button_frame = tk.Frame(main_frame, bg="#f7f7f7")
        button_frame.pack(pady=10)

        # Botón para marcar una tarea como completada
        self.complete_task_button = tk.Button(button_frame, text="Marcar como Completada",
                                               command=self.complete_task, bg="#2196F3", fg="white",
                                               font=('Arial', 10, 'bold'))
        self.complete_task_button.grid(row=0, column=0, padx=5)

        # Botón para eliminar tareas
        self.delete_task_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task,
                                             bg="#F44336", fg="white", font=('Arial', 10, 'bold'))
        self.delete_task_button.grid(row=0, column=1, padx=5)

        # Frame para la lista de tareas
        treeview_frame = tk.Frame(main_frame)
        treeview_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        # Treeview para mostrar las tareas
        self.treeview = ttk.Treeview(treeview_frame, columns=('Estado', 'Tareas'), show='headings', selectmode='browse', height=10)
        self.treeview.heading('Estado', text='Estado')  # Encabezado para el estado de la tarea
        self.treeview.heading('Tareas', text='Tareas')  # Encabezado para el nombre de la tarea
        self.treeview.column('Estado', anchor='center', width=100)  # Configuración de columna
        self.treeview.column('Tareas', anchor='center', width=300)  # Configuración de columna

        self.treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para el Treeview
        scrollbar = ttk.Scrollbar(treeview_frame, orient=tk.VERTICAL, command=self.treeview.yview)
        self.treeview.configure(yscroll=scrollbar.set)  # Conectar scrollbar con Treeview
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Eventos de teclas y mouse
        self.task_entry.bind('<Return>', self.add_task_event)  # Evento para agregar tarea con Enter
        self.root.bind('<Escape>', self.on_escape_pressed)  # Evento para cerrar la aplicación con Escape
        self.treeview.bind('<Double-1>', self.complete_task_double_click)  # Evento para completar tarea con doble clic
        self.root.bind('<Delete>', self.delete_task_event)  # Evento para eliminar tarea con la tecla Delete

    # Método para añadir tareas
    def add_task(self):
        task = self.task_entry.get()  # Obtener el texto del campo de entrada
        if task:
            # Insertar la tarea en el Treeview con estado inicial 'Pendiente'
            self.treeview.insert('', tk.END, values=('Pendiente', task))
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            # Mostrar advertencia si el campo está vacío
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea antes de agregarla.")

    # Evento para añadir tarea con la tecla Enter
    def add_task_event(self, event):
        self.add_task()  # Llamar al método para añadir tarea

    # Método para marcar una tarea como completada
    def complete_task(self):
        selected_item = self.treeview.selection()  # Obtener la tarea seleccionada
        if selected_item:
            task = self.treeview.item(selected_item, 'values')  # Obtener los valores de la tarea
            # Verificar si la tarea ya está marcada como completada
            if task[0] == "Pendiente":
                # Cambiar el estado a 'Completada' y cambiar su color
                self.treeview.item(selected_item, values=('Completada', task[1]))
                self.treeview.tag_configure('completed', foreground='gray')  # Cambiar el color del texto a gris
                self.treeview.item(selected_item, tags=('completed',))  # Aplicar etiqueta de completada
            else:
                messagebox.showinfo("Información", "Esta tarea ya está marcada como completada.")  # Mensaje si ya está completada
        else:
            # Mostrar advertencia si no hay tarea seleccionada
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    # Método para marcar tarea como completada con doble clic
    def complete_task_double_click(self, event):
        selected_item = self.treeview.selection()  # Obtener la tarea seleccionada
        if selected_item:
            self.complete_task()  # Llamar al método para completar la tarea

    # Método para eliminar tareas
    def delete_task(self):
        selected_item = self.treeview.selection()  # Obtener la tarea seleccionada
        if selected_item:
            self.treeview.delete(selected_item)  # Eliminar la tarea seleccionada
        else:
            # Mostrar advertencia si no hay tarea seleccionada
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    # Evento para eliminar tarea con la tecla Delete
    def delete_task_event(self, event):
        self.delete_task()  # Llamar al método para eliminar la tarea

    # Evento para cerrar la aplicación con la tecla Escape
    def on_escape_pressed(self, event):
        messagebox.showinfo("Salir", "La aplicación se cerrará.")  # Mensaje de advertencia
        self.root.destroy()  # Cerrar la ventana

# Crear la ventana principal
root = tk.Tk()
app = TaskApp(root)  # Instanciar la clase TaskApp
root.mainloop()  # Iniciar el bucle principal de la GUI
