idade = int(input("Quantos anos você tem? "))

if idade <= 10:
    print("Você é uma criança!")
elif idade >= 10 and idade < 18:
    print("Você é um adolescente!")
else:
    print("Você é um adulto!")