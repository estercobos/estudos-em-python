def saudacao(nome = "Visitante"):
    return f"Olá, {nome}! Seja bem-vinda(o)!"

# Chamada com argumento:
mensagem1 = saudacao()
print(mensagem1)

# Chamada sem argumento:
mensagem2 = saudacao("Ester")
print(mensagem2)

def idade(idade):
    return f"Entendi, você tem {idade} anos!"

idade_usuario = int(input("Quantos anos você tem? "))
mensagem_idade = idade(idade_usuario)
print(mensagem_idade)

# No código, a ordem de execução acontece da maneira como você escreveu o código, e não da ordem lógica de perguntas. Isso é algo que acontece por causa do fluxo do programa e como as funções são chamadas.

#Como a execução funciona:
# Primeiro o Python vai começar a execução do código do topo para baixo. 
# Ele vai definir as funções (saudacao() e idade()), mas não vai executá-las ainda — isso acontece quando elas são chamadas. 
# Quando você faz um input(), o programa pausa e espera o usuário digitar algo. Nesse momento, o Python não pula para o final do código, ele só vai para o próximo comando depois que a entrada for dada. Ou seja, ele pede a idade primeiro.
# Depois de o usuário digitar a idade, a função idade() é chamada com o valor que o usuário digitou e o programa continua a execução para o próximo comando.