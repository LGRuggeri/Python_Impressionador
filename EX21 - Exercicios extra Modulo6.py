# 21. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                      Até 5 Kg           Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
# receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) 
# de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

def frutas(kg_morango,kg_maca):
    peso_combinado= kg_maca + kg_morango
    if kg_morango <5 and kg_maca <5:
        valor_morango= kg_morango * 2.5
        valor_maca= kg_maca * 1.8
        valor_total= valor_maca + valor_morango
        print(f'Você comprou {kg_maca} Kg de maça e(ou) {kg_morango} Kg de morango, o peso total comprado foi {peso_combinado} Kg, o valor total a pagar é R${valor_total}')
    elif kg_morango == 5 and  kg_maca < 5:
        valor_morango= kg_morango * 2.2
        valor_maca= kg_maca * 1.8
        valor_desc= (valor_maca + valor_morango) * 0.10
        valor_total= (valor_maca + valor_morango) - valor_desc
        print(f'Você comprou {kg_maca} Kg de maça e(ou) {kg_morango} Kg de morango, o peso total comprado foi {peso_combinado} Kg, o valor total a pagar é R${valor_total}')
    elif  kg_morango < 5 and  kg_maca == 5: 
        valor_morango= kg_morango * 2.5
        valor_maca= kg_maca * 1.5
        valor_desc= (valor_maca + valor_morango) * 0.10
        valor_total= (valor_maca + valor_morango) - valor_desc
        print(f'Você comprou {kg_maca} Kg de maça e(ou) {kg_morango} Kg de morango, o peso total comprado foi {peso_combinado} Kg, o valor total a pagar é R${valor_total}')
    elif kg_morango >=5 and  kg_maca >=5:
        valor_morango= kg_morango * 2.2
        valor_maca= kg_maca * 1.5
        valor_desc= (valor_maca + valor_morango) * 0.10
        valor_total= (valor_maca + valor_morango) - valor_desc
        print(f'Você comprou {kg_maca} Kg de maça e(ou) {kg_morango} Kg de morango, o peso total comprado foi {peso_combinado} Kg, o valor total a pagar é R${valor_total}')
        
        
kg_morango= float(input('Quantos kilos de Morango foram comprados? '))
kg_maca= float(input('Quantos kilos de Maça foram comprados? '))
frutas(kg_morango=kg_morango,kg_maca=kg_maca)