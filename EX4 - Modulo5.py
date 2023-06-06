# 4. Faça um Programa que peça as 4 notas bimestrais de um aluno 
# e mostre a média de todas as notas.

nota1= float(input('Digite a 1 nota: '))
nota2= float(input('Digite a 2 nota: '))
nota3= float(input('Digite a 3 nota: '))
nota4= float(input('Digite a 4 nota: '))

soma= nota1+nota2+nota3+nota4
media= soma/4
print(f'A média do aluno é {media}')