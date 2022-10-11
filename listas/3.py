# 3) A seguinte lista foi produzida por um processo automático e contém strings vazias indesejadas. Crie uma nova lista usando o for-loop que não contenha esses valores.

# ```python
# >>> nomes = ["Michael", "", "Ana", "Joao", "", "Marcia"]
# ```

# Resultado esperado:
# ```python
# >>> nomes = ["Michael", "Ana", "Joao", "Marcia"]
# ```

nomes = ["Michael", "", "Ana", "Joao", "", "Marcia"]

lista_nova = []

for i in nomes:
    if i != "":
        lista_nova.append(i)
print(lista_nova)