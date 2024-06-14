#definicion de la funcion y su parametro y valor por defecto
def hola(nombre, apellido= "soria"):
    print("hola mundo")
    print(f"bienvenido a la clase {nombre} {apellido}") #uso del parametro
#ejecucion de la funcion y su argumento
hola("brandon", "gonzalez")
hola("nicolas" )

# el parametro apellido que tiene el valor por defecto es opcional
# y si no se le pasa un valor para el argumento se toma el valor por defecto del parametro
