# Começamos com o controle de loop
continuar = True

while continuar:
    # Recebe o número do usuário
    numero = int(input("Digite um número para ver a tabuada: "))

    print(f"\nTabuada do {numero}:\n")

    # Usando for e range
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

    # Pergunta se o usuário quer continuar
    resposta = input("\nDeseja ver a tabuada de outro número? (s/n): ").lower()
    if resposta != 's':
        continuar = False
        print("Vasco não sobe se você não estudar")
