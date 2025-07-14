# Autor: Leslye Valencia
# Ejemplo de cómo usar constructores (__init__) y destructores (__del__) en Python.

class Dispositivo:
    # Constructor: se ejecuta automáticamente cuando creo un nuevo dispositivo.
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        # Aquí muestro un mensaje para confirmar que el objeto fue creado correctamente.
        print(f"[INICIADO] El dispositivo '{self.nombre}' de tipo '{self.tipo}' ha sido conectado.")

    # Metodo que hice para mostrar los datos del dispositivo.
    def mostrar_info(self):
        print(f"Dispositivo: {self.nombre} | Tipo: {self.tipo}")

    # Destructor: se activa cuando el objeto ya no existe o se cierra el programa.
    def __del__(self):
        # Uso este mensaje para saber cuándo el dispositivo fue desconectado.
        print(f"[CERRADO] El dispositivo '{self.nombre}' ha sido desconectado correctamente.")


# Parte principal del programa
if __name__ == "__main__":
    # Aquí creo una instancia de la clase Dispositivo.
    dispositivo1 = Dispositivo("Sensor de temperatura", "Sensor IoT")

    # Llamo al metodo para mostrar la información del dispositivo.
    dispositivo1.mostrar_info()

    # Elimino el objeto manualmente para ver cuándo se activa el destructor.
    del dispositivo1

    # Nota: también el destructor se activa si no uso 'del', solo que sería al final del programa.
