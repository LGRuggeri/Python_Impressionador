# Faremos algo parecido com "filtrar" uma lista. Mais pra frente no curso aprenderemos outras formas
# de fazer isso, mas com o nosso conhecimentoa atual já conseguimos resolver o desafio.

# Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores 
# que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta. 
# Ou seja, se temos 10 vendedores e 3 bateram a meta, temos 30% dos vendedores que bateram a meta.
# Vamos resolver de 2 formas:
#     1. Criando uma lista auxiliar apenas com os vendedores que bateram a meta
#     2. Fazendo o cálculo diretamente na lista que já temos

vendedores_meta=[]
meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

# 1 Forma.
for venda in vendas:
    if venda[1] >= meta:
        vendedores_meta.append(venda)
        
print('{:.1%} de vendedores que bateram a meta' .format(len(vendedores_meta) / len(vendas)))

# 2 Forma.
qtd_vend_acima_meta= 0
for venda in vendas:
    if venda[1] >= meta:
        qtd_vend_acima_meta+=1
        
print('{:.1%} de vendedores que bateram a meta' .format(qtd_vend_acima_meta / len(vendas)))

# Para treinar uma estrutura parecida, crie um código para responder: 
# quem foi o vendedor que mais vendeu?

melhor_vendedor= ''
maior_vendas= 0

for venda in vendas:
    if venda[1] > maior_vendas:
        maior_vendas = venda[1]
        melhor_vendedor= venda[0]
        
print('{} Foi o vendedor(a) que mais vendeu, com R${} em vendas' .format(melhor_vendedor,maior_vendas))