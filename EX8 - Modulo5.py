# 8. Vamos criar um conversor de temperatura. 
# Faça um Programa que peça a temperatura em graus Fahrenheit, 
# transforme e mostre a temperatura em graus Celsius.


temp_Fahrenheit= float(input('Digite a temperatura em graus Fahrenheit: '))

temp_Celsius= round((temp_Fahrenheit-32)/1.8)
print(f'A temperatura em Celsius é {temp_Celsius} Celsius. ')