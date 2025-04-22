# Exemplo com 'break' em um laço while

contador = 1

while True:
    print("Contador:", contador)
    if contador == 3:
        print("Chegamos ao 3! Parando o laço com break.")
        break
    contador += 1