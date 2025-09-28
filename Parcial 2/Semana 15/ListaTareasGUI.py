import tkinter as tk
from tkinter import messagebox

# Clase principal que maneja toda la aplicación de lista de tareas
class ListaDeTareas:
    def __init__(self, ventana):
        # Ventana principal
        self.ventana = ventana
        self.ventana.title("Mi Lista de Tareas")
        self.ventana.geometry("420x450")
        self.ventana.config(bg="#ECEDEB")  # Fondo gris claro

        # Colores
        self.color1 = "#0A2E57"  # Azul marino (botón eliminar)
        self.color2 = "#145374"  # Azul intermedio (botón agregar)
        self.color3 = "#0C7B93"  # Verde azulado (botón completar)
        self.color4 = "#ECEDEB"  # Gris claro (fondo)

        # Para ir guardando las tareas que agregue
        self.tareas = []

        # Para escribir las tareas nuevas
        self.entrada = tk.Entry(self.ventana, width=38, font=("Segoe UI", 11))
        self.entrada.pack(pady=10)
        # Si presiona Enter, también se agrega la tarea
        self.entrada.bind("<Return>", self.agregar_tarea)

        # Botón para añadir una tarea
        btn_agregar = tk.Button(self.ventana, text="➕ Añadir Tarea", command=self.agregar_tarea,
                                bg=self.color2, fg="white", activebackground=self.color1,
                                font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=5)
        btn_agregar.pack(pady=5)

        # Botón para marcar una tarea como completada
        btn_completar = tk.Button(self.ventana, text="✔ Marcar como Completada", command=self.marcar_completada,
                                  bg=self.color3, fg="white", activebackground=self.color1,
                                  font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=5)
        btn_completar.pack(pady=5)

        # Botón para eliminar una tarea
        btn_eliminar = tk.Button(self.ventana, text="🗑 Eliminar Tarea", command=self.eliminar_tarea,
                                 bg=self.color1, fg="white", activebackground=self.color2,
                                 font=("Segoe UI", 10, "bold"), relief="flat", padx=10, pady=5)
        btn_eliminar.pack(pady=5)

        # Lista donde se van a mostrar las tareas
        self.lista = tk.Listbox(self.ventana, width=50, height=15, font=("Segoe UI", 10), bd=0,
                                highlightthickness=0, selectbackground=self.color2, activestyle="none")
        self.lista.pack(pady=15)
        # Si hace doble clic en una tarea, también se marca como completada
        self.lista.bind("<Double-1>", self.marcar_completada)

    # Función para añadir tarea
    def agregar_tarea(self, event=None):
        tarea = self.entrada.get().strip()
        if tarea != "":
            self.lista.insert(tk.END, tarea)   # Se pone en la lista
            self.tareas.append(tarea)          # Se guarda en memoria
            self.entrada.delete(0, tk.END)     # Limpia el cuadro de texto
        else:
            messagebox.showwarning("Entrada vacía", "Por favor escribe una tarea.")

    # Función para marcar una tarea como completada
    def marcar_completada(self, event=None):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            tarea = self.lista.get(index)

            # Si ya está marcada, se avisa al usuario
            if tarea.startswith("[✔]"):
                messagebox.showinfo("Información", "La tarea ya está completada.")
            else:
                # Modifica el texto y cambia el color para que se note que está terminada
                self.lista.delete(index)
                self.lista.insert(index, "[✔] " + tarea)
                self.lista.itemconfig(index, fg=self.color3, selectbackground=self.color3)
        else:
            messagebox.showwarning("Selección vacía", "Selecciona una tarea para marcarla.")

    # Función para eliminar tarea seleccionada
    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            index = seleccion[0]
            self.lista.delete(index)
            del self.tareas[index]
        else:
            messagebox.showwarning("Selección vacía", "Selecciona una tarea para eliminarla.")


# Programa principal (aquí arranca)
if __name__ == "__main__":
    ventana = tk.Tk()
    app = ListaDeTareas(ventana)
    ventana.mainloop()
