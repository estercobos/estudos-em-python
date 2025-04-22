# Exemplo de uso do 'continue' em um while

numero = 0

while numero < 5:
    numero += 1
    if numero == 3:
        print("Pulando o número 3 com continue")
        continue
    print("Número:", numero)