# -*- coding: utf-8 -*-
"""
Tarea: Sistema de Gestión de Biblioteca Digital
Estudiante: Leslye Valencia

Descripción:
------------
Este sistema permite gestionar una biblioteca digital:
- Añadir y quitar libros.
- Registrar y dar de baja usuarios.
- Prestar y devolver libros.
- Buscar libros por título, autor o categoría.
- Listar libros prestados por usuario.
"""

from datetime import datetime


# ---------------------------
# Clase Libro
# ---------------------------
class Libro(object):
    """
    Representa un libro.
    Guarda el título y autor en una tupla (inmutable).
    """

    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo_autor = (titulo, autor)  # tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self):
        return self.titulo_autor[0]

    @property
    def autor(self):
        return self.titulo_autor[1]

    def __str__(self):
        return "[{}] {} — {} ({})".format(self.isbn, self.titulo, self.autor, self.categoria)


# ---------------------------
# Clase Usuario
# ---------------------------
class Usuario(object):
    """
    Representa un usuario de la biblioteca.
    """

    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []  # lista de ISBN

    def __str__(self):
        return "{} (ID: {})".format(self.nombre, self.user_id)

    def tiene_prestamos(self):
        return len(self.libros_prestados) > 0


# ---------------------------
# Clase Biblioteca
# ---------------------------
class Biblioteca(object):
    """
    Clase principal que maneja libros, usuarios y préstamos.
    """

    def __init__(self):
        self.libros = {}        # isbn -> Libro
        self.usuarios = {}      # user_id -> Usuario
        self.user_ids = set()   # conjunto de IDs únicos
        self.prestamos = {}     # isbn -> user_id
        self.historial = []     # lista de eventos

    def _timestamp(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def _registrar_evento(self, accion, user_id=None, isbn=None):
        self.historial.append((self._timestamp(), accion, user_id, isbn))

    # ---- Gestión de libros ----
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            return False
        self.libros[libro.isbn] = libro
        self._registrar_evento("ALTA_LIBRO", None, libro.isbn)
        return True

    def quitar_libro(self, isbn):
        if isbn not in self.libros:
            return False
        if isbn in self.prestamos:
            return False
        del self.libros[isbn]
        self._registrar_evento("BAJA_LIBRO", None, isbn)
        return True

    # ---- Gestión de usuarios ----
    def registrar_usuario(self, usuario):
        if usuario.user_id in self.user_ids:
            return False
        self.user_ids.add(usuario.user_id)
        self.usuarios[usuario.user_id] = usuario
        self._registrar_evento("ALTA_USUARIO", usuario.user_id, None)
        return True

    def dar_baja_usuario(self, user_id):
        if user_id not in self.usuarios:
            return False
        u = self.usuarios[user_id]
        if u.tiene_prestamos():
            return False
        del self.usuarios[user_id]
        self.user_ids.remove(user_id)
        self._registrar_evento("BAJA_USUARIO", user_id, None)
        return True

    # ---- Préstamos ----
    def prestar_libro(self, isbn, user_id):
        if isbn not in self.libros:
            return False
        if user_id not in self.usuarios:
            return False
        if isbn in self.prestamos:
            return False
        self.prestamos[isbn] = user_id
        self.usuarios[user_id].libros_prestados.append(isbn)
        self._registrar_evento("PRESTAMO", user_id, isbn)
        return True

    def devolver_libro(self, isbn, user_id):
        if isbn not in self.prestamos:
            return False
        if self.prestamos[isbn] != user_id:
            return False
        del self.prestamos[isbn]
        self.usuarios[user_id].libros_prestados.remove(isbn)
        self._registrar_evento("DEVOLUCION", user_id, isbn)
        return True

    # ---- Búsquedas ----
    def buscar_por_titulo(self, texto):
        q = texto.strip().lower()
        return [lib for lib in self.libros.values() if q in lib.titulo.lower()]

    def buscar_por_autor(self, texto):
        q = texto.strip().lower()
        return [lib for lib in self.libros.values() if q in lib.autor.lower()]

    def buscar_por_categoria(self, texto):
        q = texto.strip().lower()
        return [lib for lib in self.libros.values() if q in lib.categoria.lower()]

    # ---- Listados ----
    def listar_libros_prestados_usuario(self, user_id):
        if user_id not in self.usuarios:
            return []
        return [self.libros[i] for i in self.usuarios[user_id].libros_prestados]

    def catalogo(self):
        return self.libros.values()

    def prestamos_vigentes(self):
        return self.prestamos.items()

    def ver_historial(self):
        return self.historial


# ============================================================================
# DEMOSTRACIÓN
# ============================================================================
if __name__ == "__main__":
    biblioteca = Biblioteca()

    # Registrar usuarios
    u1 = Usuario("Ana Pérez", "U001")
    u2 = Usuario("Luis Gómez", "U002")
    print("Registrar usuarios:")
    print("  Ana:", biblioteca.registrar_usuario(u1))
    print("  Luis:", biblioteca.registrar_usuario(u2))
    print("")

    # Añadir libros
    l1 = Libro("Python desde Cero", "M. Ramírez", "Programación", "ISBN-001")
    l2 = Libro("Estructuras de Datos", "C. Torres", "Informática", "ISBN-002")
    biblioteca.añadir_libro(l1)
    biblioteca.añadir_libro(l2)

    # Prestar libro
    print("Prestar libro ISBN-001 a U001:", biblioteca.prestar_libro("ISBN-001", "U001"))

    # Mostrar libros prestados de U001
    print("Libros prestados a U001:")
    for lib in biblioteca.listar_libros_prestados_usuario("U001"):
        print("  ", lib)

    # Devolver libro
    print("Devolver ISBN-001:", biblioteca.devolver_libro("ISBN-001", "U001"))

    # Mostrar historial
    print("Historial de eventos:")
    for evento in biblioteca.ver_historial():
        print(" ", evento)
