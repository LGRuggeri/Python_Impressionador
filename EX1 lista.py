## 1. Faturamento do Melhor e do Pior Mês do Ano

# Qual foi o valor de vendas do melhor mês do Ano?
# E valor do pior mês do ano?


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)
i= vendas_1sem.index(max(vendas_1sem))
y= vendas_1sem.index(min(vendas_1sem))
vendas_melhor_mes= max(vendas_1sem)
vendas_pior_mes= min(vendas_1sem)
melhor_mes= meses[i]
pior_mes= meses[y]
faturamento= sum(vendas_1sem)
perc_melhor_mes= (vendas_melhor_mes * 100) / faturamento 


## 2. Continuação

# Agora relacione as duas listas para printar 'O melhor mês do ano foi {} 
# com {} vendas' e o mesmo para o pior mês do ano.

# Calcule também o faturamento total do Ano e quanto que o melhor mês 
# representou do faturamento total.

print('O melhor mês de venda foi {} e o valor vendido foi R${}' .format(melhor_mes,vendas_melhor_mes))
print('O pior mês de venda foi {} e o valor vendido foi R${}' .format(pior_mes,vendas_pior_mes))
print('O faturamento total foi de R${}' .format(faturamento))
print('O melhor mês de venda representa do faturamento total {}%' .format(round(perc_melhor_mes)))

# 3. Crie uma lista com o top 3 valores de vendas do ano
top3= []

vendas_1sem.sort(reverse=True)
top3.append(max(vendas_1sem))
vendas_1sem.remove(max(vendas_1sem))
top3.append(max(vendas_1sem))
vendas_1sem.remove(max(vendas_1sem))
top3.append(max(vendas_1sem))

print('O top 3 valores do ano em vendas foram {}' .format(top3))