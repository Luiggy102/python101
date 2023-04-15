# En este desafío, se te proporcionará un código base encontrarás las variables name y age todas como strings. 
# Tu tarea es crear un formato de string que, como resultado, muestre un mensaje en la sección Terminal. El mensaje deberá tener la siguiente forma:

# Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años

# Ten en cuenta que debes calcular la edad que tendrás en 10 años a partir de la edad. Por ejemplo, si la edad es 29 años, el mensaje mostrado deberá decir "tengo 29 años y en 10 años tendré 39 años"

name = input("¿Cual es tu nombre? => ")
print(name)
age = input("¿Cual es tu edad? => ")
print(age)


total = int(age) + 10

template = f"Hola mi nombere es {name}, tengo {age} y en 10 años tendré {total} años"
print(template)
