edad = int(input("Ingrese su edad: "))

if edad < 4:
    print("Su entrada es gratis")
elif edad >= 4 and edad <= 18:
    print("Debe pagar $5 por su entrada")
elif edad > 18:
    print("Debe pagar $10 por su entrada") 