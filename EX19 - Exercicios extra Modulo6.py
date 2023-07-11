# 19. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?" 

# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado 
# como "Inocente".

tel_vit= int(input('Telefonou para a vítima? 0- Não ou 1- Sim : '))
local_vit= int(input('Esteve no local do crime? 0- Não ou 1- Sim : '))
mora_vit= int(input('Mora perto da vítima? 0- Não ou 1- Sim : '))
devia_vit= int(input('Devia para a vítima? 0- Não ou 1- Sim : '))
trabalhou_vit= int(input('Já trabalhou com a vítima? 0- Não ou 1- Sim : '))

soma_respostas= tel_vit + local_vit + mora_vit + devia_vit + trabalhou_vit
print(soma_respostas)

if soma_respostas == 2:
    print('Suspeito(a) do crime.')
elif soma_respostas == 3 or soma_respostas == 4:
    print('Cúmplice do crime.')
elif soma_respostas == 5:
    print('Assassino!!!')
else:
    print('Inocente do crime.')