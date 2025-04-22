# O 'continue' faz com que o laço pule a iteração atual e vá para a próxima.
# Vamos criar um laço que conta de 1 até 6, mas pula o número 3.

for i in range(1, 6):
    if i == 3:  # Quando o valor de 'i' for igual a 3, pulamos essa iteração
        continue
    print(i)  # Imprime todos os valores, exceto o 3