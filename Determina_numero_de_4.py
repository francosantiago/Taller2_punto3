"""PROGRAMA
RECONOCER SI ES UN NÙMERO DE 4 CIFRAS"""

print("--------------------------------")
print("-------Nùmero de 4 cifras-------")
print("--------------------------------")

x = int(input("Ingresa el nùmero: "))

if x > 999 and x < 10000:
    msj = "es de 4 cifras"
else:
    msj = "no es de 4 cifras"

print("El nùmero ingresado " + str(msj))