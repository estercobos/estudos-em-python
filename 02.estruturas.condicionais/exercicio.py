idade = int(input("Quantos anos você tem? "))

if idade < 18:
    print("Você precisa ter 18 anos ou mais para tirar a carteira de motorista.")
else:
    carteira = input("Você tem carteira de motorista? (sim/não): ")

    if carteira == "sim":
        print("Você pode dirigir!")
    elif carteira == "não":
        print("Você precisa tirar a carteira de motorista antes de poder dirigir!")