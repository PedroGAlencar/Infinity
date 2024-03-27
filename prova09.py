from functools import reduce
# PY-A05] Considere uma lista de números inteiros 
# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Utilizando as funções map(),filter() e reduce(), escreva um código que execute as seguintes operações:

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1.Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
quadrado = list(map(lambda x: x ** 2,numeros))

print(quadrado)

# 2.Função filter() para obter uma nova lista com números pares da lista numeros
pares = list(filter(lambda x: x % 2 == 0,numeros))

print(pares)

# 3.Função reduce()  para obter a soma de todos os números da lista numeros
soma = reduce(lambda x,y: x + y,numeros)

print(soma)
