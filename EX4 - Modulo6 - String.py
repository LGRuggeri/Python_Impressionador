# Faça um programa que leia 2 strings e informe o conteúdo delas seguido
# do seu comprimento. Informe também se as duas strings possuem o mesmo 
# comprimento e são iguais ou diferentes no conteúdo.


string1= input('Digite o 1 texto: ')
string2= input('Digite o 2 texto: ')

if len(string1) == len(string2):
    print(f'Tamanho: {len(string1)}')
    print(f'Tamanho: {len(string2)}')
    print('Os tamanhos dos textos são iguais.')
else:
    print(f'Tamanho: {len(string1)}')
    print(f'Tamanho: {len(string2)}')
    print('Os tamanhos dos textos são diferentes')
    
if string1 == string2:
    print(f'Texto: {string1}')
    print(f'Texto: {string2}')
    print('As strings possuem conteúdos iguais.')
else:
    print(f'Texto: {string1}')
    print(f'Texto: {string2}')
    print('As duas strings possuem conteúdo diferente.')
    

