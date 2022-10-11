"""
4) Escreva um programa que converta uma temperatura em graus Celsius para Fahrenheit usando a fórmula:

    9 x C
F = ----- + 32
    5
    
"""

valor = int(input('Informe o numero a ser convertido para celcius: '))

F = (9 * valor) / 5 + 32

print(f'O valor convertido em celsius é: {F}')