#  Faça um programa em python que determine em duas variáveis (senha e email) e que contenha uma senha e um email cadastrados antecipadamente, em seguida solicite ao usuário uma senha e um email e utilize o laço de repetição juntamente com a estrutura de condição para verificar se o email e a senha digitado pelo usuário é igual ao email e senha cadastrados antecipadamente. E enquanto a senha e o email que o usuário digitou não for igual ao email e senha cadastrados ele continue em um loop.

email = "pedro123@gmail.com"
senha = "123456"

while True:
    email2 = input('Digite seu email:')
    senha2 = input('Digite sua senha:')
    if email == email2 and senha == senha2:
        print('Bem vindo ao seu email!')
        break
    elif email != email2 or senha != senha2:
        print('Sua senha ou email estão errados')
        continue