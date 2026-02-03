def somarElementos(lista):
    total = 0
    for n in lista:
        total += n
    return total

valores = []
for i in range(5):
    valor = int(input(f"Digite o {i+1}° valor: "))
    valores.append(valor)

resultado = somarElementos(valores)
print(f"Soma dos elementos: {resultado}")
