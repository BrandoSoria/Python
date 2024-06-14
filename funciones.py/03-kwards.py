#usando kwargs en una funcion
def get_producto(**datos):
    #muestra todos los datos es un diccionario
    #print(datos)
    #muestra solo los argumentos que se le pasaron
    print(datos["id"], datos["name"])
# asi se usa el kwargs
get_producto(id="1",
            name="thinkpad",
            price=7000,
            category="oficina")
