print("Programa para saber si un número es par o no")
num = int(input('Coloque el número a comprobar => '))

# si no tiene residuo al dividir para dos es par
if num % 2 == 0:
    print(f"El número {num} es par")
else:
    print(f"El número {num} no es par")
