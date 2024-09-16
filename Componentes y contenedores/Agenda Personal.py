import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
import tkinter.messagebox as messagebox

# Función para agregar un evento a la lista
def agregar_evento():
    fecha = date_entry.get()  # Obtener la fecha del DateEntry
    hora = hour_combo.get() + ":" + minute_combo.get()  # Obtener la hora y minutos del Combobox
    descripcion = entry_descripcion.get()  # Obtener la descripción del Entry

    # Verificar si todos los campos están completos
    if not fecha or not hora or not descripcion:
        messagebox.showwarning("Campos incompletos", "Por favor, rellena todos los campos")
    else:
        # Insertar el evento en el TreeView
        tree.insert("", "end", values=(fecha, hora, descripcion))
        # Restablecer los valores de hora y minuto a los actuales
        hour_combo.set(current_hour)
        minute_combo.set(current_minute)
        # Limpiar el campo de descripción
        entry_descripcion.delete(0, tk.END)

# Función para eliminar el evento seleccionado del TreeView
def eliminar_evento():
    seleccionado = tree.selection()  # Obtener el evento seleccionado
    if seleccionado:
        # Confirmar la eliminación del evento
        confirmar = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar el evento seleccionado?")
        if confirmar:
            tree.delete(seleccionado)  # Eliminar el evento seleccionado
    else:
        messagebox.showwarning("Selección Vacía", "Por favor, selecciona un evento para eliminar")

# Función opcional para mostrar la fecha seleccionada
def mostrar_fecha():
    messagebox.showinfo("Fecha Seleccionada", f"Has seleccionado: {calendario.get()}")

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Agenda Personal")  # Título de la ventana
root.geometry("560x500")  # Tamaño de la ventana
root.configure(bg="#f5f5f5")  # Color de fondo de la ventana

# Crear un frame para organizar los widgets en la ventana principal
frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(padx=10, pady=15, fill="both", expand=True)

# Obtener la hora actual para establecer los valores predeterminados en los Combobox
now = datetime.now()
current_hour = now.strftime("%H")
current_minute = now.strftime("%M")

# Crear y ubicar las etiquetas y campos de entrada en el frame
tk.Label(frame, text="Fecha:", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5, sticky="w")
date_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Hora:", bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5, sticky="w")

# Combobox para seleccionar la hora (formato de 24 horas)
hour_combo = ttk.Combobox(frame, values=[f"{i:02}" for i in range(0, 24)], width=5)
hour_combo.set(current_hour)
hour_combo.grid(row=1, column=1, padx=5, pady=5, sticky="w")

# Combobox para seleccionar los minutos (de 00 a 59)
minute_combo = ttk.Combobox(frame, values=[f"{i:02}" for i in range(0, 60)], width=5)
minute_combo.set(current_minute)
minute_combo.grid(row=1, column=2, padx=5, pady=5, sticky="w")

tk.Label(frame, text="Descripción:", bg="#f5f5f5").grid(row=2, column=0, padx=5, pady=5, sticky="w")

# Entry para la descripción del evento (más largo)
entry_descripcion = tk.Entry(frame, width=50)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5, columnspan=3, sticky="ew")

# Crear y ubicar los botones con colores personalizados
boton_agregar = tk.Button(frame, text="Agregar Evento", command=agregar_evento, font=("Arial", 12),
                          bg="#4CAF50", fg="#ffffff", relief=tk.RAISED)
boton_agregar.grid(row=3, column=0, padx=5, pady=10, columnspan=2, sticky="ew")

boton_eliminar = tk.Button(frame, text="Eliminar Evento Seleccionado", command=eliminar_evento, font=("Arial", 12),
                           bg="#f44336", fg="#ffffff", relief=tk.RAISED)
boton_eliminar.grid(row=3, column=2, padx=5, pady=10, columnspan=2, sticky="ew")

boton_salir = tk.Button(frame, text="Salir", command=root.quit, font=("Arial", 12),
                       bg="#2196F3", fg="#ffffff", relief=tk.RAISED)
boton_salir.grid(row=3, column=4, padx=5, pady=10)

# Crear el TreeView para mostrar los eventos
tree = ttk.Treeview(frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.grid(row=4, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

# Configurar el tamaño de las columnas del TreeView
tree.column("Fecha", width=100, anchor="center")
tree.column("Hora", width=120, anchor="center")
tree.column("Descripción", width=300)

# Ajustar el tamaño de las filas para que el TreeView se expanda correctamente
frame.grid_rowconfigure(4, weight=1)

# Etiqueta final con el nombre de la aplicación
cal_label = tk.Label(frame, text="Agenda Personal de Jose", bg="#f5f5f5")
cal_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

# Ejecutar la aplicación
root.mainloop()

