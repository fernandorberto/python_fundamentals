#4) Escreva um programa que remova os asteriscos do início de uma string informada pelo usuário. Exemplo:
"""
```shell
Informe o texto:  ******abcde
Resultado: abcde
```
"""

valor = input("Informe um texto xpto com *****: ")

print(f"Texto {valor} sem correçao")

valor_corrigido = valor.replace("*","")

print(f"Texto {valor_corrigido} com correçao")

