"""
1) Com base na lista abaixo, crie uma nova lista removendo os valores menores que 10:

```python
>>> numeros = [1, 60, 15, 87, 13, 9, 8, 31, 42, 2]
```
"""

numeros = [1, 60, 15, 87, 13, 9, 8, 31, 42, 2]

numeros_novos = [i for i in numeros if i < 10]
print(numeros_novos)

lista_nova = []
for i in numeros:
    if i > 10:
        lista_nova.append(i)
print(lista_nova)