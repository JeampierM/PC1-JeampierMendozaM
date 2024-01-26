consumo = int(input("Ingrese el consumo de su comida: "))
porcentPropina = int(input("Ingrese el porcentaje de propina que desea dejar al mesero: "))

propina = (porcentPropina / 100) * consumo
    
print(f"Cantidad de propina a dejar: {propina}")