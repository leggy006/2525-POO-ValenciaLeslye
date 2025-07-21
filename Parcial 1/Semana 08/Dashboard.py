import os  # Importo esta librería para usar funciones relacionadas con el sistema operativo (aunque en este programa no la estoy usando directamente)

# Lista donde se guardarán las tareas. Cada tarea será un diccionario con varios campos (título, descripción, etc.)
tareas = []

# Esta función muestra el menú principal y permite al usuario elegir qué acción desea hacer
def mostrar_menu():
    while True:
        print("\n--- Dashboard de Tareas de POO ---")
        print("1 - Ver tareas")
        print("2 - Agregar nueva tarea")
        print("3 - Marcar tarea como completada")
        print("4 - Eliminar tarea")
        print("0 - Salir")

        opcion = input("Elige una opción: ")  # Pido al usuario que seleccione una opción

        # Según la opción que elija, llamo a la función correspondiente
        if opcion == '1':
            ver_tareas()
        elif opcion == '2':
            agregar_tarea()
        elif opcion == '3':
            completar_tarea()
        elif opcion == '4':
            eliminar_tarea()
        elif opcion == '0':
            print("Programa finalizado.")  # Si elige salir, se termina el programa
            break
        else:
            print("Opción inválida.")  # Si escribe algo incorrecto, le aviso

# Esta función imprime todas las tareas que el usuario ha ingresado
def ver_tareas():
    if not tareas:
        print("\nNo tienes tareas registradas.")  # Si la lista está vacía, informo al usuario
        return
    print("\n--- Tus tareas ---")
    for idx, tarea in enumerate(tareas):  # Recorro todas las tareas guardadas
        estado = "Completada" if tarea['completada'] else "Pendiente"  # Muestro si está completada o no
        print(f"{idx + 1}. [{estado}] {tarea['titulo']} - {tarea['descripcion']} (Prioridad: {tarea['prioridad']})")

# Esta función permite al usuario ingresar una nueva tarea
def agregar_tarea():
    titulo = input("Título de la tarea: ")
    descripcion = input("Descripción: ")
    prioridad = input("Prioridad (Alta/Media/Baja): ")
    tarea = {
        'titulo': titulo,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'completada': False  # Por defecto, la tarea no está completada cuando se crea
    }
    tareas.append(tarea)  # Agrego la tarea a la lista
    print("Tarea agregada correctamente.")

# Esta función permite marcar una tarea como completada
def completar_tarea():
    ver_tareas()  # Primero muestro la lista de tareas para que el usuario vea cuál elegir
    if not tareas:
        return
    try:
        idx = int(input("Número de la tarea completada: ")) - 1  # Resto 1 porque la lista empieza en 0
        if 0 <= idx < len(tareas):
            tareas[idx]['completada'] = True  # Cambio el estado de la tarea a completada
            print("Tarea marcada como completada.")
        else:
            print("Número inválido.")  # Si el número no está en el rango, aviso
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")  # Si escribe letras u otro error, informo

# Esta función permite eliminar una tarea de la lista
def eliminar_tarea():
    ver_tareas()
    if not tareas:
        return
    try:
        idx = int(input("Número de la tarea a eliminar: ")) - 1
        if 0 <= idx < len(tareas):
            eliminada = tareas.pop(idx)  # Elimino la tarea seleccionada
            print(f"Tarea '{eliminada['titulo']}' eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")

# Punto de entrada del programa. Desde aquí se ejecuta
if __name__ == "__main__":
    mostrar_menu()

