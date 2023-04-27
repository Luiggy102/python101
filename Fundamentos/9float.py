# números flotantes = decimales

x = 3.3
y = 1.1 + 2.2 

print(" Comparar flotantes ")
print(f"Valor de x: {x}, tipo de dato: {type(x)}")
print(f"Valor de y: {y}, tipo de dato: {type(y)}")
print(f"La comparación de X y Y es: {x == y}")

print("*" * 50)
print(f"Para cortar decimales es con format")
print(f"Se transforma string Y")
y_str = format(y, ".2g") # Solos dos números
print(f"Y: {y_str} (string)")
print("Y se transforma la x en string")

# Comparación siendo strings
print(f"La comparación de X y Y es: {str(x) == y_str}, Igualdad")

print("*" * 50)

#############################################################
# Comparación en forma matemática 

x = 3.3
# número de decimales
print(y)
y = round(y, 1)
print(y)
print(x == y)




















