numeros=[5,4,3,2,1,0,-1,-2,-3,-4,-5]
#ordenar una lista de numeros de forma descendente
# numeros.sort(reverse=True)

# #ordenar una lista de numeros de forma ascendente
# numeros.sort()

#ordena y muestra una nueva lista sin afectar la lista original
numeros2 = sorted(numeros)
print(numeros)
print(numeros2)

usuarios= [
    [4,"pedro"],
    [3,"juan"],
    [2,"maria"]
    ]

def ordenar(elemento):
    return elemento[1]

#ordenar usuarios por el numero de "id"
usuarios.sort(key=ordenar)
print(usuarios)