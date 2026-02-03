try:
    letra = input("Digite F para Feminino ou M para Masculino: ").strip().upper()

    if letra == "F":
        print("Feminino")
    elif letra == "M":
        print("Masculino")
    else:
        print("Sexo inválido")

except Exception:
    print("Erro inesperado.")
