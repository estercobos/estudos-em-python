def soma(*args):
    # Vamos criar uma variável para armazenar o total da soma
    total = 0
    
    # Percorrendo todos os números passados para a função
    for num in args:
        total += num  # Somando cada número com o total

    # Retorna o total da soma
    return total

# Agora vamos testar a função com diferentes números
resultado1 = soma(1, 2, 3, 4, 5)  # Passando 5 números
resultado2 = soma(10, 20, 30)     # Passando 3 números
resultado3 = soma(100)            # Passando 1 número
resultado4 = soma(7, 8, 9, 10, 11, 12)  # Passando 6 números

# Imprimindo os resultados
print(f"Soma dos números 1, 2, 3, 4, 5: {resultado1}")  # Espera 15
print(f"Soma dos números 10, 20, 30: {resultado2}")    # Espera 60
print(f"Soma do número 100: {resultado3}")            # Espera 100
print(f"Soma dos números 7, 8, 9, 10, 11, 12: {resultado4}")  # Espera 57