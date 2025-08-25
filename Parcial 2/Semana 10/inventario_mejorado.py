# -*- coding: utf-8 -*-
"""
Sistema de Gestión de Inventarios (versión mejorada con archivos y manejo de excepciones)
Autor: Leslye Valencia
Descripción:
- Persiste los productos en un archivo de texto (inventario.txt) usando CSV.
- Carga automáticamente el inventario al iniciar el programa.
- Maneja excepciones comunes de archivos (FileNotFoundError, PermissionError).
- Tolera líneas corruptas en el archivo y las ignora con aviso.
- La interfaz de consola informa el éxito o fallo de cada operación de archivo.

Formato del archivo (inventario.txt):
id,nombre,cantidad,precio
P001,Leche,12,1.25
P002,Pan,20,0.30
...
"""

import csv
import os


# ---------------------------
# Clase Producto
# ---------------------------
class Producto:
    def __init__(self, id_unico, nombre, cantidad, precio):
        self.id = id_unico
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


# ---------------------------
# Clase Inventario (con archivo)
# ---------------------------
class Inventario:
    """
    Esta clase mantiene una lista en memoria y además la sincroniza con un archivo CSV.
    Cada operación que modifica el inventario intenta guardarse inmediatamente en el archivo.
    """
    def __init__(self, ruta_archivo="inventario.txt"):
        self.productos = []
        self.ruta_archivo = ruta_archivo
        ok, msg = self._cargar_desde_archivo()
        # Guardamos el estado del último mensaje de archivo para que el menú pueda mostrarlo si se desea
        self.ultimo_mensaje_archivo = msg

    # -----------------------
    # Métodos públicos CRUD
    # -----------------------
    def agregar(self, producto):
        """
        Agrega un producto verificando que el ID sea único.
        Retorna (ok: bool, msg: str)
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                return False, "Error: el ID ya existe en el inventario."

        self.productos.append(producto)
        ok, msg = self._guardar_a_archivo()
        if ok:
            return True, "Producto agregado y guardado en archivo correctamente."
        else:
            # Si falló el guardado, revertimos el cambio en memoria para mantener consistencia
            self.productos.pop()
            return False, f"Error guardando en archivo. Operación revertida. Detalle: {msg}"

    def eliminar(self, id_unico):
        """
        Elimina un producto por ID.
        Retorna (ok: bool, msg: str)
        """
        for p in self.productos:
            if p.get_id() == id_unico:
                self.productos.remove(p)
                ok, msg = self._guardar_a_archivo()
                if ok:
                    return True, "Producto eliminado y cambios guardados en archivo."
                else:
                    # Si falla guardado, intentamos revertir (re-agregar)
                    self.productos.append(p)
                    return False, f"Error guardando en archivo. Operación revertida. Detalle: {msg}"
        return False, "No se encontró el producto con ese ID."

    def actualizar_cantidad(self, id_unico, nueva_cantidad):
        """
        Actualiza la cantidad de un producto.
        Retorna (ok: bool, msg: str)
        """
        for p in self.productos:
            if p.get_id() == id_unico:
                anterior = p.get_cantidad()
                p.set_cantidad(nueva_cantidad)
                ok, msg = self._guardar_a_archivo()
                if ok:
                    return True, "Cantidad actualizada y guardada en archivo."
                else:
                    # revertir
                    p.set_cantidad(anterior)
                    return False, f"Error guardando en archivo. Operación revertida. Detalle: {msg}"
        return False, "No se encontró el producto con ese ID."

    def actualizar_precio(self, id_unico, nuevo_precio):
        """
        Actualiza el precio de un producto.
        Retorna (ok: bool, msg: str)
        """
        for p in self.productos:
            if p.get_id() == id_unico:
                anterior = p.get_precio()
                p.set_precio(nuevo_precio)
                ok, msg = self._guardar_a_archivo()
                if ok:
                    return True, "Precio actualizado y guardado en archivo."
                else:
                    # revertir
                    p.set_precio(anterior)
                    return False, f"Error guardando en archivo. Operación revertida. Detalle: {msg}"
        return False, "No se encontró el producto con ese ID."

    def buscar_nombre(self, nombre):
        """
        Devuelve una lista de productos cuyo nombre contenga el texto buscado (case-insensitive).
        """
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_todos(self):
        """
        Devuelve la lista completa de productos.
        """
        return self.productos

    # -----------------------
    # Persistencia en archivo
    # -----------------------
    def _cargar_desde_archivo(self):
        """
        Carga productos desde el archivo CSV (self.ruta_archivo).
        - Si el archivo no existe, lo crea con encabezado.
        - Si una línea está corrupta (campos faltantes, tipos inválidos), se omite y se informa.
        Retorna (ok: bool, msg: str)
        """
        # Si no existe, intentamos crearlo vacío con encabezado:
        if not os.path.exists(self.ruta_archivo):
            try:
                with open(self.ruta_archivo, mode="w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["id", "nombre", "cantidad", "precio"])
                return True, f"Archivo '{self.ruta_archivo}' creado (estaba ausente)."
            except PermissionError:
                return False, (f"Sin permisos para crear '{self.ruta_archivo}'. "
                               f"El programa funcionará solo en memoria.")
            except OSError as e:
                return False, f"No se pudo crear el archivo '{self.ruta_archivo}'. Detalle: {e}"

        # Si existe, lo leemos:
        errores = 0
        cargados = 0
        try:
            with open(self.ruta_archivo, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                encabezado = next(reader, None)  # Puede ser None si el archivo está vacío
                # Si no hay encabezado válido, asumimos que no tiene encabezado y volvemos a leer desde el principio
                if encabezado is None or len(encabezado) < 4:
                    f.seek(0)
                    reader = csv.reader(f)

                for fila in reader:
                    # Cada fila debe tener 4 campos: id, nombre, cantidad, precio
                    if len(fila) != 4:
                        errores += 1
                        continue
                    id_unico, nombre, cant_str, precio_str = fila
                    if id_unico == "id" and nombre == "nombre":
                        # Si reencuentra encabezado, lo salta
                        continue
                    try:
                        cantidad = int(cant_str)
                        precio = float(precio_str)
                    except ValueError:
                        # Tipos inválidos
                        errores += 1
                        continue

                    # Si pasa todo, lo agregamos a memoria
                    self.productos.append(Producto(id_unico, nombre, cantidad, precio))
                    cargados += 1

            if errores == 0:
                return True, f"Inventario cargado: {cargados} producto(s)."
            else:
                return True, (f"Inventario cargado con advertencias: {cargados} producto(s) válidos, "
                              f"{errores} línea(s) corrupta(s) omitida(s).")
        except PermissionError:
            return False, (f"Sin permisos para leer '{self.ruta_archivo}'. "
                           f"El programa funcionará solo en memoria.")
        except FileNotFoundError:
            # Raza condición: si otro proceso borró el archivo entre exists() y open()
            try:
                with open(self.ruta_archivo, mode="w", newline="", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerow(["id", "nombre", "cantidad", "precio"])
                return True, f"Archivo '{self.ruta_archivo}' se recreó (se había eliminado)."
            except Exception as e:
                return False, f"No se pudo recrear el archivo tras FileNotFoundError: {e}"
        except csv.Error as e:
            return False, f"Error de formato CSV al leer '{self.ruta_archivo}': {e}"
        except OSError as e:
            return False, f"Error OS al abrir/leer '{self.ruta_archivo}': {e}"

    def _guardar_a_archivo(self):
        """
        Guarda el inventario completo en el archivo CSV (sobreescritura segura).
        Retorna (ok: bool, msg: str)
        NOTA: Sobrescribimos todo el archivo para mantener la consistencia (más simple para 2do semestre).
        """
        try:
            with open(self.ruta_archivo, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "nombre", "cantidad", "precio"])
                for p in self.productos:
                    writer.writerow([p.get_id(), p.get_nombre(), p.get_cantidad(), f"{p.get_precio():.2f}"])
            return True, "Cambios guardados en el archivo correctamente."
        except PermissionError:
            return False, f"Permiso denegado al escribir en '{self.ruta_archivo}'."
        except OSError as e:
            return False, f"Error OS al escribir en '{self.ruta_archivo}': {e}"
        except Exception as e:
            # Captura de cualquier otra excepción no prevista (defensivo)
            return False, f"Error inesperado al guardar: {e}"


# ---------------------------
# Utilidades de entrada segura (defensivas)
# ---------------------------
def pedir_entero(mensaje):
    """
    Solicita un entero por consola y maneja ValueError sin romper el programa.
    """
    while True:
        dato = input(mensaje)
        try:
            return int(dato)
        except ValueError:
            print("Entrada inválida: por favor, ingresa un número entero.")


def pedir_flotante(mensaje):
    """
    Solicita un float por consola y maneja ValueError sin romper el programa.
    """
    while True:
        dato = input(mensaje)
        try:
            return float(dato)
        except ValueError:
            print("Entrada inválida: por favor, ingresa un número (usa punto decimal).")


# ---------------------------
# Menú de consola
# ---------------------------
def menu():
    inventario = Inventario(ruta_archivo="inventario.txt")

    print("\n=== SISTEMA DE INVENTARIO (con archivos y excepciones) ===")
    # Mostrar mensaje de carga del archivo
    if getattr(inventario, "ultimo_mensaje_archivo", None):
        print(f"> {inventario.ultimo_mensaje_archivo}")

    while True:
        print("1) Añadir producto")
        print("2) Eliminar producto")
        print("3) Actualizar cantidad")
        print("4) Actualizar precio")
        print("5) Buscar por nombre")
        print("6) Mostrar todos")
        print("0) Salir")
        opcion = input("Opción: ").strip()

        if opcion == "1":
            id_unico = input("ID: ").strip()
            nombre = input("Nombre: ").strip()
            cantidad = pedir_entero("Cantidad (entero): ")
            precio = pedir_flotante("Precio (decimal): ")

            producto = Producto(id_unico, nombre, cantidad, precio)
            ok, msg = inventario.agregar(producto)
            print(msg)

        elif opcion == "2":
            id_unico = input("ID del producto a eliminar: ").strip()
            ok, msg = inventario.eliminar(id_unico)
            print(msg)

        elif opcion == "3":
            id_unico = input("ID del producto: ").strip()
            cantidad = pedir_entero("Nueva cantidad (entero): ")
            ok, msg = inventario.actualizar_cantidad(id_unico, cantidad)
            print(msg)

        elif opcion == "4":
            id_unico = input("ID del producto: ").strip()
            precio = pedir_flotante("Nuevo precio (decimal): ")
            ok, msg = inventario.actualizar_precio(id_unico, precio)
            print(msg)

        elif opcion == "5":
            nombre = input("Buscar por nombre: ").strip()
            resultados = inventario.buscar_nombre(nombre)
            if resultados:
                print(f"Coincidencias ({len(resultados)}):")
                for p in resultados:
                    print("  -", p)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "6":
            productos = inventario.mostrar_todos()
            if productos:
                print(f"Productos en inventario ({len(productos)}):")
                for p in productos:
                    print("  -", p)
            else:
                print("Inventario vacío.")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta nuevamente.")


# Punto de entrada
if __name__ == "__main__":
    menu()
