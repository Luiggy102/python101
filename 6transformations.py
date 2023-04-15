import datetime

name = "John"
print(type(name))

name = 40
print(type(name))

name = True
print(type(name))

name = "John"
print(f"{name}" + " Doe")

age = 30
print("La edad es " + str(age))

print("\n")
age = input("Type your age => ")
today = datetime.datetime.today()
year = today.year
print(f"The current year is {year}")
print(f"Your birthdate was in: {year - int(age)}")
