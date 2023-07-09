# 10. Faça um Programa que pergunte em que turno você estuda. 
# Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou 
# "Valor Inválido!", conforme o caso.


turno_estudo= input('Digite em qual turno estuda M-matutino, V-Vespertino ou N- Noturno: ')

if turno_estudo.upper()=='M':
    print('Bom dia')
elif turno_estudo.upper()=='V':
    print('Boa tarde')
elif turno_estudo.upper()=='N':
    print('Bom noite')
else:
    print('Valor inválido')