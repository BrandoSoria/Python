nombre_curso = "Curso de Python"
print(nombre_curso)
#mensajes largos
descripcion = """Esto es un curso de Python para principiantes y hacerte una guia."""
print(descripcion)

#longitud del mensaje largo
print (len(descripcion))
#accediendo al primer caracter del texto del mensaje corto
print(nombre_curso[0])
#accediendo a caracteres especificos de tal a tal
print(nombre_curso[0:5])
# solo le dije desde donde inicia pero no donde termina y toma hasta el final
print(nombre_curso[9:])
# no le indico donde inicia pero si donde termina y ocurre lo contrario a lo anterior
print(nombre_curso[:8])

print(nombre_curso[:])
