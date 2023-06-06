# 13. Faça um programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados 
# e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# Informe ao usuário a quantidades de latas de tinta a serem compradas 
# e o preço total. (para simplificação nesse momento, não se preocupe em arredondar
# a quantidade de latas a serem compradas - vamos trabalhar isso em breve)

valor_lata18= 80

area_pintar= int(input('Digite o tamanho da área a ser pintada em metro: '))

cobertura= area_pintar/18
cobertura_total= cobertura/3
valor_gasto= cobertura_total*valor_lata18
print(f'Vai ser gasto {cobertura_total} lata(s) e o valor total da compra é R${valor_gasto}')