# 11. Tendo como dado de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: P = 72,7h - 58
# b. Para mulheres: P = 62,1h - 44,7

altura= float(input('Digite a sua altura: '))
sexo= int(input('Digite seu sexo 1 - (Masculino) ou 2 - (Feminino): '))

if sexo == 1:
    peso_ideal= round(72.7*altura) - 58
    print(f'Seu peso ideal é {peso_ideal} Kg')
elif sexo == 2:
    peso_ideal= round(62.1*altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal} Kg')
else:
    print('Sexo digitado errado. ')