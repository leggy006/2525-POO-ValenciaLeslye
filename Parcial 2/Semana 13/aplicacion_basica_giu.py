# -------------------------------------------
# Tarea: Aplicación GUI Básica con Tkinter
# Autor: Leslye Valencia
# -------------------------------------------

import tkinter as tk
from tkinter import messagebox

# -------------------------------------------
# Clase principal de la aplicación
# -------------------------------------------
class AplicacionGUI:
    def __init__(self, root):
        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestor de Datos - Leslye Valencia")  # título de la ventana
        self.root.geometry("400x400")  # tamaño fijo de la ventana

        # Etiqueta de bienvenida
        self.label_titulo = tk.Label(root, text="Aplicación Básica GUI", font=("Arial", 14))
        self.label_titulo.pack(pady=10)  # lo pongo arriba con un espacio

        # Campo de texto donde el usuario escribe datos
        self.entry_dato = tk.Entry(root, width=30)
        self.entry_dato.pack(pady=5)

        # Botón para agregar información
        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.btn_agregar.pack(pady=5)

        # Lista donde se muestran los datos agregados
        self.lista_datos = tk.Listbox(root, width=40, height=10)
        self.lista_datos.pack(pady=10)

        # Botón para limpiar datos
        self.btn_limpiar = tk.Button(root, text="Limpiar", command=self.limpiar_dato)
        self.btn_limpiar.pack(pady=5)

    # -------------------------------------------
    # Función: agregar dato a la lista
    # -------------------------------------------
    def agregar_dato(self):
        dato = self.entry_dato.get()  # obtener lo que escribió el usuario
        if dato.strip() == "":
            # si no escribió nada, mostramos un aviso
            messagebox.showwarning("Advertencia", "Debes ingresar un dato antes de agregar.")
        else:
            # agregamos el dato a la lista
            self.lista_datos.insert(tk.END, dato)
            # limpiamos el campo de texto para que quede listo
            self.entry_dato.delete(0, tk.END)

    # -------------------------------------------
    # Función: limpiar datos
    # -------------------------------------------
    def limpiar_dato(self):
        # Si hay un elemento seleccionado, solo borra ese
        seleccionado = self.lista_datos.curselection()
        if seleccionado:
            self.lista_datos.delete(seleccionado)
        else:
            # Si no hay selección, limpia toda la lista
            self.lista_datos.delete(0, tk.END)

# -------------------------------------------
# Bloque principal para ejecutar la app
# -------------------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
