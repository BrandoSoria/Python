"""metodos de string"""

animal = "chanchito feliz1"
print(animal.upper())

animall = "CHANCHITO FELIZ2"
print(animal.lower())
# la primer letra de cada palabra es mayuscula
animal = "Chanchito Feliz3"
print(animal.title())

# la primer letra de cada palabra es mayuscula
animal2 = "Chanchito Feliz4"
print(animal.strip().capitalize())

# las mayusculas se convierten en minusculas
animal = " Chanchito Feliz5"
print(animal.swapcase())
# elimina los espacios al principio y al final
print(animal.strip())

print(animal.lstrip())

print(animal.rstrip())
# la posicion de la palabra
print(animall.find("CH"))
# reemplaza una palabra por otra
print(animal.replace("nch", "j"))

# comprueba si hay una palabra en el texto
print("nCH" in animal2)
# comprueba si no hay una palabra en el texto y si no dice true
print("nCH" not in animal2)
