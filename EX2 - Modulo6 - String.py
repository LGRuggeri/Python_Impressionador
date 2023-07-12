# Agora, além das validações anteriores, vamos criar um input que permita 
# que o usuário insira pontos, traços e inclusive espaços vazios.
# Nosso programa deve "tratar" o que o usuário inserir para padronizar o 
# CPF dele em apenas números.
# A verificação de tamanho do CPF com 11 caracteres continua válida,
# mas ela só deve ser feita depois de retirar todos os pontos, 
# traços e espaços do CPF que o cliente inserir e, 
# uma vez retirados pontos, traços e espaços, 
# devem sobrar apenas números no CPF. 
# Qualquer outro caractere deve ser considerado inválido.
# No final, nosso programa deve exibir uma mensagem para o usuário,
# caso ele tenha inserido o CPF inválido ou então apenas deve printar
# o CPF correto já só com número.


cpf_clientes= input('Insira seu CPF: ')

#Retirar espaço início e no final
cpf_clientes= cpf_clientes.strip()
#Retirar pontos
cpf_clientes= cpf_clientes.replace('.','')
#Retirar traço
cpf_clientes= cpf_clientes.replace('-','')

if len(cpf_clientes) == 11 and cpf_clientes.isnumeric():
    print('O cpf digitado foi {}' .format(cpf_clientes))
else:
    print('Digite seu CPF corretamente e digite apenas números')