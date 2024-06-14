#calculadora interactiva
# verificar si ya ingreso el primer valor o si no lo pide
#que ingrese una operacion
# que ingrese el segundo valor
# que imprima el resultado
# que ingrese nuevos valores o salga del programa
while True:
    s = input("que haras hoy: ")
    if s.lower() == "salir":
        print("bays")
        break
    elif s.lower() == "empezar":

        n1 =input("digite el primer valor: ")
        n1= int(n1)

        operacion = input("digite la operacion: ")
        n2 =input("digite el segundo valor: ")
        n2= int(n2)
        
        if operacion == "+":
            print(n1 + n2)
        elif operacion == "-":
            print(n1 - n2)
        elif operacion == "*":
            print(n1 * n2)
        elif operacion == "/":
            print(n1 / n2)
        else:
            print("la operacion no es valida")
            break

