lista1 = [8, 2, 5]
lista2 = [12, 22, 30, 45]

def intercalarListas(lista1, lista2):
    resultado = []
    tamanho = min(len(lista1), len(lista2))
    for i in range(tamanho):
        resultado.append(lista1[i])
        resultado.append(lista2[i])
    return resultado

resultado = intercalarListas(lista1, lista2)
print(resultado)