# Programación Orientada a Objetos: Promedio semanal del clima

class DiaClima:
    def __init__(self, dia, temperatura):
        self.dia = dia
        self.temperatura = temperatura

class SemanaClima:
    def __init__(self):
        self.dias = []

    def agregar_dia(self, dia, temperatura):
        self.dias.append(DiaClima(dia, temperatura))

    def calcular_promedio(self):
        total = sum(dia.temperatura for dia in self.dias)
        return total / len(self.dias)

# Uso del programa
print("== PROMEDIO SEMANAL DEL CLIMA (POO) ==")
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semana = SemanaClima()

for dia in dias_semana:
    temp = float(input(f"Ingrese la temperatura del {dia}: "))
    semana.agregar_dia(dia, temp)

promedio = semana.calcular_promedio()
print(f"Promedio semanal de temperatura: {promedio:.2f}°")
