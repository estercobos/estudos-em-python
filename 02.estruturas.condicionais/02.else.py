"""
O 'else' é a parte do código que executa se a condição do 'if' for falsa.
Ou seja, se a condição do 'if' não for atendida, o que estiver no 'else' vai ser executado.
"""
# Pergunta um número para a pessoa
numero = int(input("Digite um número inteiro: "))

# Se o número for divisível por 2, é par, se não, é ímpar
if numero % 2 == 0:  # Se o número for divisível por 2, ele é par
    print("Par")
else:  # Se não for divisível por 2, então é ímpar
    print("Ímpar")