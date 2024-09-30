import tkinter as tk
from tkinter import ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")  # Título de la ventana

        # Configuración de la ventana principal
        self.root.geometry("400x400")  # Tamaño de la ventana

        # Crear un frame para la entrada de nuevas tareas
        self.entry_frame = ttk.Frame(self.root)
        self.entry_frame.pack(pady=10)  # Añadir espacio vertical alrededor del frame

        # Campo de entrada para nueva tarea
        self.task_entry = ttk.Entry(self.entry_frame, width=30)  # Ancho del campo de entrada
        self.task_entry.pack(side=tk.LEFT, padx=10)  # Colocar el campo a la izquierda con margen horizontal
        self.task_entry.bind("<Return>", self.add_task)  # Asignar la tecla Enter para añadir tarea

        # Botón para añadir tarea
        self.add_button = ttk.Button(self.entry_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)  # Colocar el botón a la izquierda del campo de entrada

        # Crear un Treeview para mostrar tareas, con dos columnas: Tarea y Estado
        self.tree = ttk.Treeview(self.root, columns=("task", "status"), show="headings")
        self.tree.heading("task", text="Tarea")  # Encabezado para la columna de tareas
        self.tree.heading("status", text="Estado")  # Encabezado para la columna de estado
        self.tree.column("task", width=200)  # Ancho de la columna de tareas
        self.tree.column("status", width=100)  # Ancho de la columna de estado
        self.tree.pack(expand=True, fill=tk.BOTH, pady=10)  # Expandir y llenar el espacio disponible

        # Asignar eventos de teclas para el Treeview
        self.tree.bind("<Delete>", self.delete_task)   # Eliminar tarea con tecla Delete
        self.tree.bind("<d>", self.delete_task)        # Eliminar tarea con la tecla D
        self.tree.bind("<c>", self.complete_task)      # Completar tarea con la tecla C
        self.root.bind("<Escape>", self.exit_app)      # Salir de la aplicación con la tecla Escape

        # Crear un frame para botones de completar y eliminar tareas
        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.pack(pady=10)  # Añadir espacio vertical alrededor del frame de botones

        # Botón para completar tareas
        self.complete_button = ttk.Button(self.buttons_frame, text="Completar", command=self.complete_task)
        self.complete_button.pack(side=tk.LEFT, padx=5)  # Colocar el botón a la izquierda con margen horizontal

        # Botón para eliminar tareas
        self.delete_button = ttk.Button(self.buttons_frame, text="Eliminar", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)  # Colocar el botón a la izquierda con margen horizontal

    def add_task(self, event=None):
        task = self.task_entry.get()  # Obtener texto del campo de entrada
        if task:  # Comprobar que no está vacío
            # Añadir la tarea al Treeview como "Pendiente"
            self.tree.insert("", "end", values=(task, "Pendiente"))
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada después de añadir

    def complete_task(self, event=None):
        selected_item = self.tree.selection()  # Obtener elementos seleccionados
        for item in selected_item:
            # Obtener el valor de la tarea seleccionada
            task = self.tree.item(item, "values")[0]
            # Cambiar el estado de la tarea a "Completada"
            self.tree.item(item, values=(task, "Completada"))

    def delete_task(self, event=None):
        selected_item = self.tree.selection()  # Obtener elementos seleccionados
        for item in selected_item:
            self.tree.delete(item)  # Eliminar los elementos seleccionados del Treeview

    def exit_app(self, event=None):
        self.root.quit()  # Salir de la aplicación

if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    app = TaskManagerApp(root)  # Instanciar la aplicación
    root.mainloop()  # Iniciar el bucle de eventos
