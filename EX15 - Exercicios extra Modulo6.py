# 15. Você está construindo um calendário para controlar dias de trabalho a pedido do RH.
# Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, 
# para montar o calendário de forma correta. Faça um Programa que peça um número correspondente 
# a um determinado ano e em seguida informe se este ano é ou não bissexto.

import calendar


ano= int(input('Digite o ano: '))


# if calendar.isleap(ano) == True:
#     print('Ano Bissexto')
# else:
#     print('Não é Bissexto')

rest400= ano%400
rest100= ano%100
rest4= ano%4


if rest400 == rest100 and rest4 == rest100:
    print('Ano Bissexto')
elif rest4 != rest100 and rest4 == rest400:
    print('Ano Bissexto')
else:
    print('Não é Bissexto')     