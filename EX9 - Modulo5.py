# 9. Faça um Programa que peça a temperatura em graus Celsius, 
# transforme e mostre em graus Fahrenheit.


temp_Celsius= float(input('Digite a temperatura em graus Celsius: '))

temp_Fahrenheit= round((temp_Celsius*1.8)+32)
print(f'A temperatura em Fahrenheit é {temp_Fahrenheit} Fahrenheit. ')