"""
03_elif.py
É uma forma de testar várias condições. Ele é usado quando queremos testar mais de uma condição.
Depois de um 'if', podemos ter vários 'elif' para checar outras condições. Se nenhum for verdadeiro, podemos usar o 'else' no final.
"""

# Pergunta a nota da pessoa
nota = float(input("Qual sua nota (0.0 a 10.0)? "))

# Testa as condições de acordo com a nota
if nota >= 9:  # Se a nota for 9 ou maior, a pessoa ganha um 'A'
    print("A")
elif nota >= 7:  # Se a nota for 7 ou maior, mas menor que 9, a pessoa ganha um 'B'
    print("B")
elif nota >= 5:  # Se a nota for 5 ou maior, mas menor que 7, a pessoa ganha um 'C'
    print("C")
else:  # Se a nota for menor que 5, a pessoa ganha um 'D'
    print("D ou abaixo")