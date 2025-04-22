# Exemplo com 'break': interrompe o laço quando uma condição é atendida

for numero in range(1, 11):
    print("Número atual:", numero)
    if numero == 5:
        print("Número 5 encontrado! Encerrando o laço com break.")
        break

# O 'break' encerra o laço imediatamente.