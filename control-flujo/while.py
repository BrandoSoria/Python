# # si se cumple que al multiplicar un numero por dos es menor a 100 imprime ese numero
# numero = 1
# while numero < 100:
#     print(numero)
#     numero *=2

#loop infinito
comando = ""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
