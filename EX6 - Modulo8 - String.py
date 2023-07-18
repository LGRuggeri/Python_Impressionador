# Reformas e mudanças de cargas tributárias são bem comuns no Brasil.
# Digamos que você trabalhe em uma empresa de ecommerce
# No Brasil, o imposto sobre livros é zerado. De um ano para o outro, 
# o governo criou um novo imposto que incide em 10% sobre o valor dos 
# livros e agora você precisa alterar o registro dos preços dos livros 
# da empresa para garantir que esse imposto vai ser repassado para o 
# preço final do produto.
# Crie um código que recalcule o valor do livro da sua lista de produtos
# e ajuste na tabela.
# Além disso, calcule qual vai ser o impacto financeiro da criação desse 
# imposto para a empresa (ou seja, quanto que o imposto vai aumentar de 
# custo para a empresa)

# Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve 
# vamos aprender um for que vai adaptar esse cenário para qualquer 
# quantidade de livros na sua lista.

# Obs2: Seu código deve funcionar mesmo que não haja livros na lista 
# de produtos da empresa


# produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 
# 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

# cada item da lista dos produtos corresponde a quantidade de vendas no 
# mês e preço, nessa ordem
# produtos_ecommerce = [
#     [10000, 2500],
#     [50000, 40],
#     [7000, 1200],
#     [20000, 1500],
#     [5800, 1300],
#     [7200, 2500],
#     [200, 800],
#     [3300, 700],
#     [1900, 400]
# ]

produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 
'ar condicionado', 'alexa', 'máquina de café', 'kindle']

produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if 'livro' in produtos:
    i_livro= produtos.index('livro')
    total_antigo= produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    produtos_ecommerce[i_livro][1] = produtos_ecommerce[i_livro][1] * 1.1
    total_novo= produtos_ecommerce[i_livro][0] * produtos_ecommerce[i_livro][1]
    print('Vamos pagar a mais de imposto o valor de R${:,}' .format(total_novo - total_antigo))
