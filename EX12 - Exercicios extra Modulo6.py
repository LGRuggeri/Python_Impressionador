# 12 . Faça um programa para o cálculo de uma folha de pagamento, 
# sabendo que os descontos são do Imposto de Renda, que depende do salário 
# bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário 
# Bruto, mas não é descontado (é a empresa que deposita). 
# O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de 
# horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900   - isento
# Salário Bruto até 1500  - desconto de 5%
# Salário Bruto até 2500  - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00

inss= 10
fgts= 11

valor_hora= float(input('Digite o valor da sua hora de trabalho: R$'))
horas_trabalhadas= int(input('Digite a quatidade de horas trabalhadas no mês: '))

salario_bruto = valor_hora * horas_trabalhadas
if salario_bruto <= 900:
    valor_ir= 0
    valor_inss= salario_bruto * (inss/100)
    valor_fgts= salario_bruto * (fgts/100)
    desconto= valor_inss + valor_ir
    salario_liquido= salario_bruto - desconto
    print(f'Salário Bruto ({valor_hora} * {horas_trabalhadas}) = R${salario_bruto}')
    print(f'IR ({valor_ir}) ')
    print(f'INSS ({inss}%) = R${valor_inss}')
    print(f'FGTS ({fgts}%) = R${valor_fgts}')
    print(f'Total de descontos = R${desconto}')
    print(f'Salário Liquido = R${salario_liquido}')
elif salario_bruto > 900 and salario_bruto <= 1500:
    ir= 5
    valor_ir= salario_bruto * (ir/100)
    valor_inss= salario_bruto * (inss/100)
    valor_fgts= salario_bruto * (fgts/100)
    desconto= valor_inss + valor_ir
    salario_liquido= salario_bruto - desconto
    print(f'Salário Bruto ({valor_hora} * {horas_trabalhadas}) = R${salario_bruto}')
    print(f'IR ({ir}%) = R${valor_ir} ')
    print(f'INSS ({inss}%) = R${valor_inss}')
    print(f'FGTS ({fgts}%) = R${valor_fgts}')
    print(f'Total de descontos = R${desconto}')
    print(f'Salário Liquido = R${salario_liquido}')
elif salario_bruto > 1500 and salario_bruto <= 2500:
    ir= 10
    valor_ir= salario_bruto * (ir/100)
    valor_inss= salario_bruto * (inss/100)
    valor_fgts= salario_bruto * (fgts/100)
    desconto= valor_inss + valor_ir
    salario_liquido= salario_bruto - desconto
    print(f'Salário Bruto ({valor_hora} * {horas_trabalhadas}) = R${salario_bruto}')
    print(f'IR ({ir}%) = R${valor_ir} ')
    print(f'INSS ({inss}%) = R${valor_inss}')
    print(f'FGTS ({fgts}%) = R${valor_fgts}')
    print(f'Total de descontos = R${desconto}')
    print(f'Salário Liquido = R${salario_liquido}')
elif salario_bruto > 2500:
    ir= 20
    valor_ir= salario_bruto * (ir/100)
    valor_inss= salario_bruto * (inss/100)
    valor_fgts= salario_bruto * (fgts/100)
    desconto= valor_inss + valor_ir
    salario_liquido= salario_bruto - desconto
    print(f'Salário Bruto ({valor_hora} * {horas_trabalhadas}) = R${salario_bruto}')
    print(f'IR ({ir}%) = R${valor_ir} ')
    print(f'INSS ({inss}%) = R${valor_inss}')
    print(f'FGTS ({fgts}%) = R${valor_fgts}')
    print(f'Total de descontos = R${desconto}')
    print(f'Salário Liquido = R${salario_liquido}')
