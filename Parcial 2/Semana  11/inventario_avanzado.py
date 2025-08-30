# -*- coding: utf-8 -*-
"""
Sistema Avanzado de Gestión de Inventarios
Autor: Leslye Valencia

Características:
- Usa POO (clases Producto e Inventario).
- Maneja colecciones: diccionario, lista, conjunto, tupla.
- Persiste los datos en archivo CSV (inventario.csv).
- Incluye un menú de consola para interactuar.
"""

import csv
import os

# ---------------------------
# Clase Producto
# ---------------------------
class Producto:
    def __init__(self, id_unico, nombre, cantidad, precio, categoria):
        # tupla para guardar datos básicos
        self.datos = (id_unico, nombre, cantidad, precio, categoria)

    def get_id(self):
        return self.datos[0]

    def get_nombre(self):
        return self.datos[1]

    def get_cantidad(self):
        return self.datos[2]

    def get_precio(self):
        return self.datos[3]

    def get_categoria(self):
        return self.datos[4]

    def set_cantidad(self, nueva_cantidad):
        self.datos = (self.get_id(), self.get_nombre(), nueva_cantidad, self.get_precio(), self.get_categoria())

    def set_precio(self, nuevo_precio):
        self.datos = (self.get_id(), self.get_nombre(), self.get_cantidad(), nuevo_precio, self.get_categoria())

    def __str__(self):
        return f"ID: {self.get_id()} | Nombre: {self.get_nombre()} | Cantidad: {self.get_cantidad()} | Precio: {self.get_precio():.2f} | Categoría: {self.get_categoria()}"


# ---------------------------
# Clase Inventario
# ---------------------------
class Inventario:
    def __init__(self, archivo="inventario.csv"):
        # Diccionario: clave = ID, valor = Producto
        self.productos = {}
        # Conjunto de categorías
        self.categorias = set()
        self.archivo = archivo
        self.cargar()

    # CRUD --------------------
    def agregar(self, producto):
        if producto.get_id() in self.productos:
            return False, "Error: ID duplicado."
        self.productos[producto.get_id()] = producto
        self.categorias.add(producto.get_categoria())
        self.guardar()
        return True, "Producto agregado."

    def eliminar(self, id_unico):
        if id_unico in self.productos:
            eliminado = self.productos.pop(id_unico)
            self.guardar()
            return True, f"Producto {eliminado.get_nombre()} eliminado."
        return False, "No existe ese producto."

    def actualizar_cantidad(self, id_unico, nueva_cantidad):
        if id_unico in self.productos:
            self.productos[id_unico].set_cantidad(nueva_cantidad)
            self.guardar()
            return True, "Cantidad actualizada."
        return False, "No existe ese producto."

    def actualizar_precio(self, id_unico, nuevo_precio):
        if id_unico in self.productos:
            self.productos[id_unico].set_precio(nuevo_precio)
            self.guardar()
            return True, "Precio actualizado."
        return False, "No existe ese producto."

    def buscar_nombre(self, nombre):
        # Lista de coincidencias
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        return list(self.productos.values())

    # -------------------------
    # Archivos
    # -------------------------
    def guardar(self):
        with open(self.archivo, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nombre", "cantidad", "precio", "categoria"])
            for p in self.productos.values():
                writer.writerow([p.get_id(), p.get_nombre(), p.get_cantidad(), p.get_precio(), p.get_categoria()])

    def cargar(self):
        if not os.path.exists(self.archivo):
            return
        with open(self.archivo, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader, None)  # saltar encabezado
            for fila in reader:
                if len(fila) == 5:
                    id_unico, nombre, cant, precio, categoria = fila
                    try:
                        cantidad = int(cant)
                        precio = float(precio)
                        prod = Producto(id_unico, nombre, cantidad, precio, categoria)
                        self.productos[id_unico] = prod
                        self.categorias.add(categoria)
                    except ValueError:
                        continue


# ---------------------------
# Menú de consola
# ---------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA AVANZADO DE INVENTARIO ===")
        print("1) Añadir producto")
        print("2) Eliminar producto")
        print("3) Actualizar cantidad")
        print("4) Actualizar precio")
        print("5) Buscar por nombre")
        print("6) Mostrar todos")
        print("7) Mostrar categorías")
        print("0) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            id_unico = input("ID: ").strip()
            nombre = input("Nombre: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
            except ValueError:
                print("Error: cantidad y precio deben ser numéricos.")
                continue
            categoria = input("Categoría: ").strip()
            prod = Producto(id_unico, nombre, cantidad, precio, categoria)
            ok, msg = inventario.agregar(prod)
            print(msg)

        elif opcion == "2":
            id_unico = input("ID a eliminar: ").strip()
            ok, msg = inventario.eliminar(id_unico)
            print(msg)

        elif opcion == "3":
            id_unico = input("ID: ").strip()
            try:
                nueva_cantidad = int(input("Nueva cantidad: "))
            except ValueError:
                print("Error: cantidad inválida.")
                continue
            ok, msg = inventario.actualizar_cantidad(id_unico, nueva_cantidad)
            print(msg)

        elif opcion == "4":
            id_unico = input("ID: ").strip()
            try:
                nuevo_precio = float(input("Nuevo precio: "))
            except ValueError:
                print("Error: precio inválido.")
                continue
            ok, msg = inventario.actualizar_precio(id_unico, nuevo_precio)
            print(msg)

        elif opcion == "5":
            nombre = input("Buscar: ").strip()
            resultados = inventario.buscar_nombre(nombre)
            if resultados:
                for p in resultados:
                    print("-", p)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "6":
            productos = inventario.mostrar_todos()
            if productos:
                for p in productos:
                    print("-", p)
            else:
                print("Inventario vacío.")

        elif opcion == "7":
            print("Categorías registradas:", inventario.categorias)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()
