print("MENU")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")

num1 = int(input("Digite el primer numero: "))
num2 = int(input("Digite el segundo numero: "))
opcion = int(input("Digite una opcion: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

if opcion == 1:
    print(f"La suma es: {suma}")
elif opcion == 2:
    print(f"La resta es: {resta}")
elif opcion == 3:
    print(f"La multiplicacion es: {multiplicacion}")
else:
    print("Opcion invalida")