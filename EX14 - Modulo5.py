# 14. Faça um programa que peça o tamanho de um arquivo para download (em MB) 
# e a velocidade de um link de Internet (em Mbps), 
# calcule e informe o tempo aproximado de download do arquivo usando este link 
# (em minutos).

# Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. 
# Um megabit é 1/8 de um megabyte. 

from math import ceil

arquivo_download= float(input('Digite o tamanho do arquivo para download em MB: '))
velocidade_internet= int(input('Digite a velocidade da internet em MBps: '))

tempo_download= ceil((arquivo_download / velocidade_internet) / 60)
print(f'O download será baixo em {tempo_download} minuto(s)')