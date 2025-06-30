# Este es un programa para calcular el área de un cuadrado.
# Solo necesitamos saber cuánto mide un lado del cuadrado y listo.
# Es un ejercicio para practicar tipos de datos y buenas prácticas en Python :)

def calcular_area_cuadrado(lado: float) -> float:
    """
    Esta función calcula el área del cuadrado.
    Solo multiplica el lado por sí mismo (lado * lado).
    """
    area = lado * lado
    return area


# Aquí le pedimos al usuario que escriba su nombre para saludarlo :)
nombre_usuario = input("Ingrese su nombre: ")  # tipo de dato: string (texto)
print(f"Hola, {nombre_usuario}. Vamos a calcular el área de un cuadrado.")

# Ahora pedimos la medida de un lado del cuadrado
# Usamos float porque puede que escriba decimales, como 5.5 cm
lado_cuadrado = float(input("Ingrese la longitud del lado del cuadrado en cm: "))  # tipo de dato: float

# Llamamos a la función para calcular el área usando el valor que dio el usuario
area_resultado = calcular_area_cuadrado(lado_cuadrado)

# Mostramos el resultado en pantalla con unidades (centímetros cuadrados)
print(f"El área del cuadrado es: {area_resultado} cm²")

# Aquí usamos un dato booleano para saber si el área es "grande" o no
# En este caso, consideramos que es grande si tiene 100 cm² o más
area_es_grande = area_resultado >= 100  # tipo de dato: boolean (True o False)
print("¿El área es mayor o igual a 100 cm²?", area_es_grande)
