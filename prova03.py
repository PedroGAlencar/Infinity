# Escreva um programa em python que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.
soma = 0
total = 0
while True:
    num = int(input('Digite um número do teclado:'))
    total += 1
    soma+=num
    if num == 0:
        total -= 1
        print(f'Total de números digitados foram {total}')
        print(f'A soma final é {soma}')
        media = soma / total
        print(f'A média aritmética é {media}')
        break
    

        
    