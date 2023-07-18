# Valida e corrige número de telefone. Faça um programa que leia um número 
# de telefone, e corrija o número no caso deste conter somente 7 dígitos,
# acrescentando o '3' na frente. O usuário pode informar o número com ou sem
# o traço separador.

print('Valida e corrige número de telefone')

tel = input('Telefone: ')
tel = tel.replace('-', '')
if len(tel) == 7:
    print('Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.')
    tel = '3' + tel
    print(f'Telefone corrigido sem formatação: {tel}')
    print(f'Telefone corrigido com formatação: {tel[:4]}-{tel[4:]}')
else:
    print('O telefone não tem 7 dígitos.')