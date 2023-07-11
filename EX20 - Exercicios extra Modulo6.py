# 20. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

# Álcool:
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina:
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível 
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

gasolina= 2.5
alcool= 1.9

tipo_combustivel= input('Selecione o tipo de combustível A- Álcool ou G- Gasolina: ')
combustivel_vendido= float(input('Quantos litros de combustível foram vendidos? '))

# tipo_combustivel== 'a' == 'ÁLCOOL'
# tipo_combustivel== 'g' == 'GASOLINA'

if tipo_combustivel.upper() == 'A' and combustivel_vendido <= 20:
    valor_combustivel= combustivel_vendido * alcool
    desconto= valor_combustivel * 0.03
    valor_pago= valor_combustivel - desconto
    print(f'O valor a ser pago pelo combustível é de {valor_pago}')
elif tipo_combustivel.upper() == 'A' and combustivel_vendido > 20:
    valor_combustivel= combustivel_vendido * alcool
    desconto= valor_combustivel * 0.05
    valor_pago= valor_combustivel - desconto
    print(f'O valor a ser pago pelo combustível é de {valor_pago}')
elif tipo_combustivel.upper() == 'G' and combustivel_vendido <= 20:
    valor_combustivel= combustivel_vendido * alcool
    desconto= valor_combustivel * 0.04
    valor_pago= valor_combustivel - desconto
    print(f'O valor a ser pago pelo combustível é de {valor_pago}')
elif tipo_combustivel.upper() == 'G' and combustivel_vendido > 20:
    valor_combustivel= combustivel_vendido * alcool
    desconto= valor_combustivel * 0.06
    valor_pago= valor_combustivel - desconto
    print(f'O valor a ser pago pelo combustível é de {valor_pago}')
    