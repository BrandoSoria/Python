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
    ["pedro",4],
    ["juan",3],
    ["maria",1]
    ]



#funcion lambda para ordenar y el es como alias del parametro elemento esta ordenando por letra de a-z
usuarios.sort(key=lambda el: el[1])
print(usuarios)