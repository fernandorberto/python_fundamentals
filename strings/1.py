#1) Escreva um programa que peça o nome do usuário e em seguida mostre o nome de trás para frente e somente em maiúsculas.

nome = input('Insira seu nome: ')
print('Se nome ao contrario é ' + nome[::-1].upper())