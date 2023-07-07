vendas_funcionario1=1000
vendas_funcionario2=270
vendas_funcionario3=2700
meta_vendas=1000

if vendas_funcionario1 >= meta_vendas:
    if vendas_funcionario1 >= 2000:
        bonus=vendas_funcionario1 * 0.15
        print(f'O valor de bônus do funcionario 1 foi de {bonus}')
    elif vendas_funcionario1 >= 1000 and vendas_funcionario1 < 2000:
        bonus=vendas_funcionario1 * 0.10
        print(f'O valor de bônus do funcionario 1 foi de {bonus}')
else:
    print('Não atingiu a meta, não possui bônus')    
        
if vendas_funcionario2 >= meta_vendas:
    if vendas_funcionario2 >= 2000:
        bonus=vendas_funcionario2 * 0.15
        print(f'O valor de bônus do funcionario 2 foi de {bonus}')
    elif vendas_funcionario2 >= 1000 and vendas_funcionario2 < 2000:
        bonus=vendas_funcionario2 * 0.10
        print(f'O valor de bônus do funcionario 2 foi de {bonus}')
else:
    print('Não atingiu a meta, não possui bônus')    
       
if vendas_funcionario3 >= meta_vendas:
    if vendas_funcionario3 >= 2000:
        bonus=vendas_funcionario3 * 0.15
        print(f'O valor de bônus do funcionario 3 foi de {bonus}')
    elif vendas_funcionario3 >= 1000 and vendas_funcionario3 < 2000:
        bonus=vendas_funcionario3 * 0.10
        print(f'O valor de bônus do funcionario 3 foi de {bonus}')
else:
    print('Não atingiu a meta, não possui bônus')    
    