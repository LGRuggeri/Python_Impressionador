# 6. Faça um Programa que calcule a área de uma sala de um apartamento. 
# Para isso, o seu programa precisa pedir a largura da sala, 
# o comprimento da sala e imprimir a área em m² da sala.

largura_sala= int(input('Digite a largura da sala: '))
comprimento_sala= int(input('Digite o comprimento da sala: '))

tamanho_sala= largura_sala*comprimento_sala

print(f'O tamanho da sala é {tamanho_sala} m²')