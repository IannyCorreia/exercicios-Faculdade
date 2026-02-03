valores = []

for i in range(3):
    valor = int(input(f"Digite o {i+1}º elemento da lista: "))
    valores.append(valor)
    
def exibirLista(valores):
    for i in valores:
        print(i)
exibirLista(valores)