tiempo = input("Ingrese la hora: ")

horas, minutos = map(int, tiempo.split(":"))

tiempoDecimal = horas + minutos / 60

if tiempoDecimal >= 7 and tiempoDecimal <= 8:
    print("Es la hora del desayuno")
elif tiempoDecimal >= 12 and tiempoDecimal <= 13:
    print("Es la hora del almuerzo")
elif tiempoDecimal >= 18 and tiempoDecimal <= 19:
    print("Es la hora de la cena")
else:
    print("")