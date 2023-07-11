# 22. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                      Até 5 Kg           Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
# porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o 
# cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
# e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
# tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

def tabajara_dinheiro(tipo_carne,qtd_comprada,forma_pagamento):
    if qtd_comprada <= 5 and tipo_carne == 1:
        valor_file_duplo= 4.9
        valor_total= qtd_comprada*valor_file_duplo
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_total} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print('A forma de pagamento selecionado não possui desconto')
    elif qtd_comprada <= 5 and tipo_carne == 2:
        valor_alcatra= 5.9
        valor_total= qtd_comprada*valor_alcatra
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_total} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print('A forma de pagamento selecionado não possui desconto')
    elif qtd_comprada <= 5 and tipo_carne == 3:
        valor_picanha= 6.9
        valor_total= qtd_comprada*valor_picanha
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_total} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print('A forma de pagamento selecionado não possui desconto')
    elif qtd_comprada > 5 and tipo_carne == 1:
        valor_file_duplo= 5.8
        valor_total= qtd_comprada*valor_file_duplo
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_total} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print('A forma de pagamento selecionado não possui desconto')
    elif qtd_comprada > 5 and tipo_carne == 2:
        valor_alcatra= 6.8
        valor_total= qtd_comprada*valor_alcatra
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_total} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print('A forma de pagamento selecionado não possui desconto')
    elif qtd_comprada > 5 and tipo_carne == 3:
        valor_picanha= 7.8
        valor_total= qtd_comprada*valor_picanha
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_total} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print('A forma de pagamento selecionado não possui desconto')
        
        
def tabajara_cartao(tipo_carne,qtd_comprada,forma_pagamento):
    if qtd_comprada <= 5 and tipo_carne == 1:
        valor_file_duplo= 4.9
        valor_compra= qtd_comprada*valor_file_duplo
        valor_desc= valor_compra*0.05
        valor_total= valor_compra-valor_desc
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_compra} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print(f'A forma de pagamento selecionado gerou um desconto de R${valor_desc}')
        print(f'O valor total há pagar é de R${valor_total}')
    elif qtd_comprada <= 5 and tipo_carne == 2:
        valor_alcatra= 5.9
        valor_compra= qtd_comprada*valor_alcatra
        valor_desc= valor_compra*0.05
        valor_total= valor_compra-valor_desc
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_compra} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print(f'A forma de pagamento selecionado gerou um desconto de R${valor_desc}')
        print(f'O valor total há pagar é de R${valor_total}')
    elif qtd_comprada <= 5 and tipo_carne == 3:
        valor_picanha= 6.9
        valor_compra= qtd_comprada*valor_picanha
        valor_desc= valor_compra*0.05
        valor_total= valor_compra-valor_desc
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_compra} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print(f'A forma de pagamento selecionado gerou um desconto de R${valor_desc}')
        print(f'O valor total há pagar é de R${valor_total}')
    elif qtd_comprada > 5 and tipo_carne == 1:
        valor_file_duplo= 5.8
        valor_compra= qtd_comprada*valor_file_duplo
        valor_desc= valor_compra*0.05
        valor_total= valor_compra-valor_desc
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_compra} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print(f'A forma de pagamento selecionado gerou um desconto de R${valor_desc}')
        print(f'O valor total há pagar é de R${valor_total}')
    elif qtd_comprada > 5 and tipo_carne == 2:
        valor_alcatra= 6.8
        valor_compra= qtd_comprada*valor_alcatra
        valor_desc= valor_compra*0.05
        valor_total= valor_compra-valor_desc
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_compra} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print(f'A forma de pagamento selecionado gerou um desconto de R${valor_desc}')
        print(f'O valor total há pagar é de R${valor_total}')
    elif qtd_comprada > 5 and tipo_carne == 3:
        valor_picanha= 7.8
        valor_compra= qtd_comprada*valor_picanha
        valor_desc= valor_compra*0.05
        valor_total= valor_compra-valor_desc
        print(f'A quantidade de carne compra é {qtd_comprada}Kg')
        print(f'O preço total da compra é R${valor_compra} ')
        print(f'O tipo de pagamento selecionado é {forma_pagamento}')
        print(f'A forma de pagamento selecionado gerou um desconto de R${valor_desc}')
        print(f'O valor total há pagar é de R${valor_total}')   
    


print('Escolha qual carne deseja:')
tipo_carne= int(input('1- File Duplo, 2- Alcatra, 3-Picanha: '))
print('Informe a quantidade compra em KG: ')
qtd_comprada= float(input(''))
print('Forma de pagamento:') 
forma_pagamento= int(input('1- Dinheiro , 2- Cartão Tabajara: '))   
  

if forma_pagamento==1:
    tabajara_dinheiro(tipo_carne=tipo_carne,qtd_comprada=qtd_comprada,forma_pagamento=forma_pagamento)   
elif forma_pagamento==2:
    tabajara_cartao(tipo_carne=tipo_carne,qtd_comprada=qtd_comprada,forma_pagamento=forma_pagamento)