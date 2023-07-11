# 18. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do valor_saque 
# e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as 
# de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

print('Os valores de valor_saque são no mínimo de 10 reais e o máximo de 600 reais.')
valor_saque= int(input('Digite quanto deseja sacar: '))


while(valor_saque<10) or (valor_saque>600):
    print("Valor fora dos limites.")
    valor_saque = int(input("Digite novamente: R$"))
    
if(valor_saque>=10) and (valor_saque<=600):
    resto1 = valor_saque % 100
    resto2 = resto1 % 50
    resto3 = resto2 % 10
    resto4 = resto3 % 5
    nota100,nota50,nota10,nota5,nota1 = valor_saque//100,resto1//50,resto2//10,resto3//5,resto4//1
    print("R$100,00:",nota100)
    print("R$50,00:",nota50)
    print("R$10,00:",nota10)
    print("R$5,00:",nota5)
    print("R$1,00:",nota1)