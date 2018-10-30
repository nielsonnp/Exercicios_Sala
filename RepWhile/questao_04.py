'''4. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''


while True:
    nome = input('Nome de Usuário: ')
    senha = input('Senha: ')

    if nome == senha:
        print('Erro: Nome e senha igual!')
    else:
        break

