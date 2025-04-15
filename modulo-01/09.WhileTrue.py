while True:
    # Solicita a idade do usuário
    idade = input("Digite sua idade para saber se você está apto a dirigir: ")

    # Verifica se a entrada é um número válido
    if idade.isdigit():
        idade = int(idade)

        # Verifica se a idade é suficiente para dirigir
        if idade >= 18:
            print("Você está apto a dirigir!")
            break  # Se a pessoa tem 18 anos ou mais, sai do laço
        else:
            print("Você não está apto a dirigir. Precisa ser maior de 18 anos.")
    else:
        print("Por favor, digite um número válido para a idade.")