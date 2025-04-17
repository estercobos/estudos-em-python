# Uma função é como uma máquina que faz algo específico quando você a chama. E essa "máquina" pode receber entradas e devolver um resultado.Quando você usa o def, você está criando essa "máquina" para fazer alguma coisa. Mas, a diferença é que a máquina não faz nada até você "ligá-la", ou seja, até você chamar a função.

# Função saudacao: Ela recebe um parâmetro chamado nome e retorna uma string personalizada, utilizando o valor de nome na saudação.
def saudacao(nome):
    return f"Olá, {nome}! Bem-vinda(o) ao mundo as funções!"

# Quando for chamar saudacao("Ester"), o valor "Ester" é passado para a função, e o resultado é a mensagem "Olá, Ester! Bem-vinda(o) ao mundo as funções!".

# Chamando a função saudacao com "Ester" e guardando o resultado em 'mensagem'
mensagem = saudacao("Ester")
# Imprimindo a mensagem
print(mensagem)


# Função soma_dois_numeros - soma dois números
def soma_dois_numeros(num1, num2):
    # A função soma os dois números e retorna o resultado
    return num1 + num2

# Chamando a função soma_dois_numeros com os números 1 e 1 e guardando o resultado em 'resultado'
resultado = soma_dois_numeros(1, 1)
# Imprimindo o resultado da soma
print(f"A soma é: {resultado}")


# Função quadrado - calcula o quadrado de um número
def quadrado(numero):
    # A função eleva o número ao quadrado e retorna o valor
    return numero ** 2

# Chamando a função quadrado com o número 4 e guardando o resultado em 'resultado_quadrado'
resultado_quadrado = quadrado(4)
# Imprimindo o resultado do quadrado
print(f"O quadrado de 4 é: {resultado_quadrado}")