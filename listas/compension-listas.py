# compension listas
#muestra de la lista de usuarios primero nombre y despues su numero
usuarios= [
    ["pedro",4],
    ["juan",3],
    ["maria",1]
    ]

#buscar y mostrar solo el nombre de los usuarios
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])

# print(nombres)

#otra forma de mostrar solo el nombre de los usuarios
nombres = [usuario[0] for usuario in usuarios]
print(nombres)