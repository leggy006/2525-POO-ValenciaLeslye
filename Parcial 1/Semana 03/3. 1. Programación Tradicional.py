# Programación Tradicional: Promedio semanal del clima

# Función para ingresar las temperaturas de la semana
def ingresar_temperaturas():
    temperaturas = []
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    for dia in dias:
        temp = float(input(f"Ingrese la temperatura del {dia}: "))
        temperaturas.append(temp)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Uso del programa
print("== PROMEDIO SEMANAL DEL CLIMA (Tradicional) ==")
temps = ingresar_temperaturas()
promedio = calcular_promedio(temps)
print(f"Promedio semanal de temperatura: {promedio:.2f}°")
