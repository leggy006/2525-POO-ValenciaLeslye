# Sistema de Gestión de Inventarios simple para una tienda

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
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


# ---------------------------
# Clase Inventario
# ---------------------------
class Inventario:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        # Validar que el ID sea único
        for p in self.productos:
            if p.get_id() == producto.get_id():
                return False
        self.productos.append(producto)
        return True

    def eliminar(self, id_unico):
        for p in self.productos:
            if p.get_id() == id_unico:
                self.productos.remove(p)
                return True
        return False

    def actualizar_cantidad(self, id_unico, nueva_cantidad):
        for p in self.productos:
            if p.get_id() == id_unico:
                p.set_cantidad(nueva_cantidad)
                return True
        return False

    def actualizar_precio(self, id_unico, nuevo_precio):
        for p in self.productos:
            if p.get_id() == id_unico:
                p.set_precio(nuevo_precio)
                return True
        return False

    def buscar_nombre(self, nombre):
        resultados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                resultados.append(p)
        return resultados

    def mostrar_todos(self):
        return self.productos


# ---------------------------
# Menú de consola
# ---------------------------
def menu():
    inventario = Inventario()

    while True:
        print("\n=== SISTEMA DE INVENTARIO ===")
        print("1) Añadir producto")
        print("2) Eliminar producto")
        print("3) Actualizar cantidad")
        print("4) Actualizar precio")
        print("5) Buscar por nombre")
        print("6) Mostrar todos")
        print("0) Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            id_unico = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_unico, nombre, cantidad, precio)
            if inventario.agregar(producto):
                print("Producto agregado.")
            else:
                print("El ID ya existe.")

        elif opcion == "2":
            id_unico = input("ID del producto a eliminar: ")
            if inventario.eliminar(id_unico):
                print("Producto eliminado.")
            else:
                print("No se encontró el producto.")

        elif opcion == "3":
            id_unico = input("ID del producto: ")
            cantidad = int(input("Nueva cantidad: "))
            if inventario.actualizar_cantidad(id_unico, cantidad):
                print("Cantidad actualizada.")
            else:
                print("No se encontró el producto.")

        elif opcion == "4":
            id_unico = input("ID del producto: ")
            precio = float(input("Nuevo precio: "))
            if inventario.actualizar_precio(id_unico, precio):
                print("Precio actualizado.")
            else:
                print("No se encontró el producto.")

        elif opcion == "5":
            nombre = input("Buscar por nombre: ")
            resultados = inventario.buscar_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "6":
            productos = inventario.mostrar_todos()
            if productos:
                for p in productos:
                    print(p)
            else:
                print("Inventario vacío.")

        elif opcion == "0":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
