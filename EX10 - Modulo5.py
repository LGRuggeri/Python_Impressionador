# 10. Tendo como dados de entrada a altura (h) de uma pessoa, 
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# P = 72,7h - 58

altura= float(input('Digite a sua altura: '))

peso_ideal= round(72.7*altura) - 58
print(f'Seu peso ideal é {peso_ideal} Kg')