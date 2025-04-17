def calcular_media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3  # Calculando a média
    return media  # Retornando o valor da média

# Chamada da função
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

resultado_media = calcular_media(nota1, nota2, nota3)  # Chamando a função com os valores das notas

# Exibindo a média com 2 casas decimais
print(f"A média das notas é: {resultado_media:.2f}")