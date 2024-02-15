#  Faça um programa que solicite ao usuário que digite 10 valores para preencher uma lista. Em seguida, o programa deve separar os números pares e ímpares em listas diferentes. Por fim, exiba na tela os números pares, os números ímpares em uma tupla, a quantidade de números pares e ímpares presentes na lista, e a soma de todos os números pares e ímpares, respectivamente.
numeros = []
pares = []
impares = []

for n in range(10):
    n = int(input('Digite um número:'))
    numeros.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

#1
print(f'A lista dos 10 valores que você digitou é {numeros}, só de números pares é {pares} e a só de números impares é {impares}')

#2
print(f'A tupla dos pares é {tuple(pares)} e a de impares é {tuple(impares)}')

#3
print(f'A quantidade de números pares é {len(pares)} e a de números impares é {len(impares)}')

#4
soma = sum(numeros)

print(f'A soma de todos os pares e impares é {soma}')