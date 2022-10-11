"""
2) Usando o for loop, gere uma nova lista a partir do exemplo acima com todos os números multiplicados por 2.
Resultado esperado:

```python
[2, 120, 30, 174, 26, 18, 16, 62, 84, 4]
```
"""

numeros = [1, 60, 15, 87, 13, 9, 8, 31, 42, 2]
lista_nova = []
for i in numeros:
        lista_nova.append(i*2)
print(lista_nova)