print("bienbenidos")
print("salir")
print("empezar con palabras suma resta multiplicacion y division para hacer una operaciones")

resultado = ""
while True:
    if not resultado:
        resultado = input("digite el primer valor: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op= input("digite la operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("digite el segundo valor: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)
    if op == "+":
        resultado += n2
    elif op == "-":
        resultado -= n2
    elif op == "*":
        resultado *= n2
    elif op == "/":
        resultado /= n2
    print(f"el resultado es: {resultado}")
    print("fin del programa")
