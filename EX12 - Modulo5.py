# 12. Faça um Programa que pergunte quanto você ganha por hora e o 
# número de horas trabalhadas no mês.
# Calcule o salário bruto (horas * salario por hora)
# Calcule o desconto do IR (11% do salário bruto)
# Calcule o desconto do INSS (8% do salário bruto)
# Calcule o desconto do sindicato (5% do salário bruto)
# Calcule o salário líquido (salário bruto - descontos)

sal_hora= float(input('Digite quando ganha por hora: '))
horas_trabalhada= int(input('Digite quantas horas trabalhadas no mês: '))

sal_bruto= sal_hora*horas_trabalhada
desc_IR= sal_bruto * 0.11
desc_INSS= sal_bruto * 0.08
desc_SIND= sal_bruto * 0.05
sal_liquido= sal_bruto - (desc_INSS+desc_IR+desc_SIND)

print(f'Seu sálario bruto é R${sal_bruto}, teve desconto de IR no valor de R${desc_IR}, INSS no valor de {desc_INSS}, Sindicato no valor de {desc_SIND}, salário liquído ficou de R${sal_liquido} ')

