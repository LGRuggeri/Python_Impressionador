# 23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da 
# área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que 
# a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
# que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos valor gastos em 3 situações.

# 1. Comprar apenas latas de 18 litros: (apenas latas inteiras)
# 2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)
# 3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de 
# folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

tamanho = float(input('Digite o tamanho da área há ser pintada: '))

litros = tamanho // 6
latas = litros // 18

if latas % 18 != 0:
    latas += 1
preco_latas = latas * 80

galoes = litros // 3.6
if galoes % 3.6 != 0:
    galoes += 1
preco_galoes = galoes * 25

# mistura de latas e galoes
mistura_lata = int(litros // 18.0) 
acrescimo_lata= mistura_lata * 0.10
mistura_lata_acrescimo= mistura_lata + acrescimo_lata
mistura_galao = int((litros - (mistura_lata * 18)) // 3.6) 
acrescimo_galao= mistura_galao * 0.10
mistura_galao_acrescimo= mistura_galao + acrescimo_galao

if litros - (mistura_lata * 18) % 3.6 != 0:
    mistura_galao += 1

print(f'Apenas latas de 18 litros: {round(latas)}', f'valor gasto: R${round(preco_latas)}')
print(f'Apenas galões de 3.6 litros: {round(galoes)}', f'valor gasto: R${round(preco_galoes)}')
print(f'Mistura: %d lata(s) e %d galoes = %.2f' % (
    mistura_lata_acrescimo, mistura_galao_acrescimo, ((mistura_lata_acrescimo * 80) + (mistura_galao_acrescimo * 25))))