# 18. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque 
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as 
# de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

print('Os valores de saque são no mínimo de 10 reais e o máximo de 600 reais.')
valor_saque= int(input('Digite quanto deseja sacar: '))

if valor_saque >= 10 and valor_saque <= 600:
    qtd100= valor_saque%100
    if qtd100 != 0:
        qtd50= qtd100%50