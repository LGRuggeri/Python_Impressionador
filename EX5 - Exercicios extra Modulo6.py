# 5. Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:

# A mensagem "Aprovado com Distinção", se a média for igual a dez.
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;

lista_notas=[]
cont=0

while cont <= 2:
    if cont == 0:
        notas= float(input('Digite a 1 nota do aluno: '))
        lista_notas.append(notas)
        cont+=1
    elif cont == 1:
        notas= float(input('Digite a 2 nota do aluno: '))
        lista_notas.append(notas)
        cont+=1
    elif cont == 2:
        notas= float(input('Digite a 3 nota do aluno: '))
        lista_notas.append(notas)
        cont+=1
        
     
if cont == 3:
    media= sum(lista_notas) / 3
    if media ==10:
        print('Aluno aprovado com distinção')
    elif media >= 7 and media < 10:
        print('Aluno aprovado')
    elif media < 7:
        print('Aluno reprovado')
        
        