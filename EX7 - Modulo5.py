# 7. Faça um Programa que pergunte quanto você ganha por hora e o 
# número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.

salario_hora= float(input('Digite quando ganha por hora: '))
horas_mes= int(input('Digite quantas horas trabalha no mês: '))

salario_mes= salario_hora * horas_mes
print(f'O seu salário no mês é {salario_mes}')