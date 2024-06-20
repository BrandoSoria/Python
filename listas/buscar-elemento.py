#elementos de una lista
mascotas=["gato","perro","pes","loro","pes","vaca"]
#buscar elementos de una lista en este caso muestra el inidice del elemento y cuantos hay
print(mascotas.count("pes"))
if "pes" in mascotas:
    print(mascotas.index("pes"))