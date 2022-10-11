#3) Escreva um programa que exibe o primeiro e o último caractere de uma string informada pelo usuário.

palavra = input(str('Insira uma palavra: '))

ultimo = palavra[-1]
primeiro = palavra[0]

print(f'Primeiro caracter da palavra esoclhida: {primeiro}')
print(f'Ultimo caracter da palavra esoclhida: {ultimo}')