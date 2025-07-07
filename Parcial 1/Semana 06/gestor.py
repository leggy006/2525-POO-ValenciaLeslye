# Programa: Gestor de Notas y Tareas
# Autor: Leslye Valencia
# Descripción: Este programa permite crear y visualizar notas y tareas.
# Aplica los conceptos de Programación Orientada a Objetos (POO) en Python.


# Clase base que representa cualquier elemento (nota o tarea)
class Elemento:
    def __init__(self, titulo):
        self.titulo = titulo

    def mostrar_detalle(self):
        return f"Título: {self.titulo}"

# Clase Nota que hereda de Elemento
class Nota(Elemento):
    def __init__(self, titulo, contenido):
        super().__init__(titulo)
        self.contenido = contenido

    def mostrar_detalle(self):
        return f"[Nota] {self.titulo} - {self.contenido}"

# Clase Tarea que también hereda de Elemento
class Tarea(Elemento):
    def __init__(self, titulo, fecha_entrega):
        super().__init__(titulo)
        self.__fecha_entrega = fecha_entrega  # Encapsulado
        self.__completada = False             # Encapsulado

    def completar(self):
        self.__completada = True

    def esta_completada(self):
        return self.__completada

    def get_fecha_entrega(self):
        return self.__fecha_entrega

    def mostrar_detalle(self):
        estado = "Completada" if self.__completada else "Pendiente"
        return f"[Tarea] {self.titulo} - Entrega: {self.__fecha_entrega} - Estado: {estado}"

# Clase Usuario que administra sus notas y tareas
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__notas = []
        self.__tareas = []

    def agregar_nota(self, nota):
        self.__notas.append(nota)

    def agregar_tarea(self, tarea):
        self.__tareas.append(tarea)

    def mostrar_todo(self):
        print(f"\nNotas y Tareas de {self.nombre}:\n")

        print("Notas:")
        for nota in self.__notas:
            print("  -", nota.mostrar_detalle())

        print("\nTareas:")
        for tarea in self.__tareas:
            print("  -", tarea.mostrar_detalle())

# Código principal para probar el programa
if __name__ == "__main__":
    # Crear una usuaria
    leslye = Usuario("Leslye Valencia")

    # Notas personales
    nota1 = Nota("Clase de POO", "Repasar herencia y polimorfismo")
    nota2 = Nota("Recordatorio", "Enviar tarea antes del viernes")
    leslye.agregar_nota(nota1)
    leslye.agregar_nota(nota2)

    # Tareas pendientes
    tarea1 = Tarea("Subir proyecto a GitHub", "2025-07-06")
    tarea2 = Tarea("Estudiar para el parcial", "2025-07-11")
    leslye.agregar_tarea(tarea1)
    leslye.agregar_tarea(tarea2)

    # Marcar tarea completada
    tarea1.completar()

    # Mostrar notas y tareas
    leslye.mostrar_todo()
