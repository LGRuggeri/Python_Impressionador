# 4. Faça um Programa que verifique se o e-mail digitado faz 
# parte dos e-mails de spam.

mail_spam= 'gmail.com'

mail= input('Digite o e-mail para verificar se é spam: ')
separador = mail.split(sep=	'@')

if separador[1] == mail_spam:
    print(f'O email digitado está dentro da relação de spam {mail_spam}')