# 4) No exemplo abaixo temos uma lista de listas. Crie uma nova lista única com todos os nomes.


# ```python
# >>> nomes = [
#     ["Michael", "Ana", "Joao", "Marcia"],
#     ["Fabio", "Luiz", "Lucia", "Malu"],
#     ["Jorge", "Maria", "Jose"],
# ]
# ```

# Resultado esperado:

# ```python
# ["Michael", "Ana", "Joao", "Marcia", "Fabio", "Luiz", "Lucia", "Malu", "Jorge", "Maria", "Jose"]
# ```

nomes = [
    ["Michael", "Ana", "Joao", "Marcia"],
    ["Fabio", "Luiz", "Lucia", "Malu"],
    ["Jorge", "Maria", "Jose"],
]
lista_completa = []
for item in nomes:
    for subitem in item:
        lista_completa.append(subitem)
print(lista_completa)