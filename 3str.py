nombre = 'Joe'
apellido = 'Doe'

nombre_completo = nombre + ' ' + apellido
print(nombre_completo) # no deja espacio

print("para usar apostrofe se usa doble comilla: I'm Joe")

print('Frase: "Esto es una frase, se inicia con comillas simples"')

apellido = 'Doe'

# format
plantilla = "Mein Name ist " + nombre + " und mein Nachname ist " + apellido
print(plantilla)

# forma más sencilla
plantilla2 = "Mein Name ist {} und mein Nachname ist {}".format(nombre, apellido) 
print(plantilla2)

# más usada
plantilla3 = f"Mein Name ist {nombre} und mein Nachname ist {apellido}"
print(plantilla3)
