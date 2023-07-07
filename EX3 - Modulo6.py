alimentos_estq_min=50
bebidas_estq_min=75
limpeza_estq_min=30

categoria_prod= input('Digite a categoria do produto A-Alimentos, B-Bebidas ou L-limpeza: ')
if categoria_prod=='':
    while categoria_prod=='':
        print('Categoria vazia, não deixe de preencher!!')
        categoria_prod= input('Digite a categoria do produto A-Alimentos, B-Bebidas ou L-limpeza: ')
    
nome_prod= input('Digite o nome do produto: ')
if nome_prod=='':
    while nome_prod=='':
        print('Nome vazio, não deixe de preencher!!')
        nome_prod= input('Digite o nome do produto: ')

qtd_prod= input('Digite a quantidade do produto em estoque: ')
if qtd_prod=='':
    while qtd_prod=='':
        print('Quantidade de vazio, não deixe de preencher!! ')
        qtd_prod= input('Digite a quantidade do produto em estoque: ')


if categoria_prod.upper()=='A' and int(qtd_prod) < 50:
    print(f'Solicitar {nome_prod} à equipe de compras, temos apenas {int(qtd_prod)} unidades em estoque')
    
if categoria_prod.upper()=='B' and int(qtd_prod) < 75:
    print(f'Solicitar {nome_prod} à equipe de compras, temos apenas {int(qtd_prod)} unidades em estoque')
    
if categoria_prod.upper()=='L' and int(qtd_prod) < 30:
    print(f'Solicitar {nome_prod} à equipe de compras, temos apenas {int(qtd_prod)} unidades em estoque')