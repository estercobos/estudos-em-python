# Função para realizar operações matemáticas básicas
def operacoes_matematicas(n1, n2):
    soma = n1 + n2
    subtracao = n1 - n2
    multiplicacao = n1 * n2
    divisao = None
    resto = None
    
    # Verificando se a divisão por zero
    if n2 != 0:
        divisao = n1 / n2
        resto = n1 % n2
    else:
        divisao = 'Indefinido (divisão por zero)'
        resto = 'Indefinido (divisão por zero)'

    # Retornando os resultados
    return soma, subtracao, multiplicacao, divisao, resto

# Testando a função
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma, subtracao, multiplicacao, divisao, resto = operacoes_matematicas(n1, n2)

# Exibindo os resultados
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Resto: {resto}")