# O laço 'for' pode ser combinado com 'else'. O código dentro de 'else' será executado quando o laço terminar normalmente (sem interrupções como o 'break').

# Lista de números que verifica se algum número é igual a 5.
numeros = [1, 2, 3, 4, 5]

for numero in numeros:
    if numero == 5:
        print("Encontramos o número 5!")
        break  # Interrompe o laço quando encontrar o número 5
else:
    print("O número 5 não foi encontrado.")  # Esse código só será executado se o 'for' não for interrompido