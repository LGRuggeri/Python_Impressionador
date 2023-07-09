# 11. As Organizações Tabajara resolveram dar um aumento de salário aos 
# seus colaboradores e lhe contraram para desenvolver o programa que 
# calculará os reajustes. Faça um programa que recebe o salário de um 
# colaborador e o reajuste segundo o seguinte critério, baseado no 
# salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20% 
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
# salários de R$ 1500,00 em diante : aumento de 5% Após o 
# aumento ser realizado, informe na tela: 

# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario= float(input('Digite o salário do funcionário: R$ '))

if salario <= 280:
    per_aumento= 0.2
    aumento= salario * per_aumento
    salario_novo= salario + aumento
    print(f'O salário antes do aumento era R${salario}, foi aplicado um aumento de {per_aumento}%, valor de aumento foi R${aumento} e o salário novo é de R${salario_novo}')
    
elif salario > 280 and salario <= 700:
    per_aumento= 0.15
    aumento= salario * per_aumento
    salario_novo= salario + aumento
    print(f'O salário antes do aumento era R${salario}, foi aplicado um aumento de {per_aumento}%, valor de aumento foi R${aumento} e o salário novo é de R${salario_novo}')
    
elif salario > 700 and salario <= 1500:
    per_aumento= 0.1
    aumento= salario * per_aumento
    salario_novo= salario + aumento
    print(f'O salário antes do aumento era R${salario}, foi aplicado um aumento de {per_aumento}%, valor de aumento foi R${aumento} e o salário novo é de R${salario_novo}')
    
elif salario > 1500:
    per_aumento= 0.05
    aumento= salario * per_aumento
    salario_novo= salario + aumento
    print(f'O salário antes do aumento era R${salario}, foi aplicado um aumento de {per_aumento}%, valor de aumento foi R${aumento} e o salário novo é de R${salario_novo}')
    
    



