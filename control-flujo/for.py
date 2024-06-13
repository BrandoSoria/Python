buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print("no encontrado")

#iterar una cadena
for char in "Ultimate Python":
    print(char)
    