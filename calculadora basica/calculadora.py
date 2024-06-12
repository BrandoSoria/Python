# por teclado
n1 = input("digite o primer valor: ")
n2 = input("digite o segundo valor: ")

# convertir a entero las variables
n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

mensaje = f"""
para los numeros {n1} y {n2},
el resultado de la suma es de : {suma}
el resultado de la resta es de : {resta}
el resultado de la multiplicacion es de : {multiplicacion}
el resultado de la division es de : {division}
"""
print(mensaje)
