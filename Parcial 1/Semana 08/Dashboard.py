import os

tareas = []

def mostrar_menu():
    while True:
        print("\n--- Dashboard de Tareas de POO ---")
        print("1 - Ver tareas")
        print("2 - Agregar nueva tarea")
        print("3 - Marcar tarea como completada")
        print("4 - Eliminar tarea")
        print("0 - Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            ver_tareas()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            completar_tarea()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '0':
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida.")

def ver_tareas():
    if not tareas:
        print("\nNo tienes tareas registradas.")
        return
    print("\n--- Tus tareas ---")
    for idx, tarea in enumerate(tareas):
        estado = "Completada" if tarea['completada'] else "Pendiente"
        print(f"{idx + 1}. [{estado}] {tarea['titulo']} - {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")

def agregar_tarea():
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'completada': False
    }
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def completar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        idx = int(input("Número de la tarea completada: ")) - 1
        if 0 <= idx < len(tareas):
            tareas[idx]['completada'] = True
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        idx = int(input("Número de la tarea a eliminar: ")) - 1
        if 0 <= idx < len(tareas):
            eliminada = tareas.pop(idx)
            print(f"Tarea '{eliminada['titulo']}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

if __name__ == "__main__":
    mostrar_menu()
