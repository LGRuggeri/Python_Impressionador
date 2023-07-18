### Exercícios Módulo 1

### Exercícios do Módulo 1 - Operações, Variáveis e Input

### Parte 1 - Operações e Variáveis

Crie um programa que imprima (print) os principais indicadores da loja Hashtag &Drink no último ano.
Obs: faça tudo usando variáveis.

Valores do último ano:

Quantidade de Vendas de Coca = 150
Quantidade de Vendas de Pepsi = 130
Preço Unitário da Coca = 1,50 
Preço Unitário da Pepsi = 1,50
Custo da Loja: 2.500,00

Use o bloco abaixo para criar todas as variáveis que precisar.

1. Qual foi o faturamento de Pepsi da Loja?

2. Qual foi o faturamento de Coca da Loja?

3. Qual foi o Lucro da loja?

4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual


### Parte 2 - Inputs e Strings

A maioria das empresas trabalham com um Código para cada produto que possuem. A Hashtag&Drink, por exemplo, tem mais de 1.000 produtos e possui um código para cada produto.

Ex: 
Coca -> Código: BEB1300543
Pepsi -> Código: BEB1300545
Vinho Primitivo Lucarelli -> Código: BAC1546001
Vodka Smirnoff -> Código: BAC17675002

Repare que todas as bebidas não alcóolicas tem o início do Código "BEB" e todas as bebidas alcóolicas tem o início do código "BAC".

Crie um programa de consulta de bebida que, dado um código qualquer, identifique se a bebida é alcóolica. O programa deve responder True para bebidas alcóolicas e False para bebidas não alcóolicas. Para inserir um código, use um input.

Dica: Lembre-se do comando in para strings e sempre insira os códigos com letra maiúscula para facilitar.

Exercícios Módulo 5

1. Faça um Programa que mostre a mensagem (print) "Alo mundo" na tela.

2. Faça um Programa que peça um número (input) e então mostre a mensagem: 'O número informado foi [número]'.

3. Faça um Programa que peça dois números e imprima a soma.

4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

6. Faça um Programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m² da sala.

7. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

8. Vamos criar um conversor de temperatura. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = frac{5}{9}(F-32)

9. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
F = frac{9}{5}C + 32

10. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
P = 72,7h - 58

Lembrando que "algoritmo" nada mais é do que um programa, como todos os outros que você vem fazendo.

11. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: P = 72,7h - 58
b. Para mulheres: P = 62,1h - 44,7

12. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule o salário bruto (horas * salario por hora)
Calcule o desconto do IR (11% do salário bruto)
Calcule o desconto do INSS (8% do salário bruto)
Calcule o desconto do sindicato (5% do salário bruto)
Calcule o salário líquido (salário bruto - descontos)

13. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. (para simplificação nesse momento, não se preocupe em arredondar a quantidade de latas a serem compradas - vamos trabalhar isso em breve)

14. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

### Módulo 6

### Exercícios com if

### 1. Cálculo de Bônus

- Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:

A meta é 1000 vendas. 
Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
Caso contrário o valor de bônus do funcionário é 0.
Print o bônus dos 3 funcionários


vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700


### 2. Cálculo de bônus com uma nova regra

- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

A meta é 1000 vendas
Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:

- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

Use as mesmas variáveis de vendas_funcionários

### 3. Criando um mini sistema de controle de estoque

Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, o time deve ser avisado (print) para fazer um novo pedido daquele produto.
Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:

- alimentos -> Estoque mínimo: 50
- bebidas -> Estoque mínimo: 75
- limpeza -> Estoque mínimo: 30

Para isso vamos criar um programa que pede 3 inputs do usuário: nome do produto, categoria e quantidade atual em estoque.

Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"

Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.
Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.
Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.

### Lista de exercícios de decisão.

1. Faça um Programa que peça dois números e imprima o maior deles.

2. Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

3. Faça um Programa que verifique o estado civil de uma pessoa. Se a letra digitada é "C" (Casado), "S" (Solteiro), "D" (Divorciado), "V" (Viúvo) ou "O" (outros). Conforme a letra escrita pelo usuário seu programa deve escrever o estado civil.

4. Faça um Programa que verifique se o e-mail digitado faz parte dos e-mails de spam.

5. Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.

6. Faça um Programa que leia o orçamento de 3 empresas e mostre o maior deles.

7. Faça um Programa que leia três orçamentos e mostre o maior e o menor deles.

8. Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

9. Faça um Programa que leia três números e mostre-os em ordem decrescente.

10. Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

11. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

salários até R$ 280,00 (incluindo) : aumento de 20% 
salários entre R$ 280,00 e R$ 700,00 : aumento de 15% 
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10% 
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela: 

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

Obs: Não vamos nos preocupar tanto com a formatação dos números (nº de casas decimais, por exemplo, veremos isso no próximo módulo)

12 . Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

Salário Bruto: (5 * 220)        : R$ 1100,00
(-) IR (5%)                     : R$   55,00
(-) INSS ( 10%)                 : R$  110,00
FGTS (11%)                      : R$  121,00
Total de descontos              : R$  165,00
Salário Liquido                 : R$  935,00

Obs: Não vamos nos preocupar tanto com a formatação dos números (nº de casas decimais, por exemplo, veremos isso no próximo módulo)

13. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

14. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. Em seguida, mostre qual conceito o aluno teve. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E

15. Você está construindo um calendário para controlar dias de trabalho a pedido do RH. Nessa construção, você vai precisar definir quais anos são bissextos e quais não são, para montar o calendário de forma correta. Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

Dica para determinar se um ano é bissexto: 
- São bissextos todos os anos múltiplos de 400, p.ex.: 1600, 2000, 2400, 2800...
- São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400, 
p.ex.: 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028...
- Não são bissextos todos os demais anos.
ex1: 2004 é múltiplo de 4, mas não é múltiplo de 100, então é bissexto.
ex2: 2000 é múltiplo de 4, mas é múltiplo de 100, só que também é multiplo de 400, então é bissexto (porque todo ano múltiplo de 400 é bissexto, independente do resto).
ex3: 1900 é múltiplo de 4, é múltiplo de 100, mas não é múltiplo de 400, então não é bissexto

Dica: lembre que: numero % 4 é o resto da divisão do número por 4, ex: 10 % 3 = 1 (já que 10/3 = 3 e resta 1)

16. Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

17. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

18. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.
Dica2: numero % 10 vai te dar o resto da divisão do número por 10.

19. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

20. Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

21. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                     Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

22. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                     Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

23. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações.

Dica: lembre dos operadores // e % mostrados em exercícios anteriores
Dica1: numero // 10 vai te dar como resposta a parte inteira da divisão do número por 10.
Dica2: numero % 10 vai te dar o resto da divisão do número por 10.

1. Comprar apenas latas de 18 litros: (apenas latas inteiras)
2. Comprar apenas galões de 3,6 litros: (apenas galoes inteiros)
3. Misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

O custo da lata é 80/18 = 4,44 R$/L

O custo do galão é 25/3,6 = 6,94 R$/L

A lata é mais econômica, então todas as latas inteiras que pudermos usar devemos comprar em latas. Se ficar faltando alguma coisa para completar devemos avaliar se é melhor comprar latas ou galões. Exemplo:

Se queremos comprar 90 litros. 5 latas dão exatamente 90 litros. Então devemos comprar tudo em latas.

Se queremos comprar 95 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 5 litros faltantes precisamos de 2 galões que custam 50 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar 2 galões.

Se queremos comprar 107 litros. 5 latas dão exatamente 90 litros. Então devemos comprar pelo menos 5 latas e avaliar o que falta, se estes últimos 5 litros valem mais apenas em latas ou galões.

Para os 17 litros faltantes precisamos de 5 galões que custam 125 reais no total. Ou de uma lata que custa 80 reais no total. Portanto, neste caso vale mais a pena usar uma lata.

3 galões custam 75 reais, 4 galões custam 100 reais. Então, se for possível completar com até 3 galões escolhe-se galões. Qualquer quantidade maior que 3 galões, usa-se latas.

# Exercícios com string.

## 1. Cadastro de CPF

Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input box apenas com números.

Ex: 'Insira seu CPF (digite apenas números)'

Caso o usuário digite algo diferente de números ou digite menos de 11 caracteres (tamanho do CPF brasileiro), o programa deve exibir uma mensagem de "Digite seu CPF corretamente e digite apenas números"


## 2. Melhorando nosso Cadastro de CPF

Agora, além das validações anteriores, vamos criar um input que permita que o usuário insira pontos, traços e inclusive espaços vazios.

Nosso programa deve "tratar" o que o usuário inserir para padronizar o CPF dele em apenas números.

A verificação de tamanho do CPF com 11 caracteres continua válida, mas ela só deve ser feita depois de retirar todos os pontos, traços e espaços do CPF que o cliente inserir e, uma vez retirados pontos, traços e espaços, devem sobrar apenas números no CPF. Qualquer outro caractere deve ser considerado inválido.

No final, nosso programa deve exibir uma mensagem para o usuário, caso ele tenha inserido o CPF inválido ou então apenas deve printar o CPF correto já só com número.


## 3. Cadastro de e-mails

- A Hashtag sempre se comunica com seus clientes por e-mail. Para isso, a gente tem em cada página um cadastro de nome e e-mail. Nesse cadastro, nosso sistema verifica se o e-mail que a pessoa inseriu é um e-mail válido, verificando se ele tem '@' e se depois do '@' tem algum ponto, afinal:

- liragmail.com NÃO é um e-mail válido
- lira@gmail NÃO é um e-mail válido
- lira@gmail.com é um e-mail válido

Crie um programa que permita o cadastro de nome e e-mail de uma pessoa (por meio de inputs) e que verifique:
1. Se nome e e-mail foram preenchidos, caso contrário ele deve avisar para preencher todos os dados corretamente
2. Se o e-mail contém '@' e se depois do '@' existe algum '.', caso contrário ele deve exibir uma mensagem de e-mail inválido

Obs: Pode te ajudar lembrar do método .find da aula de Métodos de String. Você pode testar o que ele dá como resposta caso ele não encontre um item dentro da string.

### 4. Tamanho de strings.

Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.

### 5.Tamanho de strings.

Valida e corrige número de telefone. Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador.

Valida e corrige número de telefone
Telefone: 461-0133
Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
Telefone corrigido sem formatação: 34610133
Telefone corrigido com formatação: 3461-0133

# Exercícios Listas

## 1. Faturamento do Melhor e do Pior Mês do Ano

Qual foi o valor de vendas do melhor mês do Ano?
E valor do pior mês do ano?


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

## 2. Continuação

Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total.

Obs: Para o faturamento total, pode usar a função sum(lista) que soma todos os itens de uma lista


## 3. Crie uma lista com o top 3 valores de vendas do ano (sem fazer "no olho")

Dica: o método remove retira um item da lista.

# Exercícios

## 1. Mudança de Carga Tributária

Reformas e mudanças de cargas tributárias são bem comuns no Brasil.

Digamos que você trabalhe em uma empresa de ecommerce

No Brasil, o imposto sobre livros é zerado. De um ano para o outro, o governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o registro dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.

Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)

Obs: para facilitar, colocamos apenas 1 livro na lista, mas em breve vamos aprender um for que vai adaptar esse cenário para qualquer quantidade de livros na sua lista.

Obs2: Seu código deve funcionar mesmo que não haja livros na lista de produtos da empresa


produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

cada item da lista dos produtos corresponde a quantidade de vendas no mês e preço, nessa ordem
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

# Exercícios For.

## 1. Criando um Registro de Hóspedes

Digamos que você está criando o sistema para registrar a chegada de hóspedes em um hotel. No hotel, os hóspedes podem ter quartos com 1, 2, 3 e 4 pessoas. Seu sistema deve conseguir:

1. Identificar quantas pessoas o hóspede que acabou de chegar vai ter no quarto (perguntando por meio de input)
2. De acordo com a quantidade de pessoas do hóspede, ele deve fazer um for para perguntar o cpf e o nome de cada pessoa, a fim de registrá-la no quarto (2 inputs para cada pessoa, 1 para o cpf e outro para o nome)
3. O seu programa então deve gerar uma lista com todas as pessoas que ficarão no quarto em que cada item dessa lista é o nome da pessoa e o cpf da pessoa, assim:

quarto = [
    ['João', 'cpf:00000000000'],
    ['Julia', 'cpf:11111111111'],
    ['Marcus', 'cpf:22222222222'],
    ['Maria', 'cpf:33333333333'],
]

Para simplificar, não vamos nos preocupar com possibilidades de "tentar colocar mais de 1 hóspede, digitar o cpf errado, etc. Nosso objetivo é treinar a criação de uma rotina de cadastro.

## 2. Análise de Vendas

Nesse exercício vamos fazer uma "análise simples" de atingimento de Meta.

Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.

meta = 10000
vendas = [
    ['João', 15000],
    ['Julia', 27000],
    ['Marcus', 9900],
    ['Maria', 3750],
    ['Ana', 10300],
    ['Alon', 7870],
]

## 3. Comparação com Ano Anterior

Digamos que você está analisando as vendas de produtos de um ecommerce e quer identificar quais produtos tiveram no ano de 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.

Sua resposta pode ser um print de cada produto, qual foi a venda de 2019, a venda de 2020 e o % de crescimento de 2020 para 2019.

Lembrando, para calcular o % de crescimento de um produto de um ano para o outro, podemos fazer: (vendas_produto2020/vendas_produto2019 - 1)

Dica: lembre do enumerate, ele pode facilitar seu "for"

produtos = ['iphone', 'galaxy', 'ipad', 'tv', 'máquina de café', 'kindle', 'geladeira', 'adega', 'notebook dell', 'notebook hp', 'notebook asus', 'microsoft surface', 'webcam', 'caixa de som', 'microfone', 'câmera canon']
vendas2019 = [558147,712350,573823,405252,718654,531580,973139,892292,422760,154753,887061,438508,237467,489705,328311,591120]
vendas2020 = [951642,244295,26964,787604,867660,78830,710331,646016,694913,539704,324831,667179,295633,725316,644622,994303]
