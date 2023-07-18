# A Hashtag sempre se comunica com seus clientes por e-mail. 
# Para isso, a gente tem em cada página um cadastro de nome e e-mail. 
# Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu 
# é um e-mail válido, verificando se ele tem '@' e se depois do '@' 
# tem algum ponto, afinal:

# - liragmail.com NÃO é um e-mail válido
# - lira@gmail NÃO é um e-mail válido
# - lira@gmail.com é um e-mail válido

# Crie um programa que permita o cadastro de nome e e-mail de uma pessoa 
# (por meio de inputs) e que verifique:
# 1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar 
# para preencher todos os dados corretamente
# 2. Se o e-mail contém '@' e se depois do '@' existe algum '.', 
# caso contrário ele deve exibir uma mensagem de e-mail inválido

nome= input('Digite o seu nome: ')
email= input('Digite o seu e-mail: ')

if nome and email:
    pos_a= email.find('@')
    servidor= email[pos_a:]
    if pos_a != -1 and '.' in servidor:
        print('Cadastro concluído')
    else:    
        print('Favor preencher todos os dados corretamente!!!')
