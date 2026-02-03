def primeiraMaiuscula(texto):
    return texto[0].upper() + texto[1:].lower()

texto = str(input("Digite um texto: "))
resultado = primeiraMaiuscula(texto)
print(resultado)