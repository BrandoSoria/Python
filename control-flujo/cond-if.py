"""cond-if"""

# programa paraventa de boletos
# CASO: una persona que quiere comprar un boleto
#para ver una pelicula pero si no es mayor de edad no puede verla
# y si es mayor de 50 años tendra descuento
edad=70
if edad > 65:
    print("puede ver la pelicula con superdescuento")
elif edad >= 54:
    print("puede ver la pelicula con descuento")
elif edad >= 18:
    print("puede ver la pelicula")
else:
    print("no puede ver la pelicula")

print("fin del programa")
