# A maioria das empresas trabalham com um Código para cada produto que possuem. 
# A Hashtag & Drink, por exemplo, tem mais de 1.000 produtos e possui um código para 
# cada produto.

# Ex: 
# Coca -> Código: BEB1300543
# Pepsi -> Código: BEB1300545
# Vinho Primitivo Lucarelli -> Código: BAC1546001
# Vodka Smirnoff -> Código: BAC17675002

# Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas 
# as bebidas alcóolicas tem o início do código "BAC".

# Crie um programa de consulta de bebida que, dado um código qualquer, 
# identifique se a bebida é alcóolica. O programa deve responder True
# para bebidas alcóolicas e False para bebidas não alcóolicas. 
# Para inserir um código, use um input.

# Dica: Lembre-se do comando in para strings e sempre insira os 
# códigos com letra maiúscula para facilitar.

consulta_bebida= input('Para bebidas não alcóolicas inicial BEB e para alcóolicas BAC Ex: BEB1300543, BAC1546001: ')

if 'BEB' in consulta_bebida:
    print(False)
elif 'BAC' in consulta_bebida:
    print(True)
else:
    print('Valor informado errado verifique o exemplo')