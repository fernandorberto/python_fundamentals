#1) Usando a função len(), escreva um programa que verifica se uma senha informada pelo usuário é menor do que o tamanho mínimo de 10 caracteres.

print(str('Insira uma senha: '))
entrada = input()

if len(entrada) <= 10:
    print('Sua senha atende aos requisitos de tamanho')
else:
    print('Sua senha não atende aos requisitos de tamanho')


