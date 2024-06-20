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

#otra forma de mostrar solo el nombre de los usuarios, es decir lo transformo en una lista
# se transforma la lista para mostrar solo el nombre de usuarios y no el id de usuario
# se usa el parametro con usuario[0]

# nombres = [usuario[0] for usuario in usuarios]


#filtrar de manera que solo me muestre los usuarios que tengan un id mayor a 2

# nombres=[usuario for usuario in usuarios if usuario[1] > 2]


#filtrar y transformar la lista
# se transforma la lista para mostrar solo el nombre de usuarios y no el id de usuario
# se usa el parametro con usuario[0]

nombres=[usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)
