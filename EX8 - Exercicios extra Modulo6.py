# 8. Faça um programa que pergunte o preço de três produtos e 
# informe qual produto você deve comprar, sabendo que a decisão 
# é sempre pelo mais barato.


produto1= int(input('Digite o valor do produto 1: '))
produto2= int(input('Digite o valor do produto 2: '))
produto3= int(input('Digite o valor do produto 3: '))

if produto1 > produto2 and produto2 > produto3:
    print(f'Você deve comprar o produto {produto3}')
elif produto2 > produto1 and produto1 > produto3:
    print(f'Você deve comprar o produto {produto3}')  
elif produto3 > produto1 and produto1 > produto2:
    print(f'Você deve comprar o produto {produto2}')
elif produto1 > produto3 and produto3 > produto2:
    print(f'Você deve comprar o produto {produto2}')
elif produto2 > produto3 and produto3 > produto1:
    print(f'Você deve comprar o produto {produto1}')
elif produto3 > produto2 and produto2 > produto1:
    print(f'Você deve comprar o produto {produto1}')