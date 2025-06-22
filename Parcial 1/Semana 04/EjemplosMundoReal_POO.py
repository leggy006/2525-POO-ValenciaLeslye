# sistema_escolar.py

# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.materias = []

    def inscribirse(self, materia):
        self.materias.append(materia)
        materia.agregar_estudiante(self)
        print(f"{self.nombre} se inscribió en {materia.nombre}.")

    def ver_materias(self):
        print(f"\nMaterias inscritas de {self.nombre}:")
        for m in self.materias:
            print(f"- {m.nombre} (Profesor: {m.profesor.nombre})")


# Clase que representa a un profesor
class Profesor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"Profesor: {self.nombre} - Especialidad: {self.especialidad}")


# Clase que representa una materia escolar
class Materia:
    def __init__(self, nombre, profesor):
        self.nombre = nombre
        self.profesor = profesor
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def listar_estudiantes(self):
        print(f"\nEstudiantes en la materia {self.nombre}:")
        for est in self.estudiantes:
            print(f"- {est.nombre} ({est.matricula})")


# Simulación
if __name__ == "__main__":
    # Crear profesor
    prof_edwin = Profesor("Edwin Fernández", "Programación")

    # Crear materia
    programacion = Materia("Programación Orientada a Objetos", prof_edwin)

    # Crear estudiantes
    est1 = Estudiante("Leslye Valencia", "A001")
    est2 = Estudiante("Tatiana Alcivar", "A002")

    # Inscribir estudiantes
    est1.inscribirse(programacion)
    est2.inscribirse(programacion)

    # Mostrar materias inscritas por Leslye
    est1.ver_materias()

    # Listar estudiantes inscritos en Programación Orientada a Objetos
    programacion.listar_estudiantes()
