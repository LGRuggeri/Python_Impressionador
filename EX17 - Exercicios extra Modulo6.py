# 17. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário 
# de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de 
# pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa 
# que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

multa = 4

peso_de_peixes= float(input('Digite quantos kilos de peso de peixes carrega: '))

if peso_de_peixes <= 50:
    print('O peso que carrega está dento do permitido')
elif peso_de_peixes > 50:
    excesso= peso_de_peixes - 50
    valor_multa = excesso * multa
    print(f'Você trouxe {peso_de_peixes}Kg de peixe, passou em {excesso}kg do permitido e vai pagar de multa R${valor_multa} Reais!! ')
