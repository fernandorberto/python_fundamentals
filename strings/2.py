#2) Um palíndromo é uma sequência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Escreva um programa que peça uma string para o usuário e verifique se é um palíndromo.

print('Verificando se a palavra informada é um palindromo')
palavra = input(str('Insira uma palavra: '))

valida_palavra = palavra[::-1]

if palavra == valida_palavra:
    print ('Palavra informada é um palindromo')
else:
    print ('Palavra informada não é um palindromo')