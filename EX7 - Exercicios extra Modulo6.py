# 7. Faça um Programa que leia três orçamentos e mostre o 
# maior e o menor deles.

orcamento= []

empresa1= float(input('Digite o valor da empresa 1: '))
orcamento.append(empresa1)
empresa2= float(input('Digite o valor da empresa 2: '))
orcamento.append(empresa2)
empresa3= float(input('Digite o valor da empresa 3: '))
orcamento.append(empresa3)

print(f'O maior orçamento foi {(max(orcamento))}')
print(f'O menor orçamento foi {(min(orcamento))}')