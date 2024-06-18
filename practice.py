#recorrer una lista de forma recursiva
def recorrer(l):
    if len(l) == 0:
        return
    print(l[0])
    recorrer(l[1:])

array1 = []
array2 = []

while len(array1) < 10:
    array1.append(int(input("ingrese numeros paara el array 1: ")))
    
while len(array2) < 10:
    array2.append(int(input("ingrese numeros para el array 2: ")))
recorrer([array1, array2])
