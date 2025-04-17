def pode_dirigir(idade, tem_cnh):
    if idade < 0:
        return "Idade inválida! Você ainda nem nasceu, criatura!"
    elif idade >= 18 and tem_cnh:
        return "Você está apta(o) a dirigir!"
    elif idade >= 18 and not tem_cnh:
        return "Você tem idade pra dirigir, mas precisa tirar a CNH. Vamos lá!"
    else:
        return f"Você ainda não pode dirigir. Faltam {18 - idade} ano(s). Tenha paciência!"

# Coletando a idade e a CNH do usuário:
try:
    idade_usuario = int(input("Quantos anos você tem? "))
    cnh_usuario = input("Você tem CNH? (sim/não) ").lower() == "sim"
    
    mensagem = pode_dirigir(idade_usuario, cnh_usuario)
    print(mensagem)
except ValueError:
    print("Por favor, digite um número inteiro válido pra idade!")