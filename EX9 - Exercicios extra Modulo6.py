# 9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

lista_num=[]
cont=0

while cont < 3:
    num= int(input('Digite um número: '))
    lista_num.append(num)
    cont+=1

lista_num.sort(reverse=True)    
print(f'A ordem decrescente dos números digitados é {lista_num}')