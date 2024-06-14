# el * indica que el parametro puede tomar multiples argumentos
def suma (*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(f"la suma es: {resultado}")

suma(1, 2, 4)
suma(1, 2, 4, 5, 6)