def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto

def reverse (texto):
    texto_alreves = ""
    for char in texto:
        texto_alreves = char + texto_alreves
    return texto_alreves
        

def espalindromo(texto):
    texto = no_space(texto)
    texto_alreves = reverse(texto)
    return texto.lower() == texto_alreves.lower()
    print(texto_alreves)

#boolean
print("escribe un palabra")
palabra = input()
print(espalindromo(palabra))
