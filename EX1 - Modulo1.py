# Crie um programa que imprima (print) os principais indicadores da loja Hashtag &
# Drink no último ano.
# Obs: faça tudo usando variáveis.

# Valores do último ano:

# Quantidade de Vendas de Coca = 150
# Quantidade de Vendas de Pepsi = 130
# Preço Unitário da Coca = 1,50 
# Preço Unitário da Pepsi = 1,50
# Custo da Loja: 2.500,00

# Use o bloco abaixo para criar todas as variáveis que precisar.

# 1. Qual foi o faturamento de Pepsi da Loja?

# 2. Qual foi o faturamento de Coca da Loja?

# 3. Qual foi o Lucro da loja?

# 4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). 
# Não precisa formatar em percentual

qtd_Coca= 150
qtd_Pepsi= 130
preco_Coca= 1.5
preco_Pepsi= 1.5
custo_loja= 2500

fat_Pepsi= qtd_Pepsi * preco_Pepsi
fat_Coca= qtd_Coca * preco_Coca
lucro_loja= (fat_Pepsi + fat_Coca) - custo_loja
margem_loja= (lucro_loja / (fat_Coca + fat_Pepsi))

print(f'O faturamento da loja em Pepsi foi {fat_Pepsi}')
print(f'O faturamento da loja em Coca foi {fat_Coca}')
print(f'O lucro da loja foi {lucro_loja}')
print(f'A margem da loja foi {margem_loja}')